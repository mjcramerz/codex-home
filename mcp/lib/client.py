"""Unprivileged Codex stdio connector. stdout contains MCP traffic only."""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import shlex
import signal
import stat
import struct
import time
import socket
import sys
from common import ConfigError, SERVER_NAMES
from relay import bridge, shutdown_write

CLIENT_CONFIG = Path('/etc/codex/mcp/client.json')


def configuration() -> dict:
    st = CLIENT_CONFIG.lstat()
    if not stat.S_ISREG(st.st_mode) or CLIENT_CONFIG.is_symlink() or st.st_uid != 0 or st.st_mode & 0o022:
        raise ConfigError('unsafe client configuration')
    cfg = json.loads(CLIENT_CONFIG.read_text())
    if cfg.get('version') != 1:
        raise ConfigError('unsupported client configuration')
    return cfg


def connect_unix(cfg: dict, server: str) -> int:
    stop = False
    def signal_handler(_signum: int, _frame: object) -> None:
        nonlocal stop
        stop = True
    for sig in (signal.SIGINT,signal.SIGTERM,signal.SIGHUP):
        signal.signal(sig,signal_handler)
    with socket.socket(socket.AF_UNIX,socket.SOCK_STREAM) as sock:
        deadline = time.monotonic()+cfg['connect_timeout']
        sock.settimeout(cfg['connect_timeout'])
        sock.connect(cfg['socket'])
        _, peer_uid, _ = struct.unpack('3i',sock.getsockopt(socket.SOL_SOCKET,socket.SO_PEERCRED,12))
        # PID 1 owns the listening socket until activation; the handler is devops.
        if peer_uid not in (0,cfg['devops_uid']):
            raise ConfigError('untrusted local broker identity')
        sock.sendall((json.dumps({'version':1,'server':server})+'\n').encode())
        answer = bytearray()
        while len(answer) < 4096:
            remaining = deadline-time.monotonic()
            if remaining <= 0 or stop:
                raise ConfigError('broker handshake timed out or interrupted')
            sock.settimeout(remaining)
            b = sock.recv(1)
            if not b:
                raise ConfigError('broker disconnected during startup')
            answer += b
            if b == b'\n':
                break
        else:
            raise ConfigError('invalid broker response length')
        response = json.loads(answer)
        if not isinstance(response,dict) or response.get('ok') is not True:
            raise ConfigError('MCP connection rejected; inspect the broker journal')
        if type(response.get('version')) is not int or response['version'] != 1:
            raise ConfigError('unsupported broker transport version')
        bridge(0,1,sock.fileno(),sock.fileno(),
               close_write_a=lambda: None,close_write_b=lambda: shutdown_write(sock),
               limit=cfg['max_buffer'],idle=cfg['idle_timeout']+30,
               lifetime=cfg['max_lifetime']+30,stopped=lambda:stop,
               eof_grace=cfg['stop_timeout']+5)
    return 0


def connect_ssh(cfg: dict, server: str) -> int:
    ssh = cfg['ssh']
    identity = Path(ssh['identity'])
    if identity.is_symlink() or not identity.is_file():
        raise ConfigError('missing or unsafe SSH identity')
    st = identity.stat()
    if st.st_uid != os.getuid() or st.st_mode & 0o077:
        raise ConfigError('SSH private key must be owned by the desktop account and mode 0600')
    # No user ssh_config, implicit agents, multiplexing, tunnels, or hostkey trust-on-first-use.
    args = ['/usr/bin/ssh','-F','/dev/null','-T','-p',str(ssh['port']),
            '-i',str(identity),'-o','IdentitiesOnly=yes','-o','IdentityAgent=none',
            '-o','BatchMode=yes','-o','PasswordAuthentication=no','-o','KbdInteractiveAuthentication=no',
            '-o','StrictHostKeyChecking=yes','-o','UserKnownHostsFile='+ssh['known_hosts'],
            '-o','GlobalKnownHostsFile=/dev/null','-o','ClearAllForwardings=yes',
            '-o','ServerAliveInterval=30','-o','ServerAliveCountMax=3',
            '-o','ConnectTimeout='+str(ssh['connect_timeout']),
            ssh['user']+'@127.0.0.1','mcp',server]
    os.execv(args[0],args)
    return 1


def gateway() -> int:
    command = os.environ.get('SSH_ORIGINAL_COMMAND','')
    parts = shlex.split(command)
    if len(parts) != 2 or parts[0] != 'mcp' or parts[1] not in SERVER_NAMES:
        raise ConfigError('only a named MCP stdio session is permitted')
    cfg = configuration()
    if os.getuid() != cfg['desktop_uid']:
        raise ConfigError('SSH gateway identity mismatch')
    # Never recursively use SSH inside the forced command.
    return connect_unix(cfg,parts[1])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation',choices=['connect','ssh-gateway'])
    parser.add_argument('server',nargs='?',choices=SERVER_NAMES)
    parser.add_argument('--transport',choices=['unix','ssh'])
    args = parser.parse_args()
    if args.operation == 'ssh-gateway':
        return gateway()
    if args.server is None:
        parser.error('connect requires a server name')
    cfg = configuration()
    if os.getuid() not in (cfg['desktop_uid'],cfg['devops_uid']):
        raise ConfigError('wrong desktop identity')
    transport = args.transport or cfg['transport']
    return connect_unix(cfg,args.server) if transport == 'unix' else connect_ssh(cfg,args.server)
