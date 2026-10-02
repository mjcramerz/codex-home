# POSIX sh script template (overview)

Use this template when you need posix sh script template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Use this template for BusyBox or minimal `/bin/sh` environments.

## Outputs

- `script.sh`: safe POSIX shell skeleton

## Usage

1. Copy the directory into your repo.
2. Rename `script.sh` and update `usage` + `main`.
3. Keep dependencies minimal and document them.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/style/sh.md`
- `$CODEX_HOME/snippets/sh/`
