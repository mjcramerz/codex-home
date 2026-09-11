---
title: Infra Systemd Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-systemd
- rules
- rules-md
- user
- infra
updated: '2026-02-20'
---

# Infra Systemd Rules

Apply the following infra systemd rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/system-infra/skills/infra-systemd/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/system-infra/skills/infra-systemd/scripts/`.
- Use references in `$CODEX_HOME/plugins/system-infra/skills/infra-systemd/references/` for factual guidance.
