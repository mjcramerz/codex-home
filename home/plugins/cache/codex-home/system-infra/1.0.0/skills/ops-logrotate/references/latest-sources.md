---
title: ops-logrotate reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- ops-logrotate
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-20'
---
# ops-logrotate reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Design logrotate policies with safe defaults.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/ops-logrotate/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/ops-logrotate/agents/openai.yaml`

## External references
- [Logrotate man page](https://man7.org/linux/man-pages/man8/logrotate.8.html) - Log retention and rotation semantics.
- [logrotate examples](https://github.com/logrotate/logrotate/tree/main/examples) - Reference rotation policies for linux distributions.

## Proof-of-concept prompts
- Build a minimum viable runbook for `ops-logrotate` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `ops-logrotate` before finalizing changes.

