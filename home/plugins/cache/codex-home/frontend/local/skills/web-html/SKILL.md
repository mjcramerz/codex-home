---
name: web-html
description: Build semantic, accessible HTML documents and static templates with standards-compliant
  structure, predictable form behavior, and ARIA-aware markup. Use when the user asks for
  plain HTML pages, accessibility audits, or static frontend templates without a JavaScript
  framework runtime.
metadata:
  version: '1.0'
  short-description: Build accessible, semantic HTML pages
  tags:
  - html
  - web
  - accessibility
interface:
  display-name: WEB-HTML
  short-description: Build accessible, semantic HTML pages
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3532CC'
  default-prompt: Act as the "WEB-HTML" specialist for "Build accessible, semantic HTML pages".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.
---

## Use this skill when
- building or refactoring static HTML pages, landing pages, emails, or documentation shells
- auditing semantic structure, keyboard navigation, and accessible form behavior
- creating framework-neutral templates intended for later integration

## Do not use this skill when
- the request requires React, Vue, Nuxt, Next.js, SvelteKit, or HTMX runtime behavior
- server routing, hydration boundaries, or framework build pipelines are the primary concern

## Workflow
1) Confirm page intent, audience, required accessibility level (WCAG 2.2 AA by default), and any previous browser constraints.
2) Build semantic document structure first (landmarks, heading order, form relationships).
3) Apply interaction contracts (keyboard/focus behavior, validation messaging, safe links/forms).
4) Add progressive enhancement hooks only when explicitly needed and keep no-JS fallbacks working.
5) Run markup/a11y/performance checks from `references/quality-gates.md`, including WCAG 2.2 focus and target-size checks.
6) Return artifact plus a concise remediation list for any known gaps.

## Reference loading order
- `references/implementation-playbook.md`
- `references/semantic-and-a11y-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Run standards checks for markup and accessibility (`html-validate`, W3C/Nu checker, or project equivalents).
- Verify keyboard path end-to-end: skip link, logical tab order, visible focus, and no keyboard traps.
- Check semantic structure (single `h1`, landmark regions, form labels/error text), contrast ratios, and WCAG 2.2 focus visibility.
- Harden common static-page risks: escape untrusted HTML, set safe link attrs (`rel="noopener noreferrer"`), and keep form contracts explicit.
- Capture performance basics for first paint (image dimensions, lazy loading, non-blocking scripts) and record any remaining regressions.

## Outputs
- HTML artifact with semantic landmarks, accessible form/error patterns, and documented assumptions.
- Validation report with commands run, failed/passed checks, and a prioritized remediation list.

## References
- `$CODEX_HOME/docs/lang/html.md`
- `$CODEX_HOME/templates/web/html-static/`
- `$CODEX_HOME/snippets/web/html/index.html`
- `references/implementation-playbook.md`
- `references/semantic-and-a11y-patterns.md`
- `references/quality-gates.md`
- `references/latest-sources.md`
