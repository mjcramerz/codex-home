# HTMX
Purpose: tell the Codex coding agent how to use `docs/web/htmx.md` as a runtime-pack surface and when to stop browsing.
Guidance for server-driven UI with minimal JavaScript.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep server responses small and cacheable.
- You must prefer progressive enhancement over SPA-only flows.
- You must validate and sanitize user input on the server.
- You must define endpoint/partial contracts explicitly (request params, response fragments, failure states).
- Preserve keyboard and non-JS fallbacks for critical interactions.

## Performance
- You must use partial responses; avoid full-page rerenders when possible.
- You must add HTTP caching headers for static fragments.

## Validation checklist
- You must verify idempotency and CSRF behavior for state-changing interactions.
- Test optimistic/error UI transitions for swapped fragments.
- You must validate aria-live/focus behavior after dynamic content updates.
- Ensure server templates escape untrusted content and bound payload sizes.

See also:
- `overview.md`
- `../lang/html.md`
- `$CODEX_HOME/templates/web/htmx-app/`
- `$CODEX_HOME/snippets/web/htmx/index.html`
- You must use skill web-htmx.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/htmx.md`
