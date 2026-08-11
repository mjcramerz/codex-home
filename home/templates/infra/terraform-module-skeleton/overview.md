# Terraform module skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/infra/terraform-module-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Baseline structure for a reusable Terraform module.

## Outputs
- `main.tf`: module resources
- `variables.tf`: inputs
- `outputs.tf`: outputs
- `versions.tf`: required Terraform/provider versions

## Usage
1) Copy into your repo.
2) Rename module and update `required_providers`.
3) Run `terraform fmt` and `terraform validate`.

## Notes
- You must keep modules small and composable.
- Pin provider versions and commit lockfiles.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
