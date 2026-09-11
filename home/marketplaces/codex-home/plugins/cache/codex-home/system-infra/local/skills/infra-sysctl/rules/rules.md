---
title: Infra Sysctl Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-sysctl
- rules
- rules-md
- user
- infra
updated: '2026-02-20'
---

# Infra Sysctl Rules

Apply the following infra sysctl rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/system-infra/skills/infra-sysctl/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/system-infra/skills/infra-sysctl/scripts/`.
- Use references in `$CODEX_HOME/plugins/system-infra/skills/infra-sysctl/references/` for factual guidance.
