---
title: infra-optimizations reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-optimizations
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-optimizations reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Plan host performance/security tuning with measurement and rollback.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Checkpoint gates
- Agent orchestration
- Validation and testing
- Outputs
- Local resources
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-optimizations/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-optimizations/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-optimizations/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `perf-experiment-template.md`
- `risk-register.md`
- `tuning-rollback-matrix.md`

## Context7 coverage
- `/systemd/systemd`

## Web verification targets
- `https://perf.wiki.kernel.org/index.php/Main_Page`
- `https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html`

## External references
- [Linux perf wiki](https://perf.wiki.kernel.org/index.php/Main_Page) - Performance measurement workflow and tooling pointers.
- [Linux perf docs](https://docs.kernel.org/admin-guide/perf/index.html) - Kernel perf event guidance for reproducible host profiling.
- [systemd resource control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html) - CPU, memory, and IO control boundaries for service-level tuning.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-optimizations` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-optimizations` before finalizing changes.
