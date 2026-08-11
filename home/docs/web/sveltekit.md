# Svelte / SvelteKit
Purpose: tell the Codex coding agent how to use `docs/web/sveltekit.md` as a runtime-pack surface and when to stop browsing.
Guidance for Svelte and SvelteKit applications.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep components small and declarative.
- You must choose adapters deliberately; document deployment assumptions.
- You must keep server-side logic separate from client code.

## Performance
- You must prefer server-rendered routes for content-heavy pages.
- Minimize client-side state for simple pages.

See also:
- `overview.md`
- `$CODEX_HOME/templates/web/sveltekit-app/`
- You must use skill web-sveltekit.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/sveltekit.md`
