# Observability overview

Use this guide when you change logging, metrics, tracing, audit collection or retention. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to building search/log pipelines with the Elastic Stack.

## Contents

<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/observability/aide.md` — AIDE
- `$CODEX_HOME/docs/observability/auditd.md` — auditd
- `$CODEX_HOME/docs/observability/crowdsec.md` — CrowdSec
- `$CODEX_HOME/docs/observability/elasticsearch.md` — Elasticsearch
- `$CODEX_HOME/docs/observability/kibana.md` — Kibana
- `$CODEX_HOME/docs/observability/logrotate.md` — logrotate
- `$CODEX_HOME/docs/observability/logstash.md` — Logstash
<!-- END:contents -->

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Components

- Elasticsearch: storage and search engine
- Logstash: ingestion and transformation
- Kibana: visualization and dashboards
- auditd: kernel audit events
- logrotate: log retention and rotation
- AIDE: file integrity monitoring
- CrowdSec: behavioral detection + remediation

## Safety baseline

- Restrict network exposure; enable auth where possible.
- Define retention policies and index lifecycle management.
- Treat logs as sensitive data; redact at ingestion.

## Quick map

- Elasticsearch: `elasticsearch.md`
- Kibana: `kibana.md`
- Logstash: `logstash.md`
- auditd: `auditd.md`
- logrotate: `logrotate.md`
- AIDE: `aide.md`
- CrowdSec: `crowdsec.md`

See also:
- `../workflows/elastic-stack.md`
- `$CODEX_HOME/templates/observability/elastic-stack-compose/`
- `$CODEX_HOME/index/domains/observability/stack.md`
