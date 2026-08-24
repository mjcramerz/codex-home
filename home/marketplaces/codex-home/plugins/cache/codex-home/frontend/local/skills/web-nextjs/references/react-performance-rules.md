---
title: React Performance Rules for Next.js (Adapted)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- react-performance-rules-md
- react-performance-rules
- user
- web
updated: '2026-02-25'
---
# React Performance Rules for Next.js (Adapted)

This guide adapts the React and Next.js rule catalog from:

Use this file to prioritize optimization work by impact.

## Priority 1 - Eliminate waterfalls (critical)
- `async-parallel`: parallelize independent fetches with `Promise.all`.
- `async-defer-await`: create promises early, await only when needed.
- `async-api-routes`: in handlers/actions, start independent work before awaiting.
- `async-suspense-boundaries`: stream slow sections behind Suspense boundaries.

## Priority 2 - Reduce initial bundle cost (critical)
- `bundle-dynamic-imports`: lazy-load heavy client-only components.
- `bundle-barrel-imports`: avoid broad barrel imports in hot paths.
- `bundle-defer-third-party`: load analytics/logging after hydration when possible.
- `bundle-preload`: preload likely-next resources (hover/focus/intent signals).

## Priority 3 - Strengthen server throughput (high)
- `server-cache-react`: use request-scoped dedupe for repeated fetches.
- `server-cache-lru`: introduce bounded cross-request cache only where safe.
- `server-parallel-fetching`: split component boundaries to avoid serialized fetch chains.
- `server-serialization`: minimize large object trees sent to client components.

## Priority 4 - Control client re-render pressure (medium)
- Derive values during render instead of state+effect loops.
- Use functional state updates for stable callbacks.
- Move interaction logic into event handlers when effects are unnecessary.
- Use transitions for non-urgent updates to preserve input responsiveness.

## Audit output format
- Rule applied
- Route/component impacted
- Before/after evidence (timing, bundle, or render count)
- Remaining risk and follow-up
