# Wofi
Purpose: guide Wofi launcher configuration and safe command invocation for the Codex coding agent.

## Use this guide when
- editing Wofi config, styling, or launcher mode
- reviewing how launchers map to desktop entries or helper wrappers
- checking command safety for app or admin-action launch flows

## Baseline
- Prefer desktop entries or dedicated wrappers over inline shell command strings.
- Keep launcher mode, search behavior, and style config explicit and reviewable.
- Avoid privileged actions directly in launcher commands; call a dedicated helper with clear policy instead.
- Document any coupling to Labwc keybindings or session-specific environment exports.

## Validation ladder
1. Verify launcher mode and desktop entry source.
2. Check command invocation safety and quoting boundaries.
3. Run the narrowest launcher smoke check that proves the changed behavior.
4. Recheck session docs when keybinding or wrapper assumptions move.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/wofi.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/index/domains/desktop/wofi.md`
