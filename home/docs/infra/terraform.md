# Terraform

Use this guide when you change Terraform modules, providers, state or infrastructure plans. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Terraform guidance for safe, deterministic infrastructure changes.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/infra/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Keep state remote and encrypted; restrict access by least privilege.
- Use `terraform fmt`, `validate`, and `plan` in CI before apply.
- Avoid `local-exec` and `null_resource` unless necessary and reviewed.
- Pin provider versions and commit lockfiles.

## Structure

- Prefer small, composable modules with clear inputs/outputs.
- Keep sensitive values out of logs and plan output.

## Safety

- Require review on `apply`.
- Use `-lock-timeout` and state locking in shared environments.

See also:
- `overview.md`
- `../workflows/terraform.md`
- `$CODEX_HOME/templates/infra/terraform-module-skeleton/`
- `$CODEX_HOME/snippets/terraform/versions.tf`
- `$CODEX_HOME/snippets/terraform/backend_remote.tf`
- Read the `iac-terraform` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/terraform.md`
