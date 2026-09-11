# Nethunter pixel9a plan

Use this plan when you following `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`.

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

- [ ] Read `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md` and linked references.
- [ ] Validate scope (`scope_id`, documented `device_id`, allowed operations, expiry).
- [ ] Capture preflight baseline and verify host toolchain.
- [ ] Execute kernel/installer build steps with deterministic artifact logging.
- [ ] Execute controlled root + flash validation sequence on the documented device.
- [ ] Run rollback drill and record outcome.
- [ ] Publish findings, residual risks, and re-test criteria.

## Testing and validation

- Run validation steps listed in the workflow and snippets.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout/retry limits, and failure behavior for risky operations.
- Record any documented exception, owner, and expiry before proceeding.

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

- Device build/source mismatch causing non-bootable artifacts.
- Missing rollback assets during flash failures.

## Examples

- Example objective: "Port NetHunter kernel support to the documented Pixel 9a lab device."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
