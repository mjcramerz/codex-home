"""Instruction, catalog, example and deployment contracts; entirely offline."""
import hashlib
import json
from pathlib import Path
import re
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = json.loads((ROOT/'home/config.schema.json').read_text())
SOURCE = json.loads((ROOT/'tests/fixtures/source.json').read_text())
CATALOG = json.loads((ROOT/'home/models_catalog.json').read_text())
MODELS = {m['slug']: m for m in CATALOG['models']}
MANIFEST = json.loads((ROOT/'instructions/manifest.json').read_text())
DEPLOY = '/data/codex/usr/'


def load(path):
    return tomllib.loads(path.read_text())


def flatten(data, prefix=''):
    result = {}
    for key, value in data.items():
        path = prefix+'.'+key if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, path))
        else:
            result[path] = value
    return result


def instruction_fields(node, prefix=''):
    if '$ref' in node:
        node = SCHEMA['definitions'][node['$ref'].rsplit('/', 1)[1]]
    result = set()
    for key, child in node.get('properties', {}).items():
        path = prefix+'.'+key if prefix else key
        if child.get('$ref', '').endswith('/AbsolutePathBuf'):
            result.add(path)
        elif path == 'tools.descriptions':
            result.add(path+'.functions.apply_patch')
        else:
            result.update(instruction_fields(child, path))
    return result


