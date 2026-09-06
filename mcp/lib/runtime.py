"""Per-connection container ownership, capacity locks and credential projection."""
from __future__ import annotations
import contextlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import time
import uuid
from typing import Any
from common import (SOURCE_ROOT, ConfigError, atomic_write, clean_env, locked, podman, run)
import toolchain

MANAGED_LABEL = 'io.codex-mcp.managed'
SESSION_RE = re.compile(r'[a-f0-9]{32}\Z')
CONTAINER_RE = re.compile(r'codex-mcp-[a-z0-9-]+-[a-f0-9]{32}\Z')


def catalog() -> dict[str, Any]:
    return json.loads((SOURCE_ROOT/'servers.json').read_text())


def acquire_slot(stack: contextlib.ExitStack, root: Path, stem: str, count: int) -> int:
    for index in range(count):
        try:
            stack.enter_context(locked(root/f'{stem}-{index}.lock'))
            return index
        except BlockingIOError:
            continue
    raise ConfigError('server capacity exhausted; close an existing MCP connection and reconnect')


def stage_credentials(source: Path, destination: Path, spec: dict[str, Any]) -> None:
    """Read systemd credentials, copy only the selected server's subset to tmpfs.

    A remote Podman daemon cannot see systemd's private credential mount. The
    second, host-visible copy stays devops-only and is deleted after rm succeeds.
    """
    destination.mkdir(mode=0o700)
    for name in spec.get('credentials', []):
        path = source/name
        required = name in spec.get('required_credentials', [])
        try:
            fd = os.open(path, os.O_RDONLY|os.O_NOFOLLOW|os.O_CLOEXEC)
        except FileNotFoundError:
            if required:
                raise ConfigError(f'missing required credential: {name}') from None
            continue
        with os.fdopen(fd, 'rb') as stream:
            if not stat.S_ISREG(os.fstat(stream.fileno()).st_mode):
                raise ConfigError('credential source is not a regular file')
            value = stream.read(65537)
        value = value.rstrip(b'\r\n')
        if len(value) > 65536 or b'\x00' in value or b'\n' in value or b'\r' in value:
            raise ConfigError(f'credential {name} is too large or contains invalid line breaks')
        if not value:
            if required:
                raise ConfigError(f'configure required credential: {name}')
            continue
        atomic_write(destination/name, value, 0o600)


