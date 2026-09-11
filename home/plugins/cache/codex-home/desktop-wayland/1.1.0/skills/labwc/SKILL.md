---
name: labwc
description: Configure Labwc sessions with explicit compositor, autostart, lock, and launcher policy. Use when the user asks about Labwc behavior, config layout, or session helper scripts.
metadata:
  version: '1.0'
  short-description: Labwc compositor, session, and autostart policy
  tags:
  - labwc
  - wayland
  - desktop
interface:
  display-name: Labwc
  short-description: Labwc compositor, session, and autostart policy
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCA8'
  default-prompt: Act as the "Labwc" specialist for "Labwc compositor, session, and autostart policy". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- editing Labwc compositor config, keybindings, or session helpers
- reviewing autostart sequencing for dock, bar, launcher, or greeter helpers
- checking user-session privilege boundaries or fallback TTY behavior

## Workflow
1) Confirm the session ownership model, login path, and fallback TTY before editing.
2) Keep compositor config, autostart, and helper scripts separated by responsibility.
3) Avoid privileged shell hooks in session startup; prefer user-owned helpers and systemd user units where possible.
4) Validate login, output refresh, lock, and autostart flows with the narrowest reproducible session checks.

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
- `$CODEX_HOME/plugins/cache/codex-home/desktop-wayland/1.0.0/skills/labwc/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/desktop-wayland/1.0.0/skills/labwc/scripts/skill_helper.py`

## References
- $CODEX_HOME/docs/workflows/desktop-wayland.md
- $CODEX_HOME/docs/desktop/labwc.md
- $CODEX_HOME/index/domains/desktop/labwc.md
