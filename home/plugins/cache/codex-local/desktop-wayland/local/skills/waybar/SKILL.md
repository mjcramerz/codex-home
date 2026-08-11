---
name: waybar
description: Configure Waybar modules, styles, and helper scripts with restart-safe behavior and minimal shell exposure. Use when the user asks about Waybar JSON/CSS, custom modules, or bar startup sequencing.
metadata:
  version: '1.0'
  short-description: Status bar modules, scripts, and restart-safe config
  tags:
  - waybar
  - wayland
  - status-bar
interface:
  display-name: Waybar
  short-description: Status bar modules, scripts, and restart-safe config
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCA8'
  default-prompt: Act as the "Waybar" specialist for "Status bar modules, scripts, and restart-safe config". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- editing Waybar JSONC, CSS, or custom module wrappers
- reviewing restart sequencing and duplicate-process prevention in session startup
- checking module helper scripts for shell safety and bounded output

## Workflow
1) Confirm the bar startup path, module set, and whether custom scripts are involved.
2) Keep JSONC config, CSS, and helper scripts separate so regressions stay local.
3) Ensure restart logic does not spawn duplicate bars or leave stale PID files behind.
4) Validate with the narrowest bar startup and module smoke checks that reproduce the changed behavior.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.
- A concise contract summary, the files or jobs touched, and the remaining rollout risks.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/waybar/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/waybar/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/desktop-wayland.md
- $CODEX_HOME/docs/desktop/waybar.md
- $CODEX_HOME/index/domains/desktop/waybar.md
