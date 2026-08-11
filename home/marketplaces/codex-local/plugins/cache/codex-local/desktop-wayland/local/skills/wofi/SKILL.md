---
name: wofi
description: Configure Wofi launchers with deterministic search, style, and command invocation rules. Use when the user asks about Wofi themes, launcher entries, or command safety in desktop launch flows.
metadata:
  version: '1.0'
  short-description: Wayland launcher configuration and command safety
  tags:
  - wofi
  - wayland
  - launcher
interface:
  display-name: Wofi
  short-description: Wayland launcher configuration and command safety
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCA8'
  default-prompt: Act as the "Wofi" specialist for "Wayland launcher configuration and command safety". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- editing Wofi config, styling, or launcher mode
- reviewing how launchers map to desktop entries or helper wrappers
- checking command safety for app or admin-action launch flows

## Workflow
1) Confirm launcher mode, desktop entry sources, and expected keybinding integration first.
2) Keep search, style, and command invocation settings explicit and reviewable.
3) Avoid privileged actions directly in launcher commands; call a dedicated helper with clear policy instead.
4) Validate that launcher invocations remain deterministic and non-privileged.

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
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/wofi/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/desktop-wayland/local/skills/wofi/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/desktop-wayland.md
- $CODEX_HOME/docs/desktop/wofi.md
- $CODEX_HOME/index/domains/desktop/wofi.md
