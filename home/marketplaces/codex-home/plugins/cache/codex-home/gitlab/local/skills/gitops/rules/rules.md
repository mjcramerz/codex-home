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

Apply the following gitops rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/gitlab/skills/gitops/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/gitlab/skills/gitops/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
