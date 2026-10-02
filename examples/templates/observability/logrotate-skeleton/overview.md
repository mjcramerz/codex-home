# logrotate skeleton (overview)

Use this template when you need logrotate skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal logrotate config for an application log.

## Outputs

- `app.logrotate`: example rotation policy

## Usage

1. Copy to `/etc/logrotate.d/<app>`.
2. Dry run: `logrotate -d /etc/logrotate.d/<app>`.
3. Validate ownership/permissions.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/observability/logrotate.md`
- `$CODEX_HOME/docs/workflows/logrotate.md`
