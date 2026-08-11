# Partitioning workflow
Purpose: tell the Codex coding agent how to use `docs/filesystems/partitioning.md` as a runtime-pack surface and when to stop browsing.
Partitioning is destructive. Require explicit user confirmation, double-check the target device, and use stable device paths.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/filesystems/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Preflight checklist
- You must confirm the **exact** target device using `lsblk -f` and `blkid`.
- You must use a stable path (`/dev/disk/by-id/...`) and resolve it to the block device.
- You must verify no partitions are mounted on the target disk.
- Ensure backups exist (or explicitly acknowledge data loss).

## GPT vs MBR
- **GPT**: modern default (UEFI), supports many partitions and large disks.
- **MBR**: previous compatibility only; limited partitions and disk size.

## Tooling
- **Read-only**: `lsblk`, `blkid`, `wipefs -n`, `fdisk -l`
- **Write**: `parted`, `sfdisk`, `fdisk` (use only with confirmation)

## Example (single-partition disk)
This is a *pattern*, not a command to run blindly:
1) Create a GPT label.
2) Create one partition covering the disk.
3) Format the partition.

Use your tooling of choice and verify each step before applying.

## Verification
- Re-scan: `lsblk -f`
- You must verify PARTUUID/UUID with `blkid`
- Mount and test before editing `fstab`

## References
- `overview.md`
- `filesystem-types.md`
- `fstab.md`
- `$CODEX_HOME/index/domains/system/filesystems.md`
