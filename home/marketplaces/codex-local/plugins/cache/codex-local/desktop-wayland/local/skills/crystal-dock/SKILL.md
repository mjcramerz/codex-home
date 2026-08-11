---
name: crystal-dock
description: Coordinate Crystal Dock startup, restart, and PID-file behavior with explicit session ownership and bounded stop or retry handling. Use when the user asks about Crystal Dock launchers, restart helpers, PID files, or Labwc dock integration.
metadata:
  version: '1.0'
  short-description: Dock startup, restart, and PID-file handling
  tags:
  - crystal-dock
  - wayland
  - desktop
  - dock
interface:
  display-name: Crystal Dock
  short-description: Dock startup, restart, and PID-file handling
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCA8'
  default-prompt: Act as the "Crystal Dock" specialist for "Dock startup, restart, and PID-file handling". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- editing Crystal Dock launch, stop, or restart helpers
- reviewing PID-file ownership, duplicate-process prevention, or bounded shutdown timing
- checking how the dock integrates with Labwc autostart or user session helpers

## Workflow
1) Confirm the dock command source, PID-file path, and session owner before editing.
2) Keep launch, stop, and restart helpers deterministic with explicit timeout handling.
3) Avoid privileged restart helpers; prefer user-owned commands or systemd user units where possible.
4) Validate dock startup and restart behavior with the narrowest reproducible smoke checks available.

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
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/crystal-dock/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/crystal-dock/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/crystal-dock.md
- $CODEX_HOME/docs/desktop/crystal-dock.md
- $CODEX_HOME/docs/desktop/labwc.md
- $CODEX_HOME/index/domains/desktop/crystal-dock.md
