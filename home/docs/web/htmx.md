# HTMX

Use this guide when the task concerns htmx. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Apply the following practices to server-driven UI with minimal JavaScript.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Baseline practices

- Keep server responses small and cacheable.
- Prefer progressive enhancement over SPA-only flows.
- Validate and sanitize user input on the server.
- Define endpoint/partial contracts explicitly (request params, response fragments, failure states).
- Preserve keyboard and non-JS fallbacks for critical interactions.

## Performance

- Use partial responses; avoid full-page rerenders when possible.
- Add HTTP caching headers for static fragments.

## Validation checklist

- Verify idempotency and CSRF behavior for state-changing interactions.
- Test optimistic/error UI transitions for swapped fragments.
- Validate aria-live/focus behavior after dynamic content updates.
- Ensure server templates escape untrusted content and bound payload sizes.

See also:
- `overview.md`
- `../lang/html.md`
- `$CODEX_HOME/templates/web/htmx-app/`
- `$CODEX_HOME/snippets/web/htmx/index.html`
- Read the `web-htmx` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/htmx.md`
