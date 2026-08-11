---
title: Quality Code Review Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- quality-code-review
- rules
- rules-md
- admin
updated: '2026-02-20'
---
# Quality Code Review Rules

## Required checks
- Follow the workflow in `$CODEX_SKILLS/quality-code-review/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_SKILLS/quality-code-review/scripts/`.
- Use references in `$CODEX_SKILLS/quality-code-review/references/` for factual guidance.
- Report findings first, ordered by severity, with file/line references.
- Explicitly call out missing tests, residual risks, and unverified assumptions.
- State clearly when no findings are detected and what coverage gaps remain.
