from __future__ import annotations
import contextlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'lib'))
from common import (SOURCE_ROOT,ConfigError,SERVER_NAMES,load_env,parse_env,atomic_write,locked)
import runtime
from broker import read_header
from relay import bridge,shutdown_write,RelayError
from install import render_units
import toolchain


def config(root: Path) -> dict:
    cfg=load_env(SOURCE_ROOT/'.env')
    cfg.update(DESKTOP_USER='desktop',DESKTOP_HOME='/home/desktop',DESKTOP_UID=1000,DESKTOP_GID=1000,
               DEVOPS_UID=1001,DEVOPS_GID=1001,WORKSPACE='/home/desktop/Workspace',
               MCP_RUNTIME_ROOT=str(root/'runtime'),MCP_STATE_ROOT=str(root/'state'),
               IMAGE_ID='sha256:'+'a'*64,TOOLCHAIN_ENABLED=False)
    Path(cfg['MCP_RUNTIME_ROOT']).mkdir(exist_ok=True)
    return cfg

class Base(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory(); self.root=Path(self.temp.name)
        self.cfg=config(self.root)
    def tearDown(self): self.temp.cleanup()

class EnvironmentTests(Base):
    def altered(self,key,value):
        text=(SOURCE_ROOT/'.env').read_text()
        import re
        text=re.sub(r'^'+key+r'=.*$',lambda m:key+'='+value,text,flags=re.M)
        path=self.root/'env';path.write_text(text);return path
    def test_defaults(self):
        self.assertEqual(load_env(SOURCE_ROOT/'.env')['PODMAN_USER'],'devops')
    def test_no_shell_expansion(self):
        for value in ('$(id)','`id`','${HOME}','/tmp\\path'):
            with self.subTest(value=value), self.assertRaises(ConfigError):
                load_env(self.altered('WORKSPACE',value))
    def test_rejects_unknown(self):
        p=self.root/'env';p.write_text((SOURCE_ROOT/'.env').read_text()+'\nBAD_KEY=1\n')
        with self.assertRaises(ConfigError):load_env(p)
    def test_rejects_duplicate(self):
        p=self.root/'env';p.write_text('ABC=1\nABC=2\n')
        with self.assertRaises(ConfigError):parse_env(p)
    def test_rejects_missing(self):
        p=self.root/'env';p.write_text('PODMAN_USER=devops\n')
        with self.assertRaises(ConfigError):load_env(p)
    def test_rejects_vulnerable_dbhub(self):
        with self.assertRaises(ConfigError):load_env(self.altered('DBHUB_PATCH_VERSION','0.22.3'))
    def test_rejects_unpinned_image(self):
        with self.assertRaises(ConfigError):load_env(self.altered('MCP_BASE_IMAGE','image:latest'))
    def test_rejects_nondevops(self):
        with self.assertRaises(ConfigError):load_env(self.altered('PODMAN_USER','root'))
    def test_rejects_boolean_synonyms(self):
        with self.assertRaises(ConfigError):load_env(self.altered('SSH_ENABLED','yes'))
    def test_rejects_limits(self):
        with self.assertRaises(ConfigError):load_env(self.altered('MAX_SESSIONS','999999'))
    def test_rejects_mount_delimiter(self):
        with self.assertRaises(ConfigError):load_env(self.altered('WORKSPACE','/home/desktop/Workspace,ro=false'))
    def test_rejects_traversal(self):
        with self.assertRaises(ConfigError):load_env(self.altered('WORKSPACE','/home/../etc'))
    def test_rejects_invalid_timezone(self):
        with self.assertRaises(ConfigError):load_env(self.altered('LOCAL_TIMEZONE','Invalid/Nowhere'))
    def test_rejects_public_subnet(self):
        with self.assertRaises(ConfigError):load_env(self.altered('NETWORK_SUBNET','8.8.8.0/24'))

class AtomicTests(Base):
    def test_atomic_idempotent(self):
        p=self.root/'state';self.assertTrue(atomic_write(p,'one'))
        self.assertFalse(atomic_write(p,'one')); self.assertTrue(atomic_write(p,'two'))
        self.assertEqual(p.read_text(),'two'); self.assertEqual(p.stat().st_mode&0o777,0o600)
    def test_atomic_no_symlink(self):
        p=self.root/'link';p.symlink_to(self.root/'other')
        with self.assertRaises(ConfigError):atomic_write(p,'no')
    def test_lock_excludes_second_holder(self):
        with locked(self.root/'lock'):
            with self.assertRaises(BlockingIOError):
                with locked(self.root/'lock'): pass
    def test_slots_exhaust_and_release(self):
        with contextlib.ExitStack() as one:
            self.assertEqual(runtime.acquire_slot(one,self.root,'slots',1),0)
            with contextlib.ExitStack() as two:
                with self.assertRaises(ConfigError): runtime.acquire_slot(two,self.root,'slots',1)
        with contextlib.ExitStack() as three:self.assertEqual(runtime.acquire_slot(three,self.root,'slots',1),0)

class CredentialTests(Base):
    def test_subset_only_and_permissions(self):
        source=self.root/'source';source.mkdir()
        (source/'context7-api-key').write_text('secret\n');(source/'postgres-dsn').write_text('other')
        dest=self.root/'credentials'
        runtime.stage_credentials(source,dest,runtime.catalog()['context7'])
        self.assertEqual([x.name for x in dest.iterdir()],['context7-api-key'])
        self.assertEqual((dest/'context7-api-key').read_text(),'secret')
        self.assertEqual(dest.stat().st_mode&0o777,0o700)
        self.assertEqual((dest/'context7-api-key').stat().st_mode&0o777,0o600)
    def test_required_missing(self):
        source=self.root/'source';source.mkdir()
        with self.assertRaises(ConfigError):runtime.stage_credentials(source,self.root/'dest',runtime.catalog()['postgres'])
    def test_required_empty(self):
        source=self.root/'source';source.mkdir();(source/'postgres-dsn').touch()
        with self.assertRaises(ConfigError):runtime.stage_credentials(source,self.root/'dest',runtime.catalog()['postgres'])
    def test_newline_rejected(self):
        source=self.root/'source';source.mkdir();(source/'postgres-dsn').write_text('abc\ndef')
        with self.assertRaises(ConfigError):runtime.stage_credentials(source,self.root/'dest',runtime.catalog()['postgres'])
    def test_oversize_rejected(self):
        source=self.root/'source';source.mkdir();(source/'postgres-dsn').write_bytes(b'x'*65537)
        with self.assertRaises(ConfigError):runtime.stage_credentials(source,self.root/'dest',runtime.catalog()['postgres'])
    def test_credential_symlink_rejected(self):
        source=self.root/'source';source.mkdir();(source/'postgres-dsn').symlink_to('/etc/passwd')
        with self.assertRaises(OSError):runtime.stage_credentials(source,self.root/'dest',runtime.catalog()['postgres'])

class CommandTests(Base):
    def command(self,server):
        return runtime.build_command(self.cfg,server,self.root,'codex-mcp-'+server+'-'+'b'*32,'b'*32)
    def test_all_thirteen(self):
        self.assertEqual(set(runtime.catalog()),set(SERVER_NAMES));self.assertEqual(len(SERVER_NAMES),13)
        for server in SERVER_NAMES:
            with self.subTest(server=server):
                c=self.command(server)
                self.assertIn('--read-only',c);self.assertIn('devops:devops',c)
                self.assertIn('--cap-drop=all',c);self.assertIn('--security-opt=no-new-privileges',c)
                self.assertEqual(c[-2],self.cfg['IMAGE_ID']);self.assertEqual(c[-1],server)
                self.assertNotIn('--privileged',c);self.assertNotIn('--network=host',c)
                self.assertFalse(any('podman.sock' in v for i,v in enumerate(c) if i and c[i-1]=='--mount'))
    def test_workspace_rw_only_where_registered(self):
        for server,spec in runtime.catalog().items():
            c=self.command(server); mounts=[c[i+1] for i,v in enumerate(c) if v=='--mount']
            ws=[x for x in mounts if 'destination=/workspace,' in x]
            if spec['workspace']=='none':self.assertFalse(ws)
            else:
                self.assertEqual(len(ws),1)
                self.assertIn('ro=true' if spec['workspace']=='ro' else 'rw=true',ws[0])
    def test_network_selection(self):
        for server,spec in runtime.catalog().items():
            c=self.command(server)
            self.assertEqual(c[c.index('--network')+1],self.cfg['MCP_NETWORK'] if spec['network'] else 'none')
    def test_no_secret_environment(self):
        c=self.command('postgres')
        self.assertFalse(any('POSTGRES_DSN=' in x or 'API_KEY=' in x for x in c))
    def test_no_mutable_image(self):
        self.cfg['IMAGE_ID']='image:latest'
        with self.assertRaises(ConfigError):self.command('filesystem')
    def test_no_arbitrary_server(self):
        with self.assertRaises(ConfigError):self.command('shell')
    def test_preserve_browser_assets(self):
        self.assertFalse(any('destination=/cache,' in x for x in self.command('playwright')))
    def test_browser_limits(self):
        c=self.command('playwright');self.assertEqual(c[c.index('--memory')+1],self.cfg['BROWSER_MEMORY'])
    def test_state_only_memory_sqlite(self):
        for server in SERVER_NAMES:
            has=any('destination=/state,' in x for x in self.command(server))
            self.assertEqual(has,server in ('memory','sqlite'))

class HeaderTests(unittest.TestCase):
    def header(self,data,max_size=1024):
        a,b=socket.socketpair()
        try:b.sendall(data);b.shutdown(socket.SHUT_WR);return read_header(a,0.2,max_size)
        finally:a.close();b.close()
    def test_valid(self):self.assertEqual(self.header(b'{"version":1,"server":"filesystem"}\n')['server'],'filesystem')
    def test_bad_envelopes(self):
        for obj in ([],{'version':1},{'version':True,'server':'git'},{'version':2,'server':'git'},
                    {'version':1,'server':'sh'},{'version':1,'server':'git','args':['id']}):
            with self.subTest(obj=obj),self.assertRaises(ConfigError):self.header(json.dumps(obj).encode()+b'\n')
    def test_no_newline(self):
        with self.assertRaises(ConfigError):self.header(b'{}')
    def test_oversize(self):
        with self.assertRaises(ConfigError):self.header(b'a'*1024+b'\n')
    def test_invalid_utf8(self):
        with self.assertRaises(ConfigError):self.header(b'\xff\n')
    def test_preserves_following_bytes(self):
        a,b=socket.socketpair()
        try:
            b.sendall(b'{"version":1,"server":"git"}\nMCP-BYTES')
            read_header(a,1);self.assertEqual(a.recv(99),b'MCP-BYTES')
        finally:a.close();b.close()
    def test_deadline(self):
        a,b=socket.socketpair()
        try:
            with self.assertRaises((TimeoutError,ConfigError)):read_header(a,0.01)
        finally:a.close();b.close()

class LifecycleTests(Base):
    def test_required_failure_removes_staging(self):
        credentials=self.root/'credentials';credentials.mkdir()
        with patch.dict(os.environ,{'CREDENTIALS_DIRECTORY':str(credentials)}):
            with self.assertRaises(ConfigError):
                with runtime.Session(self.cfg,'postgres'):pass
        self.assertFalse(list(Path(self.cfg['MCP_RUNTIME_ROOT']).glob('session-*')))
    def test_retains_staging_when_cleanup_fails(self):
        credentials=self.root/'credentials';credentials.mkdir()
        with patch.dict(os.environ,{'CREDENTIALS_DIRECTORY':str(credentials)}),patch('runtime.remove_container',return_value=False):
            with runtime.Session(self.cfg,'filesystem') as session:session.started=True
        self.assertTrue(session.path.exists())
    def test_deletes_staging_after_success(self):
        credentials=self.root/'credentials';credentials.mkdir()
        with patch.dict(os.environ,{'CREDENTIALS_DIRECTORY':str(credentials)}),patch('runtime.remove_container',return_value=True):
            with runtime.Session(self.cfg,'filesystem') as session:session.started=True
        self.assertFalse(session.path.exists())
    def test_api_error_not_absence(self):
        failure=subprocess.CompletedProcess([],125,b'',b'api failed')
        with patch('runtime.run',return_value=failure):
            self.assertFalse(runtime.remove_container(self.cfg,'codex-mcp-git-'+'a'*32))
    def test_wrong_container_label_refused(self):
        result=subprocess.CompletedProcess([],0,b'{}',b'')
        with patch('runtime.run',return_value=result),self.assertRaises(ConfigError):
            runtime.remove_container(self.cfg,'codex-mcp-git-'+'a'*32)
    def test_arbitrary_container_name_refused(self):
        with self.assertRaises(ConfigError):runtime.remove_container(self.cfg,'postgres-production')
    def test_gc_ignores_active_session(self):
        credentials=self.root/'credentials';credentials.mkdir()
        with patch.dict(os.environ,{'CREDENTIALS_DIRECTORY':str(credentials)}):
            with runtime.Session(self.cfg,'filesystem') as session:
                self.assertEqual(runtime.collect(self.cfg,scan_engine=False),{'removed':0,'deferred':0})
    def test_gc_removes_only_owned_staging(self):
        root=Path(self.cfg['MCP_RUNTIME_ROOT']);sid='a'*32;p=root/('session-'+sid);p.mkdir()
        (p/'metadata.json').write_text(json.dumps({'id':sid,'name':'codex-mcp-git-'+sid,'instance':'old'}))
        alien=root/'not-our-directory';alien.mkdir()
        with patch('runtime.remove_container',return_value=True):
            self.assertEqual(runtime.collect(self.cfg,scan_engine=False),{'removed':1,'deferred':0})
        self.assertTrue(alien.exists())

class RelayTests(unittest.TestCase):
    def test_binary_backpressure_and_halfclose(self):
        a,b=socket.socketpair()
        process=subprocess.Popen([sys.executable,'-u','-c',
             'import os;\nwhile True:\n b=os.read(0,2048)\n if not b:break\n os.write(1,b)\nos.write(2,b"d"*100000)'],
             stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        result={};errors=[]
        def relay():
            try:result.update(bridge(a.fileno(),a.fileno(),process.stdout.fileno(),process.stdin.fileno(),
                     close_write_a=lambda:shutdown_write(a),close_write_b=process.stdin.close,
                     limit=4096,idle=5,lifetime=10,stderr_fd=process.stderr.fileno(),eof_grace=2))
            except BaseException as exc:errors.append(exc)
        worker=threading.Thread(target=relay);worker.start()
        data=bytes(range(256))*1024
        def send():b.sendall(data);b.shutdown(socket.SHUT_WR)
        sender=threading.Thread(target=send);sender.start()
        output=bytearray();b.settimeout(8)
        try:
            while True:
                block=b.recv(65536)
                if not block:break
                output.extend(block)
        finally:
            sender.join(3);worker.join(3);a.close();b.close()
            if process.poll() is None:process.terminate()
            process.wait(timeout=3)
            for f in (process.stdin,process.stdout,process.stderr):f.close()
        self.assertFalse(worker.is_alive());self.assertFalse(errors,errors)
        self.assertEqual(bytes(output),data);self.assertEqual(result['to_server_bytes'],len(data))
    def test_interrupt(self):
        a,b=socket.socketpair()
        try:
            with self.assertRaises(RelayError):
                bridge(a.fileno(),a.fileno(),b.fileno(),b.fileno(),close_write_a=lambda:None,
                       close_write_b=lambda:None,stopped=lambda:True)
        finally:a.close();b.close()
    def test_startup_timeout(self):
        a,b=socket.socketpair()
        try:
            with self.assertRaises(RelayError):
                bridge(a.fileno(),a.fileno(),b.fileno(),b.fileno(),close_write_a=lambda:None,
                       close_write_b=lambda:None,startup_timeout=0.02)
        finally:a.close();b.close()

class IntegrationContractTests(Base):
    def test_units_render_without_unresolved_tokens(self):
        import re
        for name,text in render_units(self.cfg).items():
            self.assertFalse(re.search(r'@[A-Z_]+@',text),name)
        service=render_units(self.cfg)['codex-mcp@.service']
        self.assertIn('User=devops',service);self.assertIn('StandardInput=socket',service)
        self.assertEqual(service.count('LoadCredential='),9)
    def test_all_profile_paths_are_covered(self):
        env,paths=toolchain.profile_environment(self.cfg)
        roots=[x['target'] for x in toolchain.host_roots(self.cfg)]
        scratch=[f'/pool/{x}/desktop' for x in ('build','cache','db')]
        for path in paths:
            self.assertTrue(any(path==r or path.startswith(r+'/') for r in roots+scratch),path)
        self.assertEqual(env['NODE'],'/usr/local/lib/node-26/bin/node')
        self.assertEqual(env['HOME'],'/home/devops')
    def test_tool_roots_do_not_share_live_databases_or_home(self):
        paths=[x['source'] for x in toolchain.host_roots(self.cfg)]
        self.assertFalse(any('/postgresql' in x or '/.ssh' in x or x=='/home/desktop' for x in paths))
    def test_private_tool_scratch(self):
        self.cfg['TOOLCHAIN_ENABLED']=True
        with patch('toolchain.host_roots',return_value=[]):
            mounts,env=toolchain.mounts(self.cfg,self.root)
        self.assertEqual(len(mounts),3)
        self.assertTrue(all(str(self.root) in x[0] for x in mounts))

if __name__=='__main__':unittest.main()

class RecoveryTests(Base):
    def test_gc_reconciles_reboot_orphan(self):
        name='codex-mcp-context7-'+'b'*32
        result=subprocess.CompletedProcess([],0,(name+'\nnot-ours\n').encode(),b'')
        with patch('runtime.run',return_value=result),patch('runtime.remove_container',return_value=True) as remove:
            self.assertEqual(runtime.collect(self.cfg),{'removed':1,'deferred':0})
            remove.assert_called_once_with(self.cfg,name)
    def test_gc_defers_unavailable_engine(self):
        result=subprocess.CompletedProcess([],125,b'',b'failure')
        with patch('runtime.run',return_value=result):
            self.assertEqual(runtime.collect(self.cfg),{'removed':0,'deferred':1})
    def test_snapshot_refuses_remaining_containers(self):
        import admin
        result=subprocess.CompletedProcess([],0,b'codex-mcp-memory-owned\n',b'')
        with patch('admin.run'),patch('admin.as_devops',return_value=result),self.assertRaises(ConfigError):
            admin.quiesce(self.cfg)
    def test_snapshot_accepts_drained_engine(self):
        import admin
        result=subprocess.CompletedProcess([],0,b'',b'')
        with patch('admin.run') as stop,patch('admin.as_devops',return_value=result):
            admin.quiesce(self.cfg)
            stop.assert_called_once_with(['/usr/bin/systemctl','stop','codex-mcp.target'])
    def test_git_safe_directory_when_host_tools_off(self):
        p=self.root/'session';p.mkdir();(p/'credentials').mkdir()
        args=runtime.build_command(self.cfg,'git',p,'codex-mcp-git-'+'a'*32,'a'*32)
        self.assertIn('GIT_CONFIG_VALUE_0=/workspace',args)
    def test_ssh_runtime_preparation_is_boot_scoped(self):
        import inspect,install
        self.assertIn("Path('/run/sshd')",inspect.getsource(install.prepare))
    def test_prepare_drops_privilege_for_mutable_runtime(self):
        import inspect,install
        source=inspect.getsource(install.prepare)
        self.assertIn("'/usr/sbin/runuser','-u','devops'",source)
        self.assertNotIn("owned_directory(Path(cfg['MCP_RUNTIME_ROOT'])",source)

class BrowserSecurityTests(Base):
    def test_preserves_seccomp_baseline(self):
        from browser_security import derive_profile
        base={'defaultAction':'SCMP_ACT_ERRNO','archMap':[],
              'syscalls':[{'names':['ptrace'],'action':'SCMP_ACT_ERRNO'}]}
        result=derive_profile(base)
        self.assertEqual(len(base['syscalls']),1)
        self.assertEqual(result['syscalls'][0],base['syscalls'][0])
        self.assertEqual(set(result['syscalls'][-1]['names']),{'clone','setns','unshare'})
    def test_rejects_permissive_seccomp(self):
        from browser_security import derive_profile
        with self.assertRaises(ConfigError):derive_profile({'defaultAction':'SCMP_ACT_ALLOW','syscalls':[]})
    def test_browser_has_scoped_seccomp(self):
        p=self.root/'session';p.mkdir();(p/'credentials').mkdir()
        args=runtime.build_command(self.cfg,'playwright',p,'codex-mcp-playwright-'+'a'*32,'a'*32)
        self.assertIn('seccomp=/etc/codex/mcp/browser-seccomp.json',args)
    def test_other_modes_keep_engine_seccomp(self):
        p=self.root/'session';p.mkdir();(p/'credentials').mkdir()
        args=runtime.build_command(self.cfg,'git',p,'codex-mcp-git-'+'a'*32,'a'*32)
        self.assertFalse(any(x.startswith('seccomp=') for x in args))
