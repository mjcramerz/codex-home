# Plan
Purpose: update docs, workflows, or doc indexes without breaking runtime-pack routing or memory boundaries for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

You must use this plan when updating docs, workflows, or doc indexes.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- Updated docs with clear ownership and scope.
- No host-specific repository paths in user-facing docs or instruction assets.
- Runtime-home docs must reflect one-way source-to-target install behavior.
- Repo-aware memory routing stays explicit and installed-path references stay coherent.

## Scope
- In: `$CODEX_HOME/docs/` and related index entrypoints.
- Out: code changes outside documentation.

## Files and entry points
- `$CODEX_HOME/docs/OVERVIEW.md`
- `$CODEX_HOME/docs/workflows/overview.md`
- `$CODEX_HOME/index/pack/docs.md`
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/memories/`

## Action items
[ ] Update or add docs under `$CODEX_HOME/docs/` (include overview/README as needed).
[ ] Keep `$CODEX_HOME/memories/`, workflow catalogs, and cross-links aligned when the memory contract changes.
[ ] Update `$CODEX_HOME/index/pack/docs.md` related links in the manifest.
[ ] Remove hardcoded workstation paths and stale routing references in the touched docs.

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
- Missing documentation for new surfaces.

## Examples
- Example objective: "Refresh runtime docs and workflow links after a routing or contract change."
- Example validation: "python3 -m unittest tests.test_runtime_pack_docs_contract tests.test_runtime_pack_structure_contract"

## Open questions
- None.
