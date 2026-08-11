# VS Code settings
Purpose: tell the Codex coding agent how to use `docs/vscode/settings.md` as a runtime-pack surface and when to stop browsing.
Guidance for curating stable, secure, and ergonomic `settings.json` defaults.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/vscode/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Where settings live
- User settings: `~/.config/Code/User/settings.json` (platform-specific)
- Workspace settings: `.vscode/settings.json` (project-level)
- Additional user-data layers: machine-scoped under the user data dir when needed

## Recommended defaults
- **Security**: enable workspace trust and verify extension signatures.
- **Hygiene**: trim whitespace, insert final newline, format on save.
- **Consistency**: keep editor and files settings aligned across machines and workspaces.

## Profile propagation
Use `workbench.settings.applyToAllProfiles` to enforce shared defaults for:
- Security and telemetry
- Formatting and whitespace hygiene
- File excludes and watcher excludes
- Terminal defaults and Git UX

## Snippet
- `$CODEX_HOME/snippets/vscode/settings.json`

See also:
- `overview.md`
- `theming.md`
- `$CODEX_HOME/index/domains/vscode/guidance.md`
