# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-offsec-defense.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/offsec-defense.md`.

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
[ ] Read `$CODEX_HOME/docs/workflows/offsec-defense.md` and related references.
[ ] Validate documented scope (`scope_id`, targets, allowed operation classes).
[ ] Execute bounded simulation and defense validation tracks inside the documented scope.
[ ] Record evidence, findings, owners, and re-test criteria.
[ ] Re-run targeted validation after remediation updates.

## Testing and validation
- You must run validation steps specified by the workflow and linked references.

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
- Scope drift between documented targets and executed targets.
- Defensive telemetry gaps that hide meaningful simulation outcomes.

## Examples

- Example objective: "Execute the offsec-defense workflow for the current repository scope."
- Example validation: "Run the workflow's fast-path checks first, then the deeper verification commands if the risk profile requires them."

## Open questions
- None.
