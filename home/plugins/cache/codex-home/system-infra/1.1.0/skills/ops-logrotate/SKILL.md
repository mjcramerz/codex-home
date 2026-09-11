---
name: ops-logrotate
description: Design logrotate policies for predictable retention, rotation cadence, and service-
  safe log handling. Use when the user asks to configure or troubleshoot Linux log rotation.
metadata:
  version: '1.0'
  short-description: Design logrotate policies with safe defaults
  tags:
  - logrotate
  - logs
  - observability
  - linux
interface:
  display-name: OPS-Logrotate
  short-description: Design logrotate policies with safe defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3235'
  default-prompt: Act as the "OPS-Logrotate" specialist for "Design logrotate policies with
    safe defaults". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- creating log rotation rules
- reviewing retention/compression policies

## Workflow
1) Identify log sources and retention requirements
2) Draft rotation policy
3) Validate with dry‑run
4) Deploy and verify permissions

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
- `$CODEX_HOME/index/domains/observability/logrotate.md`
- `$CODEX_HOME/docs/observability/logrotate.md`
- `$CODEX_HOME/docs/workflows/logrotate.md`
- `$CODEX_HOME/templates/observability/logrotate-skeleton/`
- `$CODEX_HOME/snippets/logrotate/app.logrotate`
