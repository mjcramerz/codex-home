---
title: ci-github-actions-fix reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- ci-github-actions-fix
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-20'
---
# ci-github-actions-fix reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Inspect GitHub PR checks with gh, pull failing GitHub Actions logs, summarize failure context, then create a fix plan and implement after user approval. Use when a user asks to debug or fix failing PR CI/CD checks on GitHub Actions and wants a plan + code changes; for external checks (e.g., Buildkite), only report the details URL and mark them out of scope.

## SKILL.md coverage checklist
- Overview
- Inputs
- Quick start
- Workflow
- Bundled Resources
- `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/ci-github-actions-fix/scripts/inspect_pr_checks.py`
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/ci-github-actions-fix/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/github/local/skills/ci-github-actions-fix/agents/openai.yaml`

## External references
- [Git documentation](https://git-scm.com/doc) - Core git behavior and safe workflows.
- [GitHub Actions docs](https://docs.github.com/actions) - Workflow syntax and security hardening.
- [GitLab CI/CD docs](https://docs.gitlab.com/ci/) - Pipeline orchestration and variables.
- [GitHub CLI manual](https://cli.github.com/manual/) - Check inspection and issue automation tooling.

## Proof-of-concept prompts
- Build a minimum viable runbook for `ci-github-actions-fix` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `ci-github-actions-fix` before finalizing changes.

