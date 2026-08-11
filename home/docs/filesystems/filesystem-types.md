# Filesystem types (quick reference)
Purpose: tell the Codex coding agent how to use `docs/filesystems/filesystem-types.md` as a runtime-pack surface and when to stop browsing.
Choose based on workload, platform compatibility, and operational constraints.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/filesystems/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Linux-native
- **ext4**: general-purpose default; easy recovery.
  Create: `mkfs.ext4 -F -L <LABEL> /dev/<partition>`
- **xfs**: excellent for large files; cannot shrink easily.
  Create: `mkfs.xfs -f -L <LABEL> /dev/<partition>`
- **btrfs**: snapshots, subvolumes; more tuning required.
  Create: `mkfs.btrfs -f -L <LABEL> /dev/<partition>`
- **f2fs**: optimized for flash/SSD; use for flash-heavy workloads.
  Create: `mkfs.f2fs -f -l <LABEL> /dev/<partition>`

## Cross-platform/removable
- **exFAT**: good for large removable media; minimal permissions semantics.
  Create: `mkfs.exfat -n <LABEL> /dev/<partition>`
- **FAT32 / vfat**: compatibility (e.g., EFI System Partition).
  Create: `mkfs.vfat -F 32 -n <LABEL> /dev/<partition>`
- **NTFS**: Windows interoperability; not recommended for Linux root.
  Create: `mkfs.ntfs -F -L <LABEL> /dev/<partition>` (or `mkntfs`)

## ZFS (special)
- **zfs**: uses `zpool` + `zfs` commands, not `mkfs`.
  Create: `zpool create <pool> /dev/<partition>` then `zfs create <pool>/<dataset>`

## Mount option guidance
- Default to `defaults,noatime` for most data volumes.
- For removable media, consider `nodev,nosuid,noexec` when appropriate.
- Apply options based on use case; avoid blanket `noexec` for application volumes.

## References
- `overview.md`
- `fstab.md`
- `$CODEX_HOME/index/domains/system/filesystems.md`
