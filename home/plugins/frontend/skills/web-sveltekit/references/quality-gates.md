---
title: Web SvelteKit Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-sveltekit
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web SvelteKit Quality Gates

## Mandatory checks
- `pnpm lint`
- `pnpm check`
- `pnpm test`
- `pnpm build`

## Security checks
- Server routes/actions validate schema and enforce authz.
- Private env vars remain server-only.
- Outbound requests use bounded timeout/retry settings.

## Behavior checks
- Route errors and redirects are deterministic and covered by tests for expected status flows.
- Form actions handle success/validation-error/server-error paths with and without `use:enhance`.
- SSR/prerender mode matches route expectations.

## UX and accessibility checks
- Focus restoration works on navigation and action responses.
- Keyboard flow and semantic structure are intact.
- Form errors are linked to controls and announced appropriately.

## Performance checks
- Avoid duplicated fetches across nested loads.
- Monitor payload size and hydration cost on changed routes.
