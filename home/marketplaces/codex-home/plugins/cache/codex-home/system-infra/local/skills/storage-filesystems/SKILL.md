---
name: storage-filesystems
description: Design safe filesystem provisioning including partitioning, mkfs, mounts, and
  fstab entries with rollback notes. Use when the user asks for disk layout or mount configuration
  changes.
metadata:
  version: '1.0'
  short-description: 'Safe filesystem planning: partitioning, mkfs, mounting, and fstab with
    explicit confirmation and rollback'
  tags:
  - filesystems
  - partitioning
  - fstab
  - disks
  - storage
  - linux
interface:
  display-name: STORAGE-Filesystems
  short-description: 'Safe filesystem planning: partitioning, mkfs, mounting, and fstab with explicit confirmation and rollback'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7032CC'
  default-prompt: 'Act as the "STORAGE-Filesystems" specialist for "Safe filesystem planning: partitioning, mkfs, mounting, and fstab with explicit confirmation and rollback". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and
    bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.'
---

## Use this skill when
- the task involves partitioning or formatting disks
- you need to add or modify `/etc/fstab`
- you must choose a filesystem type (ext4/xfs/btrfs/f2fs/exfat/vfat/ntfs/zfs)

## Safety rules (non-negotiable)
- Never run destructive commands without explicit confirmation.
- Use stable device paths (`/dev/disk/by-id/...`) in commands.
- Require backups or an explicit wipe acknowledgement.

## Workflow
1) **Clarify intent**: OS/distro, device(s), filesystem(s), mountpoints, downtime window.
2) **Preflight**: `lsblk -f`, `blkid`, confirm stable device paths.
3) **Plan**: partition scheme (GPT/MBR), filesystem choice, mount options.
4) **Apply** (only with approval):
   - Partition (if needed).
   - `mkfs` with explicit label.
   - Mount and verify.
5) **Persist**: UUID-based `fstab` entries; validate with `mount -a`.
6) **Rollback**: document how to revert (fstab backup, remount, restore).

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- A safe, step-by-step plan with explicit commands and checks.
- A UUID-based `fstab` entry with sane defaults.
- A rollback checklist.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/storage-filesystems/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/storage-filesystems/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/storage-filesystems/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/storage-filesystems/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/storage-filesystems/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/filesystems/overview.md`
- `$CODEX_HOME/docs/filesystems/partitioning.md`
- `$CODEX_HOME/docs/filesystems/fstab.md`
- `$CODEX_HOME/docs/filesystems/filesystem-types.md`
- `$CODEX_HOME/docs/workflows/filesystems.md`
- `$CODEX_HOME/snippets/bash/fstab_update.sh`
