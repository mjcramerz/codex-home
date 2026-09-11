# Agent orchestration plan

Use this plan when you following `$CODEX_HOME/docs/workflows/agent-orchestration.md`. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when following `$CODEX_HOME/docs/workflows/agent-orchestration.md`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs

- `$CODEX_HOME/docs/workflows/agent-orchestration.md`
- `$CODEX_HOME/AGENTS.md`
- Active task objective, acceptance criteria, and constraints

## Scope

- In: multi-agent decomposition, ownership boundaries, and reconciliation workflow.
- Out: implementation details not needed for coordination design.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items

- [ ] Read `$CODEX_HOME/docs/workflows/agent-orchestration.md` and related references.
- [ ] Read `$CODEX_HOME/AGENTS.md` and pick the coordinator plus execution roles.
- [ ] Decompose work into independent tracks with explicit file ownership.
- [ ] Assign each track a role, entrypoint, stop condition, and verification expectations.
- [ ] Execute tracks and collect structured handoff summaries.
- [ ] Reconcile outputs, resolve overlaps, and produce final verification evidence.

## Testing and validation

- Verify each track includes relevant test/lint/build evidence.
- Run coordinator-level verification covering all touched subsystems.

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

- Overlapping ownership causing conflicting edits.
- Missing handoff details that block final verification.

## Examples

- Example objective: "Split pack-wide refactor into routing, scripts, and skills tracks."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- None.
