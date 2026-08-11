# Terraform workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-terraform.md` before executing this workflow.
Purpose: plan, review, and apply Terraform changes safely for the Codex coding agent.
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
1) **Scope**: modules, environments, backends, credentials.
2) **Init**: `terraform init` with backend config.
3) **Validate**: `fmt`, `validate`, `plan`.
4) **Review**: inspect plan output and policy checks.
5) **Apply**: run `apply` only after approval.
6) **Verify**: confirm state and outputs.

## Safety rules
- Never `apply` without a reviewed plan.
- You must treat state as sensitive; avoid leaking it.
- You must use locks to prevent concurrent applies.

## Security checkpoints
- Pin provider/module versions and verify source trust before planning.
- Protect remote state with encryption, locking, and least-privilege credentials.
- Review plan output for privilege expansion, public exposure, or destructive drift.

## Testing checkpoints
- You must run `terraform fmt -check`, `terraform validate`, and environment-specific `plan`.
- Execute repository policy checks for IaC security if configured.
- You must confirm drift-sensitive resources with refresh/import checks before apply.

## Deployment checkpoints
- You must require approved plan artifacts tied to the exact commit/workspace before apply.
- Apply in smallest safe scope and avoid ad-hoc concurrent runs.
- You must capture apply logs, resulting outputs, and lock/unlock events for auditability.

## Multi-agent handoff
- Coordinator provides workspace/backend context and approval gate owner.
- Executor shares plan summary, apply transcript, and any manual follow-up steps.
- Receiver schedules post-apply drift checks and next review window.
See also:
- `overview.md`
- `../infra/terraform.md`
- `$CODEX_HOME/templates/infra/terraform-module-skeleton/`
- `$CODEX_HOME/snippets/terraform/versions.tf`
- You must use skill `iac-terraform`.
- `$CODEX_HOME/index/pack/workflows.md`
