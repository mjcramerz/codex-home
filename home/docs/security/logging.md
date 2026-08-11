# Logging policy
Purpose: tell the Codex coding agent how to use `docs/security/logging.md` as a runtime-pack surface and when to stop browsing.
- Default to structured logs.
- Log to stderr.
- Include request-id/correlation-id.
- Avoid logging request bodies or auth headers.
- You must use log levels; do not spam info logs on hot paths.


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
- You must treat user-provided values as potentially sensitive; prefer hashing or truncation for identifiers.
- Consider log retention and access controls (logs are data).

See also:
- `overview.md`
- `secrets.md`
- `web-hardening.md`
- `$CODEX_HOME/index/core/security.md`
