# Wayland desktop skeleton (overview)

Use this template when you need wayland desktop skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Minimal configs for a Labwc‑based Wayland session.

## Outputs

- `labwc/rc.xml`
- `waybar/config.jsonc`
- `waybar/style.css`
- `kanshi/config`
- `swaylock/config`
- `wofi/config`
- `greetd/config.toml`
- `regreet.css`

## Usage

1. Copy configs into `~/.config/` (or `/etc/` for greetd).
2. Adjust Labwc keybindings, Waybar modules, Wofi launch commands, and greeter behavior for your system.
3. Test login, launcher, bar, and lock flows with a fallback TTY available.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

Related:
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/docs/desktop/labwc.md`
- `$CODEX_HOME/docs/desktop/waybar.md`
- `$CODEX_HOME/docs/desktop/wofi.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
