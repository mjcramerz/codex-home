# Debian preseed template (overview)

Use this template when you need debian preseed template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Unattended installer baseline for Debian with split seeds and staged helper boundaries.

## Outputs

- `preseed.cfg`: top‑level preseed (includes other files)
- `preseed/`: split seed files (account/network/apt/partman/packages or equivalent)
- `scripts/post-install.sh`: optional post-install hook referenced by `preseed/finish.preseed.cfg`

## Usage

1. Replace `__SEED_BASE__` (URL), `__DISK__`, and `__SHA512_HASH__`.
2. Customize seed files in `preseed/` and keep destructive storage, network, and class-selection logic explicit.
3. Host the directory and boot with:
   `auto=true priority=critical preseed/url=__SEED_BASE__/preseed.cfg`
4. Validate in a VM before using on real hardware.

## Password hash

Example:

```
openssl passwd -6
```

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/index/domains/system/debian-preseed.md`
- `$CODEX_HOME/docs/workflows/debian-preseed.md`
- `$CODEX_HOME/docs/virtualization/debian-preseed.md`
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- Read the `os-debian-preseed` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/snippets/virtualization/preseed_boot_params.txt`
