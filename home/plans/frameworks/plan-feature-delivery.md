# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-feature-delivery.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when implementing a new feature or significant enhancement.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements
- Clear user story or problem statement.
- Acceptance criteria with observable behavior.
- Compatibility and migration expectations (if any).

## Scope
- In: feature behavior, touchpoints, and tests.
- Out: unrelated refactors or platform upgrades.

## Delivery mode
- PoC mode: timebox to validate hypotheses and feasibility with explicit go/no-go criteria.
- Implementation mode: production-ready delivery with complete rollout, rollback, and operational readiness.

## PoC hypothesis and decision gate (required in PoC mode)
- State the hypothesis and why the PoC reduces implementation risk.
- You must record the timebox, budget, and the maximum acceptable scope for the PoC.
- You must define the success thresholds and how evidence will be collected.
- Name the go/no-go owner and the decision date.

## Dependencies and assumptions
- List internal and external dependencies plus an owner for each.
- You must record environment, access, and tooling assumptions that must hold.
- Note approval checkpoints or decision deadlines that can block delivery.

## Success metrics and exit criteria
- You must define business outcomes and user-visible success metrics.
- You must define technical reliability, performance, and operational targets.
- State the go/no-go decision criteria and the approver.

## Files and entry points
- You must record the entrypoints you will inspect first.
- List the files or modules most likely to change.

## Data model / API changes
- Describe the schemas or contracts affected by the feature.
- You must record versioning or compatibility notes.
- If API surfaces change, specify the contract source, normalized error model, and idempotency/retry policy.

## Action items
[ ] Choose delivery mode (PoC vs implementation) and define decision gate.
[ ] Define PoC hypothesis, timebox, evidence plan, and go/no-go owner when PoC mode is selected.
[ ] Confirm requirements, constraints, and non-goals.
[ ] Define measurable success metrics and exit criteria.
[ ] Inventory existing patterns and dependencies.
[ ] Design the minimal change set and interfaces.
[ ] Define API contract/error model/versioning if API or protocol surfaces change.
[ ] Implement core functionality.
[ ] Add or update tests (unit/integration/contract).
[ ] Verify non-functional targets (security/reliability/performance/operability).
[ ] Update `$CODEX_HOME/docs/workflows/` and user-facing notes.
[ ] Validate behavior end-to-end.

## Testing and validation
- List the validation commands from fastest to deepest.
- State the evidence required for PoC go/no-go or implementation launch.

## Rollout / migration
- You must document backward-compatibility strategy, flags, migrations, and rollback steps.
- Name phased rollout owners and post-deploy verification checkpoints.

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
- Call out correctness, security, performance, and rollout risks that still need explicit mitigation.

## Examples
- Example objective: "Add a typed config lock export flow with clear validation and rollback criteria."
- Example validation: "run the smallest syntax, unit, and contract checks that prove the feature delivery change"

## Open questions
- You must record only the open questions that block implementation or rollout.
