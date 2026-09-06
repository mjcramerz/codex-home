---
name: devtools-app-scaffolder
description: Scaffold new production-ready applications from templates (FastAPI, Axum, React,
  and supporting services) with config, logging, tests, and CI wired in. Use when the user
  asks to bootstrap a new app, starter repo, or full project skeleton.
metadata:
  version: '1.1'
  short-description: Scaffold full-fledged apps using the provided templates; wire up config,
    logging, tests, and CI with secure defaults
  tags:
  - scaffolding
  - templates
  - fastapi
  - axum
  - react
  - app
interface:
  display-name: DEVTOOLS-App Scaffolding
  short-description: Scaffold full-fledged apps using the provided templates; wire up config,
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#93CC32'
  default-prompt: Act as the "DEVTOOLS-App Scaffolding" specialist for "Scaffold full-fledged
    apps using the provided templates; wire up config,". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and
    bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

## Use this skill when
- user asks to create a new app/service/CLI
- you need a production-ready project skeleton quickly

## Workflow
1) Clarify objective, trust boundaries, and success criteria.
2) Inspect current implementation and constraints before editing.
3) Apply minimal, deterministic changes using approved patterns.
4) Validate with the narrowest relevant checks and summarize risks/follow-ups.


## Non-negotiables
- Prefer templates and snippets in this pack over inventing from scratch.
- Keep dependencies minimal and pinned; commit lockfiles when available.
- Add basic tests and make them run in CI before adding features.
- Apply security defaults at trust boundaries: validation, size limits, timeouts, auth hooks.

## Procedure (end-to-end)
1) Pick a template matching the stack and the user’s target (API/CLI/web).
2) Copy into target directory and rename placeholders (package/crate/app name).
3) Wire up:
   - config (env vars, validation at startup)
   - structured logging (stderr) + correlation IDs (APIs)
   - error handling with redaction (no internal leaks)
4) Run the narrowest checks (format/lint/unit tests) and fix issues immediately.
5) Add CI workflows from `$CODEX_HOME/templates/ci/github-actions/` and ensure minimal permissions.
6) Add supply-chain guardrails: lockfiles, audits, dependency review.
7) Add container/compose scaffolds when requested (`$CODEX_HOME/templates/containers/`).
8) Add a short README: run commands, env vars, tests, and any security notes.

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
- A runnable scaffold with pinned deps and basic tests.
- CI workflows with minimal permissions and audits.
- README with setup, run, test, and security notes.

## Templates
- Python: `$CODEX_HOME/templates/python/fastapi-app`
- Python CLI: `$CODEX_HOME/templates/python/cli-app`
- Rust: `$CODEX_HOME/templates/rust/axum-api`
- Rust CLI: `$CODEX_HOME/templates/rust/cli-app`
- Web: `$CODEX_HOME/templates/web/react-vite-app`
- CI: `$CODEX_HOME/templates/ci/github-actions`

## References
- `$CODEX_HOME/AGENTS.md`
- `$CODEX_HOME/index/pack/docs.md`
- `$CODEX_HOME/docs/workflows/build-an-app.md`
- `$CODEX_HOME/docs/security/threat-model.md`
- `$CODEX_HOME/index/core/ci-cd.md`
- `$CODEX_HOME/docs/templates/using-templates.md`
