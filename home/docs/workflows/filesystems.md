# Filesystems workflow

Use this guide when the task concerns filesystems workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-filesystems.md` before executing this workflow.

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

1. **Clarify intent**: device(s), target filesystem(s), mountpoints, and OS.
2. **Preflight**: `lsblk -f`, `blkid`, confirm stable device paths.
3. **Plan**: partition scheme (GPT/MBR), FS type, mount options, fstab entry.
4. **Backup**: confirm data backups or explicit wipe approval.
5. **Apply**:
   - Partition (if needed).
   - `mkfs` for the chosen filesystem.
   - Mount and verify.
6. **Persist**:
   - Update `fstab` using UUID.
   - Validate with `mount -a` or `findmnt --verify`.
7. **Document**: record commands and rollback steps.

## Safety rules

- Never run destructive commands without explicit confirmation.
- Require stable device paths (`/dev/disk/by-id/...`).
- Make `fstab` edits idempotent and keep backups.

## Security checkpoints

- Confirm target devices by stable `/dev/disk/by-id` path and expected size before `mkfs`.
- Apply mount options (`nodev`, `nosuid`, `noexec`) based on workload threat model.
- Set mountpoint ownership and mode before exposing the filesystem to services.

## Testing checkpoints

- Run `findmnt --verify` and non-destructive mount checks before any reboot.
- Perform create/read/write/delete smoke tests and permission checks on new mounts.
- Reboot or remount to confirm `fstab` persistence and clean startup behavior.

## Deployment checkpoints

- Roll out one device/filesystem change at a time within a maintenance window.
- Keep partition-table and `fstab` backups for rapid rollback.
- Document restore source and rollback commands before closing the task.

## Multi-agent handoff

- Coordinator provides approved device IDs, filesystem choice, and mount options.
- Executor records partition/mkfs/mount/fstab commands and verification output.
- Receiver confirms dependent services are updated to the new mount layout.

## References

- `overview.md`
- `../filesystems/overview.md`
- `../filesystems/partitioning.md`
- `../filesystems/fstab.md`
- `../filesystems/filesystem-types.md`
- `$CODEX_HOME/templates/filesystems/ops-scripts/`
- `$CODEX_HOME/snippets/bash/fs_probe.sh`
- `$CODEX_HOME/snippets/bash/fstab_update.sh`
- Read the `storage-filesystems` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/filesystems.md`
