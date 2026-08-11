---
title: Semantic and Accessibility Patterns for HTML
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-html
- references
- semantic-and-a11y-patterns-md
- semantic-and-a11y-patterns
- user
- web
updated: '2026-02-25'
---
# Semantic and Accessibility Patterns for HTML

## Landmarks and headings
- Use one `h1` per page-level document context.
- Keep heading levels sequential; do not skip levels for visual styling.
- Include landmarks (`header`, `nav`, `main`, `footer`) to improve screen-reader navigation.
- Include a skip link as the first focusable element on content-heavy pages.

## Forms and validation
- Associate every input with a visible `<label>`.
- Use `aria-describedby` for helper and error text IDs.
- Announce validation state via `aria-invalid` and deterministic error containers.
- Keep server-side validation authoritative even when client-side validation exists.

## Tables and lists
- Use real `<table>` markup for tabular data, including headers.
- Prefer `<ul>` and `<ol>` for grouped items rather than repeated generic containers.
- Provide captions/summaries when table context is not obvious.

## Interactive controls
- Use `<button>` for actions and `<a>` for navigation.
- Preserve visible focus indicators; do not remove outlines without accessible replacement.
- Ensure keyboard activation (`Enter`/`Space`) works for custom controls.

## Links and external navigation
- Add `rel="noopener noreferrer"` for `target="_blank"` links.
- Make link text descriptive out of context (avoid bare "click here").

## Media and performance basics
- Set explicit width/height on images to reduce layout shift.
- Provide `alt` text based on intent (informative, decorative, functional).
- Prefer lazy loading for below-the-fold images.
