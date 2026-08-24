---
title: github-pr-comments reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- github-pr-comments
- references
- latest-sources-md
- latest-sources
- admin
updated: '2026-02-25'
---
# github-pr-comments reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.

## SKILL.md coverage checklist
- Use this skill when
- Scope boundary
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-home/github/local/skills/github-pr-comments/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-home/github/local/skills/github-pr-comments/agents/openai.yaml`

## External references
- [Git documentation](https://git-scm.com/doc) - Core git behavior and safe workflows.
- [GitHub GraphQL API docs](https://docs.github.com/en/graphql) - PR review thread schema and pagination model.
- [gh pr view](https://cli.github.com/manual/gh_pr_view) - PR metadata discovery for current branch context.
- [gh api](https://cli.github.com/manual/gh_api) - Deterministic API invocation patterns with gh CLI.

## Proof-of-concept prompts
- Build a minimum viable runbook for `github-pr-comments` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `github-pr-comments` before finalizing changes.
