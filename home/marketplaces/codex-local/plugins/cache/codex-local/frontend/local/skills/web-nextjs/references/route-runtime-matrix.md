---
title: Next.js Route and Runtime Matrix
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- route-runtime-matrix-md
- route-runtime-matrix
- user
- web
updated: '2026-02-25'
---
# Next.js Route and Runtime Matrix

## Route ownership model
- **Server Component**: default for data-heavy UI and secure server access.
- **Client Component**: interactive islands needing browser APIs or immediate local state.
- **Route handler**: HTTP boundary for API-like interactions; validate inputs and authz.
- **Middleware**: lightweight auth/routing decisions; avoid heavy work.

## Rendering and caching decisions
| Scenario | Preferred mode | Cache strategy | Notes |
| --- | --- | --- | --- |
| Personal dashboard | Dynamic SSR | `no-store` or short revalidate | User-specific data |
| Marketing page | Static/ISR | long `revalidate` | Favor CDN cache |
| Catalog listing | ISR + tag invalidation | `revalidateTag` on writes | Balance freshness and speed |
| Search UI | Dynamic + streamed partials | request scoped | Latency-sensitive |

## Server action checklist
- Validate schema and normalize inputs.
- Re-check authz server-side for every mutation.
- Bound retries/timeouts for outbound calls.
- Return typed error states for deterministic UI rendering.

## Middleware checklist
- Keep logic deterministic and fast.
- Avoid database-heavy work in middleware.
- Add explicit bypass rules for static assets and health checks.
