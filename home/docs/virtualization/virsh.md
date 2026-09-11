# virsh / libvirt

Use this guide when you change POSIX shell, Bash or zsh scripts and repository automation. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to managing KVM/libvirt with `virsh`.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Use explicit domain XML checked into version control.
- Prefer QCOW2 images for snapshots.
- Restrict host device passthrough.

## Safety

- Avoid destructive operations without confirmation.
- Keep network definitions explicit and documented.

See also:
- `overview.md`
- `qemu-kvm-libvirt.md`
- `$CODEX_HOME/templates/virtualization/virsh-vm-skeleton/`
- `$CODEX_HOME/snippets/virsh/domain.xml`
- Read the `infra-virsh` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/infra/virtualization.md`
- `$CODEX_HOME/index/domains/infra/virsh.md`
