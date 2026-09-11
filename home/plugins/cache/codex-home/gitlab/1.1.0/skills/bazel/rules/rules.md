---
title: Bazel Rules
status: active
owner: Matthew Cramer
tags:
- skills
- bazel
- rules
updated: '2026-06-28'
---

# Bazel Rules

Apply the following bazel rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/gitlab/skills/bazel/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/gitlab/skills/bazel/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
