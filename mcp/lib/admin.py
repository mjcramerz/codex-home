"""Explicit deployment commands; .env is data, never shell code."""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tarfile
import tempfile
import time
from common import (SOURCE_ROOT,CREDENTIALS,ConfigError,atomic_write,load_env,
                    load_runtime,locked,resolve_accounts,run)
from install import (as_devops,install,preflight,prepare,root_required,protected_directory)
from runtime import catalog


def image_id(value: str) -> str:
    value = value.removeprefix('sha256:')
    if not re.fullmatch(r'[a-f0-9]{64}',value):
        raise ConfigError('invalid image ID returned by Podman')
    return 'sha256:'+value


def pull(cfg: dict) -> None:
    as_devops(cfg,['pull',cfg['MCP_BASE_IMAGE']],timeout=1800)
    images = json.loads(as_devops(cfg,['image','inspect',cfg['MCP_BASE_IMAGE']]).stdout)
    if len(images)!=1 or image_id(images[0]['Id'])!=cfg['MCP_BASE_CONFIG_DIGEST']:
        raise ConfigError('base image configuration digest does not match the supplied image; refusing to build')
    print('Verified public base image manifest reference and configuration digest.')


def build(cfg: dict) -> None:
    root_required()
    # Source is the root-owned, installed release, not a desktop-writable build context.
    source = Path(cfg['MCP_INSTALL_ROOT'])/'releases'/cfg['RELEASE_SHA256']
    pull(cfg)
    args = ['build','--pull=never','--no-cache','--layers=false','--file',str(source/'container/Containerfile'),
            '--tag',cfg['MCP_DERIVED_IMAGE'],'--build-arg','BASE_IMAGE='+cfg['MCP_BASE_IMAGE'],
            '--build-arg','DBHUB_PATCH_VERSION='+cfg['DBHUB_PATCH_VERSION'],
            '--build-arg','CONTAINER_UID='+str(cfg['CONTAINER_UID']),
            '--build-arg','CONTAINER_GID='+str(cfg['CONTAINER_GID']),str(source)]
    result = as_devops(cfg,args,timeout=1800)
    images = json.loads(as_devops(cfg,['image','inspect',cfg['MCP_DERIVED_IMAGE']]).stdout)
    ident = image_id(images[0]['Id'])
    # Verify the patched package version and nonroot identity inside the actual image.
    script = 'import json,os,pwd; from pathlib import Path; assert os.geteuid()!=0; assert pwd.getpwuid(os.geteuid()).pw_name=="devops"; assert all(os.access("/usr/local/bin/"+v["executable"],os.X_OK) for v in json.load(open("/opt/codex-mcp/servers.json")).values()); assert os.access("/usr/local/bin/chrome-for-mcp",os.X_OK); print(json.load(open("/opt/mcp-node/node_modules/@bytebase/dbhub/package.json"))["version"])'
    probe = as_devops(cfg,['run','--rm','--network=none','--read-only','--cap-drop=all',
          '--security-opt=no-new-privileges','--entrypoint=/usr/bin/python3',ident,'-I','-c',script])
    if probe.stdout.decode().strip()!=cfg['DBHUB_PATCH_VERSION']:
        raise ConfigError('patched image verification failed')
    cfg = dict(cfg,IMAGE_ID=ident)
    atomic_write(Path(cfg['MCP_CONFIG_DIR'])/'runtime.json',json.dumps(cfg,indent=2)+'\n',0o644)
    # Record the resolved transitive npm lock instead of claiming dependency reproducibility.
    npm_lock = as_devops(cfg,['run','--rm','--network=none','--read-only','--entrypoint=/bin/cat',
                             ident,'/opt/mcp-node/package-lock.json']).stdout
    atomic_write(Path(cfg['MCP_CONFIG_DIR'])/'built-package-lock.json',npm_lock,0o644)
    attestation = {'built_at_unix':time.time(),'image_id':ident,'base':cfg['MCP_BASE_IMAGE'],
                   'base_config_digest':cfg['MCP_BASE_CONFIG_DIGEST'],
                   'dbhub_version':cfg['DBHUB_PATCH_VERSION'],'release':cfg['RELEASE_SHA256'],
                   'npm_lock_sha256':hashlib.sha256(npm_lock).hexdigest(),
                   'build_log_sha256':hashlib.sha256(result.stdout+result.stderr).hexdigest()}
    atomic_write(Path(cfg['MCP_CONFIG_DIR'])/'image-attestation.json',json.dumps(attestation,indent=2)+'\n',0o644)
    network(cfg)
    print('Built and pinned derived image '+ident)


