---
name: iac-terraform
description: Plan, review, and modify Terraform configurations with safe state handling, module
  hygiene, and deterministic workflows. Use when the user asks for Terraform changes, plan
  analysis, or IaC drift fixes.
metadata:
  version: '1.0'
  short-description: Plan and review Terraform changes with safe defaults
  tags:
  - terraform
  - iac
  - infra
  - security
interface:
  display-name: IAC-Terraform
  short-description: Plan and review Terraform changes with safe defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C432CC'
  default-prompt: Act as the "IAC-Terraform" specialist for "Plan and review Terraform changes
    with safe defaults". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating or modifying Terraform modules
- planning safe apply workflows

## Workflow
1) Identify backend/state location and credentials.
2) Run `fmt`, `validate`, and `plan`.
3) Review plan output and risks.
4) Apply only after approval.

## Checkpoint gates
- State safety gate: confirm backend encryption, state locking, workspace selection, and recovery path before planning.
- Planning gate: run `terraform fmt -check -recursive`, `terraform validate`, and `terraform plan -out=tfplan` before any apply.
- Risk gate: inspect plan for replacements/destroys and provider or module drift; do not continue until these are acknowledged.
- Apply gate: apply only the reviewed plan file (`terraform apply tfplan`) with lock timeout and scoped variables.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Static checks: `terraform fmt -check -recursive` and `terraform validate` in the target root/module.
- Plan checks: `terraform plan -detailed-exitcode -out=tfplan` and `terraform show -json tfplan` to surface destructive actions.
- Environment checks: verify required variables and credentials fail early; avoid implicit defaults for region/account/project selection.
- Post-apply checks: run focused smoke validation for created resources (connectivity, IAM bindings, or endpoint health) and capture drift follow-up if skipped.

## Outputs
- Plan summary with add/change/destroy counts and explicit callout of any replacements or destroys.
- Apply runbook with exact init/plan/apply commands, required vars, workspace, and lock behavior.
- State and rollback notes covering backend location, locking strategy, and how to recover from a partial apply.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-terraform/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-terraform/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-terraform/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-terraform/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/iac/local/skills/iac-terraform/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/workflows/terraform.md`
- `$CODEX_HOME/docs/infra/terraform.md`
- `$CODEX_HOME/templates/infra/terraform-module-skeleton/`
- `$CODEX_HOME/snippets/terraform/versions.tf`
