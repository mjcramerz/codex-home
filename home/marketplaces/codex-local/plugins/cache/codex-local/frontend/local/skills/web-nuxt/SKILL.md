---
name: web-nuxt
description: Build and maintain Nuxt applications with explicit runtime configuration, rendering-mode
  decisions, and deployment-safe defaults. Use when the user asks for Nuxt-specific work,
  including Vue full-stack app structure, Nitro routes, and SSR/SSG behavior.
metadata:
  version: '1.0'
  short-description: Build Nuxt apps with explicit runtime config
  tags:
  - nuxt
  - vue
  - web
  - frontend
interface:
  display-name: WEB-Nuxt
  short-description: Build Nuxt apps with explicit runtime config
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC7C'
  default-prompt: Act as the "WEB-Nuxt" specialist for "Build Nuxt apps with explicit runtime
    config". Deliver focused, deterministic results with minimal, reviewable changes and explicit
    assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks,
    and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- scaffolding or refactoring Nuxt 4 applications with SSR/SSG/hybrid targets
- implementing Nitro server routes, middleware, or runtime config contracts
- reviewing hydration behavior, payload size, and caching strategy

## Do not use this skill when
- the request is generic Vue component work without Nuxt runtime concerns
- the task is primarily Next.js, SvelteKit, HTMX, or static HTML

## Workflow
1) Confirm render target and deployment assumptions (Node, edge, static, hybrid).
2) Define route-mode/data-loading strategy plus explicit `routeRules` (`prerender`, `swr`, `isr`, `ssr`) using `references/runtime-and-data-patterns.md`.
3) Keep `runtimeConfig` explicit and prevent secret leakage into `public` config.
4) Validate server routes/actions with strict input schemas and bounded external I/O.
5) Check hydration, route rules, cache headers, and invalidation flow.
6) Return implementation notes plus quality gate outcomes.

## Reference loading order
- `references/implementation-playbook.md`
- `references/runtime-and-data-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Execute Nuxt gates (for example: `pnpm lint`, `pnpm nuxi typecheck`, `pnpm test`, `pnpm build`) and record exact command output.
- Verify `runtimeConfig` boundaries so secrets stay private and only intended values are exposed via `public`.
- Test server routes/actions for input validation, authz, CSRF/origin protections, and bounded retries/timeouts on outbound I/O (including keyed `useAsyncData`/`useFetch` callers).
- Check SSR/hydration correctness, route rules (`prerender`, `swr`, `isr`, cache headers), and payload-size budgets.
- Run accessibility checks on rendered pages (semantic headings/landmarks, keyboard navigation, focus management, and form error messaging).

## Outputs
- Nuxt implementation plan with route-mode/runtime-config decisions and concrete file targets.
- Checkpoint report listing security, performance, accessibility, and test outcomes with unresolved risks.

## References
- `$CODEX_HOME/docs/web/nuxt.md`
- `$CODEX_HOME/templates/web/nuxt-app/`
- `references/implementation-playbook.md`
- `references/runtime-and-data-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
