---
name: lang-typescript
description: Implement and refactor TypeScript projects with strict typing, tsconfig hygiene,
  and safe build defaults. Use when the user asks for TypeScript code, type errors, or project
  configuration changes.
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
  default-prompt: Act as the "LANG-TypeScript" specialist for "Configure TypeScript projects
    with strict defaults". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- setting TS defaults or linting rules

## Workflow
1) Define strict `tsconfig` with explicit module/runtime boundaries.
2) Add deterministic install + typecheck/lint/test/build gates to CI.
3) Keep build outputs isolated and package exports explicit.
4) Validate untrusted input handling with `unknown` + runtime narrowing.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- TypeScript project hardening steps with concrete config and CI checks.
- Compatibility notes for Node/browser boundaries and package-manager determinism.

## References
- `$CODEX_HOME/docs/workflows/codex-repo.md`
- `$CODEX_HOME/docs/workflows/web-frontend.md`
- `$CODEX_HOME/docs/lang/typescript.md`
- `$CODEX_HOME/docs/style/typescript.md`
- `$CODEX_HOME/templates/typescript/ts-lib/`
- `$CODEX_HOME/snippets/typescript/tsconfig.json`
- `$CODEX_HOME/docs/prompt-writing.md`
