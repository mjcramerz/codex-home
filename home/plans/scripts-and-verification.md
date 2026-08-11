# Plan
Purpose: tell the Codex coding agent how to use `plans/scripts-and-verification.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when modifying pack scripts or verification workflows.


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
[ ] Update scripts with safe defaults and clear usage.
[ ] Update documentation or READMEs that reference the scripts.
[ ] Run the narrowest relevant verification command(s).
[ ] Confirm output artifacts are updated (if any).

## Testing and validation

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
- Scripts rely on missing dependencies.
- Validation steps not aligned with current pack structure.

## Examples

- Example objective: "Tighten a verification script and align the referenced docs with its current behavior."
- Example validation: "python3 -m unittest discover -s tests"

## Open questions
- None.
