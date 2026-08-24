---
title: Web HTMX Implementation Playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-htmx
- references
- implementation-playbook-md
- implementation-playbook
- user
- web
updated: '2026-02-25'
---
# Web HTMX Implementation Playbook

## Scope and intent
Use this playbook for server-rendered interfaces where HTMX progressively enhances links/forms with partial swaps.

## Intake checklist
- Enumerate each interaction: trigger element, endpoint, method, target, and swap strategy.
- Confirm fallback behavior when JavaScript/HTMX is unavailable.
- Confirm mutation safety requirements (authz, CSRF, idempotency, retry policy).

## Delivery sequence
1. Define fragment contracts in `endpoint-contracts.md`.
2. Implement server responses for success, empty, validation-error, and server-error states.
3. Attach HTMX attributes only after baseline forms/links are functional.
4. Add indicators (`hx-indicator`) and optimistic UX only when consistency guarantees exist.
5. Validate contract behavior and quality gates.
6. Return endpoint-to-fragment matrix and follow-up risks.

## Decision rules
- Keep fragments small and deterministic.
- Favor idempotent GET interactions for read-only updates.
- Use POST/PUT/PATCH/DELETE only with CSRF and authz checks.
- Prefer explicit `hx-target` selectors over broad container swaps.
- Use out-of-band swaps (`hx-swap-oob`) only when state coherence is clear.
