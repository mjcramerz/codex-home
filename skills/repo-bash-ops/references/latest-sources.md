---
title: repo-bash-ops reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- repo-bash-ops
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# repo-bash-ops reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Repo operations automation in Bash: safe git workflows, CI scripting, release hygiene, and low-risk automation primitives.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/repo-bash-ops/SKILL.md`
- `$CODEX_SKILLS/repo-bash-ops/agents/openai.yaml`

## External references
- [Git documentation](https://git-scm.com/doc) - Core git behavior and safe workflows.
- [GitHub Actions docs](https://docs.github.com/actions) - Workflow syntax and security hardening.
- [GitLab CI/CD docs](https://docs.gitlab.com/ci/) - Pipeline orchestration and variables.
- [Bash strict mode guidance](https://man7.org/linux/man-pages/man1/bash.1.html) - Shell safety behavior for automation scripts.
- [Git push documentation](https://git-scm.com/docs/git-push) - Branch/tag push safety and protected workflow considerations.

## Proof-of-concept prompts
- Build a minimum viable runbook for `repo-bash-ops` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `repo-bash-ops` before finalizing changes.
