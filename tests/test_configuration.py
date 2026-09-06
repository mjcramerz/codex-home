"""Regression tests for restoring and retaining the user's custom configuration."""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import build_home
import install_assets
import validate

SCHEMA = json.loads((ROOT / 'generate/schemas/config.schema.json').read_text())
POLICY = json.loads((ROOT / 'generate/feature-policy.json').read_text())
HOME = tomllib.loads((ROOT / 'home/config.toml').read_text())
ORIGINAL = tomllib.loads((ROOT / 'migration/original-home-config.toml').read_text())


class ConfigurationTests(unittest.TestCase):
    def test_all_config_layers_and_assets(self):
        report = validate.validate(ROOT, write=False)
        self.assertEqual(report['active_configuration_files'], 26)
        self.assertEqual(report['original_files_present'], 6802)
        self.assertEqual(report['original_instruction_files_unchanged'], 491)

    def test_exact_supplied_schema_pin(self):
        self.assertEqual(hashlib.sha256((ROOT / 'home/config.schema.json').read_bytes()).hexdigest(),
                         '30c625df04c94d5e71129945a930ef092827f03c85e14848399346fa328577af')

    def test_unknown_root_rejected(self):
        with self.assertRaises(ValueError):
            validate.validate_data({'unsupported_custom_guess': True}, SCHEMA, POLICY, 'test')

    def test_unknown_feature_rejected(self):
        with self.assertRaises(ValueError):
            validate.validate_data({'features': {'child_agents_md': True}}, SCHEMA, POLICY, 'test')

    def test_schema_accepted_removed_flag_still_rejected(self):
        for name in POLICY['removed']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate.validate_data({'features': {name: True}}, SCHEMA, POLICY, 'test')

    def test_schema_accepted_deprecated_flag_rejected(self):
        for name in POLICY['deprecated']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                validate.validate_data({'features': {name: False}}, SCHEMA, POLICY, 'test')

    def test_active_custom_features_and_original_values(self):
        expected = set(SCHEMA['properties']['features']['properties']) - set(POLICY['removed']) - set(POLICY['deprecated']) - set(POLICY['aliases'])
        self.assertEqual(len(expected), 81)
        self.assertEqual(set(HOME['features']), expected)
        for key in expected:
            old = copy.deepcopy(ORIGINAL['features'][key])
            if isinstance(old, dict):
                old.pop('usage_hint_enabled', None)
            self.assertEqual(HOME['features'][key], old, key)

    def test_not_deprecated_in_requested_base_version(self):
        validate.validate_data({'features': {'unified_exec_zsh_fork': True, 'code_mode_buffered_exec': True}}, SCHEMA, POLICY, 'test')

    def test_custom_instruction_and_catalog_bindings_preserved(self):
        for key in ('instruction_overrides', 'model_instructions_file', 'model_catalog_json', 'experimental_compact_prompt_file'):
            self.assertEqual(HOME[key], ORIGINAL[key])

    def test_model_selection_and_full_permissions_preserved(self):
        for key in ('model', 'review_model', 'model_provider', 'model_providers', 'approval_policy', 'default_permissions'):
            self.assertEqual(HOME[key], ORIGINAL[key])

    def test_no_original_root_setting_lost(self):
        self.assertFalse(set(ORIGINAL) - set(HOME))

    def test_full_system_mirror_not_reduced_subset(self):
        self.assertEqual((ROOT / 'home/config.toml').read_bytes(), (ROOT / 'etc/config.toml').read_bytes())

    def test_invalid_open_permission_map_internals_rejected(self):
        import jsonschema
        with self.assertRaises(jsonschema.ValidationError):
            validate.validate_data({'permissions': {'full': {'network': {'unknown': True}}}}, SCHEMA, POLICY, 'test')

    def test_permission_selectors_cannot_compete(self):
        with self.assertRaises(ValueError):
            validate.validate_data({'default_permissions': 'full', 'sandbox_mode': 'workspace-write'}, SCHEMA, POLICY, 'test')

    def test_shell_filter_shapes_cannot_compete(self):
        with self.assertRaises(ValueError):
            validate.validate_data({'shell_environment_policy': {'filters': {}, 'exclude': []}}, SCHEMA, POLICY, 'test')

    def test_all_original_mcp_registrations_retained(self):
        self.assertEqual(set(HOME['mcp_servers']), set(ORIGINAL['mcp_servers']))
        self.assertEqual(len(HOME['mcp_servers']), 30)

    def test_node_repl_remains_distinct_from_removed_feature(self):
        self.assertTrue(HOME['mcp_servers']['node_repl']['enabled'])
        self.assertNotIn('js_repl', HOME['features'])
        self.assertEqual(HOME['mcp_servers']['node_repl']['env'], ORIGINAL['mcp_servers']['node_repl']['env'])

    def test_sequential_thinking_identity_and_broker_name(self):
        self.assertEqual(HOME['mcp_servers']['sequential_thinking']['args'], ['connect', 'sequential-thinking'])

    def test_developer_instruction_text_not_replaced(self):
        self.assertEqual(HOME['developer_instructions'], ORIGINAL['developer_instructions'])

    def test_no_original_hook_handler_removed(self):
        hooks = json.loads((ROOT/'home/hooks.json').read_text())['hooks']
        self.assertEqual(len(hooks), 11)
        self.assertEqual(sum(len(g['hooks']) for groups in hooks.values() for g in groups), 97)

    def test_desktop_settings_retained_recursively(self):
        new = b'model = "reviewed"\n[desktop]\n[desktop.ui]\nzoom = 2\n'
        old = b'model = "obsolete"\n[desktop]\nopaque = "keep"\n[desktop.ui]\nzoom = 1\ntheme = "dark"\n'
        merged = tomllib.loads(install_assets.merge_desktop(new, old).decode())
        self.assertEqual(merged['model'], 'reviewed')
        self.assertEqual(merged['desktop'], {'opaque': 'keep', 'ui': {'zoom': 2, 'theme': 'dark'}})

    def test_no_existing_desktop_does_not_reformat(self):
        source = b'# keep formatting\nmodel = "custom"\n'
        self.assertEqual(install_assets.merge_desktop(source, b'model="old"\n'), source)

    def test_bad_existing_desktop_fails_closed(self):
        with self.assertRaises(ValueError):
            install_assets.merge_desktop(b'model="custom"\n', b'desktop="bad"\n')

    def test_generator_idempotent_and_does_not_rewrite_authoritative_files(self):
        before = {p: p.read_bytes() for p in validate.active_files(ROOT)}
        self.assertEqual(build_home.generate(), 0)
        self.assertEqual(build_home.generate(), 0)
        self.assertTrue(all(p.read_bytes() == data for p, data in before.items()))

    def test_atomic_write_refuses_symlink(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            target = root/'target'; target.write_bytes(b'keep')
            link = root/'link'; link.symlink_to(target)
            with self.assertRaises(ValueError):
                build_home.atomic(link, b'delete')
            with self.assertRaises(ValueError):
                install_assets.atomic(link, b'delete', 0o644)
            self.assertEqual(target.read_bytes(), b'keep')

    def test_bad_schema_pin_cannot_mutate_derived_files(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root/'home').mkdir(); (root/'generate/schemas').mkdir(parents=True)
            (root/'home/config.toml').write_text('model="custom"\n')
            (root/'generate/schemas/config.schema.json').write_text(json.dumps(SCHEMA))
            (root/'generate/feature-policy.json').write_text('{"schema_sha256":"wrong"}')
            with patch.object(build_home, 'ROOT', root), self.assertRaises(ValueError):
                build_home.generate()
            self.assertFalse((root/'etc').exists())


if __name__ == '__main__':
    unittest.main()
