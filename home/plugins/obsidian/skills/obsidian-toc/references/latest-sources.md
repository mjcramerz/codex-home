---
title: obsidian-toc reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- obsidian-toc
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---

# obsidian-toc reference bundle

Consult this reference when obsidian-toc reference bundle is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose

Generate or update a table of contents for Obsidian Markdown notes. Use when a note needs a consistent TOC or when headings have changed.

## SKILL.md coverage checklist

- Overview
- Workflow
- Agent orchestration
- Validation and testing
- Outputs
- References
- Resources

## Local implementation anchors

- `$CODEX_HOME/plugins/obsidian/skills/obsidian-toc/SKILL.md`
- `$CODEX_HOME/plugins/obsidian/skills/obsidian-toc/agents/openai.yaml`

## External references

- [Obsidian help](https://help.obsidian.md/) - Obsidian Markdown and vault workflow references.
- [Markdown heading syntax](https://www.markdownguide.org/basic-syntax/#headings) - Heading patterns for deterministic TOC generation.

## Proof-of-concept prompts

- Build a minimum viable runbook for `obsidian-toc` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `obsidian-toc` before finalizing changes.
