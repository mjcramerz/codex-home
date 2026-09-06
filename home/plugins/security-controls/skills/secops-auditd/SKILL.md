---
name: secops-auditd
description: Configure auditd rules and log capture policies with safe performance tradeoffs
  and compliance alignment. Use when the user asks for Linux auditing policy design or audit
  event tuning.
metadata:
  version: '1.0'
  short-description: Configure auditd rules and logging safely
  tags:
  - auditd
  - security
  - linux
  - observability
interface:
  display-name: SECOPS-auditd
  short-description: Configure auditd rules and logging safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#6D32CC'
  default-prompt: Act as the "SECOPS-auditd" specialist for "Configure auditd rules and logging
    safely". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- authoring or reviewing auditd rules
- deploying auditd with minimal noise

## Workflow
1) Scope required audit events
2) Draft minimal ruleset
3) Validate and measure event volume
4) Deploy and monitor

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
- `$CODEX_HOME/index/domains/observability/auditd.md`
- `$CODEX_HOME/docs/observability/auditd.md`
- `$CODEX_HOME/docs/workflows/auditd.md`
- `$CODEX_HOME/templates/observability/auditd-rules-skeleton/`
- `$CODEX_HOME/snippets/auditd/audit.rules`
