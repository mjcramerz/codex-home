---
title: Iac Ansible Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- iac-ansible
- rules
- rules-md
- user
- infra
updated: '2026-02-20'
---

# Iac Ansible Rules

Apply the following iac ansible rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/iac/skills/iac-ansible/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/iac/skills/iac-ansible/scripts/`.
- Use references in `$CODEX_HOME/plugins/iac/skills/iac-ansible/references/` for factual guidance.
