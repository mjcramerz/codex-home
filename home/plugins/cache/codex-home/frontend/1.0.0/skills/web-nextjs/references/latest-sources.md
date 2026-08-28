---
title: web-nextjs reference bundle
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- latest-sources-md
- latest-sources
- user
- web
updated: '2026-02-25'
---
# web-nextjs reference bundle

- Last refreshed: 2026-02-25 (UTC)
- Freshness method: official Next.js + React docs and latest stable release artifacts.

## Version snapshot (captured 2026-02-25)
- Next.js: `v16.1.6` (released 2026-01-27).
- React: `v19.2.4` (released 2026-01-26).

## High-priority guidance deltas
- App Router remains the default architecture; keep server/client boundaries explicit.
- Prefer on-demand invalidation via `revalidatePath` and `revalidateTag(tag, 'max')`.
- Treat route handlers, server actions, and middleware as untrusted boundaries with strict validation.

## Skill purpose
Build Next.js apps with explicit route ownership, safe server/client boundaries, and measurable performance behavior.

## Local references in this folder
- `implementation-playbook.md`
- `route-runtime-matrix.md`
- `react-performance-rules.md`
- `react-native-web-adaptations.md`
- `quality-gates.md`

## Adaptation sources

## External references
- [Next.js docs](https://nextjs.org/docs)
- [Next.js App Router docs](https://nextjs.org/docs/app)
- [Next.js caching and revalidation guide](https://nextjs.org/docs/app/getting-started/caching-and-revalidating)
- [Next.js release v16.1.6](https://github.com/vercel/next.js/releases/tag/v16.1.6)
- [React docs](https://react.dev/)
- [React release v19.2.4](https://github.com/facebook/react/releases/tag/v19.2.4)
