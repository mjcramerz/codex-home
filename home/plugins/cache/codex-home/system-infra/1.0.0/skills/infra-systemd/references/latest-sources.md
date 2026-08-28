---
title: infra-systemd reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-systemd
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-systemd reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Design and harden systemd services and timers with safe defaults, validation, and install steps.

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
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-systemd/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-systemd/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-systemd/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## Context7 coverage
- `/systemd/systemd`

## Web verification targets
- `https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html`
- `https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html`

## External references
- [systemd.exec](https://www.freedesktop.org/software/systemd/man/latest/systemd.exec.html) - Sandboxing, process credentials, and filesystem permission controls.
- [systemd.service](https://www.freedesktop.org/software/systemd/man/latest/systemd.service.html) - Service lifecycle semantics and restart behavior.
- [systemd.timer](https://www.freedesktop.org/software/systemd/man/latest/systemd.timer.html) - Scheduling, jitter, and persistence behavior for timer units.
- [systemd-analyze](https://www.freedesktop.org/software/systemd/man/latest/systemd-analyze.html) - Verification and security scoring workflows.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-systemd` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-systemd` before finalizing changes.
