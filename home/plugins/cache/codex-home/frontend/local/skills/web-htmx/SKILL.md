---
name: web-htmx
description: Build server-driven HTMX interfaces with progressive enhancement, explicit fragment
  contracts, and minimal custom JavaScript. Use when the user asks for HTMX flows, partial
  swaps, or hypermedia-style frontend behavior.
metadata:
  version: '1.0'
  short-description: Build server-driven HTMX pages with minimal JS
  tags:
  - htmx
  - web
  - frontend
interface:
  display-name: WEB-HTMX
  short-description: Build server-driven HTMX pages with minimal JS
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC6D32'
  default-prompt: Act as the "WEB-HTMX" specialist for "Build server-driven HTMX pages with
    minimal JS". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- building UI flows where the server remains the source of truth for rendered HTML
- replacing SPA-style interactions with incremental fragment swaps
- defining request/response contracts for forms, tables, filters, and modal dialogs

## Do not use this skill when
- the request requires a client-rendered SPA as the primary architecture
- cross-page state synchronization depends on heavy client-side state stores

## Workflow
1) Confirm HTMX major version/extension constraints and define interaction inventory (trigger, endpoint, method, target, swap strategy).
2) Specify fragment contracts before coding (`references/endpoint-contracts.md`).
3) Implement endpoints with bounded I/O, authz, deterministic error states, and explicit CSRF header propagation strategy.
4) Keep non-JS fallbacks fully functional (links/forms first, HTMX second).
5) Validate loading, empty, validation-error, and server-error paths.
6) Return an endpoint-to-fragment matrix with remaining risks.

## Reference loading order
- `references/implementation-playbook.md`
- `references/endpoint-contracts.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Verify each interaction contract: request method/URL, expected status codes, swap targets, and empty/error responses.
- Test progressive enhancement by executing flows without JS (forms/links still work), with HTMX swaps enabled, and with `hx-boost` navigation where used.
- Enforce security controls on mutating endpoints: CSRF headers/tokens, authz checks, output escaping, and idempotency rules.
- Measure performance guardrails for fragments (response size budgets, cache headers, retry/timeout behavior, and duplicate-request suppression).
- Run automated checks for accessibility and interaction states (loading, success, validation error, server error) and record evidence.

## Outputs
- Endpoint-to-fragment contract table including swap behavior, cache policy, and failure semantics.
- Verification checklist with exact commands plus results for a11y, CSRF/auth, and latency/size budgets.

## References
- `$CODEX_HOME/docs/workflows/web-frontend.md`
- `$CODEX_HOME/docs/web/htmx.md`
- `$CODEX_HOME/templates/web/htmx-app/`
- `$CODEX_HOME/snippets/web/htmx/index.html`
- `references/implementation-playbook.md`
- `references/endpoint-contracts.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
