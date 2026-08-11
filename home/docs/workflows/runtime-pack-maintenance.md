# Runtime-pack maintenance workflow
Purpose: maintain the runtime-home pack, routing tree, skill catalog, templates, snippets, and plugin metadata with installed-path coherence for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

You must start with `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md` before executing this workflow.

## Scope
- `$CODEX_HOME/**`
- `$CODEX_HOME/.agents/skills/**`
- `$CODEX_HOME/plugins/cache/**`
- `$CODEX_HOME/.agents/plugins/marketplace.json`
- routing metadata under `$CODEX_HOME/index/manifest.yml`

## Execution flow
1) Route through the pack hubs and confirm the smallest entrypoint.
2) Audit whether the requested change affects docs, plans, templates, skills, or routing metadata.
3) Keep scope on stable pack assets: routing, docs, plans, templates, snippets, skills, and plugins. Treat runtime memory as generated state when the task is memory-related.
4) Update cross-links, plan/workflow catalogs, and manifest links in the same change.
5) Run the narrowest contract tests for docs, skills, and manifest shape.

## Required checks
- You must verify changed Markdown paths exist.
- Reparse JSON metadata after edits.
- You must run the runtime-pack docs contract tests when touching routing/docs.
- You must run skill/plugin contract tests when touching skill catalogs.

## After that, you must check related files
- `$CODEX_HOME/plans/workflows/workflow-runtime-pack-maintenance.md`
- `$CODEX_HOME/index/pack/overview.md`
- `$CODEX_HOME/docs/architecture.md`
