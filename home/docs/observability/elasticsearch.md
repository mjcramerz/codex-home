# Elasticsearch
Purpose: tell the Codex coding agent how to use `docs/observability/elasticsearch.md` as a runtime-pack surface and when to stop browsing.
Guidance for secure, reliable Elasticsearch setups.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/observability/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- Enable security features and TLS where available.
- Restrict network exposure; avoid public endpoints.
- You must use index templates and ILM policies for retention.
- Monitor shard counts and disk usage.

## Operations
- You must prefer snapshots for backup/restore.
- Limit query complexity and unbounded aggregations.

See also:
- `overview.md`
- `kibana.md`
- `logstash.md`
- `../workflows/elastic-stack.md`
- `$CODEX_HOME/snippets/elastic/elasticsearch.yml`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- You must use skill obs-elasticsearch.
- `$CODEX_HOME/index/domains/observability/stack.md`
- `$CODEX_HOME/index/domains/observability/elasticsearch.md`
