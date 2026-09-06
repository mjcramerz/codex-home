#!/usr/bin/python3
"""Container entrypoint: fixed executable map, file-backed secrets, exec semantics."""
from __future__ import annotations
import json
import os
from pathlib import Path
import pwd
import re
import subprocess
import sys
from urllib.parse import urlparse, parse_qs

ROOT=Path('/opt/codex-mcp')
CREDENTIAL_DIR=Path('/run/mcp-credentials')
SECRET_ENV={
 'context7-api-key':'CONTEXT7_API_KEY','semgrep-app-token':'SEMGREP_APP_TOKEN',
 'openai-api-key':'OPENAI_API_KEY','azure-openai-api-key':'AZURE_OPENAI_API_KEY',
 'azure-openai-endpoint':'AZURE_OPENAI_ENDPOINT','azure-openai-api-version':'AZURE_OPENAI_API_VERSION'}

def credential(name: str, required: bool=False) -> str:
    p=CREDENTIAL_DIR/name
    if not p.exists():
        if required:raise ValueError('required credential not provisioned: '+name)
        return ''
    if p.is_symlink() or not p.is_file():raise ValueError('invalid credential file')
    try:value=p.read_bytes().decode('utf-8').rstrip('\r\n')
    except UnicodeError:raise ValueError('credential must use UTF-8: '+name) from None
    if len(value)>65536 or '\x00' in value or '\n' in value or '\r' in value:
        raise ValueError('invalid credential format: '+name)
    if required and not value:raise ValueError('empty required credential: '+name)
    return value


def boolenv(name: str, default: bool=False) -> bool:
    value=os.environ.get(name,'true' if default else 'false')
    if value not in ('true','false'):raise ValueError('invalid boolean '+name)
    return value=='true'


def prepare_paths() -> None:
    for p in ('/tmp/xdg/cache','/tmp/xdg/config','/tmp/xdg/state','/tmp/devops-runtime',
              '/tmp/devops-runtime/python/pycache','/tmp/devops-runtime/ansible/tmp',
              '/tmp/devops-runtime/ansible/pc','/tmp/devops-runtime/ansible/ssh',
              '/tmp/browser-output','/home/devops/.config','/home/devops/.local/state'):
        Path(p).mkdir(parents=True,exist_ok=True,mode=0o700)
    # Only known path variables from our profile map are considered. Values are
    # fixed by the root-owned broker; no mkdir on a caller-supplied arbitrary path.
    names=('PYTHONUSERBASE','UV_TOOL_DIR','UV_TOOL_BIN_DIR','PIP_CACHE_DIR','UV_CACHE_DIR',
           'CARGO_HOME','CARGO_TARGET_DIR','CARGO_INSTALL_ROOT','RUSTUP_HOME','SCCACHE_DIR',
           'NPM_CONFIG_CACHE','NPM_CONFIG_PREFIX','PNPM_HOME','YARN_CACHE_FOLDER',
           'ANSIBLE_HOME','ANSIBLE_GALAXY_CACHE_DIR','TF_PLUGIN_CACHE_DIR',
           'PACKER_CACHE_DIR','PACKER_CONFIG_DIR','PACKER_PLUGIN_PATH',
           'MISE_CONFIG_DIR','MISE_DATA_DIR','MISE_STATE_DIR','MISE_CACHE_DIR','MISE_TMP_DIR',
           'COREPACK_HOME','BAZELISK_HOME','GOMODCACHE','GOPATH','DENO_DIR','DENO_INSTALL_ROOT')
    for name in names:
        value=os.environ.get(name,'')
        if value.startswith(('/pool/build/','/pool/cache/','/pool/db/','/home/devops/.config/')):
            try:Path(value).mkdir(parents=True,exist_ok=True,mode=0o700)
            except PermissionError:
                # A shared installation root is deliberately read-only.
                if not Path(value).is_dir():raise


def db_config(server: str) -> str:
    if server=='postgres':
        dsn=credential('postgres-dsn',required=True)
        u=urlparse(dsn)
        if u.scheme not in ('postgres','postgresql') or not u.hostname:
            raise ValueError('postgres-dsn must be a PostgreSQL URI')
        sslmode=parse_qs(u.query).get('sslmode',[''])[0]
        if boolenv('MCP_POSTGRES_REQUIRE_TLS',True) and sslmode not in ('verify-full','verify-ca','require'):
            raise ValueError('postgres-dsn must request TLS with sslmode; prefer verify-full')
        readonly=boolenv('MCP_POSTGRES_READONLY',True)
    else:
        dsn='sqlite:///state/default.db'
        readonly=boolenv('MCP_SQLITE_READONLY')
    # Use TOML basic strings, never DSNs in process argv or Podman metadata.
    data='[[sources]]\nid = "default"\ndsn = '+json.dumps(dsn)+'\n\n'
    data+='[[tools]]\nname = "execute_sql"\nsource = "default"\n'
    data+='readonly = '+str(readonly).lower()+'\nmax_rows = 1000\n\n'
    data+='[[tools]]\nname = "search_objects"\nsource = "default"\n'
    path=Path('/tmp/dbhub.toml')
    fd=os.open(path,os.O_WRONLY|os.O_CREAT|os.O_EXCL,0o600)
    with os.fdopen(fd,'w') as f:f.write(data)
    return str(path)


