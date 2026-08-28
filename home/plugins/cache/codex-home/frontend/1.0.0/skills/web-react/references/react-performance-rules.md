---
title: React Performance Rules (Adapted Catalog)
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-react
- references
- react-performance-rules-md
- react-performance-rules
- user
- web
updated: '2026-02-25'
---
# React Performance Rules (Adapted Catalog)

This catalog adapts the rule set from:

Use this order when triaging performance work.

## 1) Eliminate waterfalls (critical)
- `async-defer-await`
- `async-parallel`
- `async-dependencies`
- `async-api-routes`
- `async-suspense-boundaries`

## 2) Reduce bundle pressure (critical)
- `bundle-barrel-imports`
- `bundle-conditional`
- `bundle-defer-third-party`
- `bundle-dynamic-imports`
- `bundle-preload`

## 3) Optimize server-side boundaries (high)
- `server-auth-actions`
- `server-cache-react`
- `server-cache-lru`
- `server-dedup-props`
- `server-parallel-fetching`
- `server-serialization`
- `server-after-nonblocking`

## 4) Improve client data flow (medium-high)
- `client-swr-dedup`
- `client-event-listeners`
- `client-passive-event-listeners`
- `client-localstorage-schema`

## 5) Reduce rerender churn (medium)
- `rerender-defer-reads`
- `rerender-dependencies`
- `rerender-derived-state`
- `rerender-derived-state-no-effect`
- `rerender-functional-setstate`
- `rerender-lazy-state-init`
- `rerender-memo`
- `rerender-memo-with-default-value`
- `rerender-move-effect-to-event`
- `rerender-simple-expression-in-memo`
- `rerender-transitions`
- `rerender-use-ref-transient-values`

## 6) Improve rendering behavior (medium)
- `rendering-activity`
- `rendering-animate-svg-wrapper`
- `rendering-conditional-render`
- `rendering-content-visibility`
- `rendering-hoist-jsx`
- `rendering-hydration-no-flicker`
- `rendering-hydration-suppress-warning`
- `rendering-svg-precision`
- `rendering-usetransition-loading`

## 7) Apply JS hot-path optimizations (low-medium)
- `js-batch-dom-css`
- `js-cache-function-results`
- `js-cache-property-access`
- `js-cache-storage`
- `js-combine-iterations`
- `js-early-exit`
- `js-hoist-regexp`
- `js-index-maps`
- `js-length-check-first`
- `js-min-max-loop`
- `js-set-map-lookups`
- `js-tosorted-immutable`

## 8) Use advanced patterns selectively (low)
- `advanced-event-handler-refs`
- `advanced-init-once`
- `advanced-use-latest`

## Recommended adoption pattern
1. Fix waterfall and bundle issues first.
2. Address server/client data duplication.
3. Tackle rerender/rendering hotspots with profiler evidence.
4. Apply JS micro-optimizations only in measured hot paths.

## Evidence format
- Rule name
- Affected component(s)
- Before/after metric
- Risk or follow-up