def network(cfg: dict) -> None:
    name = cfg['MCP_NETWORK']
    result = as_devops(cfg,['network','inspect',name],check=False)
    if result.returncode:
        as_devops(cfg,['network','create','--label','io.codex-mcp.managed=true',
                      '--subnet',cfg['NETWORK_SUBNET'],name])
        result = as_devops(cfg,['network','inspect',name])
    entries = json.loads(result.stdout)
    item = entries[0]
    if ((item.get('labels') or {}).get('io.codex-mcp.managed')!='true'
        or cfg['NETWORK_SUBNET'] not in [s.get('subnet') for s in item.get('subnets',[])]):
        raise ConfigError('existing network name is not owned by this deployment or has a different subnet')


def credential(cfg: dict, name: str, path: Path | None) -> None:
    root_required()
    if name not in CREDENTIALS:
        raise ConfigError('unknown credential name')
    if path is None:
        import getpass
        data = getpass.getpass('Value for '+name+' (input hidden): ').encode()
    else:
        fd = os.open(path,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK|os.O_CLOEXEC)
        with os.fdopen(fd,'rb') as source:
            st = os.fstat(source.fileno())
            if not stat.S_ISREG(st.st_mode) or st.st_mode & 0o077:
                raise ConfigError('credential import must be a private regular file')
            if st.st_size > 65538:
                raise ConfigError('credential import is too large')
            data = source.read(65539).rstrip(b'\r\n')
    if not data or len(data)>65536 or any(b in data for b in (b'\x00',b'\r',b'\n')):
        raise ConfigError('credential must be nonempty, single-line, and at most 65536 bytes')
    try:
        data.decode('utf-8')
    except UnicodeError:
        raise ConfigError('credential must be UTF-8 text') from None
    # No secret value is accepted on a command line, written to stdout, or copied into .env.
    atomic_write(Path(cfg['MCP_CONFIG_DIR'])/'credentials'/name,data,0o600,0,0)
    print(name+' updated atomically. Reconnect affected MCP sessions to load it.')


def doctor(cfg: dict) -> int:
    findings = []
    def item(name: str, okay: bool, detail: str = '') -> None:
        findings.append({'check':name,'ok':okay,'detail':detail})
    for error in preflight(cfg):
        item('preflight',False,error)
    item('immutable_image',bool(re.fullmatch(r'sha256:[a-f0-9]{64}',cfg.get('IMAGE_ID',''))))
    for name in ('codex-mcp.target','codex-mcp.socket'):
        p = run(['/usr/bin/systemctl','is-active',name],check=False)
        item(name,p.returncode==0)
    credentials = Path(cfg['MCP_CONFIG_DIR'])/'credentials'
    for name,spec in catalog().items():
        for key in spec.get('required_credentials',[]):
            p = credentials/key
            item(name+'.credential',p.exists() and p.stat().st_size>0,key)
    from toolchain import coverage
    report = {'checks':findings,'toolchain':coverage(cfg),
              'note':'No API keys, database DSNs, tool payloads or full Podman inspect output are printed.'}
    print(json.dumps(report,indent=2))
    return int(any(not x['ok'] for x in findings))


def toolchain_check(cfg: dict) -> int:
    root_required()
    # A dedicated transient system service keeps the check under the devops identity.
    # No systemd credentials are loaded, and the special command is unavailable to clients.
    command = ['/usr/bin/systemd-run','--quiet','--wait','--pipe','--collect',
               '--unit=codex-mcp-toolchain-check','--property=User=devops',
               '--property=Group=devops','--property=UMask=0077',
               cfg['MCP_INSTALL_ROOT']+'/current/bin/codex-mcp-admin','toolchain-check-worker']
    result = subprocess.run(command,check=False)
    return result.returncode


def toolchain_worker(cfg: dict) -> int:
    if os.geteuid()!=cfg['DEVOPS_UID']:
        raise ConfigError('toolchain worker must run as devops')
    import uuid
    from runtime import build_command,remove_container
    from common import clean_env
    sid = uuid.uuid4().hex
    root = Path(cfg['MCP_RUNTIME_ROOT'])/('session-'+sid)
    root.mkdir(mode=0o700)
    name = 'codex-mcp-filesystem-'+sid
    with locked(root/'active.lock'):
        atomic_write(root/'metadata.json',json.dumps({'id':sid,'name':name,'server':'filesystem',
                    'instance':'toolchain-check','created':time.time(),'pid':os.getpid()}))
        (root/'credentials').mkdir(mode=0o700)
        gone = False
        try:
            args = build_command(cfg,'filesystem',root,name,sid,internal_check=True)
            # The check only invokes fixed --version commands; make Workspace read-only too.
            args = [x.replace('destination=/workspace,rw=true','destination=/workspace,ro=true') for x in args]
            result = run(args,timeout=360,env=clean_env(cfg),check=False)
            # entrypoint emits only structured per-executable version diagnostics.
            sys.stdout.buffer.write(result.stdout)
            return result.returncode
        finally:
            gone = remove_container(cfg,name)
            if gone:
                shutil.rmtree(root)


