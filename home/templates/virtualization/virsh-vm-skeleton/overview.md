# virsh VM skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/virtualization/virsh-vm-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal libvirt domain template.

## Outputs
- `domain.xml`

## Usage
1) Replace placeholders (name, disk path, memory).
2) Define with `virsh define domain.xml`.
3) Start with `virsh start <name>`.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
