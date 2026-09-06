#!/usr/bin/env python3
"""Fetch pinned upstream REFERENCES, never the authoritative custom schema.

Does not silently update active configuration or replace the supplied snapshot.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import urllib.request
ROOT=Path(__file__).resolve().parents[1]

def fetch(url):
    req=urllib.request.Request(url,headers={'User-Agent':'codex-home-schema-validator/1.0'})
    with urllib.request.urlopen(req,timeout=30) as response:
        body=response.read(4*1024*1024+1)
        if len(body)>4*1024*1024:raise ValueError('upstream file exceeds size bound')
        return body

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--version',default='0.147.0');args=p.parse_args()
    if not re.fullmatch(r'\d+\.\d+\.\d+',args.version):p.error('use a fixed stable semantic version')
    base=f'https://raw.githubusercontent.com/openai/codex/rust-v{args.version}/codex-rs/'
    dest=ROOT/'generate/schemas'/('codex-'+args.version);dest.mkdir(exist_ok=True)
    evidence={}
    for remote,local in [('core/config.schema.json','config.schema.json'),('features/src/lib.rs','features.rs'),('features/src/legacy.rs','legacy.rs')]:
        url=base+remote;data=fetch(url)
        if local.endswith('.json'):json.loads(data)
        (dest/local).write_bytes(data)
        evidence[local]={'url':url,'sha256':hashlib.sha256(data).hexdigest()}
    (dest/'provenance.json').write_text(json.dumps(evidence,indent=2)+'\n')
    print('Fetched reference-only upstream sources (custom schema unchanged) into '+str(dest))
if __name__=='__main__':main()
