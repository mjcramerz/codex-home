# Docs and workflows plan

Use this plan when you are updating docs, workflows, or doc indexes. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when updating docs, workflows, or doc indexes.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Updated docs with clear ownership and scope.
- No host-specific repository paths in generated documentation or instruction assets.
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

- [ ] Update or add docs under `$CODEX_HOME/docs/` (include overview/README as needed).
- [ ] Keep `$CODEX_HOME/memories/`, workflow catalogs, and cross-links aligned when the memory contract changes.
- [ ] Update `$CODEX_HOME/index/pack/docs.md` related links in the manifest.
- [ ] Remove hardcoded workstation paths and stale routing references in the touched docs.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Capture expected outcomes and acceptance criteria for each validation step.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Confirm migration/backfill or feature-flag sequencing when applicable.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## Risks and edge cases

- Missing documentation for new surfaces.

## Examples

- Example objective: "Refresh runtime docs and workflow links after a routing or contract change."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
