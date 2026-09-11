# VS Code theming

Use this guide when the task concerns vs code theming. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to consistent and accessible editor theming.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/vscode/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Recommended approach

- Choose a theme and icon theme that meet contrast requirements.
- Keep UI motion and animations minimal for accessibility.
- Prefer built-in theming over custom CSS/JS injection.

## Customization tips

- Use `editor.tokenColorCustomizations` for code tokens.
- Use `workbench.colorCustomizations` for UI accents.
- Avoid theme drift across machines or workspaces unless intentional.

## Safety note

Custom CSS/JS loaders expand the attack surface; use only when required and
document the enable/disable steps for each update.

See also:
- `overview.md`
- `settings.md`
- `$CODEX_HOME/index/domains/vscode/guidance.md`