def build_command(cfg: dict[str, Any], server: str, session: Path,
                  name: str, session_id: str, *, internal_check: bool = False) -> list[str]:
    specs = catalog()
    if server not in specs:
        raise ConfigError('unknown server')
    if not CONTAINER_RE.fullmatch(name) or not SESSION_RE.fullmatch(session_id):
        raise ConfigError('invalid container ownership identifier')
    image = cfg.get('IMAGE_ID', '')
    if not re.fullmatch(r'sha256:[a-f0-9]{64}', image):
        raise ConfigError('no immutable derived image ID; run make build first')
    spec = specs[server]
    browser = spec.get('browser', False)
    uid, gid = cfg['CONTAINER_UID'], cfg['CONTAINER_GID']
    args = podman(cfg) + [
        'run', '--rm', '--interactive', '--name', name,
        '--label', MANAGED_LABEL+'=true', '--label', 'io.codex-mcp.server='+server,
        '--label', 'io.codex-mcp.session='+session_id,
        '--label', 'io.codex-mcp.desktop='+str(cfg['DESKTOP_UID']),
        '--userns', f'keep-id:uid={uid},gid={gid}', '--user', 'devops:devops',
        '--read-only', '--cap-drop=all', '--security-opt=no-new-privileges',
        '--pids-limit', str(cfg['BROWSER_PIDS'] if browser else cfg['CONTAINER_PIDS']),
        '--memory', cfg['BROWSER_MEMORY'] if browser else cfg['CONTAINER_MEMORY'],
        '--memory-swap', cfg['BROWSER_MEMORY'] if browser else cfg['CONTAINER_MEMORY'],
        '--cpus', str(cfg['BROWSER_CPUS'] if browser else cfg['CONTAINER_CPUS']),
        '--stop-timeout', str(cfg['STOP_TIMEOUT_SECONDS']), '--log-driver=none',
        '--shm-size', cfg['BROWSER_SHM_SIZE'] if browser else '64m',
        '--network', cfg['MCP_NETWORK'] if spec['network'] else 'none',
        '--workdir', '/workspace',
        '--tmpfs', f'/tmp:rw,nosuid,nodev,size={cfg["TMPFS_SIZE"]},mode=1777',
        '--tmpfs', f'/home/devops:rw,nosuid,nodev,size=64m,mode=0700,uid={uid},gid={gid}',
        '--tmpfs', f'/workspace:rw,nosuid,nodev,size=16m,mode=0700,uid={uid},gid={gid}',
    ]
    if browser:
        args += ['--security-opt','seccomp='+cfg['MCP_CONFIG_DIR']+'/browser-seccomp.json']
    mounts, env = toolchain.mounts(cfg, session)
    # Replace the empty workspace tmpfs with an explicit bind only where needed.
    if spec['workspace'] != 'none':
        # Remove by exact target rather than depending on option ordering.
        for i in range(len(args)-1, 0, -1):
            if args[i].startswith('/workspace:') and args[i-1] == '--tmpfs':
                del args[i-1:i+1]
                break
        mounts.append((cfg['WORKSPACE'], '/workspace', spec['workspace'] == 'ro'))
    if spec['state']:
        mounts.append((str(Path(cfg['MCP_STATE_ROOT'])/server), '/state', False))
    mounts.append((str(session/'credentials'), '/run/mcp-credentials', True))
    # Bind parent scratch roots first, followed by read-only tool overlays.
    for source, target, readonly in mounts:
        if any(c in source+target for c in ',\n\r'):
            raise ConfigError('unsupported mount path')
        args += ['--mount', f'type=bind,source={source},destination={target},'
                 + ('ro=true' if readonly else 'rw=true') + ',bind-propagation=rprivate']
    public = {
        'GIT_CONFIG_NOSYSTEM': '1', 'GIT_CONFIG_GLOBAL': '/dev/null',
        'GIT_TERMINAL_PROMPT': '0', 'GIT_CONFIG_COUNT': '2',
        'GIT_CONFIG_KEY_0': 'safe.directory', 'GIT_CONFIG_VALUE_0': '/workspace',
        'GIT_CONFIG_KEY_1': 'safe.directory', 'GIT_CONFIG_VALUE_1': '/workspace/*',
        'MCP_TOOLCHAIN_REQUIRE_ALL': str(cfg['TOOLCHAIN_REQUIRE_ALL']).lower(),
        'LOCAL_TIMEZONE': cfg['LOCAL_TIMEZONE'],
        'MCP_BROWSER_NO_SANDBOX': str(cfg['BROWSER_NO_SANDBOX']).lower(),
        'MCP_POSTGRES_READONLY': str(cfg['POSTGRES_READONLY']).lower(),
        'MCP_POSTGRES_REQUIRE_TLS': str(cfg['POSTGRES_REQUIRE_TLS']).lower(),
        'MCP_SQLITE_READONLY': str(cfg['SQLITE_READONLY']).lower(),
        'MCP_FETCH_IGNORE_ROBOTS_TXT': str(cfg['FETCH_IGNORE_ROBOTS_TXT']).lower(),
        'MCP_FETCH_USER_AGENT': cfg['FETCH_USER_AGENT'], 'MCP_GIT_REPOSITORY': cfg['GIT_REPOSITORY'],
    }
    env.update(public)
    for key, value in sorted(env.items()):
        args += ['--env', key+'='+value]
    args += [image, '__toolchain-check' if internal_check else server]
    return args


def remove_container(cfg: dict[str, Any], name: str) -> bool:
    if not CONTAINER_RE.fullmatch(name):
        raise ConfigError('refusing to remove a non-owned container name')
    try:
        # Label verification protects against accidental name reuse; engine API
        # access by another devops-group member is inherently equivalent authority.
        result = run(podman(cfg)+['inspect', '--format', '{{json .Config.Labels}}', name],
                     env=clean_env(cfg), timeout=15, check=False)
        if result.returncode:
            exists = run(podman(cfg)+['container', 'exists', name],
                         env=clean_env(cfg), timeout=15, check=False)
            return exists.returncode == 1  # 125 is API failure, never "gone".
        labels = json.loads(result.stdout)
        if (labels.get(MANAGED_LABEL) != 'true'
            or labels.get('io.codex-mcp.desktop') != str(cfg['DESKTOP_UID'])
            or labels.get('io.codex-mcp.session') != name.rsplit('-',1)[1]):
            raise ConfigError('container ownership label mismatch')
        result = run(podman(cfg)+['rm', '--force', '--time', str(cfg['STOP_TIMEOUT_SECONDS']), name],
                     env=clean_env(cfg), timeout=cfg['STOP_TIMEOUT_SECONDS']+20, check=False)
        if result.returncode == 0:
            return True
        result = run(podman(cfg)+['container', 'exists', name], env=clean_env(cfg),
                     timeout=15, check=False)
        return result.returncode == 1
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
        return False


