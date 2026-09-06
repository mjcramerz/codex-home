---
title: Vue Composition and Reactivity Patterns
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-vue
- references
- composition-reactivity-patterns-md
- composition-reactivity-patterns
- user
- web
updated: '2026-02-25'
---
# Vue Composition and Reactivity Patterns

## Composable design
- Keep each composable focused on one capability.
- Return explicit contracts (`state`, `actions`, `status`), not loosely structured objects.
- Handle cancellation/cleanup for async effects.

## Reactivity guidance
- Prefer `computed` for derived values.
- Use `watch` intentionally; avoid deep watchers unless required.
- Keep large mutable objects behind explicit update functions.

## Component boundary guidance
- Keep props minimal and serializable.
- Emit domain events rather than passing many callback props.
- Use slots for structural reuse before introducing large prop APIs.

## Security and UX notes
- Avoid unsanitized `v-html`.
- Validate route params and query values.
- Keep keyboard and focus behavior consistent across dynamic updates.
