---
title: Nuxt Runtime and Data Patterns
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nuxt
- references
- runtime-and-data-patterns-md
- runtime-and-data-patterns
- user
- web
updated: '2026-02-25'
---
# Nuxt Runtime and Data Patterns

## Rendering strategy matrix
| Route type | Suggested mode | Notes |
| --- | --- | --- |
| Marketing/static | SSG or prerender | Maximize cacheability |
| User dashboard | SSR dynamic | User-specific data |
| Mixed catalog | Hybrid ISR-style | Route rules + revalidation |
| Internal admin | SSR dynamic + auth middleware | Strong authz controls |

## Runtime config boundaries
- Put secrets in private `runtimeConfig` keys only.
- Use `runtimeConfig.public` only for non-sensitive client values.
- Validate required keys at startup and fail closed if missing.

## Data loading patterns
- Use `useAsyncData` with explicit keys and dedupe strategy.
- Bound request retries and enforce network timeouts.
- Normalize error payloads for predictable UI handling.

## Nitro route checklist
- Validate request body/query/params with schemas.
- Enforce authz for every mutating action.
- Return explicit error codes and non-ambiguous payloads.
