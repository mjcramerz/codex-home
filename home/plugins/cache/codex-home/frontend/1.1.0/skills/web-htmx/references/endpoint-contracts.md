---
title: HTMX Endpoint and Fragment Contracts
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-htmx
- references
- endpoint-contracts-md
- endpoint-contracts
- user
- web
updated: '2026-02-25'
---

# HTMX Endpoint and Fragment Contracts

Consult this reference when htmx endpoint and fragment contracts is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Contract template

For each interaction, document:
- Trigger source (`button`, `form`, event)
- Method and endpoint
- Expected status codes
- Target selector and swap mode
- Response fragment root element
- Empty/validation/server error payload shape
- Cache and retry policy

## Common patterns

### Search/filter

- Use `GET` with query params.
- Return only result fragment, not full page shell.
- Debounce where possible and bound query length.

### Inline form validation

- Use form POST and return field-level error fragments.
- Preserve previously entered values.
- Keep deterministic IDs for accessibility references.

### Table row actions

- Use POST/DELETE for mutations with CSRF token.
- Return updated row fragment or OOB count badges.
- Include server-side authorization checks per row action.

### Modal/drawer content

- Fetch body fragment with GET.
- Keep close action functional without JS where possible.
- Return explicit empty/error fallback fragments.

## Anti-patterns

- Returning full layout for every fragment swap.
- Implicit dependencies on global JS state for critical operations.
- Unbounded polling intervals without backoff or cancel conditions.
