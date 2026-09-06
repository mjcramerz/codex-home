# Restoration and deliberate changes

Every original file is back in the live source tree. The correction does not replace the user's custom model/instruction configuration with stock defaults.

## Preserved without semantic replacement

All original root configuration settings are present. Model/provider IDs, model catalogs, inline developer/realtime instructions, all instruction_overrides families, agent registrations, app/plugin configuration, memory settings and TUI/keymaps retain their original values. All 491 original instruction/template/catalog files and the original hook registration JSON are byte-identical. The remaining original content includes the full home documentation/index/plan/workflow/template/snippet/plugin/skill trees, not only a migration archive.

## Deliberate config changes

Removed/deprecated flags and aliases are identified in generate/feature-policy.json. The field multi_agent_v2.usage_hint_enabled is ignored/deprecated according to the supplied schema. The original agents' child_agents_md feature is rejected by that schema and removed. Shell filter arrays are normalized to the canonical map. Network permission domains/sockets use the supplied typed definitions, unsupported admin settings are omitted, and the broker socket is permitted.

The original 13 local MCP entries now use the retained devops Podman broker, preserving their original config IDs. All other registrations remain. The original desktop Node environment is retained. Host Node and Codex path environment conventions are explicit; PATH remains inherited. The full etc config mirrors home. Requirements are explicitly nonrestrictive locally rather than pinning obsolete wrapper identities, omitting desktop MCP IDs, or forcing US residency. These policy changes are not mislabeled as schema deprecations.

## Tooling safeguards

The synchronizer validates the exact schema and updates derived files only. Regression tests prohibit reduction of config, loss of instructions, feature-value drift and loss of original MCP IDs. The installer validates before writing, preserves opaque desktop settings, backs up replaced files, rejects symlink destinations and serializes installations. Hook-schema discovery now finds the shipped schemas without a Codex Rust checkout. The plugin checker works in an extracted archive without git and distinguishes the product-generated marketplace from local source mirrors.

The full main config diff is in home-config.diff. Raw original path checksums are in migration/original-files.json. No original files are deleted.

## Modified original files

Only the following original paths differ from their original bytes; additional new deployment/validation documents are not included in this list:

- `agents/analyst.toml`
- `agents/coder.toml`
- `agents/default.toml`
- `agents/delegator.toml`
- `agents/explorer.toml`
- `agents/hunter.toml`
- `agents/integrator.toml`
- `agents/manager.toml`
- `agents/orchestrator.toml`
- `agents/planner.toml`
- `agents/reviewer.toml`
- `agents/synthesizer.toml`
- `agents/tester.toml`
- `agents/worker.toml`
- `etc/config.toml`
- `etc/requirements.toml`
- `generate/examples/config.home.toml`
- `generate/scripts/config_toml_coverage.py`
- `generate/scripts/plugin_catalog_coverage.py`
- `home/.hooks/modules/Codex/Hook/Schema.pm`
- `home/agents.config.toml`
- `home/config.toml`
- `home/cyber.config.toml`
- `home/debug.config.toml`
- `home/default.config.toml`
- `home/fast.config.toml`
- `home/maximus.config.toml`
- `home/review.config.toml`
- `home/spark.config.toml`
- `home/test.config.toml`

The exhaustive schema example is a reference, not an installable preset. Historical compatibility schema entries and original migration baselines remain as evidence; they are not automatically activated.
