# Vue
Purpose: tell the Codex coding agent how to use `docs/web/vue.md` as a runtime-pack surface and when to stop browsing.
Guidance for Vue applications with Composition API defaults.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/web/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must prefer Composition API for shared logic.
- You must keep state local; avoid global singletons where possible.
- You must use `<script setup>` for clarity.

See also:
- `overview.md`
- `nuxt.md`
- `$CODEX_HOME/templates/web/vue-app/`
- You must use skill web-vue.
- `$CODEX_HOME/index/domains/web/frameworks.md`
- `$CODEX_HOME/index/domains/web/vue.md`
