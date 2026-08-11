# Logstash
Purpose: tell the Codex coding agent how to use `docs/observability/logstash.md` as a runtime-pack surface and when to stop browsing.
Guidance for safe, testable ingestion pipelines.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep pipelines small and composable.
- Avoid unbounded regex/grok patterns on untrusted input.
- You must validate inputs early; add tags for routing.

## Operations
- Version control pipeline configs.
- You must add dead-letter queues where supported.

See also:
- `overview.md`
- `elasticsearch.md`
- `kibana.md`
- `../workflows/elastic-stack.md`
- `$CODEX_HOME/snippets/elastic/logstash.conf`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- You must use skill obs-logstash.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/logstash.md`
