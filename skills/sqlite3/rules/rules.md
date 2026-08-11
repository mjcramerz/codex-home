---
title: DB SQLite3 Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- sqlite3
- rules
- rules-md
- user
- default
updated: '2026-03-11'
---
# DB SQLite3 Rules

## Required checks
- Follow the workflow in `$CODEX_SKILLS/sqlite3/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_SKILLS/sqlite3/scripts/`.
- Use references in `$CODEX_SKILLS/sqlite3/references/` for factual guidance.
- Prefer read-only commands first and bound result sizes before inspecting live data.
- Wrap write-oriented SQL in explicit transactions with a documented rollback path.
