# GRUB baseline template (overview)

Use this template when you need grub baseline template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal GRUB defaults example.

## Outputs

- `grub.default`: example `/etc/default/grub` content

## Usage

1. Copy to `/etc/default/grub`.
2. Run `update-grub` or `grub-mkconfig`.
3. Reboot and verify.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/system/grub.md`
- `$CODEX_HOME/docs/workflows/grub.md`
