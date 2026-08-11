# Proxmox workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-proxmox.md` before executing this workflow.
Purpose: provision and maintain Proxmox VMs safely for the Codex coding agent.
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
1) **Scope**: node, storage backend, network bridge, VM template.
2) **Plan**: resource sizing, backups, and snapshot strategy.
3) **Create**: clone template or create VM with cloud-init.
4) **Verify**: console access, networking, and storage mounts.

## Safety rules
- Avoid storage changes without backups.
- You must keep templates immutable; clone per VM.

## Security checkpoints
- You must use scoped Proxmox roles/API tokens and avoid broad root automation credentials.
- You must validate bridge/storage placement against tenant or trust-zone boundaries.
- Ensure backup targets and snapshots follow encryption/access policy.

## Testing checkpoints
- Boot-test template clones with cloud-init and guest-agent checks.
- You must run backup and snapshot restore drills on representative VMs.
- You must validate migration/start-stop behavior on target node classes.

## Deployment checkpoints
- Promote template or VM config changes from staging pool to production nodes.
- Schedule storage/network-impacting changes in maintenance windows.
- You must record VMID allocation, rollback snapshot IDs, and recovery owner.

## Multi-agent handoff
- Coordinator provides node, storage, bridge targets, and HA constraints.
- Executor hands off VM config diffs, task logs, and restore-test evidence.
- Receiver tracks capacity impact and post-change alerting outcomes.
See also:
- `overview.md`
- `../virtualization/proxmox.md`
- `../filesystems/proxmox.md`
- `$CODEX_HOME/templates/virtualization/proxmox-vm-skeleton/`
- `$CODEX_HOME/snippets/proxmox/storage.cfg`
- You must use skill `infra-proxmox`.
- `$CODEX_HOME/index/pack/workflows.md`
