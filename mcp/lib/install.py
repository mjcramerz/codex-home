"""Root installation, protected versioned releases, ACL integration and SSH keys."""
from __future__ import annotations
import grp
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import tempfile
from typing import Any
from common import (SOURCE_ROOT,CREDENTIALS,ConfigError,atomic_write,clean_env,
                    digest_tree,load_env,locked,podman,resolve_accounts,run)
import toolchain

DEPENDENCIES = ('python3','podman','systemctl','loginctl','setfacl','getfacl',
                'runuser','ssh-keygen','sshd','apparmor_parser')


def root_required() -> None:
    if os.geteuid() != 0:
        raise ConfigError('this operation requires root; use sudo make <target>')


def protected_directory(path: Path, mode: int = 0o755) -> None:
    """Reject symlink/non-root-writable ancestry before writing privileged files."""
    for parent in reversed([path,*path.parents]):
        if parent == Path('/'):
            continue
        if not parent.exists():
            parent.mkdir(mode=mode if parent == path else 0o755)
        st = parent.lstat()
        if not stat.S_ISDIR(st.st_mode) or st.st_uid != 0 or st.st_mode & 0o022:
            raise ConfigError('unsafe root-managed directory: '+str(parent))
    os.chmod(path,mode)


def owned_directory(path: Path, uid: int, gid: int, mode: int) -> None:
    if path.is_symlink():
        raise ConfigError('refusing symlink directory: '+str(path))
    path.mkdir(parents=True,exist_ok=True,mode=mode)
    if not path.is_dir():
        raise ConfigError('not a directory: '+str(path))
    os.chown(path,uid,gid); os.chmod(path,mode)


def preflight(cfg: dict[str,Any], *, need_engine: bool = True) -> list[str]:
    errors: list[str] = []
    for command in DEPENDENCIES:
        if shutil.which(command) is None:
            errors.append('missing executable: '+command)
    if not Path('/run/systemd/system').is_dir():
        errors.append('a running systemd system manager is required')
    if not Path('/sys/fs/cgroup/cgroup.controllers').exists():
        errors.append('unified cgroup v2 is required')
    if not Path('/etc/podman-devops/client.conf').is_file():
        errors.append('preseed Podman client configuration is missing')
    for name in ('subuid','subgid'):
        try:
            lines = Path('/etc/'+name).read_text().splitlines()
            if not any(line.startswith('devops:') and int(line.rsplit(':',1)[1])>=65536 for line in lines):
                errors.append('devops requires at least 65536 subordinate IDs in /etc/'+name)
        except (OSError,ValueError):
            errors.append('cannot validate /etc/'+name)
    try:
        groups = os.getgrouplist(cfg['DESKTOP_USER'],cfg['DESKTOP_GID'])
        if cfg['DEVOPS_GID'] not in groups:
            errors.append('desktop account is not in the trusted devops group')
    except OSError:
        errors.append('cannot resolve desktop groups')
    profile = Path(cfg['TOOLCHAIN_PROFILE'])
    if not profile.is_file():
        errors.append('installed devops profile is missing')
    elif hashlib.sha256(profile.read_bytes()).digest() != hashlib.sha256(
            (SOURCE_ROOT/'integration/71-devops-de.sh.reference').read_bytes()).digest():
        errors.append('installed devops profile differs from audited reference; review/rebase integration first')
    seccomp=Path(cfg['BROWSER_SECCOMP_BASE'])
    try:
        st=seccomp.lstat()
        if not stat.S_ISREG(st.st_mode) or st.st_uid!=0 or st.st_mode&0o022:
            raise ValueError()
        from browser_security import derive_profile
        derive_profile(json.loads(seccomp.read_text()))
    except (OSError,ValueError,ConfigError):
        errors.append('protected deny-default browser seccomp baseline is unavailable or invalid')
    if not Path(cfg['HOST_NODE']).is_file():
        errors.append('configured host Node executable is missing')
    home = Path(cfg['DESKTOP_HOME'])
    if home.is_symlink() or home.resolve() != home:
        errors.append('desktop HOME must have direct, non-symlink ancestry')
    workspace = Path(cfg['WORKSPACE'])
    if workspace.is_symlink() or (workspace.exists() and workspace.resolve()!=workspace):
        errors.append('Workspace must be a direct directory, not a symlink')
    socket_path = Path(cfg['PODMAN_SOCKET'])
    try:
        st = socket_path.lstat()
        if not stat.S_ISSOCK(st.st_mode) or st.st_uid!=cfg['DEVOPS_UID'] or st.st_gid!=cfg['DEVOPS_GID'] or st.st_mode&0o007:
            errors.append('Podman socket identity/mode does not match the preseed boundary')
    except OSError:
        errors.append('preseed devops engine socket is unavailable')
    if need_engine and Path(cfg['PODMAN_BINARY']).is_file():
        try:
            p = as_devops(cfg,['version','--format','json'])
            version = json.loads(p.stdout)['Server']['Version']
            info = json.loads(as_devops(cfg,['info','--format','json']).stdout)
            if info.get('host',{}).get('security',{}).get('rootless') is not True:
                errors.append('the configured engine is not confirmed rootless')
            nums = tuple(int(n) for n in re.match(r'(\d+)\.(\d+)\.(\d+)',version).groups())
            if nums < (5,8,6):
                errors.append('Podman server >=5.8.6 is required by this preseed integration')
        except (OSError,ValueError,KeyError,AttributeError,RuntimeError,subprocess.TimeoutExpired):
            errors.append('cannot confirm the existing rootless Podman server version')
    return errors


