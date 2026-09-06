---
title: backend-axum reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- backend-axum
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-20'
---
# backend-axum reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Axum API production patterns: routing, extractors, typed errors, tracing, timeouts, and secure defaults.

## SKILL.md coverage checklist
- Use this skill when
- Defaults
- Testing
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/backend/1.0.0/skills/backend-axum/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/backend/1.0.0/skills/backend-axum/agents/openai.yaml`

## External references
- [Axum crate docs](https://docs.rs/axum/latest/axum/) - Router, extractor, and middleware behavior.
- [Tokio runtime docs](https://docs.rs/tokio/latest/tokio/) - Async runtime behavior and task orchestration.

## Proof-of-concept prompts
- Build a minimum viable runbook for `backend-axum` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `backend-axum` before finalizing changes.

