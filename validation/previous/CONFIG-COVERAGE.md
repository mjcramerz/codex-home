# Exact-schema configuration coverage

The schema has 94 root keys and 126 feature keys. The full config preserves every original root setting. Mutually exclusive alternatives, product-owned values and compatibility-only fields are documented rather than invented or activated simultaneously. All original file-backed instruction overrides remain active.

## Root settings

| Key | Disposition |
| --- | --- |
| `agents` | Active, retained from original (with documented normalization where applicable). |
| `allow_login_shell` | Active, retained from original (with documented normalization where applicable). |
| `analytics` | Active, retained from original (with documented normalization where applicable). |
| `approval_policy` | Active, retained from original (with documented normalization where applicable). |
| `approvals_reviewer` | Active, retained from original (with documented normalization where applicable). |
| `apps` | Active, retained from original (with documented normalization where applicable). |
| `apps_mcp_product_sku` | Product-owned SKU; no invented subscription value. |
| `audio` | Active, retained from original (with documented normalization where applicable). |
| `auto_review` | Active, retained from original (with documented normalization where applicable). |
| `background_terminal_max_timeout` | Active, retained from original (with documented normalization where applicable). |
| `chatgpt_base_url` | Active, retained from original (with documented normalization where applicable). |
| `check_for_update_on_startup` | Active, retained from original (with documented normalization where applicable). |
| `cli_auth_credentials_store` | Active, retained from original (with documented normalization where applicable). |
| `compact_prompt` | File-backed experimental_compact_prompt_file is already configured; avoid competing text. |
| `default_permissions` | Active, retained from original (with documented normalization where applicable). |
| `desktop` | Active, retained from original (with documented normalization where applicable). |
| `developer_instructions` | Active, retained from original (with documented normalization where applicable). |
| `disable_paste_burst` | Active, retained from original (with documented normalization where applicable). |
| `experimental_compact_prompt_file` | Active, retained from original (with documented normalization where applicable). |
| `experimental_realtime_start_instructions` | Active, retained from original (with documented normalization where applicable). |
| `experimental_realtime_webrtc_call_base_url` | No user endpoint supplied; preserve the original default transport endpoint. |
| `experimental_realtime_ws_backend_prompt` | Active, retained from original (with documented normalization where applicable). |
| `experimental_realtime_ws_base_url` | No user endpoint supplied; preserve the original default transport endpoint. |
| `experimental_realtime_ws_model` | No alternate realtime model supplied; existing realtime settings and prompts retained. |
| `experimental_realtime_ws_startup_context` | Active, retained from original (with documented normalization where applicable). |
| `experimental_thread_store` | No alternate thread store requested; original persistence settings retained. |
| `experimental_use_unified_exec_tool` | Legacy root alias; use features.unified_exec. |
| `features` | Active, retained from original (with documented normalization where applicable). |
| `feedback` | Active, retained from original (with documented normalization where applicable). |
| `file_opener` | Active, retained from original (with documented normalization where applicable). |
| `forced_chatgpt_workspace_id` | Would restrict login to invented workspace IDs; intentionally unrestricted. |
| `forced_login_method` | Active, retained from original (with documented normalization where applicable). |
| `ghost_snapshot` | Schema calls this compatibility-only; fields are legacy no-ops. |
| `goals` | Active, retained from original (with documented normalization where applicable). |
| `hide_agent_reasoning` | Active, retained from original (with documented normalization where applicable). |
| `history` | Active, retained from original (with documented normalization where applicable). |
| `hooks` | 97 original handlers are in home/hooks.json; do not execute them twice via inline duplicates. |
| `include_apps_instructions` | Active, retained from original (with documented normalization where applicable). |
| `include_collaboration_mode_instructions` | Active, retained from original (with documented normalization where applicable). |
| `include_environment_context` | Active, retained from original (with documented normalization where applicable). |
| `include_permissions_instructions` | Active, retained from original (with documented normalization where applicable). |
| `instruction_overrides` | Active, retained from original (with documented normalization where applicable). |
| `instructions` | No inline system string in original; all configured model_instructions_file and instruction_overrides retained. Do not inject placeholder companion templates. |
| `log_dir` | Active, retained from original (with documented normalization where applicable). |
| `marketplaces` | Active, retained from original (with documented normalization where applicable). |
| `mcp_oauth_callback_port` | Active, retained from original (with documented normalization where applicable). |
| `mcp_oauth_callback_url` | Active, retained from original (with documented normalization where applicable). |
| `mcp_oauth_credentials_store` | Active, retained from original (with documented normalization where applicable). |
| `mcp_servers` | Active, retained from original (with documented normalization where applicable). |
| `memories` | Active, retained from original (with documented normalization where applicable). |
| `model` | Active, retained from original (with documented normalization where applicable). |
| `model_auto_compact_token_limit` | Active, retained from original (with documented normalization where applicable). |
| `model_auto_compact_token_limit_scope` | Active, retained from original (with documented normalization where applicable). |
| `model_catalog_json` | Active, retained from original (with documented normalization where applicable). |
| `model_context_window` | Active, retained from original (with documented normalization where applicable). |
| `model_instructions_file` | Active, retained from original (with documented normalization where applicable). |
| `model_provider` | Active, retained from original (with documented normalization where applicable). |
| `model_providers` | Active, retained from original (with documented normalization where applicable). |
| `model_reasoning_effort` | Active, retained from original (with documented normalization where applicable). |
| `model_reasoning_summary` | Active, retained from original (with documented normalization where applicable). |
| `model_verbosity` | Active, retained from original (with documented normalization where applicable). |
| `notice` | Active, retained from original (with documented normalization where applicable). |
| `notify` | Active, retained from original (with documented normalization where applicable). |
| `openai_base_url` | Active, retained from original (with documented normalization where applicable). |
| `orchestrator` | Active, retained from original (with documented normalization where applicable). |
| `oss_provider` | Original custom remote provider selected, not a fabricated local provider. |
| `otel` | Active, retained from original (with documented normalization where applicable). |
| `permissions` | Active, retained from original (with documented normalization where applicable). |
| `personality` | Active, retained from original (with documented normalization where applicable). |
| `plan_mode_reasoning_effort` | Active, retained from original (with documented normalization where applicable). |
| `plugins` | Active, retained from original (with documented normalization where applicable). |
| `profile` | Original config-file profiles retained; no invented default named-profile selection. |
| `profiles` | Original separate *.config.toml profiles retained; schema reference demonstrates named-profile alternative. |
| `project_doc_fallback_filenames` | Active, retained from original (with documented normalization where applicable). |
| `project_doc_max_bytes` | Active, retained from original (with documented normalization where applicable). |
| `project_root_markers` | Active, retained from original (with documented normalization where applicable). |
| `projects` | No hard-coded project trust grants; original full/workspace/readonly permission profiles retained. |
| `realtime` | Active, retained from original (with documented normalization where applicable). |
| `responses_api_metadata` | Product-owned per-request metadata; no fabricated values. |
| `review_model` | Active, retained from original (with documented normalization where applicable). |
| `sandbox_mode` | Alternative to the configured default_permissions profile; do not set competing selectors. |
| `sandbox_workspace_write` | Legacy-style alternative for sandbox_mode; use existing named workspace permission profile. |
| `service_tier` | Active, retained from original (with documented normalization where applicable). |
| `shell_environment_policy` | Active, retained from original (with documented normalization where applicable). |
| `show_raw_agent_reasoning` | Active, retained from original (with documented normalization where applicable). |
| `skills` | Active, retained from original (with documented normalization where applicable). |
| `sqlite_home` | Active, retained from original (with documented normalization where applicable). |
| `suppress_unstable_features_warning` | Active, retained from original (with documented normalization where applicable). |
| `tool_output_token_limit` | Active, retained from original (with documented normalization where applicable). |
| `tool_suggest` | Feature toggle retained; no fabricated additional connector/plugin IDs. |
| `tools` | Active, retained from original (with documented normalization where applicable). |
| `tui` | Active, retained from original (with documented normalization where applicable). |
| `web_search` | Active, retained from original (with documented normalization where applicable). |
| `windows` | Active, retained from original (with documented normalization where applicable). |

