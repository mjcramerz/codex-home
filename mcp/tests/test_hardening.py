"""Offline tests for framing, secret imports, cancellation and client snippets."""
import importlib.util
import io
import json
import os
from pathlib import Path
import signal
import socket
import subprocess
import tempfile
import time
import tomllib
import unittest
from unittest.mock import patch,MagicMock
from test_mcp import Base,SOURCE_ROOT,ConfigError,load_env
import admin
import broker
import client
import runtime
from common import digest_tree
import struct
from relay import bridge

class HardeningTests(Base):
    def test_duplicate_header_keys_rejected(self):
        a,b=socket.socketpair()
        try:
            b.sendall(b'{"version":1,"server":"time","server":"git"}\n')
            with self.assertRaises(ConfigError):broker.read_header(a,1)
        finally:a.close();b.close()
    def test_header_does_not_consume_mcp_payload(self):
        a,b=socket.socketpair()
        try:
            b.sendall(b'{"version":1,"server":"time"}\n{"jsonrpc":"2.0"}\n')
            self.assertEqual(broker.read_header(a,1)['server'],'time')
            self.assertEqual(a.recv(1024),b'{"jsonrpc":"2.0"}\n')
        finally:a.close();b.close()
    def test_zero_relay_capacity_rejected_before_io(self):
        with self.assertRaises(ValueError):bridge(-1,-1,-1,-1,close_write_a=lambda:None,close_write_b=lambda:None,limit=0)
    def test_import_refuses_unknown_credential_name(self):
        with patch.object(admin,'root_required'),self.assertRaises(ConfigError):admin.credential(self.cfg,'../escape',None)
    def test_import_refuses_public_secret_file(self):
        p=self.root/'secret';p.write_text('value');p.chmod(0o644)
        with patch.object(admin,'root_required'),self.assertRaises(ConfigError):admin.credential(self.cfg,'postgres-dsn',p)
    def test_import_refuses_symlink(self):
        p=self.root/'secret';p.symlink_to('/etc/passwd')
        with patch.object(admin,'root_required'),self.assertRaises(OSError):admin.credential(self.cfg,'postgres-dsn',p)
    def test_import_refuses_oversize_and_non_utf8(self):
        p=self.root/'secret'
        for content in (b'x'*65539,b'\xff'):
            p.write_bytes(content);p.chmod(0o600)
            with patch.object(admin,'root_required'),self.assertRaises(ConfigError):admin.credential(self.cfg,'postgres-dsn',p)
    def test_private_import_does_not_emit_value(self):
        p=self.root/'secret';p.write_text('private-value\n');p.chmod(0o600)
        with patch.object(admin,'root_required'),patch.object(admin,'atomic_write') as write,patch('sys.stdout',new_callable=io.StringIO) as out:
            admin.credential(self.cfg,'postgres-dsn',p)
        self.assertEqual(write.call_args.args[1],b'private-value')
        self.assertNotIn('private-value',out.getvalue())
    def test_process_termination_targets_owned_group(self):
        session=runtime.Session(self.cfg,'time');session.path.mkdir()
        process=MagicMock();process.pid=123456;process.poll.return_value=None
        session.process=process
        with patch.object(runtime.os,'killpg') as kill:
            session.__exit__()
        kill.assert_any_call(123456,signal.SIGTERM)
    def fake_client(self,reply,uid=1001):
        sock=MagicMock();sock.__enter__.return_value=sock
        sock.getsockopt.return_value=struct.pack('3i',123,uid,1001)
        sock.recv.side_effect=[reply[i:i+1] for i in range(len(reply))]
        cfg={'connect_timeout':1,'socket':'/unused','devops_uid':1001,
             'max_buffer':4096,'idle_timeout':60,'max_lifetime':60,'stop_timeout':1}
        return sock,cfg
    def test_client_response_requires_protocol_version(self):
        sock,cfg=self.fake_client(b'{"ok":true,"version":true}\n')
        with patch.object(client.socket,'socket',return_value=sock),patch.object(client.signal,'signal'),self.assertRaises(ConfigError):
            client.connect_unix(cfg,'time')
    def test_client_rejects_impostor_peer(self):
        sock,cfg=self.fake_client(b'',uid=9999)
        with patch.object(client.socket,'socket',return_value=sock),patch.object(client.signal,'signal'),self.assertRaises(ConfigError):
            client.connect_unix(cfg,'time')
        sock.sendall.assert_not_called()
    def test_handshake_uses_absolute_deadline(self):
        sock,cfg=self.fake_client(b'{"ok":true}\n')
        with patch.object(client.socket,'socket',return_value=sock),patch.object(client.signal,'signal'),patch.object(client.time,'monotonic',side_effect=[10,10.2,11.01]),self.assertRaises(ConfigError):
            client.connect_unix(cfg,'time')
        self.assertEqual(sock.recv.call_count,1)
    def test_release_digest_excludes_env_and_generated_outputs(self):
        root=self.root/'release';root.mkdir();(root/'a.py').write_text('code')
        first=digest_tree(root)
        (root/'.env').write_text('operator-specific');(root/'build').mkdir();(root/'build/report').write_text('generated')
        self.assertEqual(first,digest_tree(root))
        (root/'a.py').write_text('changed');self.assertNotEqual(first,digest_tree(root))
    def test_release_symlink_rejected(self):
        root=self.root/'release';root.mkdir();(root/'bad').symlink_to('/etc/passwd')
        with self.assertRaises(ConfigError):digest_tree(root)
    def test_deployment_mutations_share_one_lock(self):
        text=Path(admin.__file__).read_text()
        self.assertIn("Path('/etc/codex/mcp/admin.lock')",text)
        self.assertIn("locked(root/'admin.lock',blocking=True)",(SOURCE_ROOT/'lib/install.py').read_text())
    def test_generated_transports_have_all_servers_without_secrets(self):
        spec=importlib.util.spec_from_file_location('configure_clients',SOURCE_ROOT/'scripts/configure_clients.py')
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        for mode in ('configured','unix','ssh'):
            text=module.render(load_env(SOURCE_ROOT/'.env'),mode)
            servers=tomllib.loads(text)['mcp_servers'];self.assertEqual(len(servers),13)
            for cfg in servers.values():
                self.assertTrue(cfg['enabled']);self.assertNotIn('env',cfg)
                if mode!='configured':self.assertEqual(cfg['args'][-2:],['--transport',mode])

if __name__=='__main__':unittest.main()
