# Logging policy

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Default to structured logs.
- Log to stderr.
- Include request-id/correlation-id.
- Avoid logging request bodies or auth headers.
- Use log levels; do not spam info logs on hot paths.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

Recommended fields (when applicable):
- `request_id`, `user_id` (hashed), `route`, `status`, `latency_ms`

Sanitization:
- Redact tokens, passwords, session cookies.
- Avoid dumping entire objects that may contain secrets.
- Treat user-provided values as potentially sensitive; prefer hashing or truncation for identifiers.
- Consider log retention and access controls (logs are data).

See also:
- `overview.md`
- `secrets.md`
- `web-hardening.md`
- `$CODEX_HOME/index/core/security.md`
