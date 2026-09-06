#!/usr/bin/env python3
"""Synchronize derived assets WITHOUT regenerating or replacing custom configuration.

home/config.toml and instructions/ are authoritative. This command does not
rewrite model choices, prompts, feature values, agent roles, hooks, or profiles.
"""
from __future__ import annotations
import fcntl
import hashlib
import json
import os
from pathlib import Path
import sys
import tempfile
import tomllib
ROOT=Path(__file__).resolve().parents[1]

def atomic(path: Path, payload: bytes) -> bool:
    if path.is_symlink(): raise ValueError(f'refusing symlink target: {path}')
    if path.exists() and path.read_bytes()==payload:return False
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,name=tempfile.mkstemp(prefix='.codex-generate-',dir=path.parent)
    try:
        with os.fdopen(fd,'wb') as out:
            out.write(payload);out.flush();os.fsync(out.fileno())
        os.chmod(name,0o644);os.replace(name,path)
        directory_fd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try:os.fsync(directory_fd)
        finally:os.close(directory_fd)
    finally:
        if os.path.exists(name):os.unlink(name)
    return True

def generate() -> int:
    # Validate source shape before any derived file is touched.
    from jsonschema import Draft7Validator
    data=tomllib.loads((ROOT/'home/config.toml').read_text())
    schema_bytes=(ROOT/'generate/schemas/config.schema.json').read_bytes()
    schema=json.loads(schema_bytes);Draft7Validator.check_schema(schema)
    Draft7Validator(schema).validate(data)
    policy=json.loads((ROOT/'generate/feature-policy.json').read_text())
    if hashlib.sha256(schema_bytes).hexdigest()!=policy['schema_sha256']:
        raise ValueError('custom schema changed; review and update the explicit schema pin first')
    count=0
    for target in ('home/config.schema.json','etc/config.schema.json','generate/schemas/supplied-config.schema.json'):
        count+=atomic(ROOT/target,schema_bytes)
    count+=atomic(ROOT/'etc/config.toml',(ROOT/'home/config.toml').read_bytes())
    for source in sorted((ROOT/'instructions').rglob('*')):
        if source.is_symlink():raise ValueError(f'source symlink: {source}')
        if source.is_file():
            count+=atomic(ROOT/'home/instructions'/source.relative_to(ROOT/'instructions'),source.read_bytes())
    for source in sorted((ROOT/'generate/schemas').glob('*.command.*.schema.json')):
        count+=atomic(ROOT/'home/.hooks/schemas'/source.name,source.read_bytes())
    count+=atomic(ROOT/'home/index/servers.json',(ROOT/'mcp/servers.json').read_bytes())
    return count

def main() -> int:
    try:
        # The lock is in /tmp, not the distributed source or an app-owned directory.
        tag=hashlib.sha256(str(ROOT).encode()).hexdigest()[:24]
        name=Path(tempfile.gettempdir())/('codex-home-generate-'+str(os.getuid())+'-'+tag+'.lock')
        fd=os.open(name,os.O_RDWR|os.O_CREAT|os.O_NOFOLLOW,0o600)
        with os.fdopen(fd,'a') as lock:
            fcntl.flock(lock,fcntl.LOCK_EX)
            count=generate()
        print(f'Synchronized {count} derived files; custom config, hooks and instruction sources preserved.')
        return 0
    except (OSError,ValueError) as exc:
        print(str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
