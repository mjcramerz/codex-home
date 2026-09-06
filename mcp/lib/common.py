"""Shared, dependency-free configuration and filesystem primitives (Python 3.12+)."""
from __future__ import annotations
import contextlib
import fcntl
import hashlib
import json
import os
from pathlib import Path
import pwd
import re
import stat
import subprocess
import tempfile
from typing import Any, Iterator

SOURCE_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = Path('/etc/codex/mcp/runtime.json')
CREDENTIALS = ('context7-api-key', 'postgres-dsn', 'semgrep-app-token',
               'openai-api-key', 'azure-openai-api-key', 'azure-openai-endpoint',
               'azure-openai-api-version', 'fetch-proxy-url', 'github-token')
SERVER_NAMES = ('filesystem', 'git', 'fetch', 'memory', 'sequential-thinking',
                'time', 'markdown', 'context7', 'playwright', 'chrome-devtools',
                'postgres', 'sqlite', 'semgrep')
SAFE_PATH = re.compile(r'/[A-Za-z0-9_./+@-]+\Z')
BOOL_KEYS = {'CAPTURE_SERVER_STDERR','BROWSER_NO_SANDBOX','TOOLCHAIN_ENABLED',
             'TOOLCHAIN_REQUIRE_ALL','WORKSPACE_EXISTING_ACL','TOOLCHAIN_READ_ACL',
             'SSH_ENABLED','POSTGRES_READONLY','POSTGRES_REQUIRE_TLS',
             'SQLITE_READONLY','FETCH_IGNORE_ROBOTS_TXT'}
INT_RANGES = {
 'CONTAINER_UID':(1,65535),'CONTAINER_GID':(1,65535), 'MAX_SESSIONS':(1,256),
 'MAX_SESSIONS_PER_SERVER':(1,32),'HEADER_TIMEOUT_SECONDS':(1,60),
 'CONNECT_TIMEOUT_SECONDS':(1,120),'IDLE_TIMEOUT_SECONDS':(60,86400),
 'SESSION_MAX_SECONDS':(60,604800),'STOP_TIMEOUT_SECONDS':(1,60),
 'STARTUP_TIMEOUT_SECONDS':(5,600),'TOOL_TIMEOUT_SECONDS':(5,3600),
 'MAX_BUFFER_BYTES':(4096,16777216),'MAX_STDERR_BYTES':(1024,1048576),
 'MIN_FREE_MIB':(32,1048576),'CONTAINER_CPUS':(1,128),'BROWSER_CPUS':(1,128),
 'CONTAINER_PIDS':(32,8192),'BROWSER_PIDS':(32,8192),'SSH_PORT':(1024,65535),
 'SSH_CONNECT_TIMEOUT_SECONDS':(1,120)}
PATH_KEYS = {'PODMAN_HOME','PODMAN_SOCKET','PODMAN_BINARY','WORKSPACE',
             'MCP_SOCKET','MCP_STATE_ROOT','MCP_RUNTIME_ROOT','MCP_CONFIG_DIR',
             'MCP_INSTALL_ROOT','TOOLCHAIN_PROFILE','HOST_NODE'}

class ConfigError(ValueError):
    """Invalid or unsafe deployment input."""


def parse_env(path: Path, *, expected: set[str] | None = None) -> dict[str, str]:
    """Parse a strict subset of dotenv, with no evaluation or expansion."""
    out: dict[str,str] = {}
    for number, line in enumerate(path.read_text(encoding='utf-8').splitlines(),1):
        line=line.strip()
        if not line or line.startswith('#'): continue
        if '=' not in line: raise ConfigError(f'{path.name}:{number}: expected KEY=value')
        key,value=line.split('=',1)
        if not re.fullmatch(r'[A-Z][A-Z0-9_]*',key): raise ConfigError(f'invalid key on line {number}')
        if key in out: raise ConfigError(f'duplicate key: {key}')
        if expected is not None and key not in expected: raise ConfigError(f'unknown key: {key}')
        value=value.strip()
        if value[:1] in ('"',"'"):
            if len(value)<2 or value[-1]!=value[0]: raise ConfigError(f'unclosed quote: {key}')
            value=value[1:-1]
        if any(ord(c)<32 or ord(c)==127 for c in value) or any(c in value for c in '$`\\'):
            raise ConfigError(f'control characters or shell substitutions in {key}')
        out[key]=value
    return out


