---
title: Aptly Rules
status: active
owner: Matthew Cramer
tags:
- skills
- aptly
- rules
updated: '2026-06-28'
---

# Aptly Rules

Apply the following aptly rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/system-infra/skills/aptly/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/system-infra/skills/aptly/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
