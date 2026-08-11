# Plan
Purpose: tell the Codex coding agent how to use `plans/workflows/workflow-codex-manager.md` as a runtime-pack surface and when to stop browsing.

You must use this plan when following `$CODEX_HOME/docs/workflows/codex-manager.md`.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/plans/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Inputs
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- Current repo scope, constraints, and validation commands

## Scope
- In: work covered by the `codex-manager` workflow.
- Out: unrelated repository changes.

## Action items
[ ] Route to the workflow and confirm the smallest concrete entrypoint.
[ ] Inventory the affected files, repos, and runtime contracts.
[ ] Confirm runtime-home changes remain source-to-target only with no runtime->repo sync.
[ ] Check runtime lifecycle shell-export, backup, and secret-cleanup behavior.
[ ] Verify MCP auth fields match server transport semantics.
[ ] Apply focused updates and keep cross-links in sync.
[ ] Run the narrowest relevant validation and record evidence.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Ensure URL transports are the only MCP servers that declare `bearer_token_env_var`; use `env_vars` for stdio wrappers.
- You must validate input bounds, timeout/retry limits, and failure behavior for risky operations.

## Deployment checkpoints
- Call out whether current shells need a refresh after env-export cleanup.
- You must document rollout order, blast-radius controls, and rollback conditions.
- You must record any required follow-up validation owners.
