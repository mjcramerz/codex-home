# React

Use this guide when the task concerns react. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Use this file when

- the task is primarily React component, hook, or client-state work
- Next.js routing/runtime concerns are not the main issue
- you need React-specific validation expectations before editing

## Defaults

- Prefer function components and hooks.
- Keep state local until a wider ownership boundary is justified.
- Separate view logic from data fetching and mutation side effects.
- Keep prop and callback contracts typed and explicit.

## Validation

- Run typecheck on the affected packages.
- Run lint plus targeted unit/component tests.
- Check keyboard flow, focus order, semantics, and contrast.
- Keep secrets and unsafe HTML/URL handling out of client code.

## After that, check related files

- `overview.md`
- `nextjs.md`
- `$CODEX_HOME/templates/web/react-vite-app/`
- Read the `web-react` skill only when its trigger matches this task and the skill is available.
