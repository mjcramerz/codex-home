# virsh / KVM workflow

Use this guide when you change POSIX shell, Bash or zsh scripts and repository automation. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-virsh.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: domain XML, storage, networks, permissions.
2. **Validate**: `virsh domxml-to-native` or `virt-xml-validate` when available.
3. **Apply**: define and start domains.
4. **Verify**: console access, network, disk attach.

## Safety rules

- Avoid destructive actions without confirmation.
- Keep XML definitions versioned.

## Security checkpoints

- Restrict libvirt access to approved operators/groups and audit privileged command usage.
- Review domain XML for passthrough or privilege-sensitive options before define/start.
- Validate network and storage isolation boundaries for each domain.

## Testing checkpoints

- Validate XML (`virsh define --validate` when available) before live updates.
- Boot and smoke-test console, network, and disk attach/detach behavior.
- Test snapshot/backup restore paths for changed domains.

## Deployment checkpoints

- Apply domain changes in maintenance windows aligned to downtime tolerance.
- Canary one representative VM before bulk XML or pool updates.
- Keep prior XML and rollback snapshot IDs ready for restore.

## Multi-agent handoff

- Coordinator provides domain list, storage/network constraints, and downtime budget.
- Executor hands off virsh command history, XML diffs, and validation output.
- Receiver monitors host and guest stability during the post-change window.
See also:
- `overview.md`
- `../virtualization/virsh.md`
- `$CODEX_HOME/templates/virtualization/virsh-vm-skeleton/`
- `$CODEX_HOME/snippets/virsh/domain.xml`
- Read the `infra-virsh` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
