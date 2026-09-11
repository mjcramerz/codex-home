---
title: Perl Rules
status: active
owner: Matthew Cramer
tags:
- skills
- perl
- rules
updated: '2026-06-28'
---

# Perl Rules

Apply the following perl rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/codex-runtime/skills/perl/SKILL.md`.
- Use references in `$CODEX_HOME/plugins/codex-runtime/skills/perl/references/` for factual guidance.
- Keep inputs bounded, secrets out of tracked files, and validation scoped to the touched contract.