def command(server: str) -> tuple[list[str],dict[str,str]]:
    catalog=json.loads((ROOT/'servers.json').read_text())
    if server not in catalog:raise ValueError('unknown MCP server')
    spec=catalog[server]; env=dict(os.environ)
    for name in spec['credentials']:
        if name in SECRET_ENV:
            value=credential(name)
            if value:env[SECRET_ENV[name]]=value
    args=['/usr/local/bin/'+spec['executable']]
    if server=='filesystem':args+=['/workspace']
    elif server=='git':
        repo=env.get('MCP_GIT_REPOSITORY','')
        if repo:
            path=(Path('/workspace')/repo).resolve(strict=True)
            if not path.is_relative_to('/workspace'):raise ValueError('Git repository escapes Workspace')
            args+=['--repository',str(path)]
        if credential('github-token'):
            env['GIT_ASKPASS']='/opt/codex-mcp/git-askpass.py'
            env['GIT_TERMINAL_PROMPT']='0'
    elif server=='fetch':
        args+=['--user-agent',env.get('MCP_FETCH_USER_AGENT','Codex-MCP')]
        if boolenv('MCP_FETCH_IGNORE_ROBOTS_TXT'):args+=['--ignore-robots-txt']
        proxy=credential('fetch-proxy-url')
        # HTTP proxy libraries consume env values; do not expose user:password in argv.
        if proxy:env.update(HTTP_PROXY=proxy,HTTPS_PROXY=proxy,ALL_PROXY=proxy)
    elif server=='memory':env['MEMORY_FILE_PATH']='/state/memory.jsonl'
    elif server=='sequential-thinking':env['DISABLE_THOUGHT_LOGGING']='true'
    elif server=='time':args+=['--local-timezone',env.get('LOCAL_TIMEZONE','Europe/Stockholm')]
    elif server=='context7':args+=['--transport','stdio']
    elif server=='playwright':
        args+=['--headless','--isolated','--executable-path','/usr/local/bin/chrome-for-mcp',
               '--output-dir','/tmp/browser-output']
        if boolenv('MCP_BROWSER_NO_SANDBOX'):args+=['--no-sandbox']
    elif server=='chrome-devtools':
        args+=['--headless','--isolated','--no-usage-statistics','--no-performance-crux',
               '--executable-path','/usr/local/bin/chrome-for-mcp']
        if boolenv('MCP_BROWSER_NO_SANDBOX'):args+=['--chrome-arg=--no-sandbox']
    elif server in ('postgres','sqlite'):args+=['--transport','stdio','--config',db_config(server)]
    elif server=='semgrep':args+=['mcp']
    return args,env


def toolchain_check() -> int:
    # Non-mutating probes; each gets an independent hard deadline.
    probes={
        'host-node':[os.environ.get('NODE','/usr/local/lib/node-26/bin/node'),'--version'],
        'image-node':['/usr/local/bin/node','--version'],
        'python':['/usr/bin/python3','--version'], 'perl':['perl','-e','print "$^V\\n"'],
        'rust':['rustc','--version'],'cargo':['cargo','--version'],
        'go':['go','version'],'clang':['clang','--version'],'cmake':['cmake','--version'],
        'ansible':['ansible','--version'],'terraform':['terraform','version'],
        'packer':['packer','version'],'deno':['deno','--version']}
    import shutil
    results=[]
    for name,argv in probes.items():
        executable=shutil.which(argv[0])
        if not executable:
            results.append({'tool':name,'status':'absent'});continue
        try:
            p=subprocess.run(argv,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=20,check=False)
            results.append({'tool':name,'status':'ok' if p.returncode==0 else 'failed',
                            'exit':p.returncode,'output':p.stdout.decode(errors='replace')[:1000]})
        except (OSError,subprocess.TimeoutExpired) as e:
            results.append({'tool':name,'status':'failed','reason':type(e).__name__})
    print(json.dumps(results,indent=2))
    return int(any(r['status']=='failed' or (r['status']=='absent' and (os.environ.get('MCP_TOOLCHAIN_REQUIRE_ALL')=='true' or r['tool']=='host-node')) for r in results))


def main() -> int:
    os.umask(0o077)
    if os.geteuid()==0 or pwd.getpwuid(os.geteuid()).pw_name!='devops':
        raise ValueError('container must run as the non-root devops user')
    prepare_paths()
    if len(sys.argv)!=2:raise ValueError('exactly one server selector required')
    if sys.argv[1]=='__toolchain-check':return toolchain_check()
    argv,env=command(sys.argv[1])
    os.execve(argv[0],argv,env)
    return 127

if __name__=='__main__':
    try:raise SystemExit(main())
    except (ValueError,OSError) as e:
        # Messages in these exceptions are deliberately credential-free.
        print('codex-mcp entrypoint: '+str(e),file=sys.stderr)
        raise SystemExit(78)
