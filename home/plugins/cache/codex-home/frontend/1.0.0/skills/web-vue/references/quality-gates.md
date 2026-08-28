---
title: Web Vue Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-vue
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web Vue Quality Gates

## Mandatory checks
- `npm run lint`
- `npm run typecheck`
- `npm test`
- `npm run build`

## Security checks
- No unsafe unsanitized HTML rendering.
- Route param and query input validation is explicit.
- Session/auth data handling is bounded and non-leaky.

## Reactivity checks
- Derived state uses `computed` when possible.
- Watchers are scoped, cleaned up, and minimized unless requirements demand deeper observation.
- Expensive recalculations are memoized or split by component boundaries.

## UX and accessibility checks
- Keyboard navigation and focus order are preserved.
- Form labels/help/error relationships are explicit.
- Dynamic updates do not break screen-reader context or keyboard focus order after async state changes.

## Performance checks
- Bundle impact tracked for changed views.
- Hot components checked for unnecessary rerenders/watch triggers.
- Large lists/tables use pagination or virtualization where needed.
