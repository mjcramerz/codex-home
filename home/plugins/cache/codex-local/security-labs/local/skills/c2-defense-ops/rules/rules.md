---
title: C2 Defense Ops Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- c2-defense-ops
- rules
- rules-md
- user
- security-labs
updated: '2026-02-20'
---
# C2 Defense Ops Rules

## Required checks
- Follow the workflow in `$CODEX_HOME/plugins/cache/codex-local/security-labs/local/skills/c2-defense-ops/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/cache/codex-local/security-labs/local/skills/c2-defense-ops/scripts/`.
- Use references in `$CODEX_HOME/plugins/cache/codex-local/security-labs/local/skills/c2-defense-ops/references/` for factual guidance.
- Run `$CODEX_HOME/plugins/cache/codex-local/security-labs/local/skills/c2-defense-ops/scripts/c2_scope_guard.py` before replay/validation activity.
- Require allowed target labels, operation class allowlists, and an unexpired scope window.
- Refuse persistence enablement, credential theft, or stealth abuse requests.
