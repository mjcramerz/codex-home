#!/usr/bin/env python3
"""Offline consistency checks. No system accounts, engine or network required."""
import ast
import json
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'lib'))
from common import SOURCE_ROOT,SERVER_NAMES,load_env
from install import validate_codex_mcp_configs
from runtime import catalog

def main():
    cfg=load_env(SOURCE_ROOT/'.env')
    assert set(catalog())==set(SERVER_NAMES)
    containerfile=(SOURCE_ROOT/'container/Containerfile').read_text()
    assert 'ARG BASE_IMAGE='+cfg['MCP_BASE_IMAGE']+'\n' in containerfile
    assert 'ARG DBHUB_PATCH_VERSION='+cfg['DBHUB_PATCH_VERSION']+'\n' in containerfile
    docker=(SOURCE_ROOT/'container/Dockerfile.supplied').read_text()
    for name,spec in catalog().items():
        assert name in docker,name
        assert '/usr/local/bin/'+spec['executable'] in docker,name
    layers=[SOURCE_ROOT.parent/name for name in ('etc/config.toml','home/config.toml')]
    validate_codex_mcp_configs([(path,path.lstat().st_uid,None) for path in layers])
    for p in [*(SOURCE_ROOT/'lib').glob('*.py'),*(SOURCE_ROOT/'container').glob('*.py'),
              *(SOURCE_ROOT/'scripts').glob('*.py'),*(SOURCE_ROOT/'bin').iterdir()]:
        if p.is_file():ast.parse(p.read_text(),filename=str(p))
    for spec in catalog().values():
        assert spec['workspace'] in ('rw','ro','none')
        assert isinstance(spec['network'],bool)
        assert not spec['executable'].startswith('/')
    assert cfg['PODMAN_USER']=='devops'
    print('MCP image contract, Codex registrations, 13 modes and Python syntax: PASS')
    return 0
if __name__=='__main__':raise SystemExit(main())
