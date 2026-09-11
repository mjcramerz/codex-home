---
name: web-vue
description: Build Vue applications with Composition API patterns, state-flow discipline,
  and reusable component boundaries. Use when the user asks for Vue component logic, composables,
  and client-side architecture outside Nuxt-specific SSR/runtime concerns.
metadata:
  version: '1.0'
  short-description: Build Vue apps with Composition API defaults
  tags:
  - vue
  - web
  - frontend
interface:
  display-name: WEB-Vue
  short-description: Build Vue apps with Composition API defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC5132'
  default-prompt: Act as the "WEB-Vue" specialist for "Build Vue apps with Composition API
    defaults". Deliver focused, deterministic results with minimal, reviewable changes and
    explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant
    checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- implementing Vue components, composables, client routing, and state modules
- improving reactivity boundaries, rendering performance, and testability
- reviewing Vue code for accessibility, security, and maintainability

## Do not use this skill when
- Nuxt runtime configuration, Nitro server routes, or SSR policy is the main concern
- the request is primarily React/Next.js, SvelteKit, HTMX, or static HTML

## Workflow
1) Build component/composable ownership map and reactive state flow.
2) Validate API boundaries and type contracts before implementing features.
3) Apply `<script setup>`, Composition API, and reactivity patterns from `references/composition-reactivity-patterns.md`.
4) Harden dangerous surfaces (`v-html`, route params, external links, auth/session handling).
5) Run lint/typecheck/test/build plus accessibility/performance checks.
6) Return changed-file summary, verification evidence, and prioritized follow-ups.

## Reference loading order
- `references/implementation-playbook.md`
- `references/composition-reactivity-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Run Vue quality gates with TypeScript where enabled (for example: `npm run lint`, `npm run typecheck`, `npm test`, `npm run build`).
- Validate composable/component boundaries and reactive state updates with tests for async success, empty, and failure states, including watcher cleanup paths.
- Apply security checks for `v-html`/template injection, route-param validation, and safe handling of auth/session data.
- Profile performance on key screens (watcher/computed hot spots, code-splitting, hydration and bundle budgets).
- Verify accessibility for component semantics, keyboard navigation, focus order, and error/help text associations.

## Outputs
- Vue implementation checklist with component/composable targets and migration/cleanup notes.
- Verification summary with command output pointers, failing/passing checks, and prioritized follow-up actions.

## References
- `$CODEX_HOME/docs/web/vue.md`
- `$CODEX_HOME/templates/web/vue-app/`
- `references/implementation-playbook.md`
- `references/composition-reactivity-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
