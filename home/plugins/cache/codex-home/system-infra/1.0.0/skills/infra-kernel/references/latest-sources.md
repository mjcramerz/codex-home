---
title: infra-kernel reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-kernel
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-kernel reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Plan and validate custom Linux kernel builds.

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
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-kernel/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-kernel/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-kernel/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## Context7 coverage
- None

## Web verification targets
- `https://docs.kernel.org/admin-guide/README.html`
- `https://docs.kernel.org/kbuild/index.html`

## External references
- [Kernel admin guide](https://docs.kernel.org/admin-guide/README.html) - Baseline kernel build/install guidance and admin caveats.
- [Kernel Kbuild docs](https://docs.kernel.org/kbuild/index.html) - Build system behavior, targets, and reproducible build controls.
- [Kernel Kconfig docs](https://docs.kernel.org/kbuild/kconfig-language.html) - Config semantics for deterministic fragment management.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-kernel` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-kernel` before finalizing changes.
