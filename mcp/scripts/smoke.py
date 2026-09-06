#!/usr/bin/env python3
"""Live MCP initialize + tools/list probe for every configured server; no secrets printed."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import selectors
import subprocess
import sys
import time
import uuid
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'lib'))
from common import SERVER_NAMES

class RPC:
    def __init__(self,server: str,transport: str,timeout: int) -> None:
        self.timeout,self.serial,self.buffer = timeout,0,bytearray()
        self.process = subprocess.Popen(['/usr/local/bin/codex-mcp','connect',server,'--transport',transport],
            stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.DEVNULL)
        self.sel = selectors.DefaultSelector()
        self.sel.register(self.process.stdout,selectors.EVENT_READ)
    def send(self,value: dict) -> None:
        self.process.stdin.write((json.dumps(value)+'\n').encode()); self.process.stdin.flush()
    def request(self,method: str,params: dict) -> dict:
        self.serial += 1
        self.send({'jsonrpc':'2.0','id':self.serial,'method':method,'params':params})
        deadline=time.monotonic()+self.timeout
        while time.monotonic()<deadline:
            if b'\n' in self.buffer:
                line,_,tail=self.buffer.partition(b'\n'); self.buffer=bytearray(tail)
                value=json.loads(line)
                if value.get('id')==self.serial:
                    if 'error' in value: raise RuntimeError('MCP JSON-RPC error')
                    return value['result']
                continue
            if not self.sel.select(min(0.2,max(0,deadline-time.monotonic()))): continue
            chunk=os.read(self.process.stdout.fileno(),65536)
            if not chunk: raise RuntimeError('transport closed')
            self.buffer.extend(chunk)
            if len(self.buffer)>4*1024**2: raise RuntimeError('response exceeded probe limit')
        raise TimeoutError('MCP response timed out')
    def close(self) -> None:
        self.sel.close()
        self.process.stdin.close()
        try: self.process.wait(timeout=20)
        except subprocess.TimeoutExpired:
            self.process.terminate()
            try: self.process.wait(timeout=5)
            except subprocess.TimeoutExpired: self.process.kill();self.process.wait(timeout=5)
        self.process.stdout.close()


def main() -> int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--server',choices=SERVER_NAMES,action='append')
    p.add_argument('--transport',choices=('unix','ssh'),default='unix')
    p.add_argument('--write-workspace',action='store_true',help='Create/read/delete only a uniquely named smoke-test file')
    p.add_argument('--browser-probe',action='store_true',help='Launch each isolated browser on about:blank')
    p.add_argument('--timeout',type=int,default=120)
    args=p.parse_args()
    if os.geteuid()==0: p.error('run smoke as the desktop user, not root')
    report=[]
    for server in args.server or SERVER_NAMES:
        rpc=None;test_file=None
        try:
            rpc=RPC(server,args.transport,args.timeout)
            init=rpc.request('initialize',{'protocolVersion':'2025-03-26','capabilities':{},
                 'clientInfo':{'name':'codex-mcp-acceptance','version':'1.0.0'}})
            rpc.send({'jsonrpc':'2.0','method':'notifications/initialized'})
            tools=rpc.request('tools/list',{}).get('tools',[])
            if not tools: raise RuntimeError('server returned no tools')
            if server=='filesystem' and args.write_workspace:
                name='.codex-mcp-smoke-'+uuid.uuid4().hex+'.txt'
                test_file=Path.home()/'Workspace'/name
                body='codex-mcp filesystem write/read acceptance\n'
                result=rpc.request('tools/call',{'name':'write_file','arguments':{'path':'/workspace/'+name,'content':body}})
                if result.get('isError') or test_file.read_text()!=body:
                    raise RuntimeError('Workspace write or desktop read verification failed')
                reader='read_text_file' if any(t['name']=='read_text_file' for t in tools) else 'read_file'
                result=rpc.request('tools/call',{'name':reader,'arguments':{'path':'/workspace/'+name}})
                if result.get('isError'): raise RuntimeError('filesystem read tool failed')
                # Desktop edit + removal verifies the shared ACL contract too.
                test_file.write_text('desktop-owned edit\n'); test_file.unlink();test_file=None
            if server in ('playwright','chrome-devtools') and args.browser_probe:
                tool='browser_navigate' if server=='playwright' else 'new_page'
                if tool not in {t['name'] for t in tools}:
                    raise RuntimeError('browser probe tool is absent')
                result=rpc.request('tools/call',{'name':tool,'arguments':{'url':'about:blank'}})
                if result.get('isError'):raise RuntimeError('isolated browser launch probe failed')
            report.append({'server':server,'ok':True,'tools':len(tools),
                           'protocol':init.get('protocolVersion')})
        except (OSError,ValueError,RuntimeError,TimeoutError) as exc:
            report.append({'server':server,'ok':False,'error':type(exc).__name__,
                           'detail':'Check broker metadata logs and required credentials; upstream payload omitted.'})
        finally:
            if rpc: rpc.close()
            if test_file and test_file.exists(): test_file.unlink()
    print(json.dumps({'transport':args.transport,'results':report},indent=2))
    return int(any(not r['ok'] for r in report))

if __name__=='__main__': raise SystemExit(main())
