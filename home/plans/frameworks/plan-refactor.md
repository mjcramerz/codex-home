# Refactor plan

Use this plan when you restructuring code without changing external behavior. Fill in the concrete scope, evidence, ordered actions and completion criteria before executing dependent steps. Keep deployment and new test files out of scope unless the task authorizes them.

Use this plan when restructuring code without changing external behavior.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/frameworks/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Requirements

- Behavior to preserve and invariants to maintain.
- Scope boundaries and success criteria.

## Scope

- In: targeted modules/components.
- Out: feature changes or large rewrites.

## Dependencies and assumptions

- Record test-coverage assumptions and the quality gates that must stay green.
- Record shared-component ownership and review dependencies.

## Success metrics and exit criteria

- Define the regression suite that proves behavior is preserved.
- Define the maintainability improvements expected without creating SLA regressions.

## Files and entry points

- List the modules or services to refactor.
- List the tests that cover the preserved behavior.

## Action items

- [ ] Define invariants and expected behavior.
- [ ] Identify coupling points and safe seams.
- [ ] Plan incremental refactor steps.
- [ ] Apply refactor in small, reviewable chunks.
- [ ] Update or add tests to lock behavior.
- [ ] Validate performance and correctness.

## Testing and validation

- List validation commands from fastest to deepest.

## Rollback strategy

- Describe the revert plan if the refactor introduces regressions.

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

- Call out hidden dependencies, coupling surprises, or performance regressions that could surface.

## Examples

- Example objective: "Refactor the runtime routing layer while preserving every canonical entrypoint."
- Select an existing repository check that exercises the changed contract; do not copy an example command without confirming that its target, dependencies and side effects match this repository.

## Open questions

- Record only the coverage gaps or invariants that are still unclear.