class Session:
    def __init__(self, cfg: dict[str, Any], server: str, instance: str = '') -> None:
        self.cfg, self.server, self.instance = cfg, server, instance
        self.id = uuid.uuid4().hex
        self.name = f'codex-mcp-{server}-{self.id}'
        self.path = Path(cfg['MCP_RUNTIME_ROOT'])/('session-'+self.id)
        self.stack = contextlib.ExitStack()
        self.started = False
        self.process: subprocess.Popen[bytes] | None = None

    def __enter__(self) -> 'Session':
        spec = catalog().get(self.server)
        if spec is None:
            raise ConfigError('unknown MCP server')
        try:
            root = Path(self.cfg['MCP_RUNTIME_ROOT'])
            if shutil.disk_usage(root).free < self.cfg['MIN_FREE_MIB']*1024**2:
                raise ConfigError('insufficient runtime free space')
            acquire_slot(self.stack, root/'locks', 'all', self.cfg['MAX_SESSIONS'])
            acquire_slot(self.stack, root/'locks', self.server,
                         1 if spec.get('exclusive') else self.cfg['MAX_SESSIONS_PER_SERVER'])
            self.path.mkdir(mode=0o700)
            self.stack.enter_context(locked(self.path/'active.lock'))
            atomic_write(self.path/'metadata.json', json.dumps({
                'id': self.id, 'name': self.name, 'server': self.server,
                'instance': self.instance, 'created': time.time(), 'pid': os.getpid()}))
            credential_source = os.environ.get('CREDENTIALS_DIRECTORY')
            if not credential_source:
                raise ConfigError('broker must be launched by systemd with LoadCredential')
            stage_credentials(Path(credential_source), self.path/'credentials', spec)
            return self
        except BaseException:
            self.stack.close()
            if self.path.exists():
                shutil.rmtree(self.path)
            raise

    def start(self) -> subprocess.Popen[bytes]:
        args = build_command(self.cfg, self.server, self.path, self.name, self.id)
        # Set started BEFORE spawning: a failed/interrupted client may have sent
        # a create request that the remote engine completes asynchronously.
        self.started = True
        self.process = subprocess.Popen(args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, env=clean_env(self.cfg),
                                        start_new_session=True, close_fds=True)
        return self.process

    def __exit__(self, *_: Any) -> None:
        gone = not self.started
        try:
            # Stop the client before querying final container ownership/state.
            if self.process is not None:
                if self.process.poll() is None:
                    self.process.terminate()
                    try:
                        self.process.wait(timeout=5)
                    except subprocess.TimeoutExpired:
                        self.process.kill(); self.process.wait(timeout=5)
                for stream in (self.process.stdin, self.process.stdout, self.process.stderr):
                    if stream is not None:
                        stream.close()
            if self.started:
                gone = remove_container(self.cfg, self.name)
            if gone:
                shutil.rmtree(self.path, ignore_errors=False)
        finally:
            if not gone:
                # Never remove live mount sources after an ambiguous API failure.
                print(json.dumps({'event':'cleanup_pending','session':self.id}),
                      file=__import__('sys').stderr, flush=True)
            self.stack.close()


def collect(cfg: dict[str, Any], instance: str | None = None, *, scan_engine: bool = True) -> dict[str, int]:
    removed = deferred = 0
    root = Path(cfg['MCP_RUNTIME_ROOT'])
    with locked(root/'gc.lock'):
        for path in sorted(root.glob('session-*')):
            sid = path.name.removeprefix('session-')
            if not SESSION_RE.fullmatch(sid) or path.is_symlink() or not path.is_dir():
                continue
            try:
                with locked(path/'active.lock'):
                    try:
                        meta = json.loads((path/'metadata.json').read_text())
                    except (OSError, ValueError):
                        # Do not guess ownership or delete unclassified objects.
                        deferred += 1; continue
                    if instance is not None and meta.get('instance') != instance:
                        continue
                    name = meta.get('name', '')
                    if not CONTAINER_RE.fullmatch(name) or meta.get('id') != sid:
                        deferred += 1; continue
                    if remove_container(cfg, name):
                        shutil.rmtree(path); removed += 1
                    else:
                        deferred += 1
            except (BlockingIOError, FileNotFoundError):
                continue
        # A reboot loses /run metadata. Reconcile ONLY our exact labels/names;
        # never run system prune or touch another deployment's containers.
        if scan_engine and instance is None:
            try:
                result = run(podman(cfg)+['ps','--all','--filter','label='+MANAGED_LABEL+'=true',
                    '--filter','label=io.codex-mcp.desktop='+str(cfg['DESKTOP_UID']),
                    '--format','{{.Names}}'],env=clean_env(cfg),timeout=20,check=False)
                if result.returncode:
                    deferred += 1
                else:
                    for name in result.stdout.decode('utf-8').splitlines():
                        if not CONTAINER_RE.fullmatch(name):
                            continue
                        sid = name.rsplit('-',1)[1]
                        if (root/('session-'+sid)).exists():
                            continue
                        if remove_container(cfg,name):
                            removed += 1
                        else:
                            deferred += 1
            except (OSError,subprocess.TimeoutExpired,UnicodeError):
                deferred += 1
    return {'removed':removed,'deferred':deferred}
