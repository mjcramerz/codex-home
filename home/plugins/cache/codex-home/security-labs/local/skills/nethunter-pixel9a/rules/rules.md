---
title: NetHunter Pixel9a Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- nethunter-pixel9a
- rules
- rules-md
- user
- security-labs
updated: '2026-02-20'
---
# NetHunter Pixel9a Rules

## Required checks
- Follow the procedure in `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/nethunter-pixel9a/SKILL.md`.
- Validate scope first with `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/nethunter-pixel9a/scripts/nethunter_scope_guard.py`.
- Use references in `$CODEX_HOME/plugins/cache/codex-home/security-labs/local/skills/nethunter-pixel9a/references/` for factual guidance.
- Require documented owner/device scope with `lab_only=true` and an unexpired scope window.
- Refuse bootloader/FRP/carrier-lock bypass requests outside explicit lab boundaries.
