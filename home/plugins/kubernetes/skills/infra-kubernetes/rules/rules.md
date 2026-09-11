---
title: Infra Kubernetes Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-kubernetes
- rules
- rules-md
- user
- infra
updated: '2026-02-20'
---

# Infra Kubernetes Rules

Apply the following infra kubernetes rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/kubernetes/skills/infra-kubernetes/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/kubernetes/skills/infra-kubernetes/scripts/`.
- Use references in `$CODEX_HOME/plugins/kubernetes/skills/infra-kubernetes/references/` for factual guidance.
