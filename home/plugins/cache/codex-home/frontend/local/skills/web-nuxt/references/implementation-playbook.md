---
title: Web Nuxt Implementation Playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nuxt
- references
- implementation-playbook-md
- implementation-playbook
- user
- web
updated: '2026-02-25'
---
# Web Nuxt Implementation Playbook

## Scope and intent
Use this playbook for Nuxt 4 projects requiring explicit rendering strategy, secure runtime configuration, and predictable Nitro server behavior.

## Intake checklist
- Identify route types (public, authenticated, admin, API/Nitro).
- Confirm deployment target and runtime constraints.
- Confirm expected freshness model for data and pages.
- Confirm environment variable handling and secret boundaries.

## Delivery sequence
1. Define route rendering mode and caching behavior.
2. Configure `runtimeConfig` and isolate secrets from `public` config.
3. Implement data-fetching with bounded retries/timeouts.
4. Add validation/authz on server routes and actions.
5. Validate hydration behavior and payload size.
6. Return route/runtime decision summary and evidence.

## Decision rules
- Prefer server-side data fetching for sensitive or SEO-critical routes.
- Keep payloads minimal to reduce hydration cost.
- Use route rules intentionally; avoid defaulting everything to dynamic SSR.
- Treat Nitro endpoints as untrusted boundaries requiring strict validation.
