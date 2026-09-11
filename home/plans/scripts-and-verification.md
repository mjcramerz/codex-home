# Scripts and verification plan

Use this plan when you modifying pack scripts or verification workflows. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when modifying pack scripts or verification workflows.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Scripts remain deterministic and safe.
- Verification steps are documented and runnable.

## Scope

- Out: unrelated pack changes.

## Files and entry points

- `$CODEX_HOME/docs/workflows/testing.md`

## Action items

- [ ] Update scripts with safe defaults and clear usage.
- [ ] Update documentation or READMEs that reference the scripts.
- [ ] Run the narrowest relevant verification command(s).
- [ ] Confirm output artifacts are updated (if any).

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

- Scripts rely on missing dependencies.
- Validation steps not aligned with current pack structure.

## Examples

- Example objective: "Tighten a verification script and align the referenced docs with its current behavior."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
