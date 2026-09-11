---
title: pack-snippets reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- pack-snippets
- references
- latest-sources-md
- latest-sources
- user
- default
updated: '2026-02-20'
---

# pack-snippets reference bundle

Consult this reference when pack-snippets reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Create or update hardened snippets under $CODEX_HOME/snippets/. Use when adding reusable patterns, updating snippet catalogs, or wiring snippets into docs and indexes.

## SKILL.md coverage checklist

- Use this skill when
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors

- `$CODEX_SKILLS/pack-snippets/SKILL.md`
- `$CODEX_SKILLS/pack-snippets/agents/openai.yaml`

## External references

- [YAML 1.2 specification](https://yaml.org/spec/1.2.2/) - Manifest syntax and deterministic formatting rules.
- [OWASP secure coding practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) - Hardened snippet safety baseline.

## Proof-of-concept prompts

- Build a minimum viable runbook for `pack-snippets` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `pack-snippets` before finalizing changes.
