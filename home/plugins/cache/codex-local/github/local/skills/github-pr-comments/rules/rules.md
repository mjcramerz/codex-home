---
title: GITHUB-PR Comments Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- github-pr-comments
- rules
- rules-md
- admin
updated: '2026-02-20'
---
# GITHUB-PR Comments Rules

## Required checks
- Follow the workflow in `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/github-pr-comments/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/github-pr-comments/scripts/`.
- Use references in `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/github-pr-comments/references/` for factual guidance.
- Run `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/github-pr-comments/scripts/fetch_comments.py` with bounded paging/timeouts before proposing fixes.
- Require user confirmation before posting review responses or mutating PR state.
- Keep comment triage findings mapped to exact file/line references when available.
