---
name: backend-axum
description: Implement production-ready Rust Axum APIs with routing, extractors, typed errors,
  tracing, and timeout-aware handlers. Use when the user asks for backend API work in Rust/Axum.
metadata:
  version: '1.1'
  short-description: 'Axum API production patterns: routing, extractors, typed errors, tracing,
    timeouts, and secure defaults'
  tags:
  - rust
  - axum
  - api
  - tracing
  - security
  - performance
interface:
  display-name: BACKEND-Axum
  short-description: 'Axum API production patterns: routing, extractors, typed errors, tracing, timeouts, and secure defaults'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3249'
  default-prompt: 'Act as the "BACKEND-Axum" specialist for "Axum API production patterns: routing, extractors, typed errors, tracing, timeouts, and secure defaults". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and
    bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.'
---

## Use this skill when
- building or hardening Rust HTTP APIs with Axum
- adding typed extractors/responses, centralized error handling, and middleware layering
- enforcing API request limits, timeouts, and tracing defaults

## Defaults
- Typed request/response models with serde.
- Central error type mapping to HTTP errors (no panics).
- `tracing` spans per request.
- Timeouts on outbound requests.
- Bound concurrency for expensive work.
- Request body limits and request timeouts at the edge.
- Request-id propagation (`X-Request-Id`) for correlation.
- Layered middleware via `tower` for timeouts and limits.

## Testing
- Unit tests for pure functions.
- Integration tests using `axum::Router` and `tower::ServiceExt`.
- Add a test for `X-Request-Id` propagation and at least one negative test for validation limits.

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
- Typed, timeout-bounded Axum APIs with tracing and request-id propagation.
- Tests for validation boundaries and correlation IDs.

## References
- `$CODEX_HOME/templates/rust/axum-api`
- `$CODEX_HOME/docs/style/rust.md`
- `$CODEX_HOME/docs/perf/rust-perf.md`
- `$CODEX_HOME/snippets/rust/axum_timeout_layer.rs`
- `$CODEX_HOME/docs/security/review-hardening.md`