def absolute_path(value: str, key: str) -> str:
    if not SAFE_PATH.fullmatch(value) or '..' in Path(value).parts or str(Path(value))!=value:
        raise ConfigError(f'{key} must be a normalized absolute path without whitespace or mount delimiters')
    if value in ('/','/home','/run','/data','/pool','/usr','/etc'):
        raise ConfigError(f'{key} is too broad')
    return value


def load_env(path: Path) -> dict[str, Any]:
    # defaults.keys is shipped separately, so editing .env cannot redefine its schema.
    keys=set(json.loads((SOURCE_ROOT/'env-keys.json').read_text()))
    raw=parse_env(path,expected=keys)
    missing=keys-raw.keys()
    if missing: raise ConfigError('missing settings: '+', '.join(sorted(missing)))
    result: dict[str,Any]=dict(raw)
    for k in BOOL_KEYS:
        if raw[k] not in ('true','false'): raise ConfigError(f'{k} must be true or false')
        result[k]=raw[k]=='true'
    for k,(lo,hi) in INT_RANGES.items():
        if not re.fullmatch(r'[0-9]+',raw[k]): raise ConfigError(f'{k} must be an integer')
        n=int(raw[k])
        if not lo<=n<=hi: raise ConfigError(f'{k} outside {lo}..{hi}')
        result[k]=n
    for k in PATH_KEYS:
        if raw[k]=='auto' and k in {'WORKSPACE','MCP_RUNTIME_ROOT'}: continue
        absolute_path(raw[k],k)
    absolute_path(raw['BROWSER_SECCOMP_BASE'],'BROWSER_SECCOMP_BASE')
    if raw['PODMAN_USER']!='devops' or raw['PODMAN_HOME']!='/data/accounts/devops':
        raise ConfigError('this deployment requires the preseed devops identity and home')
    if raw['PODMAN_SOCKET']!='/data/accounts/devops/run/podman.sock':
        raise ConfigError('use the preseed devops engine socket, not a rootful or alternate engine')
    if raw['MCP_STATE_ROOT']!='/pool/podman/mcp':
        raise ConfigError('state is scoped to /pool/podman/mcp in this deployment')
    if raw['PODMAN_BINARY']!='/usr/bin/podman': raise ConfigError('use the native /usr/bin/podman remote client')
    if raw['MCP_CONFIG_DIR']!='/etc/codex/mcp' or raw['MCP_INSTALL_ROOT']!='/usr/local/libexec/codex-mcp':
        raise ConfigError('root-managed install paths are fixed; update the source contract to relocate them')
    if raw['DESKTOP_USER']!='auto' and not re.fullmatch(r'[a-z_][a-z0-9_-]{0,31}',raw['DESKTOP_USER']):
        raise ConfigError('invalid DESKTOP_USER')
    if raw['MCP_TRANSPORT'] not in ('unix','ssh'): raise ConfigError('MCP_TRANSPORT must be unix or ssh')
    if raw['MCP_TRANSPORT']=='ssh' and not result['SSH_ENABLED']: raise ConfigError('SSH transport requires SSH_ENABLED=true')
    if not re.fullmatch(r'registry\.gitlab\.com/registry-containers/mcp-images/mcp@sha256:[a-f0-9]{64}',raw['MCP_BASE_IMAGE']):
        raise ConfigError('MCP_BASE_IMAGE must pin the supplied registry repository by full sha256 digest')
    if not re.fullmatch(r'sha256:[a-f0-9]{64}',raw['MCP_BASE_CONFIG_DIGEST']): raise ConfigError('invalid OCI configuration digest')
    if not re.fullmatch(r'localhost/[a-z0-9][a-z0-9/_.-]*:[a-z0-9][a-z0-9_.-]*',raw['MCP_DERIVED_IMAGE']):
        raise ConfigError('invalid local image tag')
    if not re.fullmatch(r'\d+\.\d+\.\d+',raw['DBHUB_PATCH_VERSION']) or tuple(map(int,raw['DBHUB_PATCH_VERSION'].split('.')))<(0,22,6):
        raise ConfigError('DBHub must be pinned to a fixed version >=0.22.6')
    for k in ('CONTAINER_MEMORY','BROWSER_MEMORY','TMPFS_SIZE','BROWSER_SHM_SIZE'):
        if not re.fullmatch(r'[1-9][0-9]{0,5}[mg]',raw[k]): raise ConfigError(f'invalid size: {k}')
    if not re.fullmatch(r'codex-mcp-[a-z0-9-]+',raw['MCP_NETWORK']): raise ConfigError('network name must start codex-mcp-')
    import ipaddress
    try:
        net=ipaddress.ip_network(raw['NETWORK_SUBNET'],strict=True)
        if not net.is_private or net.version!=4 or not 16<=net.prefixlen<=28: raise ValueError()
    except ValueError as e: raise ConfigError('NETWORK_SUBNET must be a private IPv4 subnet /16../28') from e
    from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
    try: ZoneInfo(raw['LOCAL_TIMEZONE'])
    except (ZoneInfoNotFoundError,ValueError) as e: raise ConfigError('unknown LOCAL_TIMEZONE') from e
    repo=raw['GIT_REPOSITORY']
    if repo and (repo.startswith('/') or '..' in Path(repo).parts or not re.fullmatch(r'[A-Za-z0-9_./-]+',repo)):
        raise ConfigError('GIT_REPOSITORY must be a relative path within Workspace')
    if not re.fullmatch(r'[A-Za-z0-9 ./_()-]{1,120}',raw['FETCH_USER_AGENT']): raise ConfigError('invalid FETCH_USER_AGENT')
    return result


