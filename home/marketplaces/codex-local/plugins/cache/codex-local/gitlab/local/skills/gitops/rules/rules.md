---
title: GitOps Rules
status: active
owner: Matthew Cramer
tags:
- skills
- gitops
- rules
updated: '2026-06-28'
---
# GitOps Rules

## Required checks
- Follow the workflow in `$CODEX_HOME/plugins/cache/codex-local/gitlab/local/skills/gitops/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/cache/codex-local/gitlab/local/skills/gitops/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
