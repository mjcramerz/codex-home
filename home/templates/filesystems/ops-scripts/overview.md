# Filesystem ops scripts (template, overview)

Use this template when you need filesystem ops scripts (template, overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Safe-by-default Bash helpers for partitioning, formatting, mounting, and `fstab` updates.

## Outputs

- `fs_ops.sh`: guarded plan/apply workflow

## Usage

```bash
# Read-only probe
./fs_ops.sh probe

# Plan (no writes)
./fs_ops.sh plan --device /dev/disk/by-id/XYZ --fstype ext4 --mountpoint /data

# Apply (writes). Requires explicit flags:
./fs_ops.sh apply --device /dev/disk/by-id/XYZ --fstype ext4 --mountpoint /data \
  --partition single --danger-erase --write-fstab
```

Notes:
- Requires root for `apply`.
- Defaults to safe, non-destructive behavior.
- Review all commands in `plan` before running `apply`.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/filesystems/overview.md`
- `$CODEX_HOME/docs/filesystems/fstab.md`
- `$CODEX_HOME/snippets/bash/fstab_update.sh`
