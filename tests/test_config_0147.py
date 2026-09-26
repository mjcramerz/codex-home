"""Offline compatibility regressions for the rust-v0.147.0 configuration.

Key names were checked against openai/codex at rust-v0.147.0, core/config.schema.json.
Cross-context checks follow tui/src/keymap.rs at the same tag. These checks do
not emulate the application or claim to validate authentication/network access.
"""
from pathlib import Path
import tomllib
import unittest

ROOT = Path(__file__).resolve().parents[1]
ROOT_KEYS = set('agents allow_login_shell analytics approval_policy approvals_reviewer apps apps_mcp_product_sku audio auto_review background_terminal_max_timeout chatgpt_base_url check_for_update_on_startup cli_auth_credentials_store compact_prompt debug default_permissions desktop developer_instructions disable_paste_burst experimental_compact_prompt_file experimental_realtime_start_instructions experimental_realtime_webrtc_call_base_url experimental_realtime_ws_backend_prompt experimental_realtime_ws_base_url experimental_realtime_ws_model experimental_realtime_ws_startup_context experimental_thread_config_endpoint experimental_thread_store experimental_use_unified_exec_tool features feedback file_opener forced_chatgpt_workspace_id forced_login_method ghost_snapshot hide_agent_reasoning history hooks include_apps_instructions include_collaboration_mode_instructions include_environment_context include_permissions_instructions instructions log_dir marketplaces mcp_oauth_callback_port mcp_oauth_callback_url mcp_oauth_credentials_store mcp_servers memories model model_auto_compact_token_limit model_auto_compact_token_limit_scope model_catalog_json model_context_window model_instructions_file model_provider model_providers model_reasoning_effort model_reasoning_summary model_verbosity notice notify openai_base_url orchestrator oss_provider otel permissions personality plan_mode_reasoning_effort plugins profile profiles project_doc_fallback_filenames project_doc_max_bytes project_root_markers projects realtime review_model sandbox_mode sandbox_workspace_write service_tier shell_environment_policy show_raw_agent_reasoning skills sqlite_home suppress_unstable_features_warning tool_output_token_limit tool_suggest tools tui web_search windows'.split())
FEATURES = set('apply_patch_freeform apply_patch_streaming_events apps apps_mcp_path_override auth_elicitation browser_use browser_use_external browser_use_full_cdp_access chronicle code_mode code_mode_buffered_exec code_mode_host code_mode_only codex_git_commit codex_hooks collab collaboration_modes computer_use concurrent_reasoning_summaries connectors current_time_reminder default_mode_request_user_input deferred_executor deferred_tool_world_state elevated_windows_sandbox enable_experimental_windows_sandbox enable_fanout enable_mcp_apps enable_request_compression exec_permission_approvals executed_tool_call_metadata executor_capability_discovery experimental_use_unified_exec_tool experimental_windows_sandbox external_agent_memory_import external_migration fast_mode goals guardian_approval guardianv2 hooks image_detail_original image_generation image_resize_notice imagegenext in_app_browser in_app_updates item_ids js_repl js_repl_tools_only local_thread_store_compression mcp_2026_07_28 memories memory_tool mentions_v2 multi_agent multi_agent_mode multi_agent_v2 network_proxy non_prefixed_mcp_tool_names personality plugin_hooks plugin_sharing plugins prevent_idle_sleep realtime_conversation recommended_plugins remote_compaction_v2 remote_control remote_models remote_plugin request_permissions request_permissions_tool request_rule resize_all_images respect_system_proxy responses_websockets responses_websockets_v2 rollout_budget runtime_metrics search_tool secret_auth_storage shell_snapshot shell_tool shell_zsh_fork skill_env_var_dependency_prompt skill_mcp_dependency_install skill_search sqlite standalone_web_search steer telepathy terminal_resize_reflow terminal_visualization_instructions token_budget tool_call_mcp_elicitation tool_registry tool_search tool_search_always_defer_mcp_tools tool_suggest tui_app_server unavailable_dummy_tools undo unified_exec unified_exec_zsh_fork use_agent_identity use_legacy_landlock use_linux_sandbox_bwrap view_image web_search web_search_cached web_search_request workspace_dependencies workspace_owner_usage_nudge'.split())
TUI_KEYS = set('alternate_screen animations keymap model_availability_nux notification_condition notification_method notifications pet pet_anchor raw_output_mode resume_cwd session_picker_view show_tooltips status_line status_line_use_colors terminal_resize_reflow_max_rows terminal_title theme vim_mode_default'.split())
VIM_NORMAL = set('enter_insert append_after_cursor append_line_end insert_line_start open_line_below open_line_above move_left move_right move_up move_down move_word_forward move_word_backward move_word_end move_line_start move_line_end delete_char substitute_char delete_to_line_end change_to_line_end yank_line paste_after start_delete_operator start_yank_operator start_change_operator cancel_operator'.split())
VIM_OPERATOR = set('delete_line yank_line motion_left motion_right motion_up motion_down motion_word_forward motion_word_backward motion_word_end motion_line_start motion_line_end select_inner_text_object select_around_text_object cancel'.split())


def configs():
    paths = [ROOT/'home/config.toml', ROOT/'etc/config.toml']
    paths += sorted((ROOT/'home').glob('*.config.toml'))
    paths += sorted((ROOT/'agents').glob('*.toml'))
    return [(path, tomllib.loads(path.read_text())) for path in paths]


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
        for path, config in configs()[:2]:
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertIs(config['features']['use_agent_identity'], False)
                self.assertEqual(config['forced_login_method'], 'chatgpt')
                self.assertEqual(config['cli_auth_credentials_store'], 'file')

    def test_newer_structures_are_inactive(self):
        for path, config in configs():
            with self.subTest(path=str(path.relative_to(ROOT))):
                features = config.get('features', {})
                self.assertIsInstance(features.get('guardianv2', False), bool)
                if isinstance(features.get('code_mode'), dict):
                    self.assertNotIn('default_exec_yield_time_ms', features['code_mode'])
                if isinstance(features.get('tool_registry'), dict):
                    self.assertNotIn('turn_metadata_includes_tool_info', features['tool_registry'])
                self.assertNotIn('tool_result', config.get('otel', {}))
                self.assertNotIn('max_context_tokens', config.get('skills', {}))
                self.assertNotIn('Interrupt', config.get('hooks', {}))

    def test_auth_domain_is_explicitly_reachable_in_allowlisted_profiles(self):
        for path, config in configs()[:2]:
            for name, profile in config.get('permissions', {}).items():
                domains = profile.get('network', {}).get('domains')
                if domains is not None:
                    with self.subTest(config=str(path), profile=name):
                        self.assertEqual(domains.get('auth.openai.com'), 'allow')

    def test_keymap_contexts_are_unique_and_supported(self):
        for path, config in configs()[:2]:
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
        for _, config in configs()[:2]:
            for action, value in config['tui']['keymap']['pager'].items():
                with self.subTest(action=action):
                    self.assertFalse(bindings(value) & {'esc', 'left', 'right', 'enter'})

    def test_approval_overlay_combined_bindings_are_unique(self):
        for _, config in configs()[:2]:
            keymap = config['tui']['keymap']; seen = {}
            for context in ('list', 'approval'):
                for action, value in keymap[context].items():
                    for key in bindings(value):
                        self.assertNotIn(key, seen, (context, action, key, seen))
                        seen[key] = context+'.'+action

    def test_main_bindings_and_overlay_editor_shadowing(self):
        for _, config in configs()[:2]:
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
