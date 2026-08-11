package Codex::Hook::Catalog;

use strict;
use warnings;

use Exporter qw(import);

our @EXPORT_OK = qw(hook_catalog);

my $GENERIC_TOOL_MATCHER = '^(?:[^BEWabemsw].*|B(?:|[^a].*|a(?:|[^s].*|s(?:|[^h].*|h.+)))|E(?:|[^d].*|d(?:|[^i].*|i(?:|[^t].*|t.+)))|W(?:|[^r].*|r(?:|[^i].*|i(?:|[^t].*|t(?:|[^e].*|e.+))))|a(?:|[^p].*|p(?:|[^p].*|p(?:|[^l].*|l(?:|[^y].*|y(?:|[^_].*|_(?:|[^p].*|p(?:|[^a].*|a(?:|[^t].*|t(?:|[^c].*|c(?:|[^h].*|h.+))))))))))|b(?:|[^a].*|a(?:|[^s].*|s(?:|[^h].*|h.+)))|e(?:|[^dx].*|d(?:|[^i].*|i(?:|[^t].*|t.+))|x(?:|[^e].*|e(?:|[^c].*|c(?:|[^_].*|_(?:|[^c].*|c(?:|[^o].*|o(?:|[^m].*|m(?:|[^m].*|m(?:|[^a].*|a(?:|[^n].*|n(?:|[^d].*|d.+)))))))))))|m(?:|[^c].*|c(?:|[^p].*|p(?:|[^_].*|_(?:|[^_].*))))|s(?:|[^h].*|h(?:|[^e].*|e(?:|[^l].*|l(?:|[^l].*|l.+))))|w(?:|[^r].*|r(?:|[^i].*|i(?:|[^t].*|t(?:|[^e].*|e.+)))))$';
my $GENERIC_SUBAGENT_MATCHER = '^(?:[^acdehimoprstw].*|a(?:|[^n].*|n(?:|[^a].*|a(?:|[^l].*|l(?:|[^y].*|y(?:|[^s].*|s(?:|[^t].*|t.+))))))|c(?:|[^o].*|o(?:|[^d].*|d(?:|[^e].*|e(?:|[^r].*|r.+))))|d(?:|[^e].*|e(?:|[^fl].*|f(?:|[^a].*|a(?:|[^u].*|u(?:|[^l].*|l(?:|[^t].*|t.+))))|l(?:|[^e].*|e(?:|[^g].*|g(?:|[^a].*|a(?:|[^t].*|t(?:|[^o].*|o(?:|[^r].*|r.+))))))))|e(?:|[^x].*|x(?:|[^p].*|p(?:|[^l].*|l(?:|[^o].*|o(?:|[^r].*|r(?:|[^e].*|e(?:|[^r].*|r.+)))))))|h(?:|[^u].*|u(?:|[^n].*|n(?:|[^t].*|t(?:|[^e].*|e(?:|[^r].*|r.+)))))|i(?:|[^n].*|n(?:|[^t].*|t(?:|[^e].*|e(?:|[^g].*|g(?:|[^r].*|r(?:|[^a].*|a(?:|[^t].*|t(?:|[^o].*|o(?:|[^r].*|r.+)))))))))|m(?:|[^a].*|a(?:|[^n].*|n(?:|[^a].*|a(?:|[^g].*|g(?:|[^e].*|e(?:|[^r].*|r.+))))))|o(?:|[^r].*|r(?:|[^c].*|c(?:|[^h].*|h(?:|[^e].*|e(?:|[^s].*|s(?:|[^t].*|t(?:|[^r].*|r(?:|[^a].*|a(?:|[^t].*|t(?:|[^o].*|o(?:|[^r].*|r.+)))))))))))|p(?:|[^l].*|l(?:|[^a].*|a(?:|[^n].*|n(?:|[^n].*|n(?:|[^e].*|e(?:|[^r].*|r.+))))))|r(?:|[^e].*|e(?:|[^v].*|v(?:|[^i].*|i(?:|[^e].*|e(?:|[^w].*|w(?:|[^e].*|e(?:|[^r].*|r.+)))))))|s(?:|[^y].*|y(?:|[^n].*|n(?:|[^t].*|t(?:|[^h].*|h(?:|[^e].*|e(?:|[^s].*|s(?:|[^i].*|i(?:|[^z].*|z(?:|[^e].*|e(?:|[^r].*|r.+))))))))))|t(?:|[^e].*|e(?:|[^s].*|s(?:|[^t].*|t(?:|[^e].*|e(?:|[^r].*|r.+)))))|w(?:|[^o].*|o(?:|[^r].*|r(?:|[^k].*|k(?:|[^e].*|e(?:|[^r].*|r.+))))))$';

