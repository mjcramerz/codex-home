---
title: Web HTML Implementation Playbook
status: active
owner: Matthew Cramer
tags:
- skills
- all
- web-html
- references
- implementation-playbook-md
- implementation-playbook
- user
- web
updated: '2026-02-25'
---
# Web HTML Implementation Playbook

## Scope and intent
Use this playbook to deliver static HTML pages with strong semantics, accessibility, and predictable behavior.

## Intake checklist
- Confirm target page type (landing page, docs page, dashboard shell, email-safe markup).
- Confirm required accessibility level (WCAG 2.2 AA by default unless the user specifies otherwise).
- Confirm content sources and whether user-provided HTML is trusted.
- Confirm whether JavaScript is allowed and what must work without JavaScript.

## Delivery sequence
1. Build structure first: `header`, `nav`, `main`, `aside`, `footer`, and heading hierarchy.
2. Add interactive controls with accessible names and keyboard behavior.
3. Add forms with explicit labels, descriptions, and deterministic error message containers.
4. Add progressive enhancement hooks (`data-*` attributes, IDs) only after no-JS behavior works.
5. Validate semantic/a11y/performance checks from `quality-gates.md`.
6. Return artifact plus issue list categorized as critical/high/medium.

## Decision rules
- Prefer semantic elements over generic `div` wrappers.
- Prefer native elements (`button`, `details`, `dialog`) before ARIA-heavy custom widgets.
- Never rely on placeholder text as the only label.
- Avoid hidden keyboard traps and off-screen focus targets.
- Treat user-provided HTML as untrusted and sanitize before insertion.

## Handoff output format
- Goal and assumptions (1-3 bullets)
- Changed files
- Validation commands and outcomes
- Remaining risks and recommended next checks