def as_devops(cfg: dict[str,Any], args: list[str], *, timeout: int = 60,
              check: bool = True, input_data: bytes | None = None) -> subprocess.CompletedProcess[bytes]:
    prefix = ['/usr/sbin/runuser','-u','devops','--'] if os.geteuid()==0 else []
    if not prefix and os.geteuid()!=cfg['DEVOPS_UID']:
        raise ConfigError('Podman administration requires root or devops')
    return run(prefix+podman(cfg)+args,timeout=timeout,env=clean_env(cfg),
               check=check,input_data=input_data)


def prepare(cfg: dict[str,Any]) -> None:
    root_required()
    uid,gid = cfg['DEVOPS_UID'],cfg['DEVOPS_GID']
    parent = Path('/run/user')/str(uid)
    st = parent.lstat()
    if not stat.S_ISDIR(st.st_mode) or st.st_uid != uid or stat.S_IMODE(st.st_mode)!=0o700:
        raise ConfigError('devops user runtime must be created by logind and mode 0700')
    # Do not chmod/chown through service-writable runtime ancestry as root.
    # Only the root-owned state parent is used for a privileged creation.
    state = Path(cfg['MCP_STATE_ROOT'])
    if state.parent.resolve()!=state.parent:
        raise ConfigError('state root requires direct ancestry')
    protected_directory(state.parent,0o711)
    owned_directory(state,uid,gid,0o700)
    program = r"""
import os,stat,sys
from pathlib import Path
for item in sys.argv[1:]:
 p=Path(item)
 if p.is_symlink():raise ValueError('symlink service directory')
 p.mkdir(mode=0o700,exist_ok=True)
 fd=os.open(p,os.O_RDONLY|os.O_DIRECTORY|os.O_NOFOLLOW)
 try:
  if os.fstat(fd).st_uid!=os.geteuid():raise ValueError('wrong service directory owner')
  os.fchmod(fd,0o700)
 finally:os.close(fd)
"""
    run(['/usr/sbin/runuser','-u','devops','--','/usr/bin/python3','-I','-c',program,
         cfg['MCP_RUNTIME_ROOT'],str(Path(cfg['MCP_RUNTIME_ROOT'])/'locks'),
         str(state/'memory'),str(state/'sqlite')],env=clean_env(cfg))
    if cfg['SSH_ENABLED']:
        protected_directory(Path('/run/sshd'),0o755)


def render_units(cfg: dict[str,Any]) -> dict[str,str]:
    replacements = {k:str(v) for k,v in cfg.items()}
    replacements.update(CURRENT=cfg['MCP_INSTALL_ROOT']+'/current',
        SSH_WANT='codex-mcp-sshd.service' if cfg['SSH_ENABLED'] else '',
        SYSTEMD_SESSION_MAX=str(cfg['SESSION_MAX_SECONDS']+60),
        LOAD_CREDENTIALS='\n'.join('LoadCredential='+name+':/etc/codex/mcp/credentials/'+name for name in CREDENTIALS))
    units = {}
    for path in sorted((SOURCE_ROOT/'systemd').glob('*.in')):
        text = re.sub(r'@([A-Z_]+)@',lambda m:replacements[m[1]],path.read_text())
        units[path.name.removesuffix('.in')] = text
    return units


