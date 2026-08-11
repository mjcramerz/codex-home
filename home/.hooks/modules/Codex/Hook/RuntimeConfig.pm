package Codex::Hook::RuntimeConfig;

use strict;
use warnings;

use Exporter qw(import);
use Codex::Hook::Catalog qw(hook_catalog);

our @EXPORT_OK = qw(runtime_config);

sub runtime_config {
    my $hook_catalog = hook_catalog();
    return {
        version     => 1,
        multi_agent => {
            trigger_patterns => [
                '\bagent\b',
                '\bagents\b',
                '\bsubagent\b',
                '\bsub-agent\b',
                '\bspawn_agent\b',
                '\bspawn_agents_on_csv\b',
                '\bsend_input\b',
                '\bresume_agent\b',
                '\bwait_agent\b',
                '\bclose_agent\b',
                '\bdelegate\b',
                '\bdelegation\b',
                '\bmulti-agent\b',
                '\bmulti_agents\b',
                '\bparallel agents?\b',
                '\bfanout\b',
                '\borchestrat\b',
                '\bhandoff\b',
            ],
            shared_lines => [
                'Multi-agent roles are shared across repos and come from the shared configured role catalog.',
                'Prefer the smallest role that fits the task, keep ownership boundaries explicit, and hand off commands, files, evidence, and residual risks.',
            ],
            prompt_submit_lines => [
                'Only use `spawn_agent` when the user explicitly asks for sub-agents, delegation, or parallel agent work.',
                'Keep the next critical-path step local, then delegate only bounded sidecar work with explicit file ownership, commands, and acceptance criteria.',
                'Prefer `send_input` or `resume_agent` when follow-up depends on an existing child context, use `wait_agent` only when the critical path is blocked, and use `close_agent` only after you reconcile the child handoff.',
                'Use `planner` to turn ambiguous asks into explicit slices before fan-out, `delegator` or `orchestrator` when the main challenge is thread control, `analyst` to compare child findings, and `synthesizer` to merge converged outputs.',
            ],
            roles             => $hook_catalog->{roles},
            subagent_profiles => $hook_catalog->{subagent_profiles},
        },
        repos => [
            {
                id           => 'codex-manager',
                display_name => 'codex-manager',
                match        => {
                    repo_names   => ['codex-manager', 'codex'],
                    all_of_paths => [
                        'src/install/codex_install.py',
                        'config/usr/apps.toml',
                        'Makefile',
                    ],
                    any_of_paths => ['Makefile'],
                },
                environment => {
                    required_commands => ['bash', 'make'],
                    optional_commands => ['shellcheck', 'yamllint', 'uv', 'wrangler', 'node', 'npx', 'podman', 'docker'],
                    optional_probes   => [
                        {
                            label   => 'podman ps',
                            command => ['podman', 'ps'],
                        },
                        {
                            label   => 'docker ps',
                            command => ['docker', 'ps'],
                        },
                    ],
                },
                focus_areas => [
                    {
                        label      => 'installer',
                        path_globs => ['src/install/**', 'Makefile'],
                    },
                    {
                        label      => 'hooks',
                        path_globs => [
                            'resources/hooks/**',
                            'src/install/hook_runtime_catalog.py',
                            'src/install/hooks_builder.py',
                            'tests/test_hook_runtime_modules.py',
                            'tests/test_hooks_builder.py',
                            'tests/test_hooks_scripts.py',
                        ],
                    },
                    {
                        label      => 'skills',
                        path_globs => [
                            'resources/skills/**',
                            'src/install/skills.py',
                            'tests/test_skill_catalog_contract.py',
                        ],
                    },
                    {
                        label      => 'plugins',
                        path_globs => [
                            'resources/plugins/**',
                            'src/install/apps_config.py',
                            'src/install/plugin_bundles.py',
                            'src/install/plugins.py',
                            'tests/test_plugin_runtime_contracts.py',
                        ],
                    },
                    {
                        label      => 'runtime-config',
                        path_globs => [
                            'config/usr/**',
                            'config/vendor/**',
                            'config/agents/**',
                        ],
                    },
                    {
                        label      => 'runtime-tests',
                        path_globs => ['tests/**'],
                    },
                    {
                        label      => 'agents',
                        path_globs => ['config/agents/**', 'config/usr/apps.toml'],
                    },
                ],
                session_start => {
                    startup_context => [
                        'Repo role: Codex installer and runtime-configuration source tree.',
                        'Edit scope: `src/install/**`, `config/usr/apps.toml`, `config/usr/*`, `config/vendor/*`, `config/agents/*.toml`, and `resources/**`.',
                        'Hooks source of truth: `resources/hooks/hooks.json`, `resources/hooks/scripts/lib/Codex/Hook/**`, `src/install/hooks_builder.py`, and `src/install/hook_runtime_catalog.py`.',
                        'Skills/plugins source of truth: `resources/skills/metadata.json`, `resources/plugins/manifest.json`, and the installer rewrite logic that manages rendered `agents/openai.yaml` tool dependencies.',
                        'Validation baseline: run `python3 -m compileall src tests` and `python3 -m unittest discover -s tests` for installer/runtime changes.',
                    ],
                    resume_context => [
                        'Resume scope: `src/install/**`, `config/usr/**`, `config/vendor/**`, `config/agents/**`, `resources/**`, and `tests/**`.',
                        'Resume checklist: re-check hook, skill, and plugin source-of-truth files before patching rendered runtime outputs.',
                        'Resume validation: keep transcript-derived context concise, then rerun the narrowest syntax and unit checks for the touched hook or installer surface.',
                    ],
                },
                user_prompt_submit => {
                    rules => [
                        {
                            patterns => [
                                '\bhook\b',
                                '\bhooks\b',
                                '\bsession[- ]start\b',
                                '\bstart hook\b',
                                '\bstop hook\b',
                                '\buserpromptsubmit\b',
                                '\bpermissionrequest\b',
                                '\bpretooluse\b',
                                '\bposttooluse\b',
                            ],
                            lines => [
                                'Hook work should stay schema-first: emit only fields allowed by the event output schema, and prefer transcript-driven context over generic boilerplate.',
                                'When describing the installed runtime, use `$CODEX_HOME/hooks.json`, `$CODEX_HOME/.hooks/scripts`, and `$CODEX_HOME/.hooks/modules` instead of repository source paths.',
                                'Include the full hook context needed to resolve the task; do not omit relevant changed-file, validation, or next-step detail just for brevity.',
                                'Installed home hook config lives at `$CODEX_HOME/hooks.json`.',
                                'Installed hook entrypoints live under `$CODEX_HOME/.hooks/scripts`, and installed Perl hook modules live under `$CODEX_HOME/.hooks/modules`.',
                                'Keep matcher groups mutually exclusive because Codex runs matching command hooks concurrently. `UserPromptSubmit` and `Stop` still self-filter inside the command.',
                                'For hook-runtime work in `codex-manager`, inspect `resources/hooks/hooks.json`, `src/install/hooks_builder.py`, `src/install/hook_runtime_catalog.py`, and the hook tests in `tests/test_hook_runtime_modules.py`, `tests/test_hooks_builder.py`, and `tests/test_hooks_scripts.py`.',
                                'When Perl hook modules change, run `perl -c` on touched `.pm` or `.pl` files in addition to the targeted Python hook tests.',
                            ],
                        },
                        {
                            patterns => [
                                '\bskill\b',
                                '\bskills\b',
                                '\bplugin\b',
                                '\bplugins\b',
                                '\bmarketplace\b',
                                '\bopenai\.yaml\b',
                                '\bdependencies\.tools\b',
                            ],
                            lines => [
                                'For skill and plugin availability work, keep `src/install/skills.py`, `src/install/apps_config.py`, `src/install/plugins.py`, `src/install/plugin_bundles.py`, `resources/skills/metadata.json`, `resources/plugins/manifest.json`, and the rendered `agents/openai.yaml` tool dependencies aligned.',
                                'Validate skill/plugin changes with `python3 -m unittest tests.test_skill_catalog_contract tests.test_plugin_runtime_contracts` plus any touched hook tests.',
                            ],
                        },
                        {
                            patterns => [
                                '\binstall\b',
                                '\binstaller\b',
                                '\bruntime\b',
                                '\bconfig\b',
                                '\bconfig\.toml\b',
                                '\bapps\.toml\b',
                            ],
                            lines => [
                                'For `codex-manager`, source changes for installer and runtime configuration usually touch `src/install/**`, `config/usr/apps.toml`, `config/usr/*`, `config/vendor/*`, and `config/agents/*.toml`.',
                            ],
                        },
                        {
                            patterns => [
                                '\btest\b',
                                '\btests\b',
                                '\bverify\b',
                                '\bverification\b',
                                '\bvalidate\b',
                                '\bvalidation\b',
                                '\bcheck\b',
                            ],
                            lines => [
                                'For `codex-manager` validation, run `python3 -m compileall src tests` and `python3 -m unittest discover -s tests`.',
                            ],
                        },
                    ],
                },
                stop => {
                    rules => [
                        {
                            id                 => 'runtime_generation_validation',
                            changed_path_globs => ['resources/**', 'src/install/**', 'tests/**', 'Makefile'],
                            require_all_patterns => ['\bpython3? -m compileall\b'],
                            message            => 'Runtime-generation changes ({changed_files_preview}) need `python3 -m compileall src tests`.',
                        },
                        {
                            id                 => 'runtime_generation_unit_tests',
                            changed_path_globs => ['resources/**', 'tests/**'],
                            require_any_patterns => [
                                '\bpython3? -m unittest discover -s tests\b',
                                '\bpython3? -m unittest\b',
                                'pytest[^\n]*tests/',
                            ],
                            message            => 'Runtime-generation changes ({changed_files_preview}) need targeted regression coverage from the local test suite.',
                        },
                    ],
                },
            },
            {
                id           => 'codex',
                display_name => 'codex',
                match        => {
                    repo_names   => ['codex'],
                    all_of_paths => ['codex-rs/core/src/codex.rs', 'codex-rs/Cargo.toml'],
                    any_of_paths => ['codex-rs/tui/src', 'codex-rs/tui_app_server/**'],
                },
                environment => {
                    required_commands => ['cargo', 'just'],
                    optional_commands => ['cargo-insta'],
                    optional_probes   => [
                        {
                            label   => 'cargo test -p codex-core --target x86_64-unknown-linux-gnu --no-run',
                            command => [
                                'cargo',
                                'test',
                                '-p',
                                'codex-core',
                                '--target',
                                'x86_64-unknown-linux-gnu',
                                '--no-run',
                            ],
                        },
                    ],
                },
                focus_areas => [
                    {
                        label      => 'core',
                        path_globs => ['codex-rs/core/**'],
                    },
                    {
                        label      => 'tui',
                        path_globs => ['codex-rs/tui/**', 'codex-rs/tui_app_server/**'],
                    },
                    {
                        label      => 'workspace',
                        path_globs => ['codex-rs/**'],
                    },
                ],
                session_start => {
                    startup_context => [
                        'Repo role: upstream Codex source tree and runtime-contract implementation.',
                        'Focus on `codex-rs/core/**`, `codex-rs/tui/**`, `codex-rs/tui_app_server/**`, and related crates under `codex-rs/**`.',
                        'For local Rust work, run `cd codex-rs && just fmt`, then the smallest crate-scoped command with `--target x86_64-unknown-linux-gnu`.',
                    ],
                    resume_context => [
                        'Resume in the touched `codex-rs/**` crates and keep validation crate-scoped with `--target x86_64-unknown-linux-gnu`.',
                    ],
                },
                user_prompt_submit => {
                    rules => [
                        {
                            patterns => ['\breview\b', '\baudit\b'],
                            lines    => [
                                'For `codex` reviews, prioritize correctness, regressions, contract drift, and missing tests in the touched crates.',
                            ],
                        },
                        {
                            patterns => ['\bcore\b', '\bengine\b', '\bruntime\b', '\bprotocol\b'],
                            lines    => [
                                'For `codex` engine work, focus first on `codex-rs/core/**`, related protocol crates, and the smallest deterministic crate-scoped validation command with `--target x86_64-unknown-linux-gnu`.',
                            ],
                        },
                        {
                            patterns => ['\btui\b', '\bui\b', '\brender\b', '\bsnapshot\b'],
                            lines    => [
                                'For `codex` UI work, watch `codex-rs/tui/**`, `codex-rs/tui_app_server/**`, and snapshot coverage.',
                            ],
                        },
                        {
                            patterns => [
                                '\btest\b',
                                '\btests\b',
                                '\bverify\b',
                                '\bverification\b',
                                '\bvalidate\b',
                                '\bvalidation\b',
                                '\bcheck\b',
                            ],
                            lines => [
                                'For `codex` changes, run `cd codex-rs && just fmt`, then targeted crate commands such as `cargo check -p codex-core --target x86_64-unknown-linux-gnu`, `cargo test -p codex-core --target x86_64-unknown-linux-gnu`, or `cargo test -p codex-tui --target x86_64-unknown-linux-gnu`.',
                            ],
                        },
                    ],
                },
                stop => {
                    rules => [
                        {
                            id                 => 'rust_format',
                            changed_path_globs => ['codex-rs/**/*.rs', 'codex-rs/Cargo.toml', 'codex-rs/Cargo.lock'],
                            require_any_patterns => ['\bjust fmt\b', '\bcargo fmt\b'],
                            message            => 'Rust changes ({changed_files_preview}) need `cd codex-rs && just fmt` or `cargo fmt`.',
                        },
                        {
                            id                 => 'core_crate_validation',
                            changed_path_globs => ['codex-rs/core/**'],
                            require_any_patterns => [
                                '\bcargo test -p codex-core --target x86_64-unknown-linux-gnu\b',
                                '\bcargo check -p codex-core --target x86_64-unknown-linux-gnu\b',
                            ],
                            message            => 'Core runtime changes ({changed_files_preview}) need `cargo test -p codex-core --target x86_64-unknown-linux-gnu` or `cargo check -p codex-core --target x86_64-unknown-linux-gnu`.',
                        },
                        {
                            id                 => 'tui_crate_validation',
                            changed_path_globs => ['codex-rs/tui/**', 'codex-rs/tui_app_server/**'],
                            require_any_patterns => [
                                '\bcargo test -p codex-tui --target x86_64-unknown-linux-gnu\b',
                                '\bcargo check -p codex-tui --target x86_64-unknown-linux-gnu\b',
                            ],
                            message            => 'UI changes ({changed_files_preview}) need `cargo test -p codex-tui --target x86_64-unknown-linux-gnu` or `cargo check -p codex-tui --target x86_64-unknown-linux-gnu`.',
                        },
                        {
                            id                 => 'workspace_validation',
                            changed_path_globs => ['codex-rs/**'],
                            require_any_patterns => [
                                '\bcargo check --target x86_64-unknown-linux-gnu\b',
                                '\bcargo test --target x86_64-unknown-linux-gnu\b',
                                '\bcargo test -p codex-core --target x86_64-unknown-linux-gnu\b',
                                '\bcargo test -p codex-tui --target x86_64-unknown-linux-gnu\b',
                            ],
                            message            => 'Workspace Rust changes ({changed_files_preview}) need a deterministic target-scoped cargo validation command with `--target x86_64-unknown-linux-gnu`.',
                        },
                    ],
                },
            },
        ],
    };
}

1;
