# Desktop stack overview
Purpose: route minimal Wayland desktop, desktop-entry, and hardened-browser work to the correct guide for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope
- Wayland or Labwc session setup
- greetd/regreet/cage launch surfaces
- desktop-entry integration
- launcher, bar, and dock behavior
- hardened browser guidance

## Quick map
- Wayland stack: `wayland.md`
- Labwc compositor/session helpers: `labwc.md`
- Waybar modules and restart behavior: `waybar.md`
- Wofi launcher behavior: `wofi.md`
- Crystal Dock startup and restart behavior: `crystal-dock.md`
- Desktop entries: `desktop-entries.md`
- Browser stack: `browsers.md`

## You must enforce these guardrails
- Keep configs minimal and versioned.
- Prefer Wayland-native flags and apps.
- Keep privilege boundaries explicit around polkit, launchers, bars, docks, and browser profile handling.
