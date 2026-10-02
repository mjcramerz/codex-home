"""Schema, policy, profile and broker contracts; no host mutation or network."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('schema_check', ROOT/'home/.hooks/schema_check.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)
SCHEMA = json.loads((ROOT/'home/config.schema.json').read_text())
contract_spec = importlib.util.spec_from_file_location('config_contract', ROOT/'tests/config_contract.py')
contract = importlib.util.module_from_spec(contract_spec)
contract_spec.loader.exec_module(contract)


def load(path):
    return tomllib.loads((ROOT/path).read_text())


def merge(base, overlay, path=()):
    """Mirror the relevant ordinary/structured-feature source merge rules."""
    result = copy.deepcopy(base)
    if path == ('shell_environment_policy',):
        if 'filters' in overlay:
            result.pop('exclude', None)
            result.pop('include_only', None)
        elif 'exclude' in overlay or 'include_only' in overlay:
            result.pop('filters', None)
    for key, value in overlay.items():
        current = result.get(key)
        structured = path == ('features',) and key in {'code_mode', 'multi_agent_v2', 'network_proxy', 'sleep_tool'}
        if structured and isinstance(current, dict) and isinstance(value, bool):
            current['enabled'] = value
        elif structured and isinstance(current, bool) and isinstance(value, dict):
            result[key] = merge({'enabled': current}, value, (*path, key))
        elif isinstance(value, dict) and isinstance(current, dict):
            result[key] = merge(current, value, (*path, key))
        else:
            result[key] = copy.deepcopy(value)
    return result


class IntegrationTests(unittest.TestCase):
    def test_exact_schema_snapshot_and_all_runtime_layers(self):
        source = json.loads((ROOT/'tests/fixtures/source.json').read_text())
        self.assertEqual(hashlib.sha256((ROOT/'home/config.schema.json').read_bytes()).hexdigest(),
                         source['config_schema_sha256'])
        validator.check_schema(SCHEMA)
        paths = [ROOT/'etc/config.toml', ROOT/'home/config.toml',
                 *sorted((ROOT/'home').glob('*.config.toml')), *sorted((ROOT/'agents').glob('*.toml'))]
        for path in paths:
            with self.subTest(path=path.relative_to(ROOT)):
                validator.validate(SCHEMA, tomllib.loads(path.read_text()))
                self.assertNotRegex(path.read_text(), r'(?m)^#\s+(?:BEGIN|END)\b')
                self.assertNotIn('CONFIG-REFERENCE', path.read_text())

    def test_every_root_setting_has_an_active_or_explicit_optional_route(self):
        expected = contract.field_paths(SCHEMA)
        covered = set()
        paths = [ROOT/'etc/config.toml', ROOT/'home/config.toml',
                 *sorted((ROOT/'home').glob('*.config.toml')),
                 *sorted((ROOT/'agents').glob('*.toml')),
                 *sorted((ROOT/'examples/config').glob('*.toml'))]
        for path in paths:
            data = tomllib.loads(path.read_text())
            validator.validate(SCHEMA, data)
            covered |= contract.present_paths(SCHEMA, data)
        covered |= contract.present_paths(SCHEMA, {
            'hooks': json.loads((ROOT/'home/hooks.json').read_text())['hooks']})
        self.assertFalse(expected - covered, sorted(expected - covered))
        inventory = json.loads((ROOT/'examples/config-coverage.json').read_text())
        self.assertEqual(inventory['schema_path_count'], len(expected))
        self.assertEqual(inventory['root_key_count'], len(SCHEMA['properties']))
        self.assertEqual(set(inventory['paths']), {'.'.join(p) for p in expected})
        route_paths = {}
        for key, routes in inventory['paths'].items():
            self.assertTrue(routes, key)
            for route in routes:
                path = ROOT/route['file']
                if path not in route_paths:
                    data = json.loads(path.read_text()) if path.suffix == '.json' else tomllib.loads(path.read_text())
                    route_paths[path] = {'.'.join(p) for p in contract.present_paths(SCHEMA, data)}
                self.assertIn(key, route_paths[path], route)

    def test_canonical_features_are_active_or_explicitly_inactive(self):
        registry = json.loads((ROOT/'tests/fixtures/features.json').read_text())
        source = json.loads((ROOT/'tests/fixtures/source.json').read_text())
        self.assertEqual(len(registry), source['canonical_feature_count'])
        inactive = json.loads((ROOT/'examples/feature-lifecycle.json').read_text())
        active = load('home/config.toml')['features']
        for key, entry in registry.items():
            with self.subTest(key=key):
                if key in active:
                    self.assertNotIn(entry['stage'], {'Deprecated', 'Removed'})
                else:
                    self.assertIn(key, inactive)
                    self.assertEqual(inactive[key], entry)
                    if (key in SCHEMA['properties']['features']['properties'] and
                            entry['stage'] not in {'Deprecated', 'Removed'}):
                        self.assertIs(entry['default'], False)
        for path in [ROOT/'etc/config.toml', ROOT/'home/config.toml',
                     *(ROOT/'home').glob('*.config.toml'), *(ROOT/'agents').glob('*.toml')]:
            for key in tomllib.loads(path.read_text()).get('features', {}):
                with self.subTest(path=path.name, key=key):
                    if key == 'tool_registry':
                        continue  # Registry settings, not a feature toggle.
                    self.assertIn(key, registry)
                    self.assertNotIn(registry[key]['stage'], {'Deprecated', 'Removed'})

    def test_effective_profiles_and_agent_layers_validate(self):
        base = merge(load('etc/config.toml'), load('home/config.toml'))
        for path in [*(ROOT/'home').glob('*.config.toml'), *(ROOT/'agents').glob('*.toml')]:
            effective = merge(base, tomllib.loads(path.read_text()))
            with self.subTest(profile=path.name):
                validator.validate(SCHEMA, effective)
                self.assertNotIn('sandbox_mode', effective)
                self.assertNotIn('sandbox_workspace_write', effective)
                self.assertTrue(effective['default_permissions'].startswith(':') or
                                effective['default_permissions'] in effective['permissions'])
                self.assertNotIn('model_context_window', effective)
                self.assertNotIn('model_auto_compact_token_limit', effective)
                self.assertEqual(effective['model_catalog_json'],
                                 '/data/codex/usr/home/models_catalog.json')

    def test_models_and_reasoning_levels_exist_in_supplied_catalog(self):
        models = json.loads((ROOT/'tests/fixtures/models.json').read_text())
        base = merge(load('etc/config.toml'), load('home/config.toml'))
        for path in [ROOT/'home/config.toml', *(ROOT/'home').glob('*.config.toml'), *(ROOT/'agents').glob('*.toml')]:
            effective = merge(base, tomllib.loads(path.read_text()))
            with self.subTest(path=path.name):
                self.assertIn(effective['model'], models)
                self.assertIn(effective['model_reasoning_effort'], models[effective['model']]['reasoning_efforts'])
                self.assertIn(effective['review_model'], models)
        for key in ['extract_model', 'consolidation_model']:
            self.assertIn(base['memories'][key], models)

    def test_deployment_instruction_paths_and_agent_layers_exist(self):
        layers = [ROOT/'home/config.toml', *(ROOT/'home').glob('*.config.toml')]
        for path in layers:
            for key in ['model_instructions_file', 'experimental_compact_prompt_file']:
                name = tomllib.loads(path.read_text()).get(key)
                if name is not None:
                    relative = name.removeprefix('/data/codex/usr/')
                    self.assertNotEqual(relative, name)
                    self.assertTrue((ROOT/relative).is_file(), name)
        roles = load('home/config.toml')['agents']
        for role in roles.values():
            if isinstance(role, dict) and 'config_file' in role:
                self.assertTrue((ROOT/role['config_file'].removeprefix('/data/codex/usr/')).is_file())

    def test_default_and_online_network_semantics(self):
        base = merge(load('etc/config.toml'), load('home/config.toml'))
        self.assertEqual(base['default_permissions'], 'workspace')
        self.assertFalse(base['permissions']['workspace']['network']['enabled'])
        self.assertFalse(base['permissions']['readonly']['network']['enabled'])
        self.assertFalse(base['features']['network_proxy']['enabled'])
        online = merge(base, load('home/online.config.toml'))
        network = online['permissions'][online['default_permissions']]['network']
        self.assertTrue(network['enabled'])
        self.assertTrue(online['features']['network_proxy']['enabled'])
        self.assertNotIn('*', network['domains'])
        self.assertTrue(all('*' not in host for host in network['domains']))
        self.assertEqual(network['domains']['auth.openai.com'], 'allow')
        self.assertEqual(network['domains']['169.254.169.254'], 'deny')
        self.assertFalse(network['allow_local_binding'])
        self.assertFalse(network['dangerously_allow_all_unix_sockets'])
        full = merge(base, load('home/full-access.config.toml'))
        self.assertEqual(full['default_permissions'], 'full')
        self.assertTrue(full['permissions']['full']['network']['enabled'])
        self.assertFalse(full['features']['network_proxy']['enabled'])

    def test_workspace_does_not_grant_runtime_or_credentials_writes(self):
        fs = load('home/config.toml')['permissions']['workspace']['filesystem']
        self.assertEqual(fs[':project_roots'], {'.': 'write'})
        self.assertNotIn(':root', fs)
        self.assertNotIn('/data/codex/usr/home', fs)
        for path, value in fs.items():
            if path.startswith('/'):
                self.assertIn(value, {'read', 'deny'})
        for private in ['auth.json', '.credentials.json']:
            self.assertEqual(fs['/data/codex/usr/home/'+private], 'deny')
        self.assertEqual(fs['/etc/codex/mcp/credentials'], 'deny')
        self.assertEqual(fs['/data/codex/usr/home/INDEX.md'], 'read')
        self.assertEqual(fs['/data/codex/usr/home/skills'], 'read')
        self.assertEqual(fs['/data/codex/usr/home/plugins'], 'read')

    def test_system_permissions_and_requirements_have_separate_contracts(self):
        requirements = load('etc/requirements.toml')
        fields = json.loads((ROOT/'tests/fixtures/requirements-fields.json').read_text())
        self.assertFalse(set(requirements) - set(fields))
        coverage = json.loads((ROOT/'examples/requirements/coverage.json').read_text())['fields']
        self.assertEqual(set(coverage), set(fields))
        for field in fields:
            expected = 'active' if field in requirements else 'inherit_native_default'
            self.assertEqual(coverage[field]['status'], expected, field)
        self.assertEqual(requirements, {})
        home = load('home/config.toml')
        system = load('etc/config.toml')
        self.assertEqual(set(system), {'default_permissions', 'permissions'})
        self.assertEqual(system['default_permissions'], home['default_permissions'])
        expected_home_permissions = copy.deepcopy(system['permissions'])
        for profile in expected_home_permissions.values():
            profile['network'] = {key: value for key, value in profile['network'].items()
                                  if not isinstance(value, dict)}
        self.assertEqual(home['permissions'], expected_home_permissions)
        expected_effective = copy.deepcopy(home)
        expected_effective['permissions'] = system['permissions']
        self.assertEqual(merge(system, home), expected_effective)

    def test_optional_mcp_allowlist_matches_exact_ids_commands_and_arguments(self):
        policy = load('examples/requirements/mcp-only.toml')['mcp_servers']
        servers = load('home/config.toml')['mcp_servers']
        local_ids = {key for key, server in servers.items()
                     if server.get('command') == '/usr/local/bin/codex-mcp'}
        self.assertEqual(set(policy), local_ids)
        for key, requirement in policy.items():
            identity = requirement['identity']['command']
            self.assertEqual(identity['executable'], servers[key]['command'])
            self.assertEqual([x['value'] for x in identity['args']], servers[key]['args'])
            self.assertTrue(all(x['match'] == 'exact' for x in identity['args']))

    def test_hook_registration_contract_and_no_duplicate_inline_handlers(self):
        hooks = json.loads((ROOT/'home/hooks.json').read_text())['hooks']
        expected = set(SCHEMA['definitions']['HooksToml']['properties']) - {'state'}
        self.assertEqual(set(hooks), expected)
        validator.validate(SCHEMA, {'hooks': hooks})
        session_schema = json.loads((ROOT/'home/.hooks/schemas/session-start.command.input.schema.json').read_text())
        for source in session_schema['properties']['source']['enum']:
            self.assertTrue(re.fullmatch(hooks['SessionStart'][0]['matcher'], source))
        for path in ['etc/config.toml', 'home/config.toml']:
            self.assertNotIn('hooks', load(path))
        for event, groups in hooks.items():
            self.assertEqual(len(groups), 1)
            self.assertEqual(len(groups[0]['hooks']), 1)
            handler = groups[0]['hooks'][0]
            self.assertNotIn('async', handler)
            self.assertIn('/usr/bin/python3 -I', handler['command'])
            self.assertIn('--event '+event, handler['command'])
            if event in {'Interrupt', 'SessionEnd'}:
                self.assertLessEqual(handler['timeout'], 3)

    def test_optional_native_integrations_are_disabled_until_provisioned(self):
        user = load('home/config.toml')
        self.assertFalse(user['mcp_servers']['node_repl']['enabled'])
        self.assertNotIn('cua_repl', user['mcp_servers'])
        self.assertFalse(user['mcp_servers']['postgres']['enabled'])

    def test_unleash_removes_inherited_policy_gates(self):
        base = merge(load('etc/config.toml'), load('home/config.toml'))
        effective = merge(base, load('home/unleash.config.toml'))
        validator.validate(SCHEMA, effective)
        self.assertEqual(effective['default_permissions'], ':danger-full-access')
        self.assertEqual(effective['approval_policy'], 'never')
        self.assertTrue(effective['allow_login_shell'])
        env = effective['shell_environment_policy']
        self.assertNotIn('filters', env)
        self.assertEqual(env['inherit'], 'all')
        self.assertTrue(env['ignore_default_excludes'])
        self.assertEqual(env['exclude'], [])
        self.assertEqual(env['include_only'], [])
        self.assertFalse(effective['features']['hooks'])
        self.assertFalse(effective['features']['network_proxy']['enabled'])
        for server in effective['mcp_servers'].values():
            self.assertEqual(server['default_tools_approval_mode'], 'approve')
        self.assertEqual(effective['apps']['_default']['default_tools_approval_mode'], 'approve')
        self.assertTrue(all(v == 'allow' for v in effective['browser_use']['default_origin_policy'].values()))
        self.assertEqual(effective['computer_use']['default_app_access'], 'allow')
        for path in (ROOT/'agents').glob('*.toml'):
            child = merge(effective, tomllib.loads(path.read_text()))
            with self.subTest(role=path.name):
                validator.validate(SCHEMA, child)
                self.assertEqual(child['default_permissions'], ':danger-full-access')
                self.assertEqual(child['approval_policy'], 'never')
                for gate in ['hooks', 'guardian_approval', 'exec_permission_approvals',
                             'write_stdin_approval', 'request_permissions_tool']:
                    self.assertFalse(child['features'][gate])

    def test_custom_provider_preserves_openai_chatgpt_routing(self):
        home = load('home/config.toml')
        self.assertEqual(home['model_provider'], 'openai-custom')
        provider = home['model_providers'][home['model_provider']]
        self.assertEqual(provider['name'], 'OpenAI')
        self.assertEqual(provider['base_url'], 'https://chatgpt.com/backend-api/codex')
        self.assertTrue(provider['requires_openai_auth'])
        self.assertTrue(provider['supports_websockets'])
        self.assertEqual(provider['wire_api'], 'responses')
        self.assertFalse({'auth', 'aws', 'env_key', 'experimental_bearer_token',
                          'gateway_oauth'} & provider.keys())
        for path in [*(ROOT/'home').glob('*.config.toml'), *(ROOT/'agents').glob('*.toml')]:
            self.assertEqual(tomllib.loads(path.read_text())['model_provider'], 'openai-custom')

    def test_environment_exclusions_use_native_wildcard_syntax(self):
        import fnmatch
        filters = load('home/config.toml')['shell_environment_policy']['filters']
        for name in ['OPENAI_API_KEY', 'GITHUB_TOKEN', 'AWS_SESSION_TOKEN',
                     'DATABASE_PASSWORD', 'LD_PRELOAD', 'BASH_ENV', 'PERL5OPT']:
            self.assertTrue(any(action == 'exclude' and fnmatch.fnmatchcase(name.lower(), pattern.lower())
                                for pattern, action in filters.items()), name)

    def test_schema_rejects_actual_config_failures(self):
        for value in [
            {'approval_policy': 'untrusted'},
            {'allow_symlinked_codex_home': 'false'},
            {'features': {'code_mode': {'default_exec_yield_time_ms': -1}}},
            {'features': {'artifact': {'enabled': False}}},
            {'features': {'model_catalog_in_context': 'false'}},
            {'features': {'guardianv2': {'review_threshold': 2}}},
            {'features': {'tool_registry': {'turn_metadata_includes_tool_info': 'true'}}},
            {'skills': {'max_context_tokens': 0}},
            {'shell_environment_policy': {'filters': {}, 'exclude': []}},
            {'tui': {'keymap': {'editor': {'invented_action': 'ctrl-x'}}}},
        ]:
            with self.subTest(value=value), self.assertRaises(validator.SchemaError):
                validator.validate(SCHEMA, value)


if __name__ == '__main__':
    unittest.main()
