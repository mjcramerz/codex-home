# virsh / libvirt
Purpose: tell the Codex coding agent how to use `docs/virtualization/virsh.md` as a runtime-pack surface and when to stop browsing.
Guidance for managing KVM/libvirt with `virsh`.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must use explicit domain XML checked into version control.
- You must prefer QCOW2 images for snapshots.
- Restrict host device passthrough.

## Safety
- Avoid destructive operations without confirmation.
- You must keep network definitions explicit and documented.

See also:
- `overview.md`
- `qemu-kvm-libvirt.md`
- `$CODEX_HOME/templates/virtualization/virsh-vm-skeleton/`
- `$CODEX_HOME/snippets/virsh/domain.xml`
- You must use skill infra-virsh.
- `$CODEX_HOME/index/domains/infra/virtualization.md`
- `$CODEX_HOME/index/domains/infra/virsh.md`
