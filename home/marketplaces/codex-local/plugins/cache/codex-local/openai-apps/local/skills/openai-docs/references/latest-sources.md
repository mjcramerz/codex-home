---
title: openai-docs reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- openai-docs
- references
- latest-sources-md
- latest-sources
- user
- chatgpt
updated: '2026-02-20'
---
# openai-docs reference bundle

- Last refreshed: 2026-02-11 (UTC)
- Freshness method: web.run lookups against primary vendor/project documentation roots.

## Skill purpose
Use when the user asks how to build with OpenAI products or APIs and needs up-to-date official documentation with citations (for example: Codex, Responses API, Chat Completions, Apps SDK, Agents SDK, Realtime, model capabilities or limits); prioritize OpenAI docs MCP tools and restrict any fallback browsing to official OpenAI domains.

## SKILL.md coverage checklist
- Overview
- Quick start
- OpenAI product snapshots
- If MCP server is missing
- Workflow
- Quality rules
- Tooling notes
- Agent orchestration
- Validation and testing
- Outputs
- References

## Local implementation anchors
- `$CODEX_HOME/plugins/cache/codex-local/openai-apps/local/skills/openai-docs/SKILL.md`
- `$CODEX_HOME/plugins/cache/codex-local/openai-apps/local/skills/openai-docs/agents/openai.yaml`

## External references
- [OpenAI docs home](https://developers.openai.com/docs) - Official OpenAI platform documentation.
- [OpenAI API reference](https://developers.openai.com/docs/api-reference) - Endpoints and payload schemas.
- [OpenAI MCP guide](https://developers.openai.com/docs/mcp) - MCP usage in OpenAI ecosystem.

## Proof-of-concept prompts
- Build a minimum viable runbook for `openai-docs` using the checklist above, then validate inputs, timeouts, and rollback notes.
- Produce one positive-path and one negative-path test scenario aligned to `openai-docs` before finalizing changes.

