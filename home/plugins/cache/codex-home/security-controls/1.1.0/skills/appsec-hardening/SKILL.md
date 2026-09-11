---
name: appsec-hardening
description: Apply application security hardening controls such as input validation, authn/authz
  checks, safe subprocess patterns, security headers, and abuse-rate defenses. Use when the
  user asks to harden code paths, close security gaps, or implement secure defaults.
metadata:
  version: '1.1'
  short-description: 'Practical application security hardening: input validation, auth, safe
    subprocess, web security headers, and abuse resistance'
  tags:
  - security
  - hardening
  - web
  - api
  - auth
  - supply-chain
interface:
  display-name: APPSEC-Hardening
  short-description: 'Practical application security hardening: input validation, auth, safe
    subprocess, web security headers, and abuse resistance'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#9932CC'
  default-prompt: 'Act as the "APPSEC-Hardening" specialist for "Practical application security
    hardening: input validation, auth, safe subprocess, web security headers, and abuse resistance".
    Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions.
    Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report
    concrete actions, evidence, and residual risks.'
---

## Use this skill when
- building or modifying any API/service handling untrusted input
- touching auth/session/cookies
- adding file upload/download features
- adding dependencies or build scripts
- integrating with third-party network services

## Workflow
1) Clarify objective, trust boundaries, and success criteria.
2) Inspect current implementation and constraints before editing.
3) Apply minimal, deterministic changes using approved patterns.
4) Validate with the narrowest relevant checks and summarize risks/follow-ups.


## Hardening workflow
1) Identify trust boundaries + assets (see `$CODEX_HOME/docs/security/threat-model.md`)
2) Validate inputs with explicit size limits
3) Add timeouts + bounded retries to all I/O
4) Ensure authN/authZ is explicit and tested
5) Ensure secrets are never logged
6) Lock down dependencies (pin + lockfile + audits)
7) Add negative tests for common abuse cases
8) Add operational guardrails (rate limiting, graceful shutdown, bounded concurrency)
9) Verify logging redaction and error messages do not leak internals

## Web/API defaults
- Request body size limits
- Timeouts: read/write/idle
- Safe headers (CSP, nosniff, frame-ancestors)
- CORS allowlist; avoid `*` with credentials
- Cookie flags: Secure, HttpOnly, SameSite
- Rate limiting for public endpoints

## Subprocess safety
- Never pass user input to a shell.
- Prefer exec-arg APIs.
- Escape only as a last resort.

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
- A prioritized hardening checklist with concrete code locations.
- Tests covering key abuse cases.

## References
- `$CODEX_HOME/docs/security/review-hardening.md`
- `$CODEX_HOME/docs/security/web-hardening.md`
- `$CODEX_HOME/docs/security/supply-chain.md`
- `$CODEX_HOME/docs/security/secrets.md`
