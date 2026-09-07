#!/usr/bin/env python3
"""Bounded, quiet execution of the reviewed Perl hook handlers.

MCP/tool content never becomes shell code. On infrastructure failure policy
hooks stop the action; observational hooks report a sanitized warning. Successful
handler output passes through unchanged after JSON shape checks.
"""
from __future__ import annotations
import argparse
import contextlib
import json
import os
from pathlib import Path
import selectors
import signal
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parent
EVENTS = {'SessionStart','SessionEnd','UserPromptSubmit','Stop','PreToolUse',
          'PermissionRequest','PostToolUse','PreCompact','PostCompact',
          'SubagentStart','SubagentStop'}
POLICY_EVENTS = {'PreToolUse','PermissionRequest'}
MAX_INPUT = 1024 * 1024
MAX_OUTPUT = 256 * 1024
MAX_STDERR = 32 * 1024

class HookFailure(RuntimeError):
    pass


def stop_group(process: subprocess.Popen) -> None:
    """Terminate descendants too, including a child left after the leader exits."""
    with contextlib.suppress(ProcessLookupError):
        os.killpg(process.pid, signal.SIGTERM)
    try:
        process.wait(timeout=0.15)
    except subprocess.TimeoutExpired:
        pass
    with contextlib.suppress(ProcessLookupError):
        os.killpg(process.pid, signal.SIGKILL)
    with contextlib.suppress(subprocess.TimeoutExpired):
        process.wait(timeout=0.5)


def read_input(deadline: float) -> bytes:
    data = bytearray()
    with selectors.PollSelector() as selector:
        selector.register(0,selectors.EVENT_READ)
        while time.monotonic() < deadline:
            if not selector.select(timeout=min(.1,max(0,deadline-time.monotonic()))):
                continue
            block = os.read(0,min(65536,MAX_INPUT+1-len(data)))
            if not block:
                return bytes(data)
            data.extend(block)
            if len(data)>MAX_INPUT:
                raise HookFailure('input limit')
    raise HookFailure('input timeout')


def execute(script: Path, payload: bytes, deadline: float) -> bytes:
    expected = ROOT/'scripts'
    if script.parent != expected or script.is_symlink() or not script.is_file():
        raise HookFailure('untrusted handler path')
    if script.suffix != '.pl' or script.stat().st_mode & 0o002:
        raise HookFailure('unsafe handler')
    if len(payload)>MAX_INPUT or not isinstance(json.loads(payload),dict):
        raise HookFailure('invalid input object')
    env = {k:v for k,v in os.environ.items() if k not in {'PERL5OPT','PERL5LIB','PERLLIB','LD_PRELOAD','LD_AUDIT'}}
    env['CODEX_HOME'] = str(ROOT.parent)
    proc = subprocess.Popen(['/usr/bin/perl',str(script)],stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,stderr=subprocess.PIPE,
                            start_new_session=True,close_fds=True,env=env)
    output = bytearray()
    stderr_bytes = 0
    offset = 0
    try:
        with selectors.PollSelector() as selector:
            for stream,event,kind in ((proc.stdin,selectors.EVENT_WRITE,'input'),
                                      (proc.stdout,selectors.EVENT_READ,'output'),
                                      (proc.stderr,selectors.EVENT_READ,'error')):
                os.set_blocking(stream.fileno(),False)
                selector.register(stream,event,kind)
            while selector.get_map():
                if time.monotonic() >= deadline:
                    raise HookFailure('handler timeout')
                for key,_ in selector.select(timeout=.05):
                    stream,kind = key.fileobj,key.data
                    try:
                        if kind=='input':
                            count=os.write(stream.fileno(),payload[offset:offset+65536])
                            if count <= 0:raise HookFailure('input write failed')
                            offset += count
                            if offset==len(payload):
                                selector.unregister(stream);stream.close()
                        else:
                            block=os.read(stream.fileno(),65536)
                            if not block:
                                selector.unregister(stream);stream.close()
                            elif kind=='output':
                                output.extend(block)
                                if len(output)>MAX_OUTPUT:raise HookFailure('output limit')
                            else:
                                stderr_bytes+=len(block)
                                if stderr_bytes>MAX_STDERR:raise HookFailure('stderr limit')
                    except BlockingIOError:
                        continue
                    except BrokenPipeError:
                        raise HookFailure('handler disconnected') from None
            remaining=max(.01,deadline-time.monotonic())
            if proc.wait(timeout=remaining)!=0:
                raise HookFailure('handler failed')
        if output.strip():
            value=json.loads(output)
            if not isinstance(value,dict):raise HookFailure('invalid output object')
            if 'continue' in value and type(value['continue']) is not bool:
                raise HookFailure('invalid continuation value')
        return bytes(output)
    finally:
        stop_group(proc)
        for stream in (proc.stdin,proc.stdout,proc.stderr):
            if stream is not None:stream.close()


def failure(event: str) -> bytes:
    message='Hook infrastructure failed. Check dependencies and the local hook tests; no secret output was forwarded.'
    payload={'continue':event not in POLICY_EVENTS,'systemMessage':message}
    if event in POLICY_EVENTS:
        payload['stopReason']='Required policy hook could not complete.'
    return (json.dumps(payload,separators=(',',':'))+'\n').encode()


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--event',choices=sorted(EVENTS),required=True)
    parser.add_argument('--timeout',type=float,required=True)
    parser.add_argument('--script',required=True)
    args=parser.parse_args()
    def interrupted(_signal,_frame):raise HookFailure('interrupted')
    for sig in (signal.SIGINT,signal.SIGTERM,signal.SIGHUP):signal.signal(sig,interrupted)
    try:
        if not .1 <= args.timeout <= 120:raise HookFailure('invalid timeout')
        deadline=time.monotonic()+args.timeout
        payload=read_input(deadline)
        result=execute(Path(args.script),payload,deadline)
    except (HookFailure,OSError,ValueError,subprocess.SubprocessError):
        result=failure(args.event)
    sys.stdout.buffer.write(result)
    sys.stdout.buffer.flush()
    return 0

if __name__=='__main__':raise SystemExit(main())
