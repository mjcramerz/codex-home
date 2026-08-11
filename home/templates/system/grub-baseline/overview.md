# GRUB baseline template (overview)
Purpose: tell the Codex coding agent how to use `templates/system/grub-baseline/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal GRUB defaults example.

## Outputs
- `grub.default`: example `/etc/default/grub` content

## Usage
1) Copy to `/etc/default/grub`.
2) Run `update-grub` or `grub-mkconfig`.
3) Reboot and verify.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/system/grub.md`
- `$CODEX_HOME/docs/workflows/grub.md`
