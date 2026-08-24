---
title: Web HTMX Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-htmx
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web HTMX Quality Gates

## Mandatory checks
- Lint/type/test/build commands for the server project.
- Integration tests covering each HTMX endpoint contract.
- A11y checks on swapped fragments and full-page fallbacks.

## Security checks
- CSRF protection enabled for mutating endpoints and propagated consistently via headers/tokens.
- Authorization enforced server-side for each action.
- Output escaping applied consistently in rendered fragments.
- Request payload sizes and retry behavior bounded.

## Behavior checks
- No-JS baseline works for each interaction, including boosted navigation fallbacks.
- HTMX success/empty/validation-error/server-error states are handled.
- `hx-target` and swap strategy do not replace unintended DOM regions.

## Performance checks
- Fragment payload sizes stay within agreed budgets.
- Cache headers are intentional for read endpoints.
- Repeated requests are deduplicated or rate-limited where needed.

## Evidence to return
- Contract-by-contract verification table.
- Commands and test cases executed.
- Remaining risks with severity and proposed mitigation.
