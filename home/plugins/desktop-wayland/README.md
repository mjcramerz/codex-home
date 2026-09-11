# Desktop Wayland task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [crystal-dock](skills/crystal-dock/SKILL.md) | Coordinate Crystal Dock startup, restart, and PID-file behavior with explicit session ownership and bounded stop or retry handling |
| [desktop-entries](skills/desktop-entries/SKILL.md) | Create and validate safe .desktop launchers with correct Exec fields, metadata, and desktop integration |
| [desktop-wayland](skills/desktop-wayland/SKILL.md) | Configure a minimal Wayland plus Labwc desktop stack with secure defaults and predictable startup behavior |
| [labwc](skills/labwc/SKILL.md) | Configure Labwc sessions with explicit compositor, autostart, lock, and launcher policy |
| [waybar](skills/waybar/SKILL.md) | Configure Waybar modules, styles, and helper scripts with restart-safe behavior and minimal shell exposure |
| [wofi](skills/wofi/SKILL.md) | Configure Wofi launchers with deterministic search, style, and command invocation rules |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
