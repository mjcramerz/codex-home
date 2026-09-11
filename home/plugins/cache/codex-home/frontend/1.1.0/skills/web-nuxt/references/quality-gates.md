---
title: Web Nuxt Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nuxt
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web Nuxt Quality Gates

## Mandatory checks
- `pnpm lint`
- `pnpm nuxi typecheck`
- `pnpm test`
- `pnpm build`

## Security checks
- `runtimeConfig` separation (private vs public) is verified.
- Nitro handlers validate input and enforce authz.
- Outbound requests have bounded timeout and retry policy, including `useAsyncData`/`useFetch` callers.

## Rendering checks
- SSR/SSG/prerender behavior matches route requirements and declared `routeRules` (`prerender`, `swr`, `isr`, `ssr`).
- Hydration warnings are addressed or explicitly justified.
- Cache headers and route rules are intentional.

## UX and accessibility checks
- Forms expose labels, help text, and error associations.
- Focus order and keyboard navigation are preserved after route updates.
- Core screens have semantic heading and landmark structure.

## Performance checks
- Payload size and hydration cost tracked for changed routes.
- Heavy client plugins/components are lazy-loaded when possible.
- Image/font loading regressions are reviewed.
