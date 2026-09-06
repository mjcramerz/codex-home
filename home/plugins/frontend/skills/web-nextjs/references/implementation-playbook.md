---
title: Web Next.js Implementation Playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-nextjs
- references
- implementation-playbook-md
- implementation-playbook
- user
- web
updated: '2026-02-25'
---
# Web Next.js Implementation Playbook

## Scope and intent
Use this playbook for Next.js App Router projects with explicit server/client boundaries, route-level caching strategy, and secure mutation paths.

## Intake checklist
- Identify affected routes, layouts, and shared components.
- Confirm runtime target (Node, edge, serverless) and deployment constraints.
- Confirm data consistency rules (revalidate windows, tag invalidation, ISR behavior).
- Confirm auth/session model and protected route surfaces.

## Delivery sequence
1. Build route ownership matrix (Server Component, Client Component, route handler, middleware).
2. Choose rendering and caching strategy per route using `route-runtime-matrix.md`.
3. Apply React performance guidance from `react-performance-rules.md`.
4. Apply cross-platform UI performance patterns from `react-native-web-adaptations.md` when relevant.
5. Validate security/performance/a11y using `quality-gates.md`.
6. Return evidence with unresolved tradeoffs and rollback hints.

## Decision rules
- Keep data fetching on the server unless direct client interactivity requires client fetching.
- Treat every route handler and server action as an API surface requiring strict input validation.
- Use explicit cache invalidation APIs (`revalidatePath`, `revalidateTag`) instead of ad hoc cache busting.
- Keep secrets in server-only modules and never pass them through serialized props.