def quiesce(cfg: dict) -> None:
    """A consistent snapshot requires a stopped target AND no managed containers."""
    run(['/usr/bin/systemctl','stop','codex-mcp.target'])
    result = as_devops(cfg,['ps','--all','--filter','label=io.codex-mcp.managed=true',
                           '--filter','label=io.codex-mcp.desktop='+str(cfg['DESKTOP_UID']),
                           '--format','{{.Names}}'])
    if result.stdout.strip():
        raise ConfigError('managed containers remain after stopping; resolve cleanup before backup/restore')


def backup(cfg: dict, destination: Path) -> None:
    root_required()
    if destination.exists() or destination.is_symlink():
        raise ConfigError('backup destination must not exist')
    quiesce(cfg)
    state = Path(cfg['MCP_STATE_ROOT'])
    if not state.exists():
        raise ConfigError('state directory is missing')
    destination = destination.absolute()
    parent_mode=stat.S_IMODE(destination.parent.lstat().st_mode) if destination.parent.exists() else 0o700
    protected_directory(destination.parent,parent_mode)
    fd, temporary_name = tempfile.mkstemp(prefix='.codex-mcp-backup-',dir=destination.parent)
    temporary = Path(temporary_name)
    os.fchmod(fd,0o600)
    try:
        # Read service-controlled state as devops, never as root. A malicious
        # concurrent symlink change therefore cannot disclose root-only files.
        program = r"""
import sys,tarfile
from pathlib import Path
state=Path(sys.argv[1])
def safe(info):
 if not(info.isfile() or info.isdir()):raise ValueError('links and special files are not backup data')
 return info
with tarfile.open(fileobj=sys.stdout.buffer,mode='w|gz') as tar:
 for name in ('memory','sqlite'):
  tar.add(state/name,arcname='state/'+name,filter=safe)
"""
        with os.fdopen(fd,'wb') as stream:
            result = subprocess.run(['/usr/sbin/runuser','-u','devops','--',
                '/usr/bin/python3','-I','-c',program,str(state)],stdout=stream,
                stderr=subprocess.PIPE,timeout=600,check=False)
            if result.returncode:
                raise ConfigError('state backup failed; no partial archive retained')
            stream.flush(); os.fsync(stream.fileno())
        # Link publication is atomic and refuses to overwrite an existing backup.
        os.link(temporary,destination,follow_symlinks=False)
        directory_fd=os.open(destination.parent,os.O_RDONLY|os.O_DIRECTORY)
        try:os.fsync(directory_fd)
        finally:os.close(directory_fd)
    finally:
        temporary.unlink(missing_ok=True)
    print('State backed up to '+str(destination)+'. Services remain stopped; run make up.')


def restore(cfg: dict, archive: Path) -> None:
    root_required()
    quiesce(cfg)
    root = Path(cfg['MCP_STATE_ROOT'])
    if any((root/name).exists() and any((root/name).iterdir()) for name in ('memory','sqlite')):
        raise ConfigError('restore requires empty memory/sqlite state; preserve existing data first')
    with tarfile.open(archive,'r:*') as tar:
        total = 0
        members=[]
        for info in tar:
            members.append(info)
            if len(members)>100000:
                raise ConfigError('backup exceeds the 100000 member restore limit')
            p = Path(info.name)
            if (p.is_absolute() or '..' in p.parts or not p.parts or p.parts[0]!='state'
                or not (info.isfile() or info.isdir())):
                raise ConfigError('unsafe backup member')
            if len(p.parts)>1 and p.parts[1] not in ('memory','sqlite'):
                raise ConfigError('unexpected state directory')
            total += info.size
            if total>10*1024**3:
                raise ConfigError('backup exceeds the 10 GiB restore limit')
        # Never restore ownership from an archive supplied by a caller.
        with tempfile.TemporaryDirectory(prefix='codex-mcp-restore-',dir=root.parent) as temp:
            tar.extractall(temp,members=members,filter='data')
            for name in ('memory','sqlite'):
                source = Path(temp)/'state'/name
                if not source.is_dir():
                    continue
                # Set ownership while files remain under the root-only staging
                # directory, before publishing into service-writable state.
                for p in [source,*source.rglob('*')]:
                    os.chown(p,cfg['DEVOPS_UID'],cfg['DEVOPS_GID'])
                    os.chmod(p,0o700 if p.is_dir() else 0o600)
                target = root/name
                target.rmdir()
                os.replace(source,target)
    print('State restored. Services remain stopped; run make up.')


