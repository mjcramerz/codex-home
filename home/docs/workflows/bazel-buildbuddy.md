# Bazel and BuildBuddy workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-bazel-buildbuddy.md` before executing this workflow.
Purpose: guide Bazel workspace and BuildBuddy cache or execution changes without losing hermetic build or remote-service boundaries for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) Confirm Bazel version, workspace root, and whether BuildBuddy is cache-only or full remote execution.
2) Keep toolchains, cache endpoints, and auth inputs pinned and reviewable.
3) Separate fast local validation from remote-execution or shared-cache changes.
4) Run the smallest representative target set that proves the changed cache or execution contract.

## Safety rules
- Preserve behavior unless the task explicitly changes it.
- Keep secrets, tokens, and machine-specific state out of tracked assets.

## Security checkpoints
- You must confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- You must validate input bounds, timeout or retry limits, and failure behavior for risky operations.
- You must record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints
- Define fast-path and deep validation commands before making changes.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints
- Document rollout order, blast-radius controls, and rollback conditions.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff
- Coordinator hands off scope, constraints, and stop condition with the target entrypoint.
- Executor reports touched files, commands run, evidence, blockers, and next action.
- Receiving agent acknowledges handoff completeness before continuing execution.

## After that, you must check related files
- $CODEX_HOME/docs/infra/bazel.md
- $CODEX_HOME/docs/infra/buildbuddy.md
- $CODEX_HOME/index/domains/infra/bazel.md
- $CODEX_HOME/index/domains/infra/buildbuddy.md
