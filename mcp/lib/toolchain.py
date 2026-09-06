"""Explicit profile-to-container mapping, without importing desktop secrets."""
from __future__ import annotations
import json
import os
from pathlib import Path
import re
from typing import Any
from common import SOURCE_ROOT, ConfigError

# Match every explicit PATH root in 71-devops-de.sh. Parent directories are
# mounted rather than only bin/ so symlink targets and package resources survive.
SYSTEM_ROOTS = (
 '/usr/local/libexec/obs-publishing-bin','/usr/local/libexec/aptly-publishing-bin',
 '/usr/local/lib/opentufo','/usr/local/lib/ansible','/usr/local/lib/deno',
 '/usr/local/lib/yt-dlp','/usr/local/lib/hashicorp/terraform','/usr/local/lib/hashicorp/packer',
 '/usr/local/lib/wrangler','/usr/local/lib/aptly','/usr/local/lib/osc','/usr/local/lib/obs-build',
 '/usr/local/lib/rustup','/usr/local/lib/node-26','/usr/local/lib/bazelisk',
 '/usr/lib/llvm-24','/usr/local/cuda-12.8','/usr/local/cuda-12.9','/usr/local/cuda-13.1',
 '/data/codex/lib','/data/llama/lib','/data/llama/bin')
USER_ROOTS = (
 'build/python','build/uv','build/go/bin','build/deno/bin','build/cargo/install',
 'build/npm-global','build/pnpm/bin','build/yarn-global','cache/cargo/bin',
 'db/rustup','db/uv/tools','db/mise/data')
# Other /pool/{build,cache,db}/USER selectors from the profile deliberately point
# at private scratch trees, not at PGDATA, pgpass, cloud credentials or HOME.


def profile_environment(cfg: dict[str,Any]) -> tuple[dict[str,str],list[str]]:
    text=(SOURCE_ROOT/'integration/71-devops-de.sh.reference').read_text()
    user=cfg['DESKTOP_USER']
    variables={
        'USER':user,'HOME':'/home/devops','XDG_CONFIG_HOME':'/home/devops/.config',
        'XDG_RUNTIME_DIR':'/tmp/devops-runtime',
        'devops_de_pool_root':'/pool','devops_de_build_home':f'/pool/build/{user}',
        'devops_de_cache_home':f'/pool/cache/{user}','devops_de_db_home':f'/pool/db/{user}',
        'devops_de_xdg_config_home':'/home/devops/.config',
        'devops_de_python_runtime_root':'/tmp/devops-runtime/python',
        'devops_de_ansible_runtime_root':'/tmp/devops-runtime/ansible',
        'devops_de_hashicorp_cache_root':f'/pool/cache/{user}/hashicorp',
    }
    exported: dict[str,str]={}
    paths: list[str]=[]
    def expand(value: str) -> str:
        value=re.sub(r'\$\{([A-Za-z_][A-Za-z0-9_]*)\}',lambda m:variables.get(m[1],'${'+m[1]+'}'),value)
        value=re.sub(r'\$([A-Za-z_][A-Za-z0-9_]*)',lambda m:variables.get(m[1],'$'+m[1]),value)
        if '$' in value:raise ConfigError('unresolved profile value: '+value)
        return value
    # Limit parsing to the environment builder; never source or evaluate it.
    start=text.index('  devops_de_pool_root=/pool')
    end=text.index('  # Mark the environment active',start)
    for line in text[start:end].splitlines():
        m=re.fullmatch(r'\s*export ([A-Z][A-Z0-9_]*)=(?:"([^"]*)"|([^\s]+))\s*',line)
        if m:
            name=m[1];value=expand(m[2] if m[2] is not None else m[3])
            variables[name]=value;exported[name]=value
        p=re.search(r'devops_de_(prepend|append)_path (?:"([^"]+)"|([^ ]+))',line)
        if p:
            value=expand(p[2] or p[3])
            if value not in paths:
                if p[1]=='prepend':paths.insert(0,value)
                else:paths.append(value)
    exported['RUSTUP_TOOLCHAIN']='stable'
    # Client-owned runtime trees are not copied into containers. These variables
    # remain discoverable, but have empty private directories instead of auth data.
    exported.update(HOME='/home/devops',USER='devops',LOGNAME='devops',
                    XDG_RUNTIME_DIR='/tmp/devops-runtime',XDG_CONFIG_HOME='/home/devops/.config',
                    XDG_CACHE_HOME='/tmp/xdg/cache',XDG_STATE_HOME='/tmp/xdg/state',
                    TMPDIR='/tmp',SHELL='/bin/bash',LANG='C.UTF-8',LC_ALL='C.UTF-8',
                    GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL='/dev/null',GIT_TERMINAL_PROMPT='0',
                    GIT_CONFIG_COUNT='2',GIT_CONFIG_KEY_0='safe.directory',GIT_CONFIG_VALUE_0='/workspace',
                    GIT_CONFIG_KEY_1='safe.directory',GIT_CONFIG_VALUE_1='/workspace/*')
    # MCP uses the base image's exact Python/Node runtime, not host replacements.
    base='/opt/mcp-markdown-venv/bin:/opt/mcp-core-venv/bin:/opt/mcp-node/node_modules/.bin:/usr/local/bin:/usr/bin:/bin'
    exported['PATH']=base+':'+':'.join(paths)+':/opt/host/bin'
    # Absolute NODE is available to tools that explicitly request the host Node.
    exported['NODE']=cfg['HOST_NODE']
    return exported,paths


