---
title: Web Next.js Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web Next.js Quality Gates

## Mandatory checks
- `npm run lint`
- `npm run typecheck`
- `npm test`
- `npm run build`

## Route security checks
- Server actions and route handlers validate schema, authn, and authz.
- Middleware enforces access policies without leaking sensitive route data.
- No secrets or server-only modules appear in client bundles.

## Caching and data checks
- Route caching policy is explicit and documented.
- Invalidation strategy (`revalidatePath`/`revalidateTag(tag, "max")`) is tested.
- Error and empty states are deterministic under cache misses/timeouts, and dynamic rendering triggers are intentional.

## UX and accessibility checks
- Keyboard and focus behavior survives route transitions.
- Form errors are announced and associated with fields.
- Streaming and suspense fallbacks are meaningful and non-blocking.

## Performance checks
- Bundle delta for changed routes/components.
- Core Web Vitals/Lighthouse spot-check on impacted pages.
- React profiler or flamegraph evidence for rerender-heavy views.
