---
title: Perf Profiling Rules
status: active
owner: Matthew Cramer
tags:
- skills
- all
- perf-profiling
- rules
- rules-md
- user
- infra
updated: '2026-02-20'
---

# Perf Profiling Rules

Apply the following perf profiling rules guidance to the code or configuration you are changing. Check the stated preconditions and preserve behavior outside the authorized scope.

## Required checks

- Follow the workflow in `$CODEX_HOME/plugins/system-infra/skills/perf-profiling/SKILL.md`.
- Prefer deterministic scripts in `$CODEX_HOME/plugins/system-infra/skills/perf-profiling/scripts/`.
- Use references in `$CODEX_HOME/plugins/system-infra/skills/perf-profiling/references/` for factual guidance.
