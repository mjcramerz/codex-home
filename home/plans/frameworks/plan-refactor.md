# Plan
Purpose: tell the Codex coding agent how to use `plans/frameworks/plan-refactor.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when restructuring code without changing external behavior.

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
- You must record test-coverage assumptions and the quality gates that must stay green.
- You must record shared-component ownership and review dependencies.

## Success metrics and exit criteria
- You must define the regression suite that proves behavior is preserved.
- You must define the maintainability improvements expected without creating SLA regressions.

## Files and entry points
- List the modules or services to refactor.
- List the tests that cover the preserved behavior.

## Action items
[ ] Define invariants and expected behavior.
[ ] Identify coupling points and safe seams.
[ ] Plan incremental refactor steps.
[ ] Apply refactor in small, reviewable chunks.
[ ] Update or add tests to lock behavior.
[ ] Validate performance and correctness.

## Testing and validation
- List validation commands from fastest to deepest.

## Rollback strategy
- Describe the revert plan if the refactor introduces regressions.

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
- Call out hidden dependencies, coupling surprises, or performance regressions that could surface.

## Examples
- Example objective: "Refactor the runtime routing layer while preserving every canonical entrypoint."
- Example validation: "python3 -m unittest tests.test_runtime_pack_docs_contract tests.test_runtime_pack_structure_contract"

## Open questions
- You must record only the coverage gaps or invariants that are still unclear.
