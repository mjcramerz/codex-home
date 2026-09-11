# Terraform workflow

Use this guide when you change Terraform modules, providers, state or infrastructure plans. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-terraform.md` before executing this workflow.

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

1. **Scope**: modules, environments, backends, credentials.
2. **Init**: `terraform init` with backend config.
3. **Validate**: `fmt`, `validate`, `plan`.
4. **Review**: inspect plan output and policy checks.
5. **Apply**: run `apply` only after approval.
6. **Verify**: confirm state and outputs.

## Safety rules

- Never `apply` without a reviewed plan.
- Treat state as sensitive; avoid leaking it.
- Use locks to prevent concurrent applies.

## Security checkpoints

- Pin provider/module versions and verify source trust before planning.
- Protect remote state with encryption, locking, and least-privilege credentials.
- Review plan output for privilege expansion, public exposure, or destructive drift.

## Testing checkpoints

- Run `terraform fmt -check`, `terraform validate`, and environment-specific `plan`.
- Execute repository policy checks for IaC security if configured.
- Confirm drift-sensitive resources with refresh/import checks before apply.

## Deployment checkpoints

- Require approved plan artifacts tied to the exact commit/workspace before apply.
- Apply in smallest safe scope and avoid ad-hoc concurrent runs.
- Capture apply logs, resulting outputs, and lock/unlock events for auditability.

## Multi-agent handoff

- Coordinator provides workspace/backend context and approval gate owner.
- Executor shares plan summary, apply transcript, and any manual follow-up steps.
- Receiver schedules post-apply drift checks and next review window.
See also:
- `overview.md`
- `../infra/terraform.md`
- `$CODEX_HOME/templates/infra/terraform-module-skeleton/`
- `$CODEX_HOME/snippets/terraform/versions.tf`
- Read the `iac-terraform` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
