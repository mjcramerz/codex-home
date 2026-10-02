"""Offline schema and keymap checks for the exact supplied Codex snapshot.

These checks do not emulate the client or claim live deployment/authentication.
"""
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCHEMA = __import__('json').loads((ROOT/'home/config.schema.json').read_text())
ROOT_KEYS = set(SCHEMA['properties'])
FEATURES = set(SCHEMA['properties']['features']['properties'])
TUI_KEYS = set(SCHEMA['definitions']['Tui']['properties'])
VIM_NORMAL = set('enter_insert append_after_cursor append_line_end insert_line_start open_line_below open_line_above move_left move_right move_up move_down move_word_forward move_word_backward move_word_end move_line_start move_line_end delete_char substitute_char delete_to_line_end change_to_line_end yank_line paste_after start_delete_operator start_yank_operator start_change_operator cancel_operator'.split())
VIM_OPERATOR = set('delete_line yank_line motion_left motion_right motion_up motion_down motion_word_forward motion_word_backward motion_word_end motion_line_start motion_line_end select_inner_text_object select_around_text_object cancel'.split())


def configs():
    paths = [ROOT/'home/config.toml', ROOT/'etc/config.toml']
    paths += sorted((ROOT/'home').glob('*.config.toml'))
    paths += sorted((ROOT/'agents').glob('*.toml'))
    return [(path, tomllib.loads(path.read_text())) for path in paths]


def user_configs():
    path = ROOT/'home/config.toml'
    return [(path, tomllib.loads(path.read_text()))]


def bindings(value):
    return {str(key) for key in (value if isinstance(value, list) else [value])}


class ConfigCompatibilityTests(unittest.TestCase):
    def test_all_runtime_config_roots_are_supported(self):
        for path, config in configs():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertFalse(set(config) - ROOT_KEYS)
                self.assertFalse(set(config.get('features', {})) - FEATURES)
                self.assertFalse(set(config.get('tui', {})) - TUI_KEYS)

    def test_windows_settings_are_inactive(self):
        for path, config in configs():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertNotIn('windows', config)
                self.assertNotIn('winui@codex-home', config.get('plugins', {}))
                self.assertFalse(any('windows' in key or 'powershell' in key
                                     for key in config.get('features', {})))
                self.assertNotIn('hide_world_writable_warning', config.get('notice', {}))

    def test_registration_opt_in_is_disabled_without_changing_login_storage(self):
        config = __import__('tomllib').loads((ROOT/'etc/config.toml').read_text())
        self.assertIs(config['features']['use_agent_identity'], False)
        self.assertEqual(config['forced_login_method'], 'chatgpt')
        self.assertEqual(config['cli_auth_credentials_store'], 'file')

    def test_new_structures_are_supported_and_privacy_bounded(self):
        config = tomllib.loads((ROOT/'etc/config.toml').read_text())
        self.assertFalse(config['features']['guardianv2']['enabled'])
        self.assertFalse(config['features']['guardianv2']['persist_scores'])
        self.assertEqual(config['features']['code_mode']['default_exec_yield_time_ms'], 1000)
        self.assertTrue(config['features']['tool_registry']['turn_metadata_includes_tool_info'])
        self.assertEqual(config['otel']['tool_result']['max_bytes'], 0)
        self.assertEqual(config['skills']['max_context_tokens'], 10000)

    def test_auth_domain_is_explicitly_reachable_in_allowlisted_profiles(self):
        for path, config in configs()[:2]:
            for name, profile in config.get('permissions', {}).items():
                domains = profile.get('network', {}).get('domains')
                if domains is not None:
                    with self.subTest(config=str(path), profile=name):
                        self.assertEqual(domains.get('auth.openai.com'), 'allow')

    def test_keymap_contexts_are_unique_and_supported(self):
        for path, config in user_configs():
            keymap = config['tui']['keymap']
            self.assertFalse(set(keymap['vim_normal']) - VIM_NORMAL)
            self.assertFalse(set(keymap['vim_operator']) - VIM_OPERATOR)
            for context, actions in keymap.items():
                seen = {}
                for action, value in actions.items():
                    for key in bindings(value):
                        with self.subTest(path=str(path), context=context, key=key):
                            self.assertNotIn(key, seen, (seen, action))
                        seen[key] = action

    def test_pager_does_not_take_transcript_reserved_keys(self):
        for _, config in user_configs():
            for action, value in config['tui']['keymap']['pager'].items():
                with self.subTest(action=action):
                    self.assertFalse(bindings(value) & {'esc', 'left', 'right', 'enter'})

    def test_approval_overlay_combined_bindings_are_unique(self):
        for _, config in user_configs():
            keymap = config['tui']['keymap']; seen = {}
            for context in ('list', 'approval'):
                for action, value in keymap[context].items():
                    for key in bindings(value):
                        self.assertNotIn(key, seen, (context, action, key, seen))
                        seen[key] = context+'.'+action

    def test_main_bindings_and_overlay_editor_shadowing(self):
        for _, config in user_configs():
            k = config['tui']['keymap']
            app = {a:bindings(v) for a,v in k['global'].items()
                   if a not in {'submit', 'queue', 'toggle_shortcuts'}}
            if 'ctrl-/' in app.get('toggle_side_conversation', set()):
                app['toggle_side_conversation'].add('ctrl-7')
            main = {**app, **{'chat.'+a:bindings(v) for a,v in k['chat'].items()},
                    **{'composer.'+a:bindings(v) for a,v in k['composer'].items()}}
            seen = {}
            for action, keys in main.items():
                for key in keys:
                    self.assertNotIn(key, seen, (action,key,seen))
                    seen[key] = action
                    reserved = {'ctrl-c','ctrl-d','ctrl-v','ctrl-alt-v','shift-tab',
                                'esc','alt-left','alt-right','/','!','@','$'}
                    if (action,key) != ('chat.interrupt_turn','esc'):
                        self.assertNotIn(key, reserved)
            for action, keys in app.items():
                for context in ('list','approval'):
                    for other, value in k[context].items():
                        overlap = keys & bindings(value)
                        if (action,context,other) == ('clear_terminal','list','move_right'):
                            overlap -= {'ctrl-l'}
                        self.assertFalse(overlap, (action,context,other,overlap))
            for action, keys in main.items():
                if action in {'chat.edit_queued_message','composer.queue',
                              'composer.toggle_shortcuts','composer.history_search_next'}:
                    continue
                for other, value in k['editor'].items():
                    overlap = keys & bindings(value)
                    if (action,other) == ('composer.submit','insert_newline'):
                        overlap -= {'enter'}
                    self.assertFalse(overlap, (action,other,overlap))


if __name__ == '__main__':
    unittest.main()
