---
title: shell-sh reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- shell-sh
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---

# shell-sh reference bundle

Consult this reference when shell-sh reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Write portable POSIX/BusyBox sh scripts with safe defaults.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_SKILLS/shell-sh/SKILL.md`
- `$CODEX_SKILLS/shell-sh/agents/openai.yaml`

## External references

- [POSIX Shell Command Language](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html) - Portable shell behavior requirements.
- [Dash shell manpage](https://manpages.debian.org/stable/dash/dash.1.en.html) - Portable shell implementation notes.

## Proof-of-concept prompts

- Build a minimum viable runbook for `shell-sh` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `shell-sh` before finalizing changes.
