---
name: desktop-browser-hardening
description: Harden desktop browser configurations, profile policies, and privacy/security
  defaults across managed endpoints. Use when the user asks to lock down browser settings
  or deploy browser hardening baselines.
metadata:
  version: '1.0'
  short-description: Harden desktop browsers and profile policies
  tags:
  - browsers
  - desktop
  - security
  - privacy
interface:
  display-name: DESKTOP-Browser Hardening
  short-description: Harden desktop browsers and profile policies
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#7032CC'
  default-prompt: Act as the "DESKTOP-Browser Hardening" specialist for "Harden desktop browsers
    and profile policies". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- selecting and hardening browsers
- creating desktop launchers with safe flags

## Workflow
1) Choose browser and threat model
2) Apply overrides/policies
3) Validate profile permissions and updates

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
- `$CODEX_HOME/index/domains/desktop/browsers.md`
- `$CODEX_HOME/docs/desktop/browsers.md`
- `$CODEX_HOME/docs/workflows/browsers.md`
