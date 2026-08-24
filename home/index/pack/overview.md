# Pack maintenance router
Purpose: choose one pack-maintenance hub for runtime-pack source work for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.
Use this router when maintaining the runtime pack itself: docs, plans, skills,
templates, snippets, rules, instructions, catalogs, config, or plugin metadata.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Required runtime surfaces for pack work
- `$CODEX_HOME/index/manifest.yml` for routing metadata
- `$CODEX_HOME/memories/` when runtime memory already exists for the active workspace
- `$CODEX_HOME/docs/**` for runtime docs and workflows
- `$CODEX_HOME/plans/**` for plan templates
- `$CODEX_HOME/templates/**` for reusable scaffolds
- `$CODEX_HOME/.models/**` plus `/data/codex/usr/instructions/**` for model
  catalogs and instruction assets
- `$CODEX_HOME/.agents/skills/**` for the runtime skill catalog and skill assets
- `$CODEX_HOME/plugins/cache/**` plus `$CODEX_HOME/.agents/plugins/marketplace.json` for plugin bundles and marketplace wiring

## Pack scope
- Pack content stops at docs, plans, templates, skills, rules, snippets,
  routing metadata, and plugins. Runtime memory is generated later by Codex.
- You must keep installed-path references coherent across `$CODEX_HOME/**`, `$CODEX_AGENTS/**`, and `$CODEX_HOME/.agents/skills/**`.
- You must treat `$CODEX_HOME/memories/` and the mirrored memory instruction assets as pack source when the task is memory-related.

## Choose one hub
<!-- BEGIN:contents -->
- `$CODEX_HOME/index/pack/config.md` — Pack configuration (entrypoint)
- `$CODEX_HOME/index/pack/docs.md` — Docs index (entrypoint)
- `$CODEX_HOME/index/pack/plans.md` — Plans (entrypoint)
- `$CODEX_HOME/index/pack/prompts.md` — Prompts maintenance (entrypoint)
- `$CODEX_HOME/index/pack/rules.md` — Execpolicy rules (entrypoint)
- `$CODEX_HOME/index/pack/skills.md` — Skills (entrypoint)
- `$CODEX_HOME/index/pack/snippets.md` — Snippets (entrypoint)
- `$CODEX_HOME/index/pack/style.md` — Style guides (entrypoint)
- `$CODEX_HOME/index/pack/templates.md` — Templates (entrypoint)
- `$CODEX_HOME/index/pack/workflows.md` — Workflows (entrypoint)
<!-- END:contents -->

## Recommended progression
1. Classify the work as configuration, catalogs, docs, plans, or
   another pack surface.
2. Open the matching hub and one workflow/plan when the work is non-trivial.
3. Load only the needed skill and shell guidance.
4. Identify the source, required mirror, generated artifact, and focused
   validator before editing.