def resolve_accounts(cfg: dict[str,Any], desktop: str | None = None) -> dict[str,Any]:
    cfg=dict(cfg)
    user=desktop or cfg['DESKTOP_USER']
    if user=='auto': user=os.environ.get('SUDO_USER') or pwd.getpwuid(os.getuid()).pw_name
    if user in ('root','devops'): raise ConfigError('select a real desktop account with DESKTOP_USER or --desktop-user')
    try: account=pwd.getpwnam(user); service=pwd.getpwnam('devops')
    except KeyError as e: raise ConfigError('desktop and preseed devops accounts must already exist') from e
    import grp
    if grp.getgrnam('devops').gr_gid != service.pw_gid:
        raise ConfigError('devops must use the devops primary group')
    if account.pw_uid<1000 or service.pw_dir!=cfg['PODMAN_HOME']:
        raise ConfigError('unexpected desktop UID or devops home')
    if service.pw_shell not in ('/usr/sbin/nologin','/sbin/nologin','/bin/false'):
        raise ConfigError('devops must remain a no-login service account')
    home=absolute_path(account.pw_dir,'desktop HOME')
    workspace=home+'/Workspace' if cfg['WORKSPACE']=='auto' else cfg['WORKSPACE']
    # This deployment intentionally shares only the selected user's Workspace.
    if workspace!=home+'/Workspace': raise ConfigError('WORKSPACE must be the desktop account HOME/Workspace')
    cfg.update(DESKTOP_USER=user,DESKTOP_UID=account.pw_uid,DESKTOP_GID=account.pw_gid,
               DESKTOP_HOME=home,DEVOPS_UID=service.pw_uid,DEVOPS_GID=service.pw_gid,
               WORKSPACE=workspace)
    if cfg['MCP_RUNTIME_ROOT']=='auto':cfg['MCP_RUNTIME_ROOT']=f'/run/user/{service.pw_uid}/codex-mcp'
    if cfg['MCP_RUNTIME_ROOT']!=f'/run/user/{service.pw_uid}/codex-mcp':
        raise ConfigError('staged credentials must be under the devops volatile runtime directory')
    if not cfg['MCP_SOCKET'].startswith(cfg['PODMAN_HOME']+'/run/'):
        raise ConfigError('MCP_SOCKET must remain visible on the preseed /data mount')
    return cfg


