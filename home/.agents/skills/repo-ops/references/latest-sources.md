---
title: repo-ops reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- repo-ops
- references
- latest-sources-md
- latest-sources
- common
updated: '2026-03-06'
---
# repo-ops reference bundle

- Last refreshed: 2026-03-06 (UTC)
- Freshness method: local repo policy review plus primary git and CI documentation references.

## Skill purpose
Repo operations workflow safety across git automation, branch promotion, release tagging, patch delivery, and CI helper tooling.

## SKILL.md coverage checklist
- Use this skill when
- Inputs
- Scope and boundaries
- Workflow
- Implementation guidance
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_SKILLS/repo-ops/SKILL.md`
- `$CODEX_SKILLS/repo-ops/agents/openai.yaml`

## External references
- [Git documentation](https://git-scm.com/doc) - Core git behavior and safe workflows.
- [Git push documentation](https://git-scm.com/docs/git-push) - Protected branch and ref update considerations.
- [GitHub Actions docs](https://docs.github.com/actions) - CI workflow orchestration and security hardening.
- [GitLab CI/CD docs](https://docs.gitlab.com/ci/) - Delivery pipeline orchestration and variables.

## Proof-of-concept prompts
- Build a minimum viable runbook for `repo-ops` that covers one read-only audit, one dry-run mutation path, and one rollback note.
- Produce one positive-path and one negative-path validation scenario aligned to `repo-ops` before finalizing changes.
