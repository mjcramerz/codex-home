---
name: web-sveltekit
description: Build and maintain SvelteKit applications with clear route/load boundaries, adapter
  setup, and runtime configuration. Use when the user asks for SvelteKit-specific routing,
  form actions, or server/client integration tasks.
metadata:
  version: '1.0'
  short-description: Build SvelteKit apps with clear routing and adapters
  tags:
  - svelte
  - sveltekit
  - web
  - frontend
interface:
  display-name: WEB-SvelteKit
  short-description: Build SvelteKit apps with clear routing and adapters
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC59'
  default-prompt: Act as the "WEB-SvelteKit" specialist for "Build SvelteKit apps with clear
    routing and adapters". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- scaffolding or refactoring SvelteKit routes, layouts, load functions, and form actions
- choosing adapter/runtime behavior and deployment-aware rendering policies
- hardening server endpoints and improving navigation/data-loading UX

## Do not use this skill when
- the task is framework-neutral Svelte component work outside SvelteKit routing
- the request is primarily React/Next.js, Vue/Nuxt, HTMX, or static HTML

## Workflow
1) Build a route map (`+page`, `+layout`, `+server`, actions) with data ownership.
2) Choose adapter and rendering mode per route (`references/route-load-action-patterns.md`).
3) Validate env boundaries and secret handling (`$env/static/private` vs public env).
4) Implement action/endpoint validation, authz checks, and bounded external calls.
5) Validate SSR/prerender/hydration behavior, `use:enhance` progressive enhancement, and navigation UX.
6) Report route decisions, test evidence, and remaining risks.

## Reference loading order
- `references/implementation-playbook.md`
- `references/route-load-action-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Run SvelteKit gates (for example: `pnpm lint`, `pnpm check`, `pnpm test`, `pnpm build`) and keep failures tied to file paths.
- Validate server/client/env boundaries (`+page.server.ts` vs `+page.ts`, `$env/static/private` vs public env) to prevent secret leaks.
- Test form actions and `+server` endpoints for schema validation, authz, CSRF/origin checks, bounded external I/O, and no-JS fallback behavior.
- Verify routing/adapter behavior (SSR/CSR/prerender choices, cache headers, error boundaries, and redirect flows).
- Include accessibility and UX checks for navigation/focus transitions and real-time form validation messaging.

## Outputs
- Route and adapter decision table with data-loading strategy and security implications.
- Test evidence set covering type checks, endpoint/action tests, navigation e2e flows, and performance/a11y checkpoints.

## References
- `$CODEX_HOME/docs/web/sveltekit.md`
- `$CODEX_HOME/templates/web/sveltekit-app/`
- `references/implementation-playbook.md`
- `references/route-load-action-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
