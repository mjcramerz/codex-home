# Logstash

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to safe, testable ingestion pipelines.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Keep pipelines small and composable.
- Avoid unbounded regex/grok patterns on untrusted input.
- Validate inputs early; add tags for routing.

## Operations

- Version control pipeline configs.
- Add dead-letter queues where supported.

See also:
- `overview.md`
- `elasticsearch.md`
- `kibana.md`
- `../workflows/elastic-stack.md`
- `$CODEX_HOME/snippets/elastic/logstash.conf`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- Read the `obs-logstash` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/logstash.md`