sub hook_catalog {
    my $catalog = {
        version => 1,
        tool_profiles => [
            {
                id      => 'edit',
                matcher => '^(apply_patch|Edit|edit|Write|write)$',
                label   => 'edit operation',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_edit.pl',
                        timeout       => 20,
                        statusMessage => 'Checking edit guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_edit.pl',
                        timeout       => 15,
                        statusMessage => 'Checking edit approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_edit.pl',
                        timeout       => 15,
                        statusMessage => 'Reviewing edit follow-up',
                    },
                },
            },
            {
                id      => 'mcp_openai_developer_docs',
                matcher => '^mcp__openaiDeveloperDocs__(?:fetch_openai_doc|get_openapi_spec|list_api_endpoints|list_openai_docs|search_openai_docs)$',
                label   => 'OpenAI developer docs MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_openai_developer_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Checking OpenAI docs MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_openai_developer_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Checking OpenAI docs MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_openai_developer_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing OpenAI docs MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_context7',
                matcher => '^mcp__context7__(?:resolve-library-id|query-docs)$',
                label   => 'Context7 MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_context7.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Context7 MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_context7.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Context7 MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_context7.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Context7 MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_filesystem',
                matcher => '^mcp__filesystem__(?:create_directory|directory_tree|edit_file|get_file_info|list_allowed_directories|list_directory|list_directory_with_sizes|move_file|read_file|read_media_file|read_multiple_files|read_text_file|search_files|write_file)$',
                label   => 'filesystem MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_filesystem.pl',
                        timeout       => 20,
                        statusMessage => 'Checking filesystem MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_filesystem.pl',
                        timeout       => 20,
                        statusMessage => 'Checking filesystem MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_filesystem.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing filesystem MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_fetch',
                matcher => '^mcp__fetch__fetch$',
                label   => 'fetch MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_fetch.pl',
                        timeout       => 20,
                        statusMessage => 'Checking fetch MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_fetch.pl',
                        timeout       => 20,
                        statusMessage => 'Checking fetch MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_fetch.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing fetch MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_sequential_thinking',
                matcher => '^mcp__sequential_thinking__sequentialthinking$',
                label   => 'sequential thinking MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_sequential_thinking.pl',
                        timeout       => 20,
                        statusMessage => 'Checking sequential thinking MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_sequential_thinking.pl',
                        timeout       => 20,
                        statusMessage => 'Checking sequential thinking MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_sequential_thinking.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing sequential thinking MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_time',
                matcher => '^mcp__time__(?:get_current_time|convert_time)$',
                label   => 'time MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_time.pl',
                        timeout       => 20,
                        statusMessage => 'Checking time MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_time.pl',
                        timeout       => 20,
                        statusMessage => 'Checking time MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_time.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing time MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_git',
                matcher => '^mcp__git__.+$',
                label   => 'git MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking git MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking git MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing git MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_memory',
                matcher => '^mcp__memory__.+$',
                label   => 'memory MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking memory MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking memory MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing memory MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_markdown',
                matcher => '^mcp__markdown__.+$',
                label   => 'markdown MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking markdown MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking markdown MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing markdown MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_playwright',
                matcher => '^mcp__playwright__.+$',
                label   => 'Playwright MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Playwright MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Playwright MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Playwright MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_chrome_devtools',
                matcher => '^mcp__(?:chrome-devtools|chrome_devtools)__.+$',
                label   => 'Chrome DevTools MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Chrome DevTools MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Chrome DevTools MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Chrome DevTools MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_postgres',
                matcher => '^mcp__postgres__.+$',
                label   => 'Postgres MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Postgres MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Postgres MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Postgres MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_sqlite',
                matcher => '^mcp__sqlite__.+$',
                label   => 'SQLite MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking SQLite MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking SQLite MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing SQLite MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_semgrep',
                matcher => '^mcp__semgrep__.+$',
                label   => 'Semgrep MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Semgrep MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Semgrep MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Semgrep MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_cloudflare_observability',
                matcher => '^mcp__cloudflare-observability__(?:accounts_list|migrate_pages_to_workers_guide|observability_keys|observability_values|query_worker_observability|search_cloudflare_documentation|set_active_account|workers_get_worker|workers_get_worker_code|workers_list)$',
                label   => 'Cloudflare observability MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_cloudflare_observability.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare observability MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_cloudflare_observability.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare observability MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_cloudflare_observability.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Cloudflare observability MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_cloudflare_builds',
                matcher => '^mcp__cloudflare-builds__(?:accounts_list|set_active_account|workers_builds_get_build|workers_builds_get_build_logs|workers_builds_list_builds|workers_builds_set_active_worker|workers_get_worker|workers_get_worker_code|workers_list)$',
                label   => 'Cloudflare builds MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_cloudflare_builds.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare builds MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_cloudflare_builds.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare builds MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_cloudflare_builds.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Cloudflare builds MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_cloudflare_bindings',
                matcher => '^mcp__cloudflare-bindings__(?:accounts_list|d1_database_create|d1_database_delete|d1_database_get|d1_database_query|d1_databases_list|hyperdrive_config_delete|hyperdrive_config_edit|hyperdrive_config_get|hyperdrive_configs_list|kv_namespace_create|kv_namespace_delete|kv_namespace_get|kv_namespace_update|kv_namespaces_list|migrate_pages_to_workers_guide|r2_bucket_create|r2_bucket_delete|r2_bucket_get|r2_buckets_list|search_cloudflare_documentation|set_active_account|workers_get_worker|workers_get_worker_code|workers_list)$',
                label   => 'Cloudflare bindings MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_cloudflare_bindings.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare bindings MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_cloudflare_bindings.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare bindings MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_cloudflare_bindings.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Cloudflare bindings MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_cloudflare_docs',
                matcher => '^mcp__cloudflare-docs__(?:migrate_pages_to_workers_guide|search_cloudflare_documentation)$',
                label   => 'Cloudflare docs MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_cloudflare_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare docs MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_cloudflare_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare docs MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_cloudflare_docs.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Cloudflare docs MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp_cloudflare_api',
                matcher => '^mcp__cloudflare-api__(?:execute|search)$',
                label   => 'Cloudflare API MCP call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp_cloudflare_api.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare API MCP guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp_cloudflare_api.pl',
                        timeout       => 20,
                        statusMessage => 'Checking Cloudflare API MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp_cloudflare_api.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing Cloudflare API MCP follow-up',
                    },
                },
            },
            {
                id      => 'mcp',
                matcher => '^mcp__',
                label   => 'MCP tool call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking MCP tool guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Checking MCP approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use_mcp.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing MCP follow-up',
                    },
                },
            },
            {
                id      => 'memory',
                matcher => '^memories(?:list|read|search)$',
                label   => 'memory tool call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use.pl',
                        timeout       => 20,
                        statusMessage => 'Checking memory tool guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request.pl',
                        timeout       => 20,
                        statusMessage => 'Checking memory tool approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing memory tool follow-up',
                    },
                },
            },
            {
                id      => 'generic',
                matcher => $GENERIC_TOOL_MATCHER,
                label   => 'tool call',
                events  => {
                    PreToolUse => {
                        script        => 'pre_tool_use.pl',
                        timeout       => 20,
                        statusMessage => 'Checking generic tool guardrails',
                    },
                    PermissionRequest => {
                        script        => 'permission_request.pl',
                        timeout       => 20,
                        statusMessage => 'Checking generic tool approval scope',
                    },
                    PostToolUse => {
                        script        => 'post_tool_use.pl',
                        timeout       => 20,
                        statusMessage => 'Reviewing generic tool follow-up',
                    },
                },
            },
        ],
        roles => [
            {
                name        => 'default',
                description => 'Baseline generalist agent for most coding, configuration, and integration tasks with live web-search access.',
                use_when    => 'Use for small or mixed tasks that do not need a specialized handoff role.',
            },
            {
                name        => 'manager',
                description => 'Project manager that owns planning, gating, artifact checks, and multi-agent handoffs.',
                use_when    => 'Use to decompose work, define acceptance criteria, assign owned slices, and gate handoffs between other agents.',
            },
            {
                name        => 'orchestrator',
                description => 'Multi-agent runtime orchestrator that manages fan-out, sequencing, wait or close decisions, and reconciliation across child threads.',
                use_when    => 'Use when several child threads stay live at once and the hard part is coordinating their sequencing, waits, resumes, and close conditions.',
            },
            {
                name        => 'planner',
                description => 'Front-load planning agent that decomposes ambiguous goals into owned slices, acceptance criteria, and validation gates before delegation.',
                use_when    => 'Use before fan-out when the parent still needs crisp scope cuts, stop conditions, or a validation plan.',
            },
            {
                name        => 'delegator',
                description => 'Delegation controller that selects roles, packages handoffs, and manages spawn or resume or wait or close flow for subagents.',
                use_when    => 'Use when the main task is choosing the right child role, preparing a clean handoff, or managing follow-up inputs to existing children.',
            },
            {
                name        => 'worker',
                description => 'Scoped delivery agent for bounded tasks with explicit file ownership and tight handoffs.',
                use_when    => 'Use for fast, narrow execution on a clearly owned slice with low ambiguity.',
            },
            {
                name        => 'coder',
                description => 'Implementation-heavy coding agent for complex root-cause fixes and cross-cutting changes.',
                use_when    => 'Use for substantial implementation work, root-cause fixes, and changes that cut across modules.',
            },
            {
                name        => 'analyst',
                description => 'Cross-agent analysis agent that compares child findings, resolves conflicts, and identifies evidence gaps before synthesis.',
                use_when    => 'Use after discovery or implementation fan-out when the parent needs contradiction checks, evidence ranking, or next-step arbitration.',
            },
            {
                name        => 'synthesizer',
                description => 'Synthesis agent that merges completed child outputs into one coherent answer, patch plan, or handoff with provenance.',
                use_when    => 'Use when the child work is complete but the parent still needs one integrated artifact that keeps provenance and residual risks explicit.',
            },
            {
                name        => 'integrator',
                description => 'Read-first integration agent that checks mirror sync and release patch readiness without applying patches.',
                use_when    => 'Use for mirror-awareness, release-patch validation, and repository-safety checks where mutation should stay minimal or read-only.',
            },
            {
                name        => 'hunter',
                description => 'Search-forward research agent for current docs, APIs, runtime behavior, and external evidence.',
                use_when    => 'Use when the answer depends on live external references, current docs, or source-backed research.',
            },
            {
                name        => 'explorer',
                description => 'Read-heavy explorer for repository mapping, dependency tracing, and codebase discovery.',
                use_when    => 'Use for deep read-only repo exploration, dependency tracing, and handoff-ready architecture mapping.',
            },
            {
                name        => 'reviewer',
                description => 'Review agent for syntax, hardening, functionality, regressions, and best-practice checks.',
                use_when    => 'Use for review passes that need severity-ranked findings, correctness checks, and regression analysis.',
            },
            {
                name        => 'tester',
                description => 'Verification agent that reproduces issues, runs targeted tests, and validates completed work.',
                use_when    => 'Use for focused verification, reproduction, failure-path checks, and evidence-backed validation.',
            },
        ],
        subagent_profiles => [
            {
                id           => 'coordination',
                status_label => 'coordination',
                matcher      => '^(default|manager)$',
                role_names   => ['default', 'manager'],
                start_script => 'subagent_start_coordination.pl',
                stop_script  => 'subagent_stop_coordination.pl',
                start_lines  => [
                    'Own decomposition, acceptance criteria, and sequencing before you ask any child agent to do work.',
                    'Delegate discovery to `explorer` or `hunter`, implementation to `worker` or `coder`, and sign-off to `reviewer` or `tester`.',
                ],
                stop_lines => [
                    'Do not accept the handoff until it lists owned files, exact commands, evidence, and residual blockers.',
                    'Reconcile each child result against the parent plan before you re-delegate or end the turn.',
                ],
            },
            {
                id           => 'orchestration',
                status_label => 'orchestration',
                matcher      => '^orchestrator$',
                role_names   => ['orchestrator'],
                start_script => 'subagent_start_orchestration.pl',
                stop_script  => 'subagent_stop_orchestration.pl',
                start_lines  => [
                    'Keep one parent-owned critical path and use child threads only for genuinely parallel or independent slices.',
                    'Track spawn or resume or wait or close decisions explicitly so every live child has a clear owner, dependency, and next state.',
                ],
                stop_lines => [
                    'Do not close or supersede a child until you reconcile its files, commands, evidence, and residual risks against the parent ledger.',
                    'Call out blocked waits, stale child context, and any thread that still needs a parent-side follow-up prompt.',
                ],
            },
            {
                id           => 'planning',
                status_label => 'planning',
                matcher      => '^planner$',
                role_names   => ['planner'],
                start_script => 'subagent_start_planning.pl',
                stop_script  => 'subagent_stop_planning.pl',
                start_lines  => [
                    'Turn the request into owned slices with objective, files or surfaces, acceptance criteria, validation commands, and stop conditions before fan-out.',
                    'When ambiguity remains, say what discovery role should resolve it before any implementation child is spawned.',
                ],
                stop_lines => [
                    'Hand back a delegation-ready plan that names the next role, the exact prompt or evidence it needs, and the validation gate that closes the slice.',
                    'Highlight unresolved ambiguity instead of letting the parent guess at the next spawn sequence.',
                ],
            },
            {
                id           => 'delegation',
                status_label => 'delegation',
                matcher      => '^delegator$',
                role_names   => ['delegator'],
                start_script => 'subagent_start_delegation.pl',
                stop_script  => 'subagent_stop_delegation.pl',
                start_lines  => [
                    'Select the smallest role that fits each child slice and package the handoff with exact commands, paths, evidence, and acceptance criteria.',
                    'Prefer `send_input` or `resume_agent` for existing children, reserve `spawn_agent` for net-new owned slices, and use `wait_agent` only when the parent critical path is blocked.',
                ],
                stop_lines => [
                    'Return the active thread map: which child was spawned or resumed, what it owns, and what parent-side action should happen next.',
                    'If a child should be closed, explain why its context is fully reconciled and what evidence the parent already captured.',
                ],
            },
            {
                id           => 'delivery',
                status_label => 'delivery',
                matcher      => '^(worker|coder)$',
                role_names   => ['worker', 'coder'],
                start_script => 'subagent_start_delivery.pl',
                stop_script  => 'subagent_stop_delivery.pl',
                start_lines  => [
                    'Stay inside the assigned file boundary and return exact edits, commands, or blockers instead of broad redesign guidance.',
                    'Do not spawn another child unless the remaining task is clearly orthogonal and the parent explicitly needs that split.',
                ],
                stop_lines => [
                    'Report the owned files, commands run, and any unverified assumptions in the handoff.',
                    'If validation was skipped, say exactly what blocked it and whether the parent must rerun it.',
                ],
            },
            {
                id           => 'analysis',
                status_label => 'analysis',
                matcher      => '^analyst$',
                role_names   => ['analyst'],
                start_script => 'subagent_start_analysis.pl',
                stop_script  => 'subagent_stop_analysis.pl',
                start_lines  => [
                    'Compare child outputs, separate confirmed facts from hypotheses, and call out contradictions or evidence gaps without drifting into speculative redesign.',
                    'Use the child artifacts already produced; ask for more discovery or validation only when the current evidence cannot resolve a decision.',
                ],
                stop_lines => [
                    'Return agreements, disagreements, and the exact next check or prompt needed to settle each unresolved point.',
                    'Make confidence and evidence quality explicit so the parent knows what can be merged safely.',
                ],
            },
            {
                id           => 'synthesis',
                status_label => 'synthesis',
                matcher      => '^synthesizer$',
                role_names   => ['synthesizer'],
                start_script => 'subagent_start_synthesis.pl',
                stop_script  => 'subagent_stop_synthesis.pl',
                start_lines  => [
                    'Merge converged child outputs into one coherent artifact without erasing ownership boundaries, provenance, or skipped validation notes.',
                    'Prefer concise integration of existing evidence over opening new discovery branches.',
                ],
                stop_lines => [
                    'Identify which statements come from which child evidence and which residual risks still need parent-side confirmation.',
                    'If the merge surfaced conflicts, route them back to `analyst`, `reviewer`, or `tester` instead of papering them over.',
                ],
            },
            {
                id           => 'integrator',
                status_label => 'integrator',
                matcher      => '^integrator$',
                role_names   => ['integrator'],
                start_script => 'subagent_start_integrator.pl',
                stop_script  => 'subagent_stop_integrator.pl',
                start_lines  => [
                    'Keep the scope read-first and repository-safe unless the parent explicitly broadened the task beyond integration checks.',
                    'Focus on merge points, config layering, release or mirror contracts, and drift between child slices.',
                ],
                stop_lines => [
                    'Call out conflicts between child outputs, config layers, or promotion contracts before the parent integrates anything.',
                    'Flag unresolved compatibility or sequencing risks explicitly.',
                ],
            },
            {
                id           => 'research',
                status_label => 'research',
                matcher      => '^(explorer|hunter)$',
                role_names   => ['explorer', 'hunter'],
                start_script => 'subagent_start_research.pl',
                stop_script  => 'subagent_stop_research.pl',
                start_lines  => [
                    'Gather source-backed repository or documentation evidence and avoid speculative implementation advice.',
                    'Return precise references, affected surfaces, and confidence notes instead of patches unless the parent explicitly asked for edits.',
                ],
                stop_lines => [
                    'Separate confirmed facts from hypotheses and list any gaps that still need local validation.',
                    'If sources conflict, say that clearly instead of blending them.',
                ],
            },
            {
                id           => 'validation',
                status_label => 'validation',
                matcher      => '^(reviewer|tester)$',
                role_names   => ['reviewer', 'tester'],
                start_script => 'subagent_start_validation.pl',
                stop_script  => 'subagent_stop_validation.pl',
                start_lines  => [
                    'Reproduce or verify the claimed behavior with the narrowest deterministic checks that prove or falsify the concern.',
                    'Return raw outcomes, exact commands, and failing boundaries instead of redesign suggestions.',
                ],
                stop_lines => [
                    'State pass, fail, or untested per check, plus the exact blocker whenever a check could not run.',
                    'Surface regression risk and missing coverage explicitly before the parent closes the task.',
                ],
            },
            {
                id           => 'generic',
                status_label => 'generic',
                matcher      => $GENERIC_SUBAGENT_MATCHER,
                role_names   => [],
                start_script => 'subagent_start.pl',
                stop_script  => 'subagent_stop.pl',
                start_lines  => [],
                stop_lines   => [],
            },
        ],
    };
    return $catalog;
}

1;
