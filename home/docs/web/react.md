# React
Purpose: guide React component work with explicit state, rendering, accessibility, and validation defaults for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## You must use this file when
- the task is primarily React component, hook, or client-state work
- Next.js routing/runtime concerns are not the main issue
- you need React-specific validation expectations before editing

## Defaults
- You must prefer function components and hooks.
- You must keep state local until a wider ownership boundary is justified.
- Separate view logic from data fetching and mutation side effects.
- You must keep prop and callback contracts typed and explicit.

## Validation
- You must run typecheck on the affected packages.
- You must run lint plus targeted unit/component tests.
- You must check keyboard flow, focus order, semantics, and contrast.
- You must keep secrets and unsafe HTML/URL handling out of client code.

## After that, you must check related files
- `overview.md`
- `nextjs.md`
- `$CODEX_HOME/templates/web/react-vite-app/`
- You must use skill `web-react`.
