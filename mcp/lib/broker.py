"""systemd Accept=yes handler. Only the initial control envelope is interpreted."""
from __future__ import annotations
import contextlib
import hashlib
import json
import os
from pathlib import Path
import signal
import socket
import struct
import sys
import time
from common import ConfigError, load_runtime
from relay import RelayError, bridge, shutdown_write
from runtime import Session, catalog, collect


def log(event: str, **fields: object) -> None:
    print(json.dumps({'event':event, **fields}, sort_keys=True), file=sys.stderr, flush=True)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError('duplicate envelope key')
        result[key] = value
    return result


def read_header(sock: socket.socket, timeout: float, max_size: int = 1024) -> dict:
    deadline = time.monotonic()+timeout
    data = bytearray()
    while len(data) < max_size:
        remaining = deadline-time.monotonic()
        if remaining <= 0:
            raise ConfigError('control header timed out')
        sock.settimeout(remaining)
        chunk = sock.recv(1)  # Never consume any subsequent MCP bytes.
        if not chunk:
            raise ConfigError('incomplete control header')
        data += chunk
        if chunk == b'\n':
            try:
                result = json.loads(data, object_pairs_hook=unique_object)
            except (ValueError, UnicodeError):
                raise ConfigError('invalid control header') from None
            if not isinstance(result,dict) or set(result) != {'version','server'}:
                raise ConfigError('invalid control envelope')
            if type(result['version']) is not int or result['version'] != 1:
                raise ConfigError('unsupported transport version')
            if not isinstance(result['server'],str) or result['server'] not in catalog():
                raise ConfigError('unknown MCP server')
            return result
    raise ConfigError('control header too large')


def serve(instance: str = '') -> int:
    cfg = load_runtime()
    if os.geteuid() != cfg['DEVOPS_UID']:
        raise ConfigError('session broker must run as devops')
    sock = socket.socket(fileno=os.dup(0))
    peer_pid, peer_uid, _ = struct.unpack('3i',sock.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
    started_at = time.monotonic()
    ready = False
    interrupted = False
    def terminate(_signum: int, _frame: object) -> None:
        nonlocal interrupted
        interrupted = True
    for sig in (signal.SIGTERM,signal.SIGINT,signal.SIGHUP):
        signal.signal(sig,terminate)
    signal.signal(signal.SIGPIPE,signal.SIG_IGN)
    try:
        if peer_uid not in (cfg['DESKTOP_UID'], cfg['DEVOPS_UID']):
            raise ConfigError('desktop identity not authorized')
        header = read_header(sock,cfg['HEADER_TIMEOUT_SECONDS'])
        server = header['server']
        with Session(cfg,server,instance) as session:
            process = session.start()
            sock.sendall(b'{"ok":true,"version":1}\n')
            ready = True
            log('session_start',server=server,session=session.id,peer_uid=peer_uid,peer_pid=peer_pid)
            assert process.stdin is not None and process.stdout is not None and process.stderr is not None
            digest = hashlib.sha256()
            counters = bridge(sock.fileno(),sock.fileno(),process.stdout.fileno(),process.stdin.fileno(),
                    close_write_a=lambda: shutdown_write(sock),close_write_b=process.stdin.close,
                    limit=cfg['MAX_BUFFER_BYTES'],idle=cfg['IDLE_TIMEOUT_SECONDS'],
                    lifetime=cfg['SESSION_MAX_SECONDS'],stopped=lambda: interrupted,
                    stderr_fd=process.stderr.fileno(),stderr_limit=cfg['MAX_STDERR_BYTES'],
                    stderr_sink=digest.update if cfg['CAPTURE_SERVER_STDERR'] else None,
                    startup_timeout=cfg['STARTUP_TIMEOUT_SECONDS'],eof_grace=cfg['STOP_TIMEOUT_SECONDS'])
            log('session_end',server=server,session=session.id,duration_seconds=round(time.monotonic()-started_at,3),**counters,
                stderr_sample_sha256=digest.hexdigest() if cfg['CAPTURE_SERVER_STDERR'] else None)
        return 0
    except (ConfigError,RelayError,OSError,TimeoutError) as exc:
        # Do not log exception payloads from arbitrary upstream processes.
        message = str(exc) if isinstance(exc,(ConfigError,RelayError)) else type(exc).__name__
        log('session_error',kind=type(exc).__name__,message=message,peer_uid=peer_uid,duration_seconds=round(time.monotonic()-started_at,3))
        if not ready:
            with contextlib.suppress(OSError):
                sock.settimeout(2)
                sock.sendall((json.dumps({'ok':False,'error':message})+'\n').encode())
        return 1
    finally:
        sock.close()


def main() -> int:
    if len(sys.argv) >= 2 and sys.argv[1] == 'serve':
        return serve(sys.argv[2] if len(sys.argv)>2 else '')
    if len(sys.argv) >= 2 and sys.argv[1] == 'gc':
        try:
            log('garbage_collection',**collect(load_runtime(),sys.argv[2] if len(sys.argv)>2 else None))
        except BlockingIOError:
            return 0
        return 0
    raise ConfigError('expected serve or gc')
