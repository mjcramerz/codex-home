# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-nethunter-pixel9a.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`
- Scope file and owner contact
- Pixel 9a device baseline and rollback assets

## Scope
- In: scoped Pixel 9a NetHunter kernel porting and root validation.
- Out: device access outside the documented scope, bypass techniques, or unsupported production use.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Read `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md` and linked references.
[ ] Validate scope (`scope_id`, documented `device_id`, allowed operations, expiry).
[ ] Capture preflight baseline and verify host toolchain.
[ ] Execute kernel/installer build steps with deterministic artifact logging.
[ ] Execute controlled root + flash validation sequence on the documented device.
[ ] Run rollback drill and record outcome.
[ ] Publish findings, residual risks, and re-test criteria.

## Testing and validation
- You must run validation steps listed in the workflow and snippets.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- You must record any documented exception, owner, and expiry before proceeding.

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
- Device build/source mismatch causing non-bootable artifacts.
- Missing rollback assets during flash failures.

## Examples

- Example objective: "Port NetHunter kernel support to the documented Pixel 9a lab device."
- Example validation: "Verify boot + root + NetHunter baseline, then execute rollback drill."

## Open questions
- None.
