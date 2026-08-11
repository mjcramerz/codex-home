# Wayland / Labwc stack
Purpose: tell the Codex coding agent how to use `docs/desktop/wayland.md` as a runtime-pack surface and when to stop browsing.
Guidance for a lean Wayland desktop with Labwc and companion session services.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/desktop/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Core components
- **labwc**: compositor and session control
- **waybar**: status bar
- **wofi**: launcher
- **kanshi**: output/profile manager
- **swaylock** and optional idle helpers: lock-screen path
- **crystal-dock**: optional dock helper
- **foot** and **kitty**: terminal surfaces often wired into the desktop role
- **greetd + regreet** or **cage**: login/greeter path
- **wlroots utilities** such as `wlr-randr`: output control and diagnostics

## Baseline practices
- Keep configs in `~/.config/` and version them.
- Prefer Wayland flags for browsers/apps (`--ozone-platform=wayland`).
- Use minimal autostart entries; prefer dedicated helpers over long shell scripts.
- Record which component owns restart logic so Waybar, Wofi, docks, and lock helpers do not fight each other.

## Quick map
- Labwc compositor/session policy: `labwc.md`
- Waybar modules and restart behavior: `waybar.md`
- Wofi launcher configuration and command safety: `wofi.md`

## Config locations (typical)
- Labwc: `~/.config/labwc/`
- Waybar: `~/.config/waybar/`
- Kanshi: `~/.config/kanshi/config`
- Swaylock: `~/.config/swaylock/config`
- Wofi: `~/.config/wofi/config`
- Greetd: `/etc/greetd/config.toml`

## Safety notes
- Ensure the greeter runs with minimal privileges.
- Avoid storing secrets in desktop configs.
- Test new configs with a fallback TTY login available.

See also:
- `overview.md`
- `labwc.md`
- `waybar.md`
- `wofi.md`
- `crystal-dock.md`
- `desktop-entries.md`
- `$CODEX_HOME/templates/desktop/wayland-skeleton/`
- `$CODEX_HOME/snippets/desktop/`
- `../workflows/desktop-wayland.md`
- You must use skill `desktop-wayland`.
- `$CODEX_HOME/index/domains/desktop/stack.md`
- `$CODEX_HOME/index/domains/desktop/wayland.md`
