---
name: lang-typescript
description: Use this skill to implement and refactor TypeScript projects with strict
  typing, tsconfig hygiene, and safe build defaults. Use when the user asks for TypeScript
  code, type errors, or project configuration changes.
metadata:
  version: '1.0'
  short-description: Configure TypeScript projects with strict defaults
  tags:
  - typescript
  - frontend
  - tooling
interface:
  display-name: LANG-TypeScript
  short-description: Configure TypeScript projects with strict defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3260'
  default-prompt: Act as the "LANG-TypeScript" specialist for "Configure TypeScript
    projects with strict defaults". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Lang Typescript

## Workflow

1. Inspect package.json, the single authoritative lockfile, tsconfig, runtime versions and actual script definitions. Use the existing package manager and avoid unrelated dependency refreshes.

2. Keep strict types at module boundaries; treat network, JSON and environment values as unknown until validated. Do not replace a type error with any or an unchecked assertion.

3. Handle rejected promises, cancellation and cleanup. Bound requests and retries, and avoid event-listener leaks or unbounded concurrency.

4. Keep server credentials out of client bundles and logs. Validate URLs and output contexts, and preserve CSP, authentication and authorization boundaries.

5. Use the existing typecheck, lint, unit and build scripts after reading their commands. A script name is only a candidate until its side effects and prerequisites are understood.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/workflows/web-frontend.md`
- `$CODEX_HOME/docs/lang/typescript.md`
- `$CODEX_HOME/docs/style/typescript.md`
- `$CODEX_HOME/templates/typescript/ts-lib/`
- `$CODEX_HOME/snippets/typescript/tsconfig.json`
- `$CODEX_HOME/docs/prompt-writing.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
