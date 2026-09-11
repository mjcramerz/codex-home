# AIDE skeleton (overview)

Use this template when you need aide skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal AIDE configuration baseline.

## Outputs

- `aide.conf`: starter config

## Usage

1. Copy to `/etc/aide/aide.conf`.
2. Initialize: `aide --init` and move the DB to the live location.
3. Schedule periodic checks.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/observability/aide.md`
- `$CODEX_HOME/docs/workflows/aide.md`