def load_runtime(path: Path = DEFAULT_CONFIG, *, trusted: bool = True) -> dict[str,Any]:
    if trusted:
        st=path.lstat()
        if not stat.S_ISREG(st.st_mode) or st.st_uid!=0 or st.st_mode & 0o022:
            raise ConfigError('runtime config must be a root-owned, non-writable regular file')
    cfg=json.loads(path.read_text())
    if cfg.get('schema_version')!=1:raise ConfigError('unsupported runtime schema')
    return cfg


def atomic_write(path: Path, data: str | bytes, mode: int = 0o600,
                 uid: int | None = None, gid: int | None = None) -> bool:
    """Same-filesystem write, fsync, replace, directory fsync; no symlink following."""
    path.parent.mkdir(parents=True,exist_ok=True)
    if path.is_symlink():raise ConfigError(f'refusing symlink target: {path}')
    payload=data.encode() if isinstance(data,str) else data
    if path.exists() and path.read_bytes()==payload:
        os.chmod(path,mode)
        if uid is not None:os.chown(path,uid,gid if gid is not None else -1)
        return False
    fd,name=tempfile.mkstemp(prefix='.'+path.name+'.',dir=path.parent)
    try:
        os.fchmod(fd,mode)
        if uid is not None:os.fchown(fd,uid,gid if gid is not None else -1)
        with os.fdopen(fd,'wb') as f:f.write(payload);f.flush();os.fsync(f.fileno())
        os.replace(name,path)
        dfd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try:os.fsync(dfd)
        finally:os.close(dfd)
    finally:
        with contextlib.suppress(FileNotFoundError):os.unlink(name)
    return True


@contextlib.contextmanager
def locked(path: Path, *, blocking: bool = False) -> Iterator[int]:
    path.parent.mkdir(parents=True,exist_ok=True,mode=0o700)
    fd=os.open(path,os.O_RDWR|os.O_CREAT|os.O_NOFOLLOW|os.O_CLOEXEC,0o600)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):raise ConfigError('lock must be a regular file')
        fcntl.flock(fd,fcntl.LOCK_EX | (0 if blocking else fcntl.LOCK_NB))
        yield fd
    finally:os.close(fd)


def podman(cfg: dict[str,Any]) -> list[str]:
    return [cfg['PODMAN_BINARY'],'--remote','--url=unix://'+cfg['PODMAN_SOCKET']]


def clean_env(cfg: dict[str,Any]) -> dict[str,str]:
    return {'PATH':'/usr/sbin:/usr/bin:/sbin:/bin','HOME':cfg['PODMAN_HOME'],
            'USER':'devops','LOGNAME':'devops','LANG':'C.UTF-8','LC_ALL':'C.UTF-8',
            'XDG_RUNTIME_DIR':f"/run/user/{cfg['DEVOPS_UID']}",
            'CONTAINERS_CONF':'/etc/podman-devops/client.conf'}


def run(argv: list[str], *, timeout: int = 30, env: dict[str,str] | None = None,
        check: bool = True, input_data: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    p=subprocess.run(argv,input=input_data,stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                     env=env,timeout=timeout,check=False)
    if check and p.returncode:
        # Do not include arbitrary subprocess stderr: credentials may appear in it.
        raise RuntimeError(f'{Path(argv[0]).name} failed (exit {p.returncode}); inspect target diagnostics')
    return p


def digest_tree(root: Path) -> str:
    h=hashlib.sha256()
    for p in sorted(root.rglob('*')):
        if p.is_file() and '__pycache__' not in p.parts and '.pyc'!=p.suffix:
            h.update(str(p.relative_to(root)).encode()+b'\0'+p.read_bytes()+b'\0')
    return h.hexdigest()
