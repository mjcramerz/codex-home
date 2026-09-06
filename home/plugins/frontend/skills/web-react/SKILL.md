---
name: web-react
description: Build, refactor, and review React component systems, hooks, and client-side UI
  architecture with performance-aware rendering and predictable state boundaries. Use when
  the user asks for React logic without requiring Next.js/Nuxt/SvelteKit routing ownership
  or framework-specific server runtime behavior.
metadata:
  version: '1.0'
  short-description: Build React apps with performant component structure
  tags:
  - react
  - web
  - frontend
interface:
  display-name: WEB-React
  short-description: Build React apps with performant component structure
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC5632'
  default-prompt: Act as the "WEB-React" specialist for "Build React apps with performant
    component structure". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- building React component trees, hooks, local state models, and reusable UI primitives
- improving render performance, bundle boundaries, and data-fetching flow in client React apps
- reviewing React code quality, side-effect placement, and accessibility behavior

## Do not use this skill when
- Next.js route handlers, middleware, SSR/ISR policy, or App Router ownership is required
- the task is primarily Vue/Nuxt, SvelteKit, HTMX, React Native runtime code, or static HTML only

## Workflow
1) Classify the request: new feature, bug fix, refactor, or performance audit.
2) Build ownership map: component boundaries, state owners, side-effect locations.
3) Apply the React 19 performance catalog (`references/react-performance-rules.md`), prioritizing structural fixes before memoization.
4) Apply cross-platform heuristics adapted from React Native rules (`references/react-native-web-adaptations.md`).
5) Validate security, accessibility, and performance using `references/quality-gates.md`.
6) Return changed files, evidence, and prioritized follow-up items.

## Reference loading order
- `references/implementation-playbook.md`
- `references/react-performance-rules.md`
- `references/react-native-web-adaptations.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Run React + TypeScript quality gates (for example: `npm run lint`, `npm run typecheck`, `npm test -- --run`, `npm run build`) and keep Rules of Hooks checks clean.
- Validate component contracts and state boundaries with focused tests for async/loading/error paths and user-event flows.
- Enforce frontend security basics: sanitize or avoid unsafe HTML injection, validate URL/query inputs, and protect auth token handling.
- Measure performance impact (bundle size delta, unnecessary re-renders, list virtualization/code-splitting opportunities) before and after changes; if React Compiler is enabled, ensure manual memoization choices are still justified.
- Verify accessibility behavior using role-based tests and keyboard/focus checks, not only snapshot output.

## Outputs
- Component/state ownership map with prop boundaries, side-effect locations, and risk notes.
- Verification bundle: commands run, key test cases, perf observations, and a11y/security findings.

## References
- `$CODEX_HOME/docs/workflows/web-frontend.md`
- `$CODEX_HOME/docs/web/react.md`
- `$CODEX_HOME/templates/web/react-vite-app/`
- `references/implementation-playbook.md`
- `references/react-performance-rules.md`
- `references/react-native-web-adaptations.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
