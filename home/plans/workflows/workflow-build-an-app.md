# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-build-an-app.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/build-an-app.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/build-an-app.md`

## Scope
- In: steps defined in the `build-an-app` workflow.
- Out: unrelated workflows or tooling.

- For API/protocol surfaces, define contract versioning, timeout/retry ceilings, and idempotency/error-model expectations.

## Action items
[ ] Read `$CODEX_HOME/docs/workflows/build-an-app.md` and related references.
[ ] Collect required inputs and constraints (stack, deployment target, auth/data boundaries, branch/release policy).
[ ] Confirm branch strategy (`mcr/feature/*` -> `mcr/main` -> `mcr/staging` -> `mcr/release`) and fork-mode mirror policy (`origin/github/mcr/main -> github/mcr/main -> mcr/main`, read-only `github/*`, patch checks on `mcr/main` only).
[ ] Confirm deterministic build/install commands and lockfile/toolchain pinning.
[ ] Confirm repo delivery layout and version script strategy when release automation is in scope (for example `scripts/release/get_version.py` and `scripts/release/bump_version.py` in the target repository).
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

- Example objective: "Execute the build-an-app workflow for the current repository scope."
- Example validation: "Run the workflow's fast-path checks first, then the deeper verification commands if the risk profile requires them."

## Open questions
- None.
