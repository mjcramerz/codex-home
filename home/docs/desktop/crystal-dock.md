# Crystal Dock
Purpose: guide Crystal Dock startup, restart, and session ownership behavior for the Codex coding agent.

## Use this guide when
- editing Crystal Dock launch or restart helpers
- reviewing PID-file handling, duplicate-process prevention, or restart timing
- checking how the dock integrates with Labwc autostart or user session helpers

## Baseline
- Keep dock launch, restart, and stop behavior deterministic and user-owned.
- Prefer explicit PID tracking and bounded stop or restart timeouts over blind kill-and-restart loops.
- Keep dock-specific helpers separate from general compositor or bar startup logic.
- Document whether the dock command is a direct executable or a wrapper and keep shell exposure minimal.

## Validation ladder
1. Verify the dock command source and PID-file location.
2. Check restart or stop behavior and timeout handling.
3. Run the narrowest dock restart or autostart smoke check that proves the changed behavior.
4. Recheck related session docs when dock ownership or launch sequencing changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/crystal-dock.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/docs/desktop/labwc.md`
- `$CODEX_HOME/index/domains/desktop/crystal-dock.md`
