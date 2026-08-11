# Routing guide
Purpose: explain how to choose one router and one entrypoint without opening unnecessary files for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Required context
1. `$CODEX_HOME/AGENTS.md`
2. `$CODEX_HOME/memories/` when it is needed
3. `$CODEX_HOME/INDEX.md`
4. `$CODEX_HOME/index/pack/plans.md` and `$CODEX_HOME/index/pack/workflows.md`
5. `$CODEX_HOME/index/pack/skills.md`
6. `$CODEX_HOME/docs/style/shell-runtime.md` before shell-sensitive execution

## Routing algorithm
1. Decide whether the task is pack, domain, core workflow, or style related.
2. Open exactly one router.
3. Select exactly one entrypoint from that router.
4. Stop broad discovery and follow the entrypoint.

## Router shortcuts
<!-- BEGIN:contents -->
- `$CODEX_HOME/index/core/overview.md` — Core routing (overview)
- `$CODEX_HOME/index/domains/overview.md` — Domains routing (overview)
- `$CODEX_HOME/index/pack/overview.md` — Pack hubs routing (overview)
- `$CODEX_HOME/index/style/overview.md` — Style routing (overview)
<!-- END:contents -->

## You must stop when
- Do not open multiple routers for one task unless the scope actually changes.
- Do not treat overviews as deep reference docs.
- Restart from step 1 if the task changes category.

## Pack-wide guardrails
- `$CODEX_HOME/index/manifest.yml` is the source of truth for routing metadata.
- You must keep rendered entrypoints and the manifest aligned when canonical targets or related links change.
- You must keep routing focused on stable installed entrypoints and treat runtime memory as runtime-generated state instead of a shipped pack entrypoint.
