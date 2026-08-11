---
title: infra-sysctl reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-sysctl
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-sysctl reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Apply sysctl tuning with safety and rollback.

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
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## Context7 coverage
- None

## Web verification targets
- `https://man7.org/linux/man-pages/man8/sysctl.8.html`
- `https://docs.kernel.org/admin-guide/sysctl/index.html`

## External references
- [sysctl(8) man page](https://man7.org/linux/man-pages/man8/sysctl.8.html) - Command behavior for temporary and persistent kernel parameter changes.
- [Kernel sysctl docs](https://docs.kernel.org/admin-guide/sysctl/index.html) - Kernel-owned parameter semantics and category-specific caveats.
- [systemd-sysctl service](https://www.freedesktop.org/software/systemd/man/latest/systemd-sysctl.service.html) - Boot-time application order and drop-in file loading behavior.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-sysctl` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-sysctl` before finalizing changes.
