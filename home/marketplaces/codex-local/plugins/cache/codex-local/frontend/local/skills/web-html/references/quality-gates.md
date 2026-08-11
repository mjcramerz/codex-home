---
title: Web HTML Quality Gates
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-html
- references
- quality-gates-md
- quality-gates
- user
- web
updated: '2026-02-25'
---
# Web HTML Quality Gates

## Mandatory checks
- `npm run lint:html` or project equivalent.
- `npx html-validate "**/*.html"` (or scoped subset).
- A11y scan (`npx @axe-core/cli <url-or-file>`) for user-visible pages.

## Manual checks
- Keyboard: tab order, visible focus, skip-link behavior, and no trap states.
- Semantics: heading order, landmarks, form labels, and error associations.
- Contrast: text/UI controls meet target contrast ratios and focus indicators remain visible on all themes.

## WCAG 2.2 checks
- Focus indicators satisfy WCAG 2.2 focus appearance guidance.
- Interactive targets meet minimum pointer target-size guidance.
- Drag-only interactions provide keyboard/single-pointer alternatives.

## Security checks
- Untrusted HTML is sanitized or escaped before insertion.
- External links with new tabs include `noopener noreferrer`.
- Hidden inputs and client constraints are not treated as trusted validation.

## Performance checks
- Images have dimensions and are optimized for delivered size.
- Scripts are deferred or placed after content unless blocking is required.
- CSS avoids large unused framework payloads for simple pages.

## Evidence to return
- Command list with pass/fail status.
- Screenshots or notes for manual a11y checks.
- Residual risk list with severity and mitigation options.
