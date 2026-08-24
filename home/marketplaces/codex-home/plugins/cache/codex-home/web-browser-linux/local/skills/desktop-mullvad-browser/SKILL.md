---
name: desktop-mullvad-browser
description: Configure Mullvad Browser safely with privacy-preserving defaults and operational
  guardrails. Use when the user asks for Mullvad Browser installation, configuration, or hardening.
metadata:
  version: '1.0'
  short-description: Configure Mullvad Browser safely
  tags:
  - mullvad
  - browser
  - privacy
interface:
  display-name: DESKTOP-Mullvad Browser
  short-description: Configure Mullvad Browser safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#93CC32'
  default-prompt: Act as the "DESKTOP-Mullvad Browser" specialist for "Configure Mullvad Browser
    safely". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- installing or hardening Mullvad Browser
- configuring profiles and launchers

## Workflow
1) Verify official build
2) Configure profile location
3) Validate launch flags

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
- `$CODEX_HOME/index/domains/desktop/mullvad-browser.md`
- `$CODEX_HOME/docs/desktop/mullvad-browser.md`
