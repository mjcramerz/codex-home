# Elasticsearch

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to secure, reliable Elasticsearch setups.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Enable security features and TLS where available.
- Restrict network exposure; avoid public endpoints.
- Use index templates and ILM policies for retention.
- Monitor shard counts and disk usage.

## Operations

- Prefer snapshots for backup/restore.
- Limit query complexity and unbounded aggregations.

See also:
- `overview.md`
- `kibana.md`
- `logstash.md`
- `../workflows/elastic-stack.md`
- `$CODEX_HOME/snippets/elastic/elasticsearch.yml`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- Read the `obs-elasticsearch` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/elasticsearch.md`
