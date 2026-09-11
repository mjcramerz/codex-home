# Elastic Stack workflow

Use this guide when the task concerns elastic stack workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-elastic-stack.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: data sources, retention, access controls.
2. **Ingest**: design Logstash pipelines and validate samples.
3. **Store**: define index templates and ILM policies.
4. **Visualize**: create Kibana spaces and dashboards.
5. **Secure**: enable auth/TLS and restrict network exposure.

## Safety rules

- Treat logs as sensitive data.
- Avoid public endpoints without authentication.

## Security checkpoints

- Enable TLS and auth for Elasticsearch, Logstash, Kibana, and all ingest clients.
- Apply role/space isolation and least-privilege service credentials.
- Review pipelines for sensitive-field redaction before indexing.

## Testing checkpoints

- Validate Logstash pipelines with representative samples and mapping conflict checks.
- Test ILM rollover/retention behavior in non-production indices first.
- Verify dashboards and saved searches under restricted user roles.

## Deployment checkpoints

- Apply changes in dependency order and confirm version compatibility at each step.
- Snapshot critical indices or cluster state before template/ILM migrations.
- Track ingest lag, shard health, and auth errors during post-deploy observation.

## Multi-agent handoff

- Coordinator defines data-source priorities, retention policy, and access boundaries.
- Executor hands off pipeline test evidence, template/ILM diffs, and dashboard IDs.
- Receiver owns production monitoring thresholds and follow-up tuning backlog.
See also:
- `overview.md`
- `../observability/overview.md`
- `../observability/elasticsearch.md`
- `../observability/kibana.md`
- `../observability/logstash.md`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- `$CODEX_HOME/index/pack/workflows.md`
