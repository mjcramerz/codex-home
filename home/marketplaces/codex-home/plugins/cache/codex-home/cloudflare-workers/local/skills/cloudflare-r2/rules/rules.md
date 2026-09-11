---
title: Cloudflare R2 Rules
status: active
owner: Matthew Cramer
tags:
- skills
- cloudflare-r2
- rules
updated: '2026-06-28'
---

# Cloudflare R2 Rules

Apply the following cloudflare r2 rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/cloudflare-workers/skills/cloudflare-r2/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/cloudflare-workers/skills/cloudflare-r2/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
