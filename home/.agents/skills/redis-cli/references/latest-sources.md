---
title: redis-cli reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- redis-cli
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-03-11'
---
# redis-cli reference bundle

- Last refreshed: 2026-03-11 (UTC)
- Freshness method: local CLI skill review plus primary Redis documentation.

## Skill purpose
Inspect and operate Redis safely with the redis-cli shell.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/redis-cli/SKILL.md`
- `$CODEX_SKILLS/redis-cli/agents/openai.yaml`
- `$CODEX_SKILLS/redis-cli/references/command-catalog.md`

## External references
- [redis-cli documentation](https://redis.io/docs/latest/develop/tools/cli/) - Connection flags, shell modes, and diagnostics.
- [SCAN command](https://redis.io/docs/latest/commands/scan/) - Incremental keyspace inspection without blocking the instance.
- [TTL command](https://redis.io/docs/latest/commands/ttl/) - Expiration inspection and post-change validation.

## Proof-of-concept prompts
- Build a minimum viable runbook for `redis-cli` using the checklist above, then validate target selection, key-scan bounds, and rollback notes.
- Produce one positive-path and one negative-path scenario aligned to `redis-cli` before finalizing changes.
