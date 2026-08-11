# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-code-review.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/code-review.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/code-review.md`

## Scope
- In: steps defined in the `code-review` workflow.
- Out: unrelated workflows or tooling.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Read `$CODEX_HOME/docs/workflows/code-review.md` and related references.
[ ] Collect required inputs and constraints.
[ ] Execute the workflow steps in order.
[ ] Validate outputs and document results.

## Testing and validation
- You must run validation steps specified by the workflow.

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
- Missing prerequisites or environment constraints.
- Workflow steps out of order for current context.

## Examples

- Example objective: "Execute the code-review workflow for the current repository scope."
- Example validation: "Run the workflow's fast-path checks first, then the deeper verification commands if the risk profile requires them."

## Open questions
- None.
