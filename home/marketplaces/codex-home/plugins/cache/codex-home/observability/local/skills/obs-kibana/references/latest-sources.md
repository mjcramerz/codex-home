---
title: obs-kibana reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- obs-kibana
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---

# obs-kibana reference bundle

Consult this reference when obs-kibana reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Configure Kibana spaces, roles, and dashboards safely.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_HOME/plugins/observability/skills/obs-kibana/SKILL.md`
- `$CODEX_HOME/plugins/observability/skills/obs-kibana/agents/openai.yaml`

## External references

- [Elastic docs](https://www.elastic.co/docs) - Elasticsearch, Logstash, and Kibana platform docs.
- [Kibana docs](https://www.elastic.co/guide/en/kibana/current/index.html) - Space, role, and dashboard administration.

## Proof-of-concept prompts

- Build a minimum viable runbook for `obs-kibana` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `obs-kibana` before finalizing changes.
