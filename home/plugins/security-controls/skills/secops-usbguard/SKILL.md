---
name: secops-usbguard
description: Configure USBGuard device authorization policies and rule sets for USB attack
  surface reduction. Use when the user asks for USB allowlist/denylist policy setup.
metadata:
  version: '1.0'
  short-description: Configure USBGuard rules and policies
  tags:
  - usbguard
  - security
  - linux
  - device-control
interface:
  display-name: SECOPS-USBGuard
  short-description: Configure USBGuard rules and policies
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#82CC32'
  default-prompt: Act as the "SECOPS-USBGuard" specialist for "Configure USBGuard rules and
    policies". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating USB allow/deny policies
- deploying USBGuard safely

## Workflow
1) Audit devices and generate rules
2) Review and tighten rules
3) Enforce and validate

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
- `$CODEX_HOME/index/domains/system/usbguard.md`
- `$CODEX_HOME/docs/system/usbguard.md`
- `$CODEX_HOME/docs/workflows/usbguard.md`
- `$CODEX_HOME/templates/system/usbguard-baseline/`
- `$CODEX_HOME/snippets/system/usbguard.rules`