def grant_acls(cfg: dict[str,Any]) -> None:
    """Only Workspace gets write permission. Tool installation trees are read-only."""
    workspace = Path(cfg['WORKSPACE'])
    if not workspace.exists():
        workspace.mkdir(mode=0o700)
        os.chown(workspace,cfg['DESKTOP_UID'],cfg['DESKTOP_GID'])
    if workspace.is_symlink() or workspace.stat().st_uid != cfg['DESKTOP_UID']:
        raise ConfigError('Workspace must be owned by the selected desktop user')
    backup = Path(cfg['MCP_CONFIG_DIR'])/'acl-backups'
    protected_directory(backup,0o700)
    ws_backup = backup/'workspace.acl'
    if not ws_backup.exists():
        p = run(['/usr/bin/getfacl','-R','-P','--absolute-names',str(workspace)],timeout=300)
        atomic_write(ws_backup,p.stdout,0o600)
    # ACL traversal does not grant directory listing or read access to HOME.
    ancestors = []
    for parent in workspace.parents:
        if parent == Path('/'):
            break
        if parent.stat().st_mode & 0o001 == 0:
            ancestors.append(str(parent))
    if ancestors:
        ancestor_backup = backup/'traversal.acl'
        if not ancestor_backup.exists():
            atomic_write(ancestor_backup,run(['/usr/bin/getfacl','--absolute-names',*ancestors]).stdout)
        run(['/usr/bin/setfacl','-m',f'u:{cfg["DEVOPS_UID"]}:--x',*ancestors])
    # Defaults ensure both users can edit newly created files even with umask 077.
    access = f'u:{cfg["DEVOPS_UID"]}:rwX,u:{cfg["DESKTOP_UID"]}:rwX'
    defaults = f'd:u:{cfg["DEVOPS_UID"]}:rwx,d:u:{cfg["DESKTOP_UID"]}:rwx'
    run(['/usr/bin/setfacl','-m',access+','+defaults,str(workspace)])
    if cfg['WORKSPACE_EXISTING_ACL']:
        run(['/usr/bin/setfacl','-R','-P','-m',access,str(workspace)],timeout=300)
        # Apply default ACLs only to directories; do not depend on setfacl's
        # treatment of ordinary files during recursive default-ACL operations.
        pending = []
        for current, dirs, _ in os.walk(workspace,followlinks=False):
            dirs[:] = [d for d in dirs if not (Path(current)/d).is_symlink()]
            pending.append(current)
            if len(pending)==128:
                run(['/usr/bin/setfacl','-P','-m',defaults,*pending],timeout=300)
                pending=[]
        if pending:
            run(['/usr/bin/setfacl','-P','-m',defaults,*pending],timeout=300)
    if cfg['TOOLCHAIN_ENABLED'] and cfg['TOOLCHAIN_READ_ACL']:
        for item in toolchain.host_roots(cfg):
            source = Path(item['source'])
            if item['kind']!='user' or not source.exists():
                continue
            if source.resolve()!=source or source.is_symlink():
                raise ConfigError('symlink tool root requires manual review: '+str(source))
            saved = backup/('tool-'+hashlib.sha256(str(source).encode()).hexdigest()[:16]+'.acl')
            if not saved.exists():
                atomic_write(saved,run(['/usr/bin/getfacl','-R','-P','--absolute-names',str(source)],timeout=300).stdout)
            run(['/usr/bin/setfacl','-R','-P','-m',f'u:{cfg["DEVOPS_UID"]}:r-X',str(source)],timeout=300)
            for ancestor in source.parents:
                if str(ancestor) in ('/pool','/'):
                    break
                key = backup/('ancestor-'+hashlib.sha256(str(ancestor).encode()).hexdigest()[:16]+'.acl')
                if not key.exists():
                    atomic_write(key,run(['/usr/bin/getfacl','--absolute-names',str(ancestor)]).stdout)
                run(['/usr/bin/setfacl','-m',f'u:{cfg["DEVOPS_UID"]}:--x',str(ancestor)])



