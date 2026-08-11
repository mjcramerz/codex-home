---
title: sqlite3 reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- sqlite3
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-03-11'
---
# sqlite3 reference bundle

- Last refreshed: 2026-03-11 (UTC)
- Freshness method: local CLI skill review plus primary SQLite documentation.

## Skill purpose
Inspect, query, and maintain SQLite databases safely with the sqlite3 CLI.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/sqlite3/SKILL.md`
- `$CODEX_SKILLS/sqlite3/agents/openai.yaml`
- `$CODEX_SKILLS/sqlite3/references/command-catalog.md`

## External references
- [SQLite Command Line Shell](https://sqlite.org/cli.html) - Authoritative sqlite3 shell flags, dot commands, and import/export behavior.
- [SQLite Pragmas](https://sqlite.org/pragma.html) - Runtime tuning, integrity checks, foreign keys, and journaling controls.
- [EXPLAIN QUERY PLAN](https://sqlite.org/eqp.html) - Query-plan inspection workflow for diagnosing slow statements.

## Proof-of-concept prompts
- Build a minimum viable runbook for `sqlite3` using the checklist above, then validate access mode, integrity checks, and rollback notes.
- Produce one positive-path and one negative-path scenario aligned to `sqlite3` before finalizing changes.
