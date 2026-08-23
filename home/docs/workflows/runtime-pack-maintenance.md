# Runtime-pack maintenance workflow
Purpose: maintain the runtime-home pack, instruction system, routing tree, skill
catalog, templates, snippets, and plugin metadata with installed-path coherence
for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

You must start with `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md` before executing this workflow.

## Scope
- `$CODEX_HOME/**`
- `$CODEX_HOME/.agents/skills/**`
- `$CODEX_HOME/plugins/cache/**`
- `$CODEX_HOME/.agents/plugins/marketplace.json`
- routing metadata under `$CODEX_HOME/index/manifest.yml`
- managed instruction sources, fallback `.models` assets, and generated config
  examples when the selected configuration or catalog contract requires them

## Execution flow
1. Route through the pack hubs and select one concrete entrypoint.
2. Classify every affected artifact as authoritative source, required mirror,
   generated reference, or installed runtime output.
3. For instruction or catalog work, read
   `$CODEX_HOME/docs/instruction-system.md` before editing. Never patch an
   installed `/data/codex/usr/**` output.
4. Update the source first, then only the documented fallback mirrors,
   cross-links, workflow/plan entries, and manifest links that the contract
   requires.
5. Keep runtime memory as generated state when the task is memory-related; do
   not add it to source control merely to satisfy a documentation route.
6. Run the narrowest validation matrix for the edited surfaces and record
   blocked runtime checks precisely.

## Required checks
- Verify changed Markdown paths and manifest entrypoints exist.
- Reparse changed JSON, TOML, and YAML data.
- Run `python3 scripts/validate_runtime_pack_assets.py` for routing,
  instruction, architecture, workflow, plan, or manifest changes.
- Run `python3 scripts/validate_model_catalogs.py` for catalog or Code Mode
  profile changes.
- Run `python3 schemas/config_toml_coverage.py --check` after configuration or
  schema changes.
- Run skill/plugin contract tests only when touching their catalogs.

## After that, you must check related files
- `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md`
- `$CODEX_HOME/index/pack/overview.md`
- `$CODEX_HOME/docs/architecture.md`
- `$CODEX_HOME/docs/instruction-system.md`
