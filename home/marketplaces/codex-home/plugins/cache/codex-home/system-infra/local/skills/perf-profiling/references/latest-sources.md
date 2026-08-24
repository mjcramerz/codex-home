---
title: perf-profiling reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- perf-profiling
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---
# perf-profiling reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Performance engineering playbook: profiling, benchmarking, hot path analysis, safe optimizations, and regression guards.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Deliverables
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/perf-profiling/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/perf-profiling/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/perf-profiling/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## External references
- [Brendan Gregg performance resources](https://www.brendangregg.com/overview.html) - Profiling methodologies and troubleshooting workflows.
- [perf tool docs](https://man7.org/linux/man-pages/man1/perf.1.html) - Linux perf tooling reference.

## Proof-of-concept prompts
- Build a minimum viable runbook for `perf-profiling` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `perf-profiling` before finalizing changes.
