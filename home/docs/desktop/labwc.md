# Labwc
Purpose: guide Labwc compositor, keybinding, and autostart behavior for the Codex coding agent.

## Use this guide when
- editing Labwc session config, keybindings, or compositor helpers
- reviewing autostart sequencing for dock, bar, launcher, or lock helpers
- validating session ownership and fallback TTY recovery paths

## Baseline
- Keep compositor config, autostart helpers, and per-user overrides separated by responsibility.
- Prefer user-owned helpers and desktop entries over privileged shell wrappers.
- Record how Labwc starts companion processes such as Waybar, Wofi, Crystal Dock, and terminals.
- Keep a known-good fallback TTY or alternate session while iterating on login or autostart behavior.

## Validation ladder
1. Verify login or session ownership and fallback access.
2. Check keybinding and autostart wiring.
3. Run the narrowest session smoke checks for restart, lock, and output refresh behavior.
4. Recheck companion component docs when their launch contract changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/labwc.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/index/domains/desktop/labwc.md`
