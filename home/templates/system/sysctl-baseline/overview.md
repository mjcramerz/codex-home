# sysctl baseline template (overview)

Use this template when you need sysctl baseline template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal sysctl drop‑in.

## Outputs

- `99-hardening.conf`: example sysctl settings

## Usage

1. Copy to `/etc/sysctl.d/99-hardening.conf`.
2. Apply with `sysctl --system`.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/system/sysctl.md`
- `$CODEX_HOME/docs/workflows/sysctl.md`
