---
name: obs-logstash
description: Design Logstash ingestion and transformation pipelines with strict input validation and controlled outputs. Use when the user asks for Logstash parser/filter/pipeline work.
metadata:
  version: '1.0'
  short-description: Design Logstash pipelines with safe input validation
  tags:
  - logstash
  - observability
  - pipelines
interface:
  display-name: OBS-Logstash
  short-description: Design Logstash pipelines with safe input validation
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC6B32'
  default-prompt: Act as the "OBS-Logstash" specialist for "Design Logstash pipelines with safe input validation". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# SKILL

## Execute the scoped task

1. Identify producers, consumers, field contracts, retention requirements and sensitive-data boundaries. Preserve compatibility for existing dashboards, alerts and downstream parsers.

2. Use structured events with stable names, severity and correlation identifiers. Redact at the source and ingestion boundary; never log credentials, complete environments or unrestricted request bodies.

3. Bound message size, cardinality, buffering and retries. Define behavior for disk exhaustion or an unavailable collector without silently losing critical failures.

4. Use rotation and retention appropriate to the platform; verify ownership, reopen behavior and archival access. Avoid exposing unauthenticated log or metrics endpoints.

5. Validate representative success, error and redaction paths with existing fixtures. Distinguish configuration validity from actual delivery, searchability and alert behavior.

## Task-specific details and resources

## Use this skill when

- creating or modifying Logstash pipelines

## Workflow

1. Define inputs/filters/outputs.
2. Test on sample data.
3. Validate output mappings.

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
- `$CODEX_HOME/docs/observability/logstash.md`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- `$CODEX_HOME/snippets/elastic/logstash.conf`
