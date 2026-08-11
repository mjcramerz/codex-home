---
title: Repo Bash Ops Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- repo-bash-ops
- rules
- rules-md
- admin
updated: '2026-02-20'
---
# Repo Bash Ops Rules

## Required checks
- Follow the workflow in `$CODEX_SKILLS/repo-bash-ops/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_SKILLS/repo-bash-ops/scripts/`.
- Use references in `$CODEX_SKILLS/repo-bash-ops/references/` for factual guidance.
- Enforce clean worktree and expected branch namespace before mutating operations.
- Require explicit confirmation for destructive or release-impacting actions.
- Preserve delivery ordering and protected branch/tag controls.
