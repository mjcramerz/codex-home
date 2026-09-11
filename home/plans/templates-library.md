# Templates library plan

Use this plan when you are adding or updating templates. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when adding or updating templates.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Template overviews explain usage and constraints.

## Scope

- In: `$CODEX_HOME/templates/` and related runtime documentation and index entries.
- Out: unrelated pack changes.

## Files and entry points

- `$CODEX_HOME/templates/OVERVIEW.md`
- `$CODEX_HOME/index/pack/templates.md`
- `$CODEX_HOME/docs/templates/overview.md`

## Action items

- [ ] Add or update template directories and overview files.
- [ ] Update `$CODEX_HOME/templates/OVERVIEW.md` with new entries.

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

- Templates missing usage notes.

## Examples

- Example objective: "Update a template family and keep its overview plus linked docs aligned."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
