---
name: web-nextjs
description: Build and troubleshoot Next.js applications with app router boundaries, SSR/ISR
  behavior, and server/client separation. Use when the user asks for full-stack React framework
  behavior, route handlers, middleware, or deployment-aware Next.js runtime decisions.
metadata:
  version: '1.0'
  short-description: Build Next.js apps with safe server/client boundaries
  tags:
  - nextjs
  - web
  - frontend
interface:
  display-name: WEB-Next.js
  short-description: Build Next.js apps with safe server/client boundaries
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC9B'
  default-prompt: Act as the "WEB-Next.js" specialist for "Build Next.js apps with safe server/client
    boundaries". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- implementing or fixing App Router routes, layouts, server actions, route handlers, or middleware
- designing SSR/ISR/streaming behavior and cache invalidation
- reviewing server/client boundaries to prevent secrets from reaching client bundles

## Do not use this skill when
- the task is framework-neutral React component work without Next.js runtime concerns
- the request is primarily Vue/Nuxt, SvelteKit, HTMX, or static HTML work

## Workflow
1) Build a route ownership matrix (Server Component, Client Component, route handler, middleware).
2) Decide render/cache strategy per route (`references/route-runtime-matrix.md`) and map on-demand invalidation (`revalidatePath`, `revalidateTag(tag, "max")`).
3) Apply React performance rules adapted from Vercel guidance (`references/react-performance-rules.md`) while keeping Server Components as the default baseline.
4) Apply cross-platform UI performance heuristics adapted from React Native rules (`references/react-native-web-adaptations.md`).
5) Verify authz, input validation, error boundaries, and bounded outbound I/O.
6) Run quality gates and return evidence with unresolved risks.

## Reference loading order
- `references/implementation-playbook.md`
- `references/route-runtime-matrix.md`
- `references/react-performance-rules.md`
- `references/react-native-web-adaptations.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Run project quality gates with TypeScript enabled (for example: `npm run lint`, `npm run typecheck`, `npm test`, `npm run build`).
- Confirm server/client boundaries: no secrets in client bundles, `server-only` modules stay server-side, and Server Actions/route handlers validate inputs.
- Test auth and cache behavior per route (middleware redirects, `revalidate`/tag invalidation, and intentional dynamic vs static rendering triggers).
- Evaluate accessibility on interactive pages (form labels/errors, keyboard flow, focus restoration, and route-change announcements).
- Collect performance evidence (bundle split impact, Core Web Vitals or Lighthouse targets, image/font optimization regressions).

## Outputs
- Route ownership matrix (Server Component, Client Component, route handler, middleware) with security and data-flow notes.
- Verification log covering lint/typecheck/tests/build plus auth, caching, accessibility, and performance checkpoints.

## References
- `$CODEX_HOME/docs/workflows/web-frontend.md`
- `$CODEX_HOME/docs/web/nextjs.md`
- `$CODEX_HOME/templates/web/nextjs-app/`
- `references/implementation-playbook.md`
- `references/route-runtime-matrix.md`
- `references/react-performance-rules.md`
- `references/react-native-web-adaptations.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
