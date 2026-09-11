# QEMU/KVM + libvirt

Use this guide when the task concerns qemu/kvm + libvirt. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

This document is a pragmatic reference for working with VMs on Linux using KVM and libvirt.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Key ideas

- KVM provides hardware acceleration for QEMU.
- libvirt manages VM lifecycle, storage, and networking (via `virsh`, virt-manager, etc.).

## Common operations (examples)

- List VMs: `virsh list --all`
- VM details: `virsh dominfo <name>`
- Start/stop: `virsh start <name>` / `virsh shutdown <name>`
- Console: `virsh console <name>` (when configured)

## Networking (high level)

Common libvirt network modes:
- NAT (default): VM has outbound internet access, inbound is restricted unless forwarded.
- Bridged: VM appears on the LAN (higher exposure; requires careful policy).
- Isolated/internal: no internet (useful for hermetic test environments).

Treat network mode changes as security-sensitive.

## Images and storage

- Prefer qcow2 images for snapshots and space efficiency.
- Keep base images immutable; clone per-project instances.

## Safety notes

- Avoid enabling broad host-device passthrough unless required and reviewed.
- Prefer explicit resource limits (CPU, memory, disk).
- Document any host networking changes (bridges, firewall rules).

See also:
- `overview.md`
- `vagrant-libvirt.md`
- `virsh.md`
- `../workflows/debian-preseed.md`
- `$CODEX_HOME/index/domains/infra/virtualization.md`
