---
title: shell-bash reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- shell-bash
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---
# shell-bash reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Write production-grade Bash: strict mode, safe subprocess usage, portability, robust error handling, and security hardening.

## SKILL.md coverage checklist
- When to use
- Non-negotiables
- Skeleton
- Safe subprocess patterns
- Prefer arrays
- Never interpolate untrusted strings into a shell
- Filesystem safety
- Portability tips (macOS/Linux)
- Testing / validation
- Agent orchestration
- Validation and testing
- Outputs
- References in this pack

## Local implementation anchors
- `$CODEX_SKILLS/shell-bash/SKILL.md`
- `$CODEX_SKILLS/shell-bash/agents/openai.yaml`

## External references
- [GNU Bash manual](https://man7.org/linux/man-pages/man1/bash.1.html) - Bash scripting semantics and safety notes.
- [ShellCheck wiki](https://www.shellcheck.net/wiki/) - Practical bash lint and safety guidance.

## Proof-of-concept prompts
- Build a minimum viable runbook for `shell-bash` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `shell-bash` before finalizing changes.