def desktop_file(cfg: dict[str,Any], path: Path, data: bytes, mode: int) -> None:
    """Drop to the desktop UID before touching its mutable home-directory tree."""
    program = r"""
import os,sys,tempfile
from pathlib import Path
p=Path(sys.argv[1]);mode=int(sys.argv[2],8)
parent=p.parent
if parent.is_symlink():raise ValueError('symlink .ssh directory')
parent.mkdir(mode=0o700,parents=True,exist_ok=True)
if parent.stat().st_uid!=os.getuid():raise ValueError('wrong .ssh owner')
os.chmod(parent,0o700)
if p.is_symlink():raise ValueError('symlink identity file')
fd,tmp=tempfile.mkstemp(prefix='.codex-mcp-key-',dir=parent)
try:
 os.fchmod(fd,mode)
 with os.fdopen(fd,'wb') as f:f.write(sys.stdin.buffer.read(65537));f.flush();os.fsync(f.fileno())
 os.replace(tmp,p)
finally:
 if os.path.exists(tmp):os.unlink(tmp)
"""
    run(['/usr/sbin/runuser','-u',cfg['DESKTOP_USER'],'--','/usr/bin/python3','-I','-c',
         program,str(path),oct(mode)[2:]],input_data=data,
        env={'PATH':'/usr/bin:/bin','HOME':cfg['DESKTOP_HOME']})


def install_ssh(cfg: dict[str,Any]) -> dict[str,Any]:
    root = Path(cfg['MCP_CONFIG_DIR'])
    ssh = root/'ssh'
    protected_directory(ssh,0o755)
    host = ssh/'ssh_host_ed25519_key'
    if not host.exists():
        run(['/usr/bin/ssh-keygen','-q','-t','ed25519','-N','','-f',str(host)])
    if host.is_symlink() or host.stat().st_uid!=0:
        raise ConfigError('unsafe existing SSH host key')
    os.chmod(host,0o600)
    # Generate an unencrypted automation key, pinned and forced-command restricted.
    userdir = Path(cfg['DESKTOP_HOME'])/'.ssh'
    if userdir.is_symlink():
        raise ConfigError('desktop .ssh must be a direct directory')
    key = userdir/'codex-mcp_ed25519'
    if not key.exists():
        with tempfile.TemporaryDirectory(prefix='mcp-key-',dir=ssh) as tmp:
            generated = Path(tmp)/'key'
            run(['/usr/bin/ssh-keygen','-q','-t','ed25519','-N','','-C','codex-mcp-local','-f',str(generated)])
            desktop_file(cfg,key,generated.read_bytes(),0o600)
            desktop_file(cfg,Path(str(key)+'.pub'),Path(str(generated)+'.pub').read_bytes(),0o644)
    if key.is_symlink() or key.stat().st_uid!=cfg['DESKTOP_UID'] or key.stat().st_mode&0o077:
        raise ConfigError('unsafe existing MCP SSH key')
    public = run(['/usr/sbin/runuser','-u',cfg['DESKTOP_USER'],'--',
                  '/usr/bin/ssh-keygen','-y','-f',str(key)]).stdout.decode().strip()
    if not re.fullmatch(r'ssh-ed25519 [A-Za-z0-9+/=]+',public):
        raise ConfigError('unexpected SSH public-key type or encoding')
    host_public = run(['/usr/bin/ssh-keygen','-y','-f',str(host)]).stdout.decode().strip()
    forced = cfg['MCP_INSTALL_ROOT']+'/current/bin/ssh-gateway'
    atomic_write(ssh/'authorized_keys',f'restrict,from="127.0.0.1",command="{forced}" {public}\n',0o644)
    known = ssh/'known_hosts'
    atomic_write(known,f'[127.0.0.1]:{cfg["SSH_PORT"]} {host_public}\n',0o644)
    text = f'''# Dedicated listener; does NOT modify /etc/ssh/sshd_config or DenyUsers devops.
Port {cfg['SSH_PORT']}
ListenAddress 127.0.0.1
AddressFamily inet
HostKey {host}
PidFile /run/codex-mcp-sshd/sshd.pid
AuthorizedKeysFile {ssh}/authorized_keys
AllowUsers {cfg['DESKTOP_USER']}
AuthenticationMethods publickey
PubkeyAuthentication yes
PasswordAuthentication no
KbdInteractiveAuthentication no
PermitRootLogin no
PermitEmptyPasswords no
UsePAM no
StrictModes yes
DisableForwarding yes
AllowAgentForwarding no
AllowTcpForwarding no
X11Forwarding no
PermitTunnel no
PermitTTY no
PermitUserEnvironment no
PermitUserRC no
ForceCommand {forced}
MaxAuthTries 2
MaxSessions 1
MaxStartups 4:30:16
LoginGraceTime 15
ClientAliveInterval 30
ClientAliveCountMax 3
LogLevel VERBOSE
'''
    atomic_write(root/'sshd_config',text,0o600)
    # Debian openssh's global privilege-separation directory is normally provided
    # by ssh.service; create it as root for installations where that unit is off.
    protected_directory(Path('/run/sshd'),0o755)
    run(['/usr/sbin/sshd','-t','-f',str(root/'sshd_config')])
    return {'identity':str(key),'known_hosts':str(known),'user':cfg['DESKTOP_USER'],
            'port':cfg['SSH_PORT'],'connect_timeout':cfg['SSH_CONNECT_TIMEOUT_SECONDS']}


