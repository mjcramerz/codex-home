---
title: DB Redis CLI Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- redis-cli
- rules
- rules-md
- user
- default
updated: '2026-03-11'
---

# DB Redis CLI Rules

Apply the following db redis cli rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_SKILLS/redis-cli/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_SKILLS/redis-cli/scripts/`.
- Use references in `$CODEX_SKILLS/redis-cli/references/` for factual guidance.
- Use `SCAN` rather than `KEYS *` for non-trivial keyspaces.
- Confirm DB selection and write-risk boundaries before mutating keys.
