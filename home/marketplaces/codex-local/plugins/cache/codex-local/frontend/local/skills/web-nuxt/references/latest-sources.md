---
title: web-nuxt reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nuxt
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-25'
---
# web-nuxt reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: official Nuxt/Nitro docs plus latest stable release snapshot.

## Version snapshot (captured 2026-02-25)
- Nuxt: `v4.3.1` (released 2026-02-07).

## High-priority guidance deltas
- Prefer explicit `routeRules` (`prerender`, `swr`, `isr`, `ssr`) per route family.
- Enforce strict private/public boundaries in `runtimeConfig`.
- Use keyed `useAsyncData`/`useFetch` patterns and bounded retries/timeouts for external I/O.

## Skill purpose
Build Nuxt apps with explicit runtime configuration and rendering/data-loading strategies.

## Local references in this folder
- `implementation-playbook.md`
- `runtime-and-data-patterns.md`
- `quality-gates.md`

## External references
- [Nuxt docs](https://nuxt.com/docs/getting-started/introduction)
- [Nuxt performance and route rules](https://nuxt.com/docs/guide/best-practices/performance)
- [Nuxt runtime config guide](https://nuxt.com/docs/guide/going-further/runtime-config)
- [Nitro docs](https://nitro.unjs.io/)
- [Nuxt release v4.3.1](https://github.com/nuxt/nuxt/releases/tag/v4.3.1)
