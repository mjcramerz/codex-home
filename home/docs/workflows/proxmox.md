# Proxmox workflow

Use this guide when you change Debian packaging, APT configuration, installation or host integration. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-proxmox.md` before executing this workflow.

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

1. **Scope**: node, storage backend, network bridge, VM template.
2. **Plan**: resource sizing, backups, and snapshot strategy.
3. **Create**: clone template or create VM with cloud-init.
4. **Verify**: console access, networking, and storage mounts.

## Safety rules

- Avoid storage changes without backups.
- Keep templates immutable; clone per VM.

## Security checkpoints

- Use scoped Proxmox roles/API tokens and avoid broad root automation credentials.
- Validate bridge/storage placement against tenant or trust-zone boundaries.
- Ensure backup targets and snapshots follow encryption/access policy.

## Testing checkpoints

- Boot-test template clones with cloud-init and guest-agent checks.
- Run backup and snapshot restore drills on representative VMs.
- Validate migration/start-stop behavior on target node classes.

## Deployment checkpoints

- Promote template or VM config changes from staging pool to production nodes.
- Schedule storage/network-impacting changes in maintenance windows.
- Record VMID allocation, rollback snapshot IDs, and recovery owner.

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
- Read the `infra-proxmox` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
