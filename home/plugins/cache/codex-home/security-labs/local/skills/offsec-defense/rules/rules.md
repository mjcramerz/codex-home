---
title: OffSec Defense Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- offsec-defense
- rules
- rules-md
- user
- security-labs
updated: '2026-02-20'
---
# OffSec Defense Rules

## Required checks
- Follow the workflow in `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/scripts/`.
- Use references in `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/references/` for factual guidance.
- Run `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/offsec-defense/scripts/scope_guard.py` before dual-use operations and fail closed on scope errors.
- Require `scope_id`, `lab_only=true`, and an unexpired `expires_utc` window.
- Refuse requests outside documented ownership/scope or requests that enable stealth abuse.
