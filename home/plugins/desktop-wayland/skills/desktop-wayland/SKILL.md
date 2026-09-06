---
name: desktop-wayland
description: Configure a minimal Wayland plus Labwc desktop stack with secure defaults and
  predictable startup behavior. Use when the user asks for Wayland/Labwc session setup or
  troubleshooting.
metadata:
  version: '1.0'
  short-description: Configure a minimal Wayland/Labwc desktop stack
  tags:
  - wayland
  - labwc
  - desktop
  - linux
interface:
  display-name: DESKTOP-Wayland
  short-description: Configure a minimal Wayland/Labwc desktop stack
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCA8'
  default-prompt: Act as the "DESKTOP-Wayland" specialist for "Configure a minimal Wayland/Labwc
    desktop stack". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- setting up Labwc sessions
- wiring Waybar, Wofi, Kanshi, swaylock, greetd, Foot, Kitty, or dock helpers
- checking autostart, restart, or fallback TTY behavior for a Wayland desktop stack

## Workflow
1) Define required session components and ownership boundaries.
2) Apply minimal configs for Labwc, Waybar, Wofi, lock/idle, and greeter surfaces.
3) Validate login, launcher, bar, dock, and lock flows with a fallback TTY available.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References
- `$CODEX_HOME/index/domains/desktop/wayland.md`
- `$CODEX_HOME/docs/desktop/labwc.md`
- `$CODEX_HOME/docs/desktop/waybar.md`
- `$CODEX_HOME/docs/desktop/wofi.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/templates/desktop/wayland-skeleton/`
- `$CODEX_HOME/snippets/desktop/`
