---
title: DB PSQL Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- psql
- rules
- rules-md
- user
- default
updated: '2026-03-11'
---
# DB PSQL Rules

## Required checks
- Follow the workflow in `$CODEX_SKILLS/psql/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_SKILLS/psql/scripts/`.
- Use references in `$CODEX_SKILLS/psql/references/` for factual guidance.
- Prefer `psql -X` and `ON_ERROR_STOP` for non-interactive commands.
- Apply timeouts and transaction boundaries before exploratory writes.