## Feature keys

All 81 retained canonical/custom keys keep their original values. Experimental flags are not discarded merely because they are experimental. The 32 removed flags, 3 deprecated flags and 10 legacy aliases remain in the unchanged schema but are not activated. The exact lifecycle evidence is in `generate/feature-policy.json`.

| Feature | Disposition |
| --- | --- |
| `apply_patch_freeform` | Removed in inherited 0.147.0 registry; omitted. |
| `apply_patch_preserve_line_endings` | Retained: false |
| `apply_patch_streaming_events` | Retained: true |
| `apps` | Retained: true |
| `apps_mcp_path_override` | Removed in inherited 0.147.0 registry; omitted. |
| `auth_elicitation` | Retained: false |
| `background_paginated_rollout_migration` | Retained: false |
| `browser_use` | Retained: true |
| `browser_use_external` | Retained: true |
| `browser_use_full_cdp_access` | Retained: true |
| `chronicle` | Retained: true |
| `code_mode` | Retained: original structured settings |
| `code_mode_buffered_exec` | Retained: false |
| `code_mode_host` | Retained: original structured settings |
| `code_mode_interrupt` | Retained: true |
| `code_mode_only` | Retained: true |
| `codex_git_commit` | Removed in inherited 0.147.0 registry; omitted. |
| `codex_hooks` | Legacy alias; canonical setting: `hooks`. |
| `collab` | Legacy alias; canonical setting: `multi_agent`. |
| `collaboration_modes` | Removed in inherited 0.147.0 registry; omitted. |
| `computer_use` | Retained: true |
| `concurrent_reasoning_summaries` | Retained: false |
| `connectors` | Legacy alias; canonical setting: `apps`. |
| `current_time_reminder` | Retained: original structured settings |
| `default_mode_request_user_input` | Retained: true |
| `deferred_executor` | Retained: false |
| `deferred_tool_world_state` | Retained: false |
| `elevated_windows_sandbox` | Removed in inherited 0.147.0 registry; omitted. |
| `enable_experimental_windows_sandbox` | Legacy alias; canonical setting: `experimental_windows_sandbox`. |
| `enable_fanout` | Removed in inherited 0.147.0 registry; omitted. |
| `enable_mcp_apps` | Retained: true |
| `enable_request_compression` | Retained: true |
| `exec_permission_approvals` | Retained: false |
| `executed_tool_call_metadata` | Retained: true |
| `executor_capability_discovery` | Retained: true |
| `experimental_use_unified_exec_tool` | Legacy alias; canonical setting: `unified_exec`. |
| `experimental_windows_sandbox` | Removed in inherited 0.147.0 registry; omitted. |
| `external_agent_memory_import` | Retained: false |
| `external_migration` | Removed in inherited 0.147.0 registry; omitted. |
| `fast_mode` | Retained: false |
| `goals` | Retained: true |
| `guardian_approval` | Retained: false |
| `guardian_enhanced_node_repl_transcripts` | Retained: false |
| `guardian_node_repl_transcript_images` | Retained: false |
| `guardian_reuse_parent_compaction` | Retained: false |
| `guardianv2` | Retained: original structured settings |
| `hooks` | Retained: true |
| `image_detail_original` | Removed in inherited 0.147.0 registry; omitted. |
| `image_generation` | Retained: true |
| `image_resize_notice` | Retained: true |
| `imagegenext` | Legacy alias; canonical setting: `image_generation`. |
| `in_app_browser` | Retained: true |
| `in_app_chat` | Retained: true |
| `in_app_dictation` | Retained: true |
| `in_app_updates` | Retained: true |
| `item_ids` | Removed in inherited 0.147.0 registry; omitted. |
| `js_repl` | Removed in inherited 0.147.0 registry; omitted. |
| `js_repl_tools_only` | Removed in inherited 0.147.0 registry; omitted. |
| `local_thread_store_compression` | Retained: false |
| `mcp_2026_07_28` | Retained: false |
| `memories` | Retained: true |
| `memory_tool` | Legacy alias; canonical setting: `memories`. |
| `mentions_v2` | Retained: true |
| `multi_agent` | Retained: true |
| `multi_agent_mode` | Removed in inherited 0.147.0 registry; omitted. |
| `multi_agent_v2` | Retained: original structured settings |
| `network_proxy` | Retained: original structured settings |
| `non_prefixed_mcp_tool_names` | Retained: original structured settings |
| `personality` | Retained: true |
| `plugin_hooks` | Removed in inherited 0.147.0 registry; omitted. |
| `plugin_sharing` | Retained: true |
| `plugins` | Retained: true |
| `prevent_idle_sleep` | Retained: true |
| `psp` | Retained: false |
| `realtime_conversation` | Retained: true |
| `recommended_plugins` | Retained: true |
| `remote_compaction_v2` | Retained: true |
| `remote_control` | Removed in inherited 0.147.0 registry; omitted. |
| `remote_models` | Removed in inherited 0.147.0 registry; omitted. |
| `remote_plugin` | Retained: true |
| `request_permissions` | Legacy alias; canonical setting: `exec_permission_approvals`. |
| `request_permissions_tool` | Retained: true |
| `request_rule` | Removed in inherited 0.147.0 registry; omitted. |
| `resize_all_images` | Removed in inherited 0.147.0 registry; omitted. |
| `respect_system_proxy` | Retained: false |
| `responses_websockets` | Removed in inherited 0.147.0 registry; omitted. |
| `responses_websockets_v2` | Removed in inherited 0.147.0 registry; omitted. |
| `retain_client_developer_messages` | Retained: false |
| `rollout_budget` | Retained: original structured settings |
| `runtime_metrics` | Retained: false |
| `search_tool` | Removed in inherited 0.147.0 registry; omitted. |
| `secret_auth_storage` | Retained: true |
| `shell_snapshot` | Retained: true |
| `shell_tool` | Retained: true |
| `shell_zsh_fork` | Retained: false |
| `skill_env_var_dependency_prompt` | Removed in inherited 0.147.0 registry; omitted. |
| `skill_mcp_dependency_install` | Retained: true |
| `skill_search` | Retained: true |
| `sqlite` | Removed in inherited 0.147.0 registry; omitted. |
| `standalone_web_search` | Retained: true |
| `steer` | Removed in inherited 0.147.0 registry; omitted. |
| `telepathy` | Legacy alias; canonical setting: `chronicle`. |
| `terminal_resize_reflow` | Removed in inherited 0.147.0 registry; omitted. |
| `terminal_visualization_instructions` | Retained: true |
| `token_budget` | Retained: original structured settings |
| `tool_call_mcp_elicitation` | Retained: true |
| `tool_registry` | Retained: original structured settings |
| `tool_search` | Removed in inherited 0.147.0 registry; omitted. |
| `tool_search_always_defer_mcp_tools` | Removed in inherited 0.147.0 registry; omitted. |
| `tool_suggest` | Retained: true |
| `tui_app_server` | Removed in inherited 0.147.0 registry; omitted. |
| `unavailable_dummy_tools` | Removed in inherited 0.147.0 registry; omitted. |
| `unbounded_connection_retries` | Retained: true |
| `undo` | Removed in inherited 0.147.0 registry; omitted. |
| `unified_exec` | Retained: true |
| `unified_exec_zsh_fork` | Retained: true |
| `unified_image_budget` | Retained: true |
| `use_agent_identity` | Retained: true |
| `use_legacy_landlock` | Deprecated in inherited 0.147.0 registry; omitted. |
| `use_linux_sandbox_bwrap` | Removed in inherited 0.147.0 registry; omitted. |
| `view_image` | Retained: true |
| `web_search` | Legacy alias; canonical setting: `web_search`. |
| `web_search_cached` | Deprecated in inherited 0.147.0 registry; omitted. |
| `web_search_request` | Deprecated in inherited 0.147.0 registry; omitted. |
| `workspace_dependencies` | Retained: false |
| `workspace_owner_usage_nudge` | Removed in inherited 0.147.0 registry; omitted. |

## Additional normalization

`features.multi_agent_v2.usage_hint_enabled` is explicitly ignored/deprecated in the supplied schema. `features.child_agents_md` in old role files is not accepted by this schema. Shell include/exclude arrays become canonical filter maps without changing actions. Permission network domain/socket arrays become canonical maps; unsupported network-admin keys are removed. The broker socket is allowed. All 30 original MCP registrations remain; 13 image-backed modes use the new broker.

## Requirements are not config schema instances

`etc/config.toml` is the complete synchronized configuration. `etc/requirements.toml` is intentionally nonrestrictive locally: old identity allowlists omitted node_repl/CUA, and the old residency limit was not an allow-all policy. Original requirements are preserved for comparison; no claim is made that config.schema.json validates the requirements format.

## Examples versus live configuration

`generate/examples/config.home.toml` covers all schema definitions and alternatives in its comment ledger. It is not an installable preset. Actual active layers are listed in `static-report.json`; profile, agent and file references are independently checked.
