# Rules library plan

Use this plan when you are updating execpolicy rules or guidance. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when updating execpolicy rules or guidance.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Rules are documented with clear intent and ordering.
- Execpolicy docs and indexes are updated.

## Scope

- In: `$CODEX_HOME/rules/` and related runtime documentation and index entries.
- Out: unrelated pack changes.

## Files and entry points

- `$CODEX_HOME/rules/OVERVIEW.md`
- `$CODEX_HOME/index/pack/rules.md`
- `$CODEX_HOME/index/core/execpolicy.md`
- `$CODEX_HOME/docs/workflows/execpolicy.md`

## Action items

- [ ] Add or update rule files with explicit intent and scope.
- [ ] Update `$CODEX_HOME/rules/OVERVIEW.md` to document ordering and constraints.
- [ ] Update execpolicy docs and index references.

## Testing and validation

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

- Rule ordering conflicts.
- Missing references in docs or index.

## Examples

- Example objective: "Update execpolicy rule guidance after adding a new command family."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
