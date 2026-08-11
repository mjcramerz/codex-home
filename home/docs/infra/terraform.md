# Terraform
Purpose: tell the Codex coding agent how to use `docs/infra/terraform.md` as a runtime-pack surface and when to stop browsing.
Terraform guidance for safe, deterministic infrastructure changes.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/infra/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep state remote and encrypted; restrict access by least privilege.
- You must use `terraform fmt`, `validate`, and `plan` in CI before apply.
- Avoid `local-exec` and `null_resource` unless necessary and reviewed.
- Pin provider versions and commit lockfiles.

## Structure
- You must prefer small, composable modules with clear inputs/outputs.
- You must keep sensitive values out of logs and plan output.

## Safety
- You must require review on `apply`.
- You must use `-lock-timeout` and state locking in shared environments.

See also:
- `overview.md`
- `../workflows/terraform.md`
- `$CODEX_HOME/templates/infra/terraform-module-skeleton/`
- `$CODEX_HOME/snippets/terraform/versions.tf`
- `$CODEX_HOME/snippets/terraform/backend_remote.tf`
- You must use skill iac-terraform.
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/terraform.md`
