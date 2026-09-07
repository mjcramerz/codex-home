"""Real TOML conversion, source-only output and metadata separation regressions."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import tomllib
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'scripts'))
sys.path.insert(0, str(ROOT/'generate/scripts'))
import config_toml
import config_toml_coverage as coverage

SCHEMA = json.loads((ROOT/'generate/schemas/config.schema.json').read_text())


class TomlRenderingTests(unittest.TestCase):
    def test_scalar_types_round_trip_without_stringifying_bools(self):
        values = {'yes': True, 'no': False, 'number': 123, 'fraction': 0.125, 'text': 'normal', 'empty': []}
        self.assertEqual(tomllib.loads(config_toml.dumps(values)), values)

    def test_maps_and_arrays_use_explicit_table_headers(self):
        values = {'features': {'nested': {'enabled': True}}, 'skills': {'config': [{'path': '/one', 'enabled': True}, {'path': '/two', 'enabled': False}]}}
        text = config_toml.dumps(values)
        self.assertIn('[features.nested]', text)
        self.assertEqual(text.count('[[skills.config]]'), 2)
        self.assertNotIn('path = {', text)
        self.assertEqual(tomllib.loads(text), values)

    def test_multiple_nested_arrays_do_not_change_table_scope(self):
        values = {'hooks': {'Stop': [
            {'matcher': 'one', 'hooks': [{'type': 'command', 'command': 'echo one'}]},
            {'matcher': 'two', 'hooks': [{'type': 'command', 'command': 'echo two'}]},
        ]}, 'desktop': {'ui': {'zoom': 2}}}
        self.assertEqual(tomllib.loads(config_toml.dumps(values)), values)

    def test_quoted_dotted_and_path_keys_are_not_split(self):
        values = {'plugins': {'name@source': {'enabled': True}}, 'projects': {'/home/a.b/project': {'trust_level': 'trusted'}}, 'tui': {'key with spaces': 'value'}}
        text = config_toml.dumps(values)
        self.assertIn('[projects."/home/a.b/project"]', text)
        self.assertEqual(tomllib.loads(text), values)

    def test_multiline_prompts_escaped_quotes_unicode_and_newlines(self):
        cases = ['', '\n', '\nstart\n', 'a\r\nb', 'quote: """ and literal \\\\n\nend', 'tab\tbackspace\b', '\u00e9 \U0001f4a1', 'last line\n']
        for value in cases:
            with self.subTest(value=repr(value)):
                self.assertEqual(tomllib.loads(config_toml.dumps({'instructions': value}))['instructions'], value)

    def test_mixed_array_and_empty_tables_round_trip(self):
        values = {'values': ['a', 3, {'x': 1}], 'desktop': {}, 'otel': {'span_attributes': {}}}
        text = config_toml.dumps(values)
        self.assertIn('[desktop]', text)
        self.assertEqual(tomllib.loads(text), values)

    def test_null_and_nonfinite_values_are_not_fake_toml(self):
        for value in (None, float('nan'), float('inf')):
            with self.subTest(value=value), self.assertRaises((TypeError, ValueError)):
                config_toml.dumps({'value': value})

    def test_schema_keywords_are_not_root_configuration(self):
        for name in ('$schema', '$ref', 'definitions', 'properties', 'anyOf'):
            with self.subTest(name=name), self.assertRaises(ValueError):
                config_toml.clean_loads(json.dumps(name) + ' = "bad"\n')

    def test_real_nested_type_and_description_keys_are_allowed(self):
        text = '[experimental_thread_store]\ntype="local"\n[agents.worker]\ndescription="worker"\n'
        self.assertEqual(config_toml.clean_loads(text)['experimental_thread_store']['type'], 'local')

    def test_schema_comment_markers_are_rejected(self):
        for comment in ('# schema-entry: #/properties/model', '# schema-definition: Sample', '# BEGIN GENERATED SUPPORTED-KEY REFERENCE', '#:schema config.schema.json'):
            with self.subTest(comment=comment), self.assertRaises(ValueError):
                config_toml.clean_loads('model="custom"\n' + comment + '\n')

    def test_schema_like_text_inside_strings_is_not_a_comment(self):
        text = 'developer_instructions = """\n# schema-entry: this is quoted prompt text\n"""\nmodel="custom"\n'
        self.assertIn('schema-entry:', config_toml.clean_loads(text)['developer_instructions'])
        with self.assertRaises(ValueError):
            config_toml.clean_loads(text + '# schema-entry: this IS a comment\n')

    def test_closing_multiline_quotes_do_not_hide_later_comments(self):
        text = 'model = """a""""\n# schema-entry: must reject\n'
        tomllib.loads(text)
        with self.assertRaises(ValueError):
            config_toml.clean_loads(text)


class ExampleSeparationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.outputs = coverage.rendered_examples(SCHEMA)
        cls.report = json.loads(cls.outputs[coverage.COVERAGE_PATH])

    def test_all_nonretired_root_properties_have_real_toml_assignments(self):
        converted = set()
        for path, text in self.outputs.items():
            if path.suffix == '.toml':
                data = config_toml.clean_loads(text, str(path))
                if path != coverage.AGENT_ROLE_EXAMPLE_PATH:
                    converted.update(data)
        self.assertEqual(converted, set(SCHEMA['properties']) - set(coverage.DEPRECATED_ROOT_ALIASES))
        self.assertEqual(len(converted), 92)

    def test_schema_bookkeeping_is_separate_json(self):
        self.assertEqual(self.report['counts'], {'root_properties': 94, 'converted_root_properties': 92, 'definitions': 161, 'entries': 1072, 'union_variants': 83})
        for path, text in self.outputs.items():
            if path.suffix == '.toml':
                self.assertNotIn('# schema-entry:', text)
                self.assertNotIn('#/definitions/', text)
                self.assertNotIn('schema-definition', text)
        self.assertTrue(coverage.COVERAGE_PATH.is_relative_to(ROOT/'generate/reports'))

    def test_mutually_exclusive_settings_are_separate_toml_documents(self):
        for path, text in self.outputs.items():
            if path.suffix != '.toml':
                continue
            data = tomllib.loads(text)
            self.assertFalse('sandbox_mode' in data and 'default_permissions' in data, path)
            self.assertFalse('compact_prompt' in data and 'experimental_compact_prompt_file' in data, path)

    def test_typed_feature_forms_expand_as_tables(self):
        text = self.outputs[coverage.HOME_EXAMPLE_PATH]
        self.assertIn('[features.guardianv2.transcript]', text)
        self.assertIn('[features.current_time_reminder]', text)
        data = tomllib.loads(text)
        forbidden = coverage.OBSOLETE_FEATURE_KEYS
        self.assertFalse(set(data['features']) & forbidden)

    def test_companion_is_a_config_layer_not_an_agent_registration(self):
        from jsonschema import Draft7Validator
        role = tomllib.loads(self.outputs[coverage.AGENT_ROLE_EXAMPLE_PATH])
        Draft7Validator(SCHEMA).validate(role)
        self.assertIn('developer_instructions', role)
        self.assertNotIn('nickname_candidates', role)
        self.assertNotIn('description', role)

    def test_examples_never_target_installable_directories(self):
        for path in self.outputs:
            coverage.ensure_example_path(path)
        for target in ('home/config.toml', 'etc/config.toml', 'agents/default.toml', 'generate/scripts/modified.py'):
            with self.subTest(target=target), self.assertRaises(coverage.GenerationError):
                coverage.ensure_example_path(ROOT/target)

    def test_checked_in_outputs_are_current_and_writes_are_idempotent(self):
        runtime = [*ROOT.joinpath('home').glob('*.toml'), *ROOT.joinpath('agents').glob('*.toml'), ROOT/'etc/config.toml']
        before = {path: path.read_bytes() for path in runtime}
        for path, text in self.outputs.items():
            self.assertEqual(path.read_text(), text, path)
            self.assertFalse(coverage.write_if_changed(path, text))
        self.assertTrue(all(path.read_bytes() == payload for path, payload in before.items()))

    def test_output_symlink_cannot_redirect_to_runtime(self):
        with tempfile.TemporaryDirectory() as name:
            root = Path(name)
            (root/'examples').mkdir()
            destination = root/'runtime.toml'
            destination.write_text('model="keep"\n')
            link = root/'examples/link.toml'
            link.symlink_to(destination)
            with patch.object(coverage, 'GENERATION_ROOT', root), patch.object(coverage, 'EXAMPLES_DIRECTORY', root/'examples'), patch.object(coverage, 'REPORTS_DIRECTORY', root/'reports'):
                with self.assertRaises(coverage.GenerationError):
                    coverage.write_if_changed(link, 'model="bad"\n')
            self.assertEqual(destination.read_text(), 'model="keep"\n')


if __name__ == '__main__':
    unittest.main()
