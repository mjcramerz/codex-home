---
title: SvelteKit Route, Load, and Action Patterns
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-sveltekit
- references
- route-load-action-patterns-md
- route-load-action-patterns
- user
- web
updated: '2026-02-25'
---

# SvelteKit Route, Load, and Action Patterns

Consult this reference when sveltekit route, load, and action patterns is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Route boundary patterns

- `+page.server.ts`: server-only data and sensitive operations.
- `+page.ts`: client-usable loading, no secret access.
- `+server.ts`: HTTP interface; validate all request inputs.

## Form action patterns

- Use named actions for complex forms.
- Normalize validation error payloads for deterministic rendering.
- Re-check authz for mutating actions even when UI hides controls.

## Data loading patterns

- Parallelize independent fetch operations.
- Bound external I/O with timeout and retry policy.
- Avoid duplicate fetches across nested load functions when possible.

## Navigation and UX patterns

- Preserve focus after navigation and form submissions.
- Provide explicit pending/error/empty states.
- Keep redirect flows deterministic and tested.
