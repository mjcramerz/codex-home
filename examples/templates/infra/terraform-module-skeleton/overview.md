# Terraform module skeleton (overview)

Use this template when you need terraform module skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Baseline structure for a reusable Terraform module.

## Outputs

- `main.tf`: module resources
- `variables.tf`: inputs
- `outputs.tf`: outputs
- `versions.tf`: required Terraform/provider versions

## Usage

1. Copy into your repo.
2. Rename module and update `required_providers`.
3. Run `terraform fmt` and `terraform validate`.

## Notes

- Keep modules small and composable.
- Pin provider versions and commit lockfiles.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
