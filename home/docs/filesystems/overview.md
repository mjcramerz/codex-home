# Filesystems overview
Purpose: tell the Codex coding agent how to use `docs/filesystems/overview.md` as a runtime-pack surface and when to stop browsing.
This pack treats filesystem changes as **high-risk** operations. Default to read-only inspection and require
explicit confirmation before destructive steps (partitioning, formatting, fstab edits).


## Contents
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/filesystems/filesystem-types.md` — Filesystem types (quick reference)
- `$CODEX_HOME/docs/filesystems/fstab.md` — fstab guidance
- `$CODEX_HOME/docs/filesystems/partitioning.md` — Partitioning workflow
- `$CODEX_HOME/docs/filesystems/proxmox.md` — Proxmox filesystem guidance
<!-- END:contents -->


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Safety baseline
- Identify targets by stable path (`/dev/disk/by-id/...` or `/dev/disk/by-path/...`), not `/dev/sdX`.
- You must verify current state with `lsblk -f` and `blkid` before planning changes.
- You must require backups for any disk that contains data you care about.
- You must use dry-run / plan outputs first; apply only after explicit user confirmation.

## High-level workflow
1) **Discovery:** list devices, partitions, mountpoints, UUIDs.
2) **Plan:** pick filesystem type, mountpoint, options, and partition scheme.
3) **Partitioning (if needed):** create/adjust GPT/MBR layout.
4) **Format:** create filesystem with explicit label/UUID.
5) **Mount:** mount once manually and validate.
6) **Persist:** add `fstab` entry (UUID-based) or a systemd `.mount` unit.
7) **Verify:** `mount -a` and confirm after reboot.
8) **Rollback plan:** document how to revert (restore fstab backup, remount, etc.).

## References
- `partitioning.md`
- `filesystem-types.md`
- `fstab.md`
- `proxmox.md`
- `../workflows/filesystems.md`
- `../systemd/overview.md`
- `$CODEX_HOME/templates/filesystems/ops-scripts/`
- `$CODEX_HOME/snippets/bash/fs_probe.sh`
- `$CODEX_HOME/snippets/bash/fstab_update.sh`
- `$CODEX_HOME/index/domains/system/filesystems.md`
