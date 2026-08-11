---
title: ci-github-actions reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- ci-github-actions
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-20'
---
# ci-github-actions reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Build robust GitHub Actions pipelines with security gates, reproducible builds, minimal permissions, and fast feedback loops.

## SKILL.md coverage checklist
- Use this skill when
- Workflow
- CI design principles
- Useful gates
- GitHub Actions hygiene
- Shared wrapper contract
- Codex source alignment
- Agent orchestration
- Validation and testing
- Outputs
- Examples
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/ci-github-actions/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/ci-github-actions/agents/openai.yaml`

## External references
- [Git documentation](https://git-scm.com/doc) - Core git behavior and safe workflows.
- [GitHub Actions docs](https://docs.github.com/actions) - Workflow syntax and security hardening.
- [GitLab CI/CD docs](https://docs.gitlab.com/ci/) - Pipeline orchestration and variables.
- [Actions workflow syntax](https://docs.github.com/actions/writing-workflows/workflow-syntax-for-github-actions) - Workflow keys and behavior.

## Proof-of-concept prompts
- Build a minimum viable runbook for `ci-github-actions` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `ci-github-actions` before finalizing changes.

