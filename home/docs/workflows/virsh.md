# virsh / KVM workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-virsh.md` before executing this workflow.
Purpose: manage libvirt domains safely with `virsh` for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: domain XML, storage, networks, permissions.
2) **Validate**: `virsh domxml-to-native` or `virt-xml-validate` when available.
3) **Apply**: define and start domains.
4) **Verify**: console access, network, disk attach.

## Safety rules
- Avoid destructive actions without confirmation.
- You must keep XML definitions versioned.

## Security checkpoints
- Restrict libvirt access to approved operators/groups and audit privileged command usage.
- Review domain XML for passthrough or privilege-sensitive options before define/start.
- You must validate network and storage isolation boundaries for each domain.

## Testing checkpoints
- You must validate XML (`virsh define --validate` when available) before live updates.
- Boot and smoke-test console, network, and disk attach/detach behavior.
- Test snapshot/backup restore paths for changed domains.

## Deployment checkpoints
- Apply domain changes in maintenance windows aligned to downtime tolerance.
- Canary one representative VM before bulk XML or pool updates.
- You must keep prior XML and rollback snapshot IDs ready for restore.

## Multi-agent handoff
- Coordinator provides domain list, storage/network constraints, and downtime budget.
- Executor hands off virsh command history, XML diffs, and validation output.
- Receiver monitors host and guest stability during the post-change window.
See also:
- `overview.md`
- `../virtualization/virsh.md`
- `$CODEX_HOME/templates/virtualization/virsh-vm-skeleton/`
- `$CODEX_HOME/snippets/virsh/domain.xml`
- You must use skill `infra-virsh`.
- `$CODEX_HOME/index/pack/workflows.md`
