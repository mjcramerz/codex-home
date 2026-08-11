# Desktop entry template (overview)
Purpose: tell the Codex coding agent how to use `templates/desktop/desktop-entry/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal `.desktop` file example.

## Outputs
- `app.desktop`: starter launcher

## Usage
1) Copy to `~/.local/share/applications/`.
2) Run `desktop-file-validate` if available.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/desktop/desktop-entries.md`
- `$CODEX_HOME/docs/workflows/desktop-entries.md`
