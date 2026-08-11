---
title: psql reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- psql
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-03-11'
---
# psql reference bundle

- Last refreshed: 2026-03-11 (UTC)
- Freshness method: local CLI skill review plus primary PostgreSQL documentation.

## Skill purpose
Inspect, query, and maintain PostgreSQL databases safely with the psql CLI.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/psql/SKILL.md`
- `$CODEX_SKILLS/psql/agents/openai.yaml`
- `$CODEX_SKILLS/psql/references/command-catalog.md`

## External references
- [psql documentation](https://www.postgresql.org/docs/current/app-psql.html) - Authoritative flags, variables, and meta-command behavior.
- [EXPLAIN documentation](https://www.postgresql.org/docs/current/sql-explain.html) - Planner and execution analysis guidance.
- [Client runtime settings](https://www.postgresql.org/docs/current/runtime-config-client.html) - Safe timeout and session-level guardrails.

## Proof-of-concept prompts
- Build a minimum viable runbook for `psql` using the checklist above, then validate connection scope, timeout guards, and rollback notes.
- Produce one positive-path and one negative-path scenario aligned to `psql` before finalizing changes.
