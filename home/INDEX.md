# Codex Pack Index
Purpose: tell the Codex coding agent which router to open first, which entrypoints are authoritative, and when to stop discovery.

## Navigation
<!-- BEGIN:nav -->
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Required load order
1. You must read `$CODEX_HOME/AGENTS.md` first.
2. You must read `$CODEX_HOME/memories/` only when repo context or prior decisions matter.
3. You must route through `$CODEX_HOME/INDEX.md`.
4. You must open `$CODEX_HOME/index/pack/plans.md` and `$CODEX_HOME/index/pack/workflows.md` before large or cross-cutting work.
5. You must open `$CODEX_HOME/index/pack/skills.md` only after the workflow and plan surfaces are clear.
6. You must follow `$CODEX_HOME/docs/style/shell-runtime.md` before shell-sensitive execution.

## Fast catalogs
- Runtime memory directory: `$CODEX_HOME/memories/` when it already exists
- Documentation hub: `$CODEX_HOME/docs/OVERVIEW.md`
- Workflow hub: `$CODEX_HOME/docs/workflows/overview.md`
- Planning hub: `$CODEX_HOME/plans/OVERVIEW.md`
- Snippet hub: `$CODEX_HOME/snippets/OVERVIEW.md`
- Template hub: `$CODEX_HOME/templates/OVERVIEW.md`
- Prompt catalog: `$CODEX_HOME/docs/create-prompts.md`
- Plugin runtime guide: `$CODEX_HOME/docs/plugins.md`

## You must choose one router
- For workflow-level, cross-cutting, or unclear work, open `$CODEX_HOME/index/core/overview.md`.
- For platform, domain, or tooling-specific work, open `$CODEX_HOME/index/domains/overview.md`.
- For runtime-pack maintenance, routing, docs, prompts, snippets, templates, or rules work, open `$CODEX_HOME/index/pack/overview.md`.
- For language or shell conventions only, open `$CODEX_HOME/index/style/overview.md`.

## High-value entrypoints
- Repo-aware memory routing -> `$CODEX_HOME/memories/`
- Cloudflare R2 work -> `$CODEX_HOME/docs/workflows/cloudflare-r2.md`
- Planning and decomposition -> `$CODEX_HOME/docs/workflows/planning.md`
- Testing and verification -> `$CODEX_HOME/docs/workflows/testing.md`

## Current pack defaults
- You must treat `$CODEX_HOME/index/manifest.yml` as the routing metadata source.
- You must keep top-level routers short and deterministic.
- You must keep multi-agent rules in `$CODEX_HOME/AGENTS.md` and workflow procedure in `$CODEX_HOME/docs/workflows/agent-orchestration.md`.
- You must keep model catalog references aligned with `$CODEX_HOME/.models/default_catalog.json`.

## Stop conditions
- You must open one router.
- You must choose one concrete entrypoint from that router.
- You must stop broad discovery once the next concrete file or command is clear.

This file is aligned with `$CODEX_HOME/index/manifest.yml`.