class InstructionContractTests(unittest.TestCase):
    def test_exact_complete_catalog_and_supported_model_metadata(self):
        self.assertEqual(hashlib.sha256((ROOT/'home/models_catalog.json').read_bytes()).hexdigest(),
                         SOURCE['models_catalog_sha256'])
        fixture_models = json.loads((ROOT/'tests/fixtures/models.json').read_text())
        self.assertEqual(set(MODELS), set(fixture_models))
        for model in MODELS.values():
            self.assertTrue(model['model_messages']['instructions_template'].strip())
        self.assertIn('codex-auto-review', MODELS)
        self.assertFalse((ROOT/'home/.models').exists())
        for tree in ['instructions', 'home/instructions']:
            self.assertFalse(list((ROOT/tree).rglob('*catalog*.json')))

    def test_schema_and_supplied_rust_mismatch_is_explicit(self):
        self.assertIn('instruction_overrides', SCHEMA['properties'])
        self.assertNotEqual(SOURCE['rust_config_schema_sha256'], SOURCE['config_schema_sha256'])
        self.assertIs(SOURCE['instruction_overrides_implemented_in_supplied_rust'], False)
        guide = (ROOT/'home/docs/operations/CONFIGURATION.md').read_text().replace('\n', ' ')
        self.assertIn("the source ZIP's older schema", guide)
        self.assertIn('those fields require a binary implementing the supplied schema', guide)

    def test_generated_hook_schemas_match_pinned_source_hashes(self):
        expected = SOURCE['hook_schema_sha256']
        for tree in ['home/.hooks/schemas', 'home/.hooks/schema/generated']:
            files = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (ROOT/tree).glob('*.json')}
            self.assertEqual(files, expected)

    def test_every_instruction_set_covers_exact_supported_fields(self):
        expected = instruction_fields(SCHEMA['definitions']['InstructionOverridesToml'])
        self.assertEqual(len(expected), SOURCE['instruction_overrides_file_count'])
        self.assertEqual(len(MANIFEST['sets']), SOURCE['instruction_set_count'])
        self.assertEqual(MANIFEST['schema_sha256'], SOURCE['config_schema_sha256'])
        for family, entries in MANIFEST['sets'].items():
            with self.subTest(family=family):
                self.assertEqual(set(entries['instructions']), expected)
                base = ROOT/'instructions'/family
                self.assertEqual({p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()},
                                 {entry['file'] for entry in entries['instructions'].values()})
                for key, entry in entries['instructions'].items():
                    file = base/entry['file']
                    text = file.read_text()
                    self.assertTrue(text.strip(), key)
                    self.assertEqual(hashlib.sha256(file.read_bytes()).hexdigest(), entry['sha256'], key)
                    variables = sorted(set(re.findall(r'\{\{\s*([\w.]+)\s*\}\}', text)))
                    if '{n_remaining}' in text:
                        variables.append('n_remaining')
                    self.assertEqual(variables, entry['template_variables'], key)
                    origin = entry['origin']
                    if origin['kind'] == 'catalog_message':
                        value = MODELS[origin['model']]
                        for part in origin['pointer'].split('.'):
                            value = value[part]
                        self.assertEqual(text, value, (family, key))

    def test_canonical_instruction_mirror_is_complete_and_identical(self):
        source, mirror = ROOT/'instructions', ROOT/'home/instructions'
        files = {p.relative_to(source) for p in source.rglob('*') if p.is_file()}
        self.assertEqual(files, {p.relative_to(mirror) for p in mirror.rglob('*') if p.is_file()})
        for rel in files:
            self.assertEqual((source/rel).read_bytes(), (mirror/rel).read_bytes(), str(rel))

    def test_profiles_and_roles_select_matching_base_and_developer_prompts(self):
        home = load(ROOT/'home/config.toml')
        for file in [ROOT/'home/config.toml', *sorted((ROOT/'home').glob('*.config.toml')),
                     *sorted((ROOT/'agents').glob('*.toml'))]:
            cfg = {**home, **load(file)}
            paths = flatten(cfg['instruction_overrides'])
            self.assertEqual(set(paths), instruction_fields(SCHEMA['definitions']['InstructionOverridesToml']), file.name)
            for field, path in paths.items():
                self.assertTrue(path.startswith(DEPLOY), (file.name, field))
                self.assertTrue((ROOT/path.removeprefix(DEPLOY)).is_file(), (file.name, field))
            base = cfg['instruction_overrides']['models']['base_instructions_file']
            self.assertEqual(base, cfg['model_instructions_file'])
            self.assertEqual(cfg['instruction_overrides']['compact_instructions_file'],
                             cfg['experimental_compact_prompt_file'])
            self.assertEqual((ROOT/base.removeprefix(DEPLOY)).read_text(),
                             MODELS[cfg['model']]['model_messages']['instructions_template'], file.name)
            developer = cfg['instruction_overrides']['developer_instructions_file']
            self.assertEqual((ROOT/developer.removeprefix(DEPLOY)).read_text(), cfg['developer_instructions'], file.name)
        for field, native in [('backend_instructions_file', 'experimental_realtime_ws_backend_prompt'),
                              ('start_instructions_file', 'experimental_realtime_start_instructions'),
                              ('startup_context_instructions_file', 'experimental_realtime_ws_startup_context')]:
            path = home['instruction_overrides']['realtime'][field]
            self.assertEqual((ROOT/path.removeprefix(DEPLOY)).read_text(), home[native])

    def test_all_toml_parses_and_has_no_syntax_comments(self):
        tokens = re.compile(r"'''[\s\S]*?'''|\"\"\"(?:\\[\s\S]|[\s\S])*?\"\"\"|\"(?:\\.|[^\"\\])*\"|'[^'\n]*'|#[^\n]*")
        for file in sorted(ROOT.rglob('*.toml')):
            text = file.read_text()
            with self.subTest(file=file.relative_to(ROOT)):
                tomllib.loads(text)
                self.assertFalse(any(m.group().startswith('#') for m in tokens.finditer(text)))

    def test_examples_have_moved_with_companion_project_files(self):
        for obsolete in ['etc/examples', 'home/templates', 'home/snippets/desktop/greetd.toml']:
            self.assertFalse((ROOT/obsolete).exists())
        self.assertTrue((ROOT/'examples/desktop/greetd.toml').is_file())
        for project in ['rust/axum-api', 'rust/cli-app']:
            folder = ROOT/'examples/templates'/project
            self.assertTrue((folder/'Cargo.toml').is_file())
            self.assertTrue((folder/'src/main.rs').is_file())

    def test_provider_examples_obey_native_authentication_exclusivity(self):
        for file in (ROOT/'examples/config').glob('model_providers*.toml'):
            for name, provider in load(file)['model_providers'].items():
                with self.subTest(file=file.name, provider=name):
                    if 'auth' in provider:
                        self.assertFalse(set(provider) & {'env_key', 'experimental_bearer_token', 'aws'})
                        self.assertFalse(provider.get('requires_openai_auth', False))
                        self.assertEqual(provider['auth']['command'], '/usr/bin/false')
                    if 'aws' in provider:
                        self.assertFalse(set(provider) & {'env_key', 'experimental_bearer_token', 'auth', 'gateway_oauth'})
                        self.assertFalse(provider.get('requires_openai_auth', False))
                        self.assertFalse(provider.get('supports_websockets', False))
                        aws = provider['aws']
                        if 'credential_export' in aws:
                            self.assertNotIn('profile', aws)
                        if 'auth_refresh' in aws:
                            self.assertEqual(aws['auth_refresh']['command'], 'aws')
                    if 'gateway_oauth' in provider:
                        oauth = provider['gateway_oauth']
                        self.assertGreater(oauth['redirect_port'], 0)
                        self.assertTrue(oauth['authorization_url'].startswith('https://'))
                        delivery = oauth['delivery']
                        self.assertNotIn(delivery['name'].lower(), {'authorization', 'cookie', 'host'})
                        for table in ['http_headers', 'env_http_headers']:
                            self.assertNotIn(delivery['name'].lower(), {k.lower() for k in provider.get(table, {})})

    def test_mcp_examples_keep_transports_and_timeouts_exclusive(self):
        for file in (ROOT/'examples/config').glob('mcp_servers*.toml'):
            for name, server in load(file)['mcp_servers'].items():
                with self.subTest(file=file.name, server=name):
                    self.assertIs(server['enabled'], False)
                    self.assertFalse('startup_timeout_ms' in server and 'startup_timeout_sec' in server)
                    self.assertNotEqual('command' in server, 'url' in server)
                    if 'command' in server:
                        self.assertFalse(set(server) & {'auth', 'url', 'oauth', 'oauth_resource',
                                         'bearer_token_env_var', 'http_headers_helper', 'http_headers', 'env_http_headers', 'scopes'})
                    else:
                        self.assertFalse(set(server) & {'args', 'cwd', 'env', 'env_vars'})
                        if 'http_headers_helper' in server:
                            self.assertTrue(server['url'].startswith('http://127.0.0.1:'))


if __name__ == '__main__':
    unittest.main()