def uninstall(cfg: dict) -> None:
    root_required()
    run(['/usr/bin/systemctl','disable','--now','codex-mcp.target'],check=False)
    for path in (SOURCE_ROOT/'systemd').glob('*.in'):
        (Path('/etc/systemd/system')/path.name.removesuffix('.in')).unlink(missing_ok=True)
    for name in ('codex-mcp','codex-mcp-admin'):
        path = Path('/usr/local/bin')/name
        if path.is_symlink() and str(path.readlink()).startswith(cfg['MCP_INSTALL_ROOT']+'/'):
            path.unlink()
    base = Path('/etc/apparmor.d/abstractions/managed-codex-runtime')
    if base.exists():
        text = base.read_text().replace('\n# codex-mcp managed include\n  #include if exists <abstractions/codex-mcp-client>\n','')
        atomic_write(base,text,0o644)
    Path('/etc/apparmor.d/abstractions/codex-mcp-client').unlink(missing_ok=True)
    for name in ('managed-desktop-wrappers','chatgpt'):
        path = Path('/etc/apparmor.d')/name
        if path.exists():
            run(['/usr/sbin/apparmor_parser','-r',str(path)])
    run(['/usr/bin/systemctl','daemon-reload'])
    print('Units and client links removed. State, credentials, image, network, releases, keys and ACL backups are retained.')
    print('Review docs/OPERATIONS.md before removing retained data or restoring ACLs.')


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--env',type=Path,default=SOURCE_ROOT/'.env')
    parser.add_argument('--desktop-user')
    parser.add_argument('operation',choices=['preflight','install','prepare','pull','build','up','down',
        'restart','status','logs','doctor','credential','toolchain-check','toolchain-check-worker',
        'backup','restore','uninstall'])
    parser.add_argument('--name',choices=CREDENTIALS)
    parser.add_argument('--file',type=Path)
    args = parser.parse_args()
    if args.operation=='preflight':
        cfg = resolve_accounts(load_env(args.env),args.desktop_user)
        errors = preflight(cfg)
        print(json.dumps({'ok':not errors,'errors':errors},indent=2))
        return int(bool(errors))
    if args.operation=='install':
        cfg = install(args.env,args.desktop_user)
        print('Installed protected release '+cfg['RELEASE_SHA256']+'. Build image and start target next.')
        return 0
    if args.operation in {'pull','build','up','restart','down','credential','backup','restore','uninstall'}:
        root_required()
        # Fixed, protected directory: do not choose a lock using stale runtime data.
        with locked(Path('/etc/codex/mcp/admin.lock'),blocking=True):
            return dispatch(args,parser,load_runtime())
    return dispatch(args,parser,load_runtime())


def dispatch(args, parser, cfg) -> int:
    op = args.operation
    if op=='prepare': prepare(cfg)
    elif op in ('pull','build'):
        root_required()
        pull(cfg) if op=='pull' else build(cfg)
    elif op in ('up','restart','down'):
        root_required()
        if op!='down':
            if not cfg.get('IMAGE_ID'):
                raise ConfigError('build the patched image before starting services')
            network(cfg)
        if op=='up': command=['enable','--now','codex-mcp.target']
        elif op=='down': command=['stop','codex-mcp.target']
        else: command=['restart','codex-mcp.target']
        subprocess.run(['/usr/bin/systemctl',*command],check=True)
    elif op=='status':
        return subprocess.run(['/usr/bin/systemctl','--no-pager','status','codex-mcp.target','codex-mcp.socket','codex-mcp-gc.timer'],check=False).returncode
    elif op=='logs':
        return subprocess.run(['/usr/bin/journalctl','--no-pager','-n','100','-t','codex-mcp'],check=False).returncode
    elif op=='doctor': return doctor(cfg)
    elif op=='credential':
        if not args.name: parser.error('--name is required')
        credential(cfg,args.name,args.file)
    elif op=='toolchain-check': return toolchain_check(cfg)
    elif op=='toolchain-check-worker': return toolchain_worker(cfg)
    elif op in ('backup','restore'):
        if not args.file: parser.error('--file is required')
        backup(cfg,args.file) if op=='backup' else restore(cfg,args.file)
    elif op=='uninstall': uninstall(cfg)
    return 0
