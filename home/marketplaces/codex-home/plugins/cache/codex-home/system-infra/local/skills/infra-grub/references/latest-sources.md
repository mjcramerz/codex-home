---
title: infra-grub reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-grub
- references
- latest-sources-md
- latest-sources
- user
- infra
updated: '2026-02-25'
---
# infra-grub reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: `web.search` + `web.open` + Context7 library docs (`resolve-library-id`, `get-library-docs`) on vendor-owned sources.
- Fetch note: `mcp__fetch__fetch` was attempted in this environment and currently fails with `npm install` exit 243; references were validated via `web` + Context7 instead.

## Skill purpose
Safely modify GRUB configuration and kernel parameters.

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
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/infra-grub/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/infra-grub/agents/openai.yaml`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/local/skills/infra-grub/scripts/skill_helper.py`

## Reference files in this directory
- `latest-sources.md`
- `operations-checklist.md`
- `risk-register.md`

## Context7 coverage
- None

## Web verification targets
- `https://www.gnu.org/software/grub/manual/grub/grub.html`
- `https://docs.kernel.org/admin-guide/kernel-parameters.html`

## External references
- [GNU GRUB manual](https://www.gnu.org/software/grub/manual/grub/grub.html) - Authoritative GRUB behavior, commands, and configuration semantics.
- [GRUB project site](https://www.gnu.org/software/grub/) - Release stream and project-maintained guidance.
- [Kernel command line docs](https://docs.kernel.org/admin-guide/kernel-parameters.html) - Parameter effects and safety considerations before boot flag changes.

## Proof-of-concept prompts
- Build a minimum viable runbook for `infra-grub` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `infra-grub` before finalizing changes.
