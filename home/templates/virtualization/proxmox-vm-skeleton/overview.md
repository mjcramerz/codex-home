# Proxmox VM skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/virtualization/proxmox-vm-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Notes and placeholders for a repeatable Proxmox VM setup.

## Outputs
- `cloud-init.user-data.yml`
- `cloud-init.meta-data.yml`

## Usage
1) Update hostname and users.
2) Attach cloud-init to VM template.
3) Clone templates for new VMs.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
