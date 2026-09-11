# GitOps workflow

Use this guide when the task concerns gitops workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-gitops.md` before executing this workflow.

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

1. Confirm the source-of-truth repo, promotion refs, and reconciliation owner before editing.
2. Separate desired-state generation from apply or reconcile triggers.
3. Keep rollback and previous-good revision handling explicit.
4. Validate branch and environment promotion order before widening rollout.

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

- $CODEX_HOME/docs/infra/gitops.md
- $CODEX_HOME/docs/workflows/gitlab-ci.md
- $CODEX_HOME/index/domains/infra/gitops.md
