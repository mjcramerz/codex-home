import importlib.util
import json
import os
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('container_entrypoint',ROOT/'container/entrypoint.py')
entry=importlib.util.module_from_spec(spec);spec.loader.exec_module(entry)

class EntryTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
        self.creds=self.root/'creds';self.creds.mkdir()
        self.patches=[patch.object(entry,'ROOT',ROOT),patch.object(entry,'CREDENTIAL_DIR',self.creds),
                      patch.dict(os.environ,{},clear=True)]
        for p in self.patches:p.start()
    def tearDown(self):
        for p in reversed(self.patches):p.stop()
        self.tmp.cleanup()
    def test_context7_credential_not_argv(self):
        (self.creds/'context7-api-key').write_text('not-a-real-test-key')
        args,env=entry.command('context7')
        self.assertNotIn('not-a-real-test-key',' '.join(args))
        self.assertEqual(env['CONTEXT7_API_KEY'],'not-a-real-test-key')
    def test_all_non_database_modes_have_fixed_executable(self):
        for server in json.loads((ROOT/'servers.json').read_text()):
            if server in ('postgres','sqlite'):continue
            args,env=entry.command(server)
            self.assertTrue(args[0].startswith('/usr/local/bin/'),server)
    def test_browser_sandbox_default(self):
        for server in ('playwright','chrome-devtools'):
            args,_=entry.command(server)
            self.assertFalse(any('no-sandbox' in x for x in args))
    def test_browser_sandbox_optin(self):
        os.environ['MCP_BROWSER_NO_SANDBOX']='true'
        for server in ('playwright','chrome-devtools'):
            args,_=entry.command(server)
            self.assertTrue(any('no-sandbox' in x for x in args))
    def test_fetch_user_agent_and_robots_knobs(self):
        os.environ['MCP_FETCH_IGNORE_ROBOTS_TXT']='true';os.environ['MCP_FETCH_USER_AGENT']='TEST/1'
        args,_=entry.command('fetch')
        self.assertIn('--ignore-robots-txt',args);self.assertIn('TEST/1',args)
    def test_proxy_credential_not_argv(self):
        (self.creds/'fetch-proxy-url').write_text('http://u:p@example.invalid:8888')
        args,env=entry.command('fetch')
        self.assertNotIn('u:p',' '.join(args));self.assertIn('u:p',env['HTTPS_PROXY'])
    def test_time_zone(self):
        os.environ['LOCAL_TIMEZONE']='UTC'
        args,_=entry.command('time');self.assertEqual(args[-1],'UTC')
    def test_no_root_paths_for_memory(self):
        args,env=entry.command('memory');self.assertEqual(env['MEMORY_FILE_PATH'],'/state/memory.jsonl')
    def db(self,server):
        real=Path
        with patch.object(entry,'Path',side_effect=lambda x:self.root/'dbhub.toml' if str(x)=='/tmp/dbhub.toml' else real(x)):
            entry.db_config(server)
        return tomllib.loads((self.root/'dbhub.toml').read_text())
    def test_postgres_requires_tls(self):
        (self.creds/'postgres-dsn').write_text('postgresql://test:fake@db.example.invalid/test')
        with self.assertRaises(ValueError):self.db('postgres')
    def test_postgres_readonly_default_and_secret_file(self):
        dsn='postgresql://test:fake@db.example.invalid/test?sslmode=verify-full'
        (self.creds/'postgres-dsn').write_text(dsn)
        data=self.db('postgres');self.assertEqual(data['sources'][0]['dsn'],dsn)
        self.assertTrue(data['tools'][0]['readonly'])
        self.assertEqual((self.root/'dbhub.toml').stat().st_mode&0o777,0o600)
    def test_postgres_readonly_false_honored(self):
        os.environ['MCP_POSTGRES_READONLY']='false'
        (self.creds/'postgres-dsn').write_text('postgresql://u:p@db.example.invalid/db?sslmode=require')
        self.assertFalse(self.db('postgres')['tools'][0]['readonly'])
    def test_sqlite_readonly_knob(self):
        os.environ['MCP_SQLITE_READONLY']='true'
        self.assertTrue(self.db('sqlite')['tools'][0]['readonly'])
    def test_credential_invalid_encoding(self):
        (self.creds/'context7-api-key').write_bytes(b'\xffsecret')
        with self.assertRaises(ValueError) as raised:entry.credential('context7-api-key')
        self.assertNotIn('secret',str(raised.exception))
    def test_unknown_command_rejected(self):
        with self.assertRaises(ValueError):entry.command('bash')

if __name__=='__main__':unittest.main()
