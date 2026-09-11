# Desktop entry template (overview)

Use this template when you need desktop entry template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal `.desktop` file example.

## Outputs

- `app.desktop`: starter launcher

## Usage

1. Copy to `~/.local/share/applications/`.
2. Run `desktop-file-validate` if available.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/desktop/desktop-entries.md`
- `$CODEX_HOME/docs/workflows/desktop-entries.md`
