---
name: backend-fastapi
description: Implement production-ready Python FastAPI services with validated models, routing,
  auth hooks, error handling, and tests. Use when the user asks for backend API work in FastAPI.
metadata:
  version: '1.1'
  short-description: 'FastAPI production patterns: configuration, routing, validation, auth
    hooks, error handling, and testing with secure defaults'
  tags:
  - python
  - fastapi
  - api
  - testing
  - security
interface:
  display-name: BACKEND-FastAPI
  short-description: 'FastAPI production patterns: configuration, routing, validation, auth hooks, error handling, and testing with secure defaults'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#A532CC'
  default-prompt: 'Act as the "BACKEND-FastAPI" specialist for "FastAPI production patterns: configuration, routing, validation, auth hooks, error handling, and testing with secure defaults". Deliver focused, deterministic results
    with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and
    bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.'
---

## Use this skill when
- building or hardening FastAPI services with explicit validation and secure defaults
- adding auth/dependency layers, timeout-bounded outbound calls, and standardized error responses
- enforcing request limits, security headers, and request-id correlation

## Defaults
- Pydantic models for request/response validation.
- Explicit request size limits (middleware if needed).
- Timeouts for any outbound requests.
- Structured logging; avoid logging request bodies by default.
- Use dependency injection for auth and DB sessions.
- Correlation IDs (accept bounded `X-Request-Id` or generate; propagate to logs and responses).
- Conservative security headers for API responses.
- Request timeouts and error mapping centralized in app setup.

## Testing
- Unit tests for core logic.
- Integration tests for routes with TestClient/HTTPX.
- Negative tests for auth and validation.
- Add at least one test that asserts security headers and request-id propagation.

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
- Secure-by-default FastAPI routes with explicit validation and headers.
- Tests covering auth/validation and request-id propagation.

## References
- `$CODEX_HOME/templates/python/fastapi-app`
- `$CODEX_HOME/docs/style/python.md`
- `$CODEX_HOME/docs/security/web-hardening.md`
- `$CODEX_HOME/snippets/python/fastapi_security_headers.py`
- `$CODEX_HOME/snippets/python/http_client.py`