def apparmor(cfg: dict[str,Any]) -> None:
    base = Path('/etc/apparmor.d/abstractions/managed-codex-runtime')
    if not base.is_file():
        raise ConfigError('preseed AppArmor abstraction is missing; do not silently disable confinement')
    include = '  #include if exists <abstractions/codex-mcp-client>\n'
    text = base.read_text()
    marker = '# codex-mcp managed include'
    backup = Path(cfg['MCP_CONFIG_DIR'])/'managed-codex-runtime.before-mcp'
    if not backup.exists():
        atomic_write(backup,text,0o600)
    fragment = f'''# Client-only access; deliberately no podman.sock access.
/usr/local/bin/codex-mcp rix,
/usr/local/libexec/codex-mcp/** rix,
/etc/codex/mcp/client.json r,
/etc/codex/mcp/ssh/known_hosts r,
/usr/bin/ssh rix,
{cfg['DESKTOP_HOME']}/.ssh/codex-mcp_ed25519 r,
{cfg['MCP_SOCKET']} rw,
unix (connect, send, receive, shutdown) type=stream peer=(addr="{cfg['MCP_SOCKET']}"),
'''
    atomic_write(Path('/etc/apparmor.d/abstractions/codex-mcp-client'),fragment,0o644)
    if marker not in text:
        atomic_write(base,text+'\n'+marker+'\n'+include,0o644)
    for name in ('managed-desktop-wrappers','chatgpt'):
        path = Path('/etc/apparmor.d')/name
        if path.exists():
            run(['/usr/sbin/apparmor_parser','-r',str(path)],timeout=60)


