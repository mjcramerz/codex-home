# Web hardening quick reference

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## HTTP server defaults

- Timeouts: read, write, idle, request body
- Maximum request size
- Secure headers:
  - `Content-Security-Policy` (for apps serving HTML)
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY` (or frame-ancestors CSP)
  - `Referrer-Policy: no-referrer` (or strict)
- CORS: allowlist origins; disallow credentials unless required
- Cookies: `HttpOnly`, `Secure`, `SameSite=Lax/Strict`
- Correlation IDs: accept bounded `X-Request-Id` or generate one; propagate to responses and logs

## Auth

- Explicit auth middleware
- AuthZ checks on every protected action
- Don’t trust client-provided IDs (enforce ownership server-side)

## Rate limiting

- Token bucket / leaky bucket
- Per-IP and per-user limits
- Global circuit breakers for expensive operations

## Outbound HTTP (SSRF + reliability)

- Default-deny outbound fetch of user-provided URLs; use allowlists.
- Block link-local/private ranges when fetching by hostname resolution.
- Timeouts and bounded retries; avoid redirects by default.

## TLS

- Do not disable certificate verification.
- Pin certificates only when required by policy and documented.

See also:
- `overview.md`
- `logging.md`
- `$CODEX_HOME/snippets/python/fastapi_security_headers.py`
- `$CODEX_HOME/index/core/security.md`
