---
title: Web React Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-react
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web React Quality Gates

## Mandatory checks
- `npm run lint`
- `npm run typecheck`
- `npm test -- --run`
- `npm run build`

## Security checks
- Untrusted HTML is sanitized before rendering (`dangerouslySetInnerHTML` avoidance preferred).
- URL/query parameters are validated before use.
- Tokens/session data are not stored or exposed in unsafe contexts.

## Rendering and state checks
- Derived values are computed during render unless persistence is required, and Hooks purity rules remain clean.
- High-frequency updates use refs/transitions where appropriate.
- Large lists use virtualization or paging.

## UX and accessibility checks
- Keyboard interaction parity for all clickable controls.
- Focus management after async updates and modal interactions.
- Proper labels, descriptions, and error associations on form controls.

## Performance checks
- Bundle diff captured for changed entry points.
- Profiler evidence for rerender-heavy views (and React Compiler interactions when enabled).
- Network waterfall review for async data dependencies.
