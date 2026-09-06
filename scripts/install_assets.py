#!/usr/bin/env python3
"""Install reviewed static assets without deleting authentication or session data."""
from __future__ import annotations
import argparse
import datetime
import fcntl
import hashlib
import json
import os
from pathlib import Path
import shutil
import stat
import sys
import tempfile
import tomllib
ROOT=Path(__file__).resolve().parents[1]

def atomic(path: Path,data: bytes,mode: int) -> None:
    if path.is_symlink(): raise ValueError('refusing symlink target: '+str(path))
    fd,name=tempfile.mkstemp(prefix='.codex-asset-',dir=path.parent)
    try:
        os.fchmod(fd,mode)
        with os.fdopen(fd,'wb') as f:f.write(data);f.flush();os.fsync(f.fileno())
        os.replace(name,path)
        fd=os.open(path.parent,os.O_RDONLY|os.O_DIRECTORY)
        try:os.fsync(fd)
        finally:os.close(fd)
    finally:
        if os.path.exists(name):os.unlink(name)

def directory(path: Path,root_only: bool=False) -> None:
    for p in reversed([path,*path.parents]):
        if p==Path('/'):continue
        if p.is_symlink():raise ValueError('symlink destination ancestry: '+str(p))
        p.mkdir(mode=0o755,exist_ok=True)
        st=p.stat()
        if not stat.S_ISDIR(st.st_mode):raise ValueError('destination is not a directory')
        if root_only and (st.st_uid!=0 or st.st_mode&0o022):
            raise ValueError('unprotected system directory: '+str(p))

def merge_desktop(source: bytes, existing: bytes) -> bytes:
    """Preserve opaque product-owned settings; explicit reviewed source values win."""
    import tomlkit
    old = tomllib.loads(existing.decode('utf-8'))
    if 'desktop' not in old:
        return source
    if not isinstance(old['desktop'], dict):
        raise ValueError('existing desktop settings are not a TOML table')
    new = tomlkit.parse(source.decode('utf-8'))
    existing_doc = tomlkit.parse(existing.decode('utf-8'))
    # The opaque table may contain nested product-specific fields. Do not infer,
    # migrate, or discard them. Reviewed explicit replacements take precedence.
    def merge(a, b):
        for key, value in b.items():
            if key in a and hasattr(a[key], 'items') and hasattr(value, 'items'):
                merge(a[key], value)
            else:
                a[key] = value
        return a
    new['desktop'] = merge(existing_doc['desktop'], new.get('desktop', {}))
    result = tomlkit.dumps(new).encode('utf-8')
    from jsonschema import Draft7Validator
    schema = json.loads((ROOT/'generate/schemas/config.schema.json').read_text())
    Draft7Validator(schema).validate(tomllib.loads(result.decode('utf-8')))
    return result

def install(mode: str) -> dict:
    from validate import validate
    validate(ROOT, write=False)
    if mode=='home':
        if os.geteuid()==0:raise ValueError('run install-home as the desktop user, without sudo')
        dest=Path('/data/codex/usr')
        sources=[p for name in ('home','agents','skills','instructions')
                 for p in sorted((ROOT/name).rglob('*')) if p.is_file()]
    else:
        if os.geteuid()!=0:raise ValueError('install-config requires sudo')
        dest=Path('/etc/codex')
        sources=[ROOT/'etc/config.toml',ROOT/'etc/requirements.toml',ROOT/'etc/config.schema.json']
    directory(dest,mode=='config')
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S')
    backup=dest/'.asset-backups'/(stamp+'-'+str(os.getpid()))
    directory(backup,mode=='config');os.chmod(backup,0o700)
    records=[]
    lock_fd=os.open(dest/'.asset-install.lock',os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW,0o600)
    with os.fdopen(lock_fd,'a') as lock:
        fcntl.flock(lock,fcntl.LOCK_EX)
        for source in sources:
            if source.is_symlink():raise ValueError('source links require manual review')
            if '__pycache__' in source.parts or source.suffix=='.pyc':continue
            relative=source.relative_to(ROOT) if mode=='home' else Path(source.name)
            target=dest/relative
            if source.resolve()==target.resolve():continue
            directory(target.parent,mode=='config')
            payload=source.read_bytes()
            if target.is_symlink():raise ValueError('refusing symlink target: '+str(target))
            if target.exists():
                if not target.is_file():raise ValueError('target is not a regular file')
                previous=target.read_bytes()
                if source==ROOT/'home/config.toml' or source==ROOT/'etc/config.toml':
                    payload=merge_desktop(payload,previous)
                if previous==payload:continue
                saved=backup/relative;directory(saved.parent,mode=='config')
                atomic(saved,previous,0o600)
            atomic(target,payload,0o755 if source.stat().st_mode&0o111 else 0o644)
            records.append({'file':str(relative),'sha256':hashlib.sha256(payload).hexdigest()})
        atomic(backup/'changes.json',json.dumps(records,indent=2).encode()+b'\n',0o600)
    return {'mode':mode,'updated':len(records),'backup':str(backup),
            'note':'Close clients before installation. Auth, sessions and app caches are not removed. Existing opaque desktop preferences are preserved and backed up. Reviewed explicit desktop values override matching keys.'}

def main() -> int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('mode',choices=('home','config'))
    args=p.parse_args()
    try:print(json.dumps(install(args.mode),indent=2));return 0
    except Exception as exc:print(str(exc),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