def install(env_path: Path, desktop: str | None = None) -> dict[str,Any]:
    root_required()
    cfg = resolve_accounts(load_env(env_path),desktop)
    errors = preflight(cfg)
    if errors:
        raise ConfigError('preflight failed:\n'+ '\n'.join(errors))
    root = Path(cfg['MCP_CONFIG_DIR'])
    protected_directory(root,0o755)
    with locked(root/'install.lock',blocking=True):
        run(['/usr/bin/systemctl','stop','codex-mcp.target'],check=False)
        old_config = root/'runtime.json'
        if old_config.exists():
            old = json.loads(old_config.read_text())
            if any(old.get(k)!=cfg[k] for k in ('DESKTOP_UID','DEVOPS_UID','WORKSPACE','MCP_STATE_ROOT','MCP_SOCKET')):
                raise ConfigError('identity/path migration requires explicit uninstall/backup; refusing to reassign live data')
            # Retain pinned image only when base/build inputs are unchanged.
            keys = ('MCP_BASE_IMAGE','MCP_BASE_CONFIG_DIGEST','DBHUB_PATCH_VERSION','CONTAINER_UID','CONTAINER_GID')
            if all(old.get(k)==cfg[k] for k in keys) and old.get('CONTAINER_SOURCE_SHA256')==hashlib.sha256((digest_tree(SOURCE_ROOT/'container')+digest_tree(SOURCE_ROOT/'integration')+(SOURCE_ROOT/'servers.json').read_text()).encode()).hexdigest():
                cfg['IMAGE_ID'] = old.get('IMAGE_ID','')
        cfg['schema_version'] = 1
        cfg['CONTAINER_SOURCE_SHA256'] = hashlib.sha256((digest_tree(SOURCE_ROOT/'container')+digest_tree(SOURCE_ROOT/'integration')+(SOURCE_ROOT/'servers.json').read_text()).encode()).hexdigest()
        releases = Path(cfg['MCP_INSTALL_ROOT'])/'releases'
        protected_directory(releases)
        release_hash = digest_tree(SOURCE_ROOT)
        release = releases/release_hash
        if not release.exists():
            staging = releases/('.staging-'+release_hash)
            if staging.exists():
                shutil.rmtree(staging)
            shutil.copytree(SOURCE_ROOT,staging,ignore=shutil.ignore_patterns('__pycache__','*.pyc','.env','*.local','build','validation'))
            for path in staging.rglob('*'):
                if path.is_symlink():
                    raise ConfigError('release must not contain symlinks')
                os.chown(path,0,0)
                os.chmod(path,0o755 if path.is_dir() or path.parent.name=='bin' else 0o644)
            os.rename(staging,release)
        current = Path(cfg['MCP_INSTALL_ROOT'])/'current'
        temporary = current.with_name('.current-new')
        if temporary.is_symlink():
            temporary.unlink()
        os.symlink(release,temporary)
        os.replace(temporary,current)
        for name in ('codex-mcp','codex-mcp-admin'):
            dest = Path('/usr/local/bin')/name
            if dest.exists() and not dest.is_symlink():
                raise ConfigError('refusing to replace non-symlink executable: '+str(dest))
            temp = dest.with_name('.'+name+'.new')
            if temp.is_symlink():
                temp.unlink()
            os.symlink(current/'bin'/name,temp); os.replace(temp,dest)
        credentials = root/'credentials'
        protected_directory(credentials,0o700)
        for name in CREDENTIALS:
            path = credentials/name
            if path.is_symlink():
                raise ConfigError('credential master must not be a symlink')
            if not path.exists():
                atomic_write(path,b'',0o600)
            st = path.lstat()
            if not stat.S_ISREG(st.st_mode) or st.st_uid!=0 or st.st_mode&0o077:
                raise ConfigError('credential master must be root-owned mode 0600: '+name)
        from browser_security import derive_profile
        browser_profile=derive_profile(json.loads(Path(cfg['BROWSER_SECCOMP_BASE']).read_text()))
        atomic_write(root/'browser-seccomp.json',json.dumps(browser_profile,indent=2)+'\n',0o644)
        cfg['RELEASE_SHA256'] = release_hash
        grant_acls(cfg)
        ssh = install_ssh(cfg) if cfg['SSH_ENABLED'] else {}
        client = {'version':1,'socket':cfg['MCP_SOCKET'],'transport':cfg['MCP_TRANSPORT'],
                  'desktop_uid':cfg['DESKTOP_UID'],'devops_uid':cfg['DEVOPS_UID'],
                  'connect_timeout':cfg['CONNECT_TIMEOUT_SECONDS'],'max_buffer':cfg['MAX_BUFFER_BYTES'],
                  'idle_timeout':cfg['IDLE_TIMEOUT_SECONDS'],'max_lifetime':cfg['SESSION_MAX_SECONDS'],
                  'stop_timeout':cfg['STOP_TIMEOUT_SECONDS'],'ssh':ssh}
        atomic_write(root/'runtime.json',json.dumps(cfg,indent=2)+'\n',0o644)
        atomic_write(root/'client.json',json.dumps(client,indent=2)+'\n',0o644)
        # Persist sanitized, non-secret deployment inputs for reproducibility.
        atomic_write(root/'deployment.env',env_path.read_bytes(),0o600)
        atomic_write(root/'toolchain-coverage.json',json.dumps(toolchain.coverage(cfg),indent=2)+'\n',0o644)
        units = render_units(cfg)
        for name,text in units.items():
            atomic_write(Path('/etc/systemd/system')/name,text,0o644)
        apparmor(cfg)
        run(['/usr/bin/systemctl','daemon-reload'])
        # No target activation until an immutable patched image has been built.
        prepare(cfg)
        return cfg
