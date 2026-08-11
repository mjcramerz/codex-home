# VS Code theming
Purpose: tell the Codex coding agent how to use `docs/vscode/theming.md` as a runtime-pack surface and when to stop browsing.
Guidance for consistent and accessible editor theming.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/vscode/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Recommended approach
- You must choose a theme and icon theme that meet contrast requirements.
- You must keep UI motion and animations minimal for accessibility.
- You must prefer built-in theming over custom CSS/JS injection.

## Customization tips
- You must use `editor.tokenColorCustomizations` for code tokens.
- You must use `workbench.colorCustomizations` for UI accents.
- Avoid theme drift across machines or workspaces unless intentional.

## Safety note
Custom CSS/JS loaders expand the attack surface; use only when required and
document the enable/disable steps for each update.

See also:
- `overview.md`
- `settings.md`
- `$CODEX_HOME/index/domains/vscode/guidance.md`
