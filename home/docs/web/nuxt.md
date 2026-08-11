# Nuxt
Purpose: tell the Codex coding agent how to use `docs/web/nuxt.md` as a runtime-pack surface and when to stop browsing.
Guidance for Vue SSR/SSG apps using Nuxt.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must keep runtime config explicit and minimal.
- Avoid leaking server secrets into client code.
- You must use Nitro/server routes for server-side logic.

See also:
- `overview.md`
- `vue.md`
- `$CODEX_HOME/templates/web/nuxt-app/`
- You must use skill web-nuxt.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/nuxt.md`
