---
name: obs-kibana
description: Configure Kibana spaces, roles, and dashboards with safe authorization and observability
  defaults. Use when the user asks for Kibana access models or dashboard administration.
metadata:
  version: '1.0'
  short-description: Configure Kibana spaces, roles, and dashboards safely
  tags:
  - kibana
  - observability
  - dashboards
interface:
  display-name: OBS-Kibana
  short-description: Configure Kibana spaces, roles, and dashboards safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC3F'
  default-prompt: Act as the "OBS-Kibana" specialist for "Configure Kibana spaces, roles,
    and dashboards safely". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- configuring Kibana or its access model

## Workflow
1) Define spaces and roles.
2) Validate dashboards and saved objects.

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
- `$CODEX_HOME/docs/workflows/elastic-stack.md`
- `$CODEX_HOME/docs/observability/kibana.md`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- `$CODEX_HOME/snippets/elastic/kibana.yml`
