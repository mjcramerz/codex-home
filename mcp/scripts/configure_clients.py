#!/usr/bin/env python3
"""Generate reviewable client snippets; never mutate an installed app config."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys
import tomllib
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'lib'))
from common import SOURCE_ROOT,atomic_write,load_env
from runtime import catalog


def render(cfg: dict, transport: str) -> str:
    if transport not in {'configured','unix','ssh'}:raise ValueError('unsupported transport')
    lines=['# Generated local MCP registrations only. Merge by server ID, do not append duplicate tables.',
           '# No API values are stored here. The broker reads systemd credentials.',
           '# "configured" follows /etc/codex/mcp/client.json; explicit variants override it.','']
    for server in catalog():
        key='sequential_thinking' if server=='sequential-thinking' else server
        args=['connect',server]
        if transport!='configured':args+=['--transport',transport]
        lines += ['[mcp_servers.'+json.dumps(key)+']','command = "/usr/local/bin/codex-mcp"',
                  'args = '+json.dumps(args),'enabled = true','required = false',
                  'startup_timeout_sec = '+str(cfg['STARTUP_TIMEOUT_SECONDS']+cfg['CONNECT_TIMEOUT_SECONDS']+15),
                  'tool_timeout_sec = '+str(cfg['TOOL_TIMEOUT_SECONDS']),'']
    text='\n'.join(lines)
    assert len(tomllib.loads(text)['mcp_servers'])==13
    return text


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--env',type=Path,default=SOURCE_ROOT/'.env')
    parser.add_argument('--output',type=Path,default=SOURCE_ROOT/'build')
    args=parser.parse_args();cfg=load_env(args.env)
    if args.output.is_symlink():raise ValueError('output directory must not be a symlink')
    args.output.mkdir(parents=True,exist_ok=True)
    for mode in ('configured','unix','ssh'):
        name='mcp-servers.toml' if mode=='configured' else 'mcp-servers-'+mode+'.toml'
        atomic_write(args.output/name,render(cfg,mode),0o644)
    print('Generated configured, Unix and SSH stdio snippets in '+str(args.output))
    return 0

if __name__=='__main__':raise SystemExit(main())
