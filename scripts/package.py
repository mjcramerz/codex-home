#!/usr/bin/env python3
"""Create a deterministic, source-only tarball and its content/SHA256 manifests."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import tarfile
import tempfile
ROOT=Path(__file__).resolve().parents[1]
EPOCH=1788652800

def selected():
    for p in sorted(ROOT.rglob('*')):
        rel=p.relative_to(ROOT)
        if any(x in {'__pycache__','.git','.pytest_cache','.mypy_cache','.asset-backups'} for x in rel.parts):continue
        if p.suffix=='.pyc' or p.name.endswith('.local'):continue
        if p.is_symlink():raise ValueError('source symlink needs explicit review: '+str(rel))
        if p.is_file():yield p

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path,default=ROOT.parent/'codex-home.tar.gz')
    args=parser.parse_args();out=args.output.absolute()
    if out.is_relative_to(ROOT):raise ValueError('archive must be outside source root')
    files=[p for p in selected() if p.name!='MANIFEST.sha256']
    rows=[hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(ROOT).as_posix() for p in files]
    (ROOT/'MANIFEST.sha256').write_text('\n'.join(rows)+'\n')
    out.parent.mkdir(parents=True,exist_ok=True)
    fd,temp=tempfile.mkstemp(prefix='.codex-home-',dir=out.parent)
    try:
        with os.fdopen(fd,'wb') as stream,gzip.GzipFile(filename='',fileobj=stream,mode='wb',mtime=0) as gz:
            with tarfile.open(fileobj=gz,mode='w',format=tarfile.PAX_FORMAT) as tar:
                top=tarfile.TarInfo('codex-home');top.type=tarfile.DIRTYPE;top.mode=0o755;top.mtime=EPOCH
                tar.addfile(top)
                for p in selected():
                    info=tar.gettarinfo(str(p),arcname='codex-home/'+p.relative_to(ROOT).as_posix())
                    info.uid=info.gid=0;info.uname=info.gname='root';info.mtime=EPOCH
                    info.mode=0o755 if p.stat().st_mode&0o111 else 0o644
                    with p.open('rb') as f:tar.addfile(info,f)
        os.replace(temp,out)
    finally:
        if os.path.exists(temp):os.unlink(temp)
    digest=hashlib.sha256(out.read_bytes()).hexdigest()
    out.with_name(out.name+'.sha256').write_text(digest+'  '+out.name+'\n')
    with tarfile.open(out) as tar:
        members=tar.getmembers()
        for m in members:
            p=Path(m.name)
            assert not p.is_absolute() and '..' not in p.parts and p.parts[0]=='codex-home'
            assert m.isfile() or m.isdir()
        for p in ('bin/codex-mcp','bin/codex-mcp-admin','bin/broker','bin/ssh-gateway'):
            assert tar.getmember('codex-home/mcp/'+p).mode&0o111
    print(json.dumps({'archive':str(out),'bytes':out.stat().st_size,'sha256':digest,'members':len(members)},indent=2))
if __name__=='__main__':main()
