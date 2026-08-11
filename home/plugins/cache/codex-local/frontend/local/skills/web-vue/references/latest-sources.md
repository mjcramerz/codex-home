---
title: web-vue reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-vue
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-25'
---
# web-vue reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: official Vue docs plus latest stable release artifact.

## Version snapshot (captured 2026-02-25)
- Vue core: `v3.5.29` (released 2026-02-24).

## High-priority guidance deltas
- Prefer `<script setup>` and explicit Composition API contracts for new component work.
- Keep watcher usage deliberate; avoid deep watchers unless requirements demand them.
- Validate `v-html` and route inputs as untrusted surfaces.

## Skill purpose
Build Vue apps with disciplined Composition API usage and maintainable component/composable boundaries.

## Local references in this folder
- `implementation-playbook.md`
- `composition-reactivity-patterns.md`
- `quality-gates.md`

## External references
- [Vue docs](https://vuejs.org/guide/introduction.html)
- [Vue API reference](https://vuejs.org/api/)
- [Vue watcher guide](https://vuejs.org/guide/essentials/watchers.html)
- [Vue style guide](https://vuejs.org/style-guide/)
- [Vue core release v3.5.29](https://github.com/vuejs/core/releases/tag/v3.5.29)
