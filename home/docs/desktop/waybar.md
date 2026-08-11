# Waybar
Purpose: guide Waybar configuration, custom-module safety, and restart behavior for the Codex coding agent.

## Use this guide when
- editing Waybar JSONC, CSS, or custom module helpers
- reviewing bar startup or restart logic inside a Wayland session
- checking module scripts for bounded output and shell safety

## Baseline
- Keep Waybar config, CSS, and helper scripts separate so regressions stay localized.
- Prefer direct argv wrappers or dedicated helper scripts over shell-string module commands.
- Ensure restart logic is idempotent and does not spawn duplicate bars.
- Document any dependency on compositor, notifier, or launcher session state.

## Validation ladder
1. Verify module config, CSS, and startup path.
2. Check custom script inputs, output shape, and timeouts.
3. Run the narrowest session smoke check that confirms one healthy bar instance.
4. Recheck related session docs when restart behavior changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/waybar.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/index/domains/desktop/waybar.md`
