# Offsec defense plan

Use this plan when you following `$CODEX_HOME/docs/workflows/offsec-defense.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/offsec-defense.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/offsec-defense.md`
- Scope file and change window details

## Scope

- In: scoped offensive simulation and cyber-defense validation workflow.
- Out: out-of-scope offensive activity or target interaction outside the documented scope.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Read `$CODEX_HOME/docs/workflows/offsec-defense.md` and related references.
- [ ] Validate documented scope (`scope_id`, targets, allowed operation classes).
- [ ] Execute bounded simulation and defense validation tracks inside the documented scope.
- [ ] Record evidence, findings, owners, and re-test criteria.
- [ ] Re-run targeted validation after remediation updates.

## Testing and validation

- Run validation steps specified by the workflow and linked references.

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

- Scope drift between documented targets and executed targets.
- Defensive telemetry gaps that hide meaningful simulation outcomes.

## Examples

- Example objective: "Execute the offsec-defense workflow for the current repository scope."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
