# GitLab Runner workflow

Use this guide when you change Git workflows, repository automation, branches or release operations. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-gitlab-runner.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. Confirm executor type, service account, runner tags, and env-fragment ownership before editing.
2. Keep shared runner storage policy separate from per-role env files and helper docs.
3. Validate rootless container, cache, and build-root assumptions before rollout.
4. Run the narrowest runner smoke or ownership checks that prove the changed contract.

## Safety rules

- Preserve behavior unless the task explicitly changes it.
- Keep secrets, tokens, and machine-specific state out of tracked assets.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout or retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## After that, check related files

- $CODEX_HOME/docs/workflows/gitlab-ci.md
- $CODEX_HOME/docs/system/gitlab-runner.md
- $CODEX_HOME/index/domains/system/gitlab-runner.md
