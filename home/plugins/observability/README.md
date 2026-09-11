# Observability task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [obs-elasticsearch](skills/obs-elasticsearch/SKILL.md) | Configure Elasticsearch clusters with secure access controls, retention boundaries, and operational safety defaults |
| [obs-kibana](skills/obs-kibana/SKILL.md) | Configure Kibana spaces, roles, and dashboards with safe authorization and observability defaults |
| [obs-logstash](skills/obs-logstash/SKILL.md) | Design Logstash ingestion and transformation pipelines with strict input validation and controlled outputs |
| [sentry](skills/sentry/SKILL.md) | Use when the user asks to inspect Sentry issues or events, summarize recent production errors, or pull basic Sentry health data via the Sentry API; perform read-only queries with the bundled script and require `SENTRY_AUTH_TOKEN`. |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
