# Plan
Purpose: change entrypoints, related links, or index routing while keeping fast catalogs and memory-router paths consistent for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

You must use this plan when changing entrypoints, related links, or index routing.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- Updated manifest entries with consistent metadata.
- Regenerated index artifacts and related blocks.
- Fast catalogs and memory-router links stay aligned with the manifest.

## Scope
- In: `$CODEX_HOME/index/manifest.yml`, `$CODEX_HOME/index/` entrypoints, `$CODEX_HOME/INDEX.md`.
- Out: content changes unrelated to routing.

## Files and entry points
- `$CODEX_HOME/index/manifest.yml`
- `$CODEX_HOME/index/pack/*.md`
- `$CODEX_HOME/index/core/*.md`
- `$CODEX_HOME/index/domains/*/*.md`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/memories/`

## Action items
[ ] Update `$CODEX_HOME/index/manifest.yml` entries and related links.
[ ] Add or adjust entrypoint files under `$CODEX_HOME/index/`.
[ ] Keep `$CODEX_HOME/INDEX.md` and `$CODEX_HOME/memories/` aligned with the touched routes.
[ ] Spot-check key entrypoints for link accuracy.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints
- You must define fast-path and deep validation commands before making changes.
- You must capture expected outcomes and acceptance criteria for each validation step.
- You must re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must confirm migration/backfill or feature-flag sequencing when applicable.
- You must record post-deploy verification owners and evidence.

## Multi-agent handoff
- Coordinator hands off scope, constraints, and stop condition with the target entrypoint.
- Executor reports touched files, commands run, evidence, blockers, and next action.
- Receiving agent acknowledges handoff completeness before continuing execution.

## Risks and edge cases
- Missing related blocks in new entrypoints.
- Invalid canonical/entrypoint paths.

## Examples
- Example objective: "Update a router, entrypoint, or related-link contract in the runtime pack."
- Example validation: "python3 -m unittest tests.test_runtime_pack_docs_contract tests.test_runtime_pack_structure_contract"

## Open questions
- None.
