# QEMU/KVM + libvirt
Purpose: tell the Codex coding agent how to use `docs/virtualization/qemu-kvm-libvirt.md` as a runtime-pack surface and when to stop browsing.
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
- You must prefer qcow2 images for snapshots and space efficiency.
- You must keep base images immutable; clone per-project instances.

## Safety notes
- Avoid enabling broad host-device passthrough unless required and reviewed.
- You must prefer explicit resource limits (CPU, memory, disk).
- You must document any host networking changes (bridges, firewall rules).

See also:
- `overview.md`
- `vagrant-libvirt.md`
- `virsh.md`
- `../workflows/debian-preseed.md`
- `$CODEX_HOME/index/domains/infra/virtualization.md`
