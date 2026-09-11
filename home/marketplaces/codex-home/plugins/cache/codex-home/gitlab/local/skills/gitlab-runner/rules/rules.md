---
title: GitLab Runner Rules
status: active
owner: Matthew Cramer
tags:
- skills
- gitlab-runner
- rules
updated: '2026-06-28'
---

# GitLab Runner Rules

Apply the following gitlab runner rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/gitlab/skills/gitlab-runner/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/gitlab/skills/gitlab-runner/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
