---
title: web-sveltekit reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-sveltekit
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-25'
---
# web-sveltekit reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: official Svelte/SvelteKit docs plus latest `@sveltejs/kit` package release snapshot.

## Version snapshot (captured 2026-02-25)
- `@sveltejs/kit`: `2.53.1` (released 2026-02-24).

## High-priority guidance deltas
- Keep secrets and privileged operations in server-only modules (`+page.server`, `+layout.server`, `+server`).
- Use form actions with progressive enhancement (`use:enhance`) while keeping no-JS submissions valid.
- Make redirects/errors explicit and deterministic for navigation flows.

## Skill purpose
Build SvelteKit apps with explicit route/load/action boundaries and secure runtime behavior.

## Local references in this folder
- `implementation-playbook.md`
- `route-load-action-patterns.md`
- `quality-gates.md`

## External references
- [Svelte docs](https://svelte.dev/docs)
- [SvelteKit docs](https://svelte.dev/docs/kit)
- [SvelteKit form actions](https://svelte.dev/docs/kit/form-actions)
- [SvelteKit release `@sveltejs/kit@2.53.1`](https://github.com/sveltejs/kit/releases/tag/%40sveltejs%2Fkit%402.53.1)
