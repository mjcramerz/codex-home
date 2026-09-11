# POSIX sh script skeleton (overview)

Use this template when you need posix sh script skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Template for BusyBox or minimal `/bin/sh` environments.

## Outputs

- `script.sh`: safe POSIX shell skeleton

## Quickstart

1. Copy into your repo.
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
- `$CODEX_HOME/snippets/sh/script_skeleton.sh`
