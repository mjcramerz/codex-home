---
name: obs-elasticsearch
description: Configure Elasticsearch clusters with secure access controls, retention boundaries,
  and operational safety defaults. Use when the user asks for Elasticsearch setup, tuning,
  or hardening.
metadata:
  version: '1.0'
  short-description: Configure Elasticsearch safely with retention and access controls
  tags:
  - elasticsearch
  - observability
  - search
interface:
  display-name: OBS-Elasticsearch
  short-description: Configure Elasticsearch safely with retention and access controls
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3260CC'
  default-prompt: Act as the "OBS-Elasticsearch" specialist for "Configure Elasticsearch safely
    with retention and access controls". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O,
    run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

## Use this skill when
- configuring Elasticsearch clusters or indices

## Workflow
1) Scope access and retention policy.
2) Configure templates and ILM.
3) Verify snapshots and monitoring.

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
- `$CODEX_HOME/docs/observability/elasticsearch.md`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- `$CODEX_HOME/snippets/elastic/elasticsearch.yml`