def host_roots(cfg: dict[str,Any]) -> list[dict[str,str]]:
    roots=[{'source':p,'target':p,'kind':'system'} for p in SYSTEM_ROOTS]
    roots.append({'source':'/usr/local/bin','target':'/opt/host/bin','kind':'system'})
    for item in USER_ROOTS:
        category,tail=item.split('/',1)
        p=f"/pool/{category}/{cfg['DESKTOP_USER']}/{tail}"
        roots.append({'source':p,'target':p,'kind':'user'})
    return roots


def coverage(cfg: dict[str,Any]) -> dict[str,Any]:
    env,paths=profile_environment(cfg)
    entries=[]
    for r in host_roots(cfg):
        p=Path(r['source'])
        entries.append(dict(r,present=p.exists(),symlink=p.is_symlink(),mode='ro'))
    return {'profile':'71-devops-de.sh','profile_path':cfg['TOOLCHAIN_PROFILE'],
            'path_entries':paths,'environment':env,'mounts':entries,
            'private_scratch_roots':[f"/pool/{n}/{cfg['DESKTOP_USER']}" for n in ('build','cache','db')],
            'not_shared':['desktop HOME credentials','live PGDATA','PGPASSFILE contents',
                          'container engine sockets','host SSH agent','desktop session bus'],
            'abi_note':'Forky binaries mounted into Trixie may require newer ELF libraries; run toolchain-check on target. No host /usr or libc overmount.'}


def mounts(cfg: dict[str,Any], session: Path) -> tuple[list[tuple[str,str,bool]],dict[str,str]]:
    if not cfg['TOOLCHAIN_ENABLED']:return [],{}
    env,_=profile_environment(cfg)
    items: list[tuple[str,str,bool]]=[]
    for category in ('build','cache','db'):
        source=session/('tool-'+category);source.mkdir(mode=0o700)
        items.append((str(source),f"/pool/{category}/{cfg['DESKTOP_USER']}",False))
    for item in host_roots(cfg):
        source=Path(item['source'])
        if not source.exists():
            if cfg['TOOLCHAIN_REQUIRE_ALL']:raise ConfigError('required tool root absent: '+str(source))
            continue
        # Require a direct path: symlink roots may redirect ACL and mount authority.
        if source.is_symlink():raise ConfigError('tool root symlink requires explicit source migration: '+str(source))
        items.append((str(source),item['target'],True))
    return items,env
