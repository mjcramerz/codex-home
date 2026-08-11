# Threat modeling (lightweight)
Purpose: tell the Codex coding agent how to use `docs/security/threat-model.md` as a runtime-pack surface and when to stop browsing.
Use this when building APIs/services/CLIs that touch untrusted input.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## 1) Assets
- Secrets (tokens, keys)
- User data (PII)
- Availability (DoS surface)
- Integrity (data correctness, authZ)

## 2) Entry points
- HTTP endpoints
- CLI arguments / env vars
- Files read/written
- Webhooks
- Background jobs
- Dependency updates

## 3) Trust boundaries
- Client → server
- Server → DB
- Server → 3rd party APIs
- CI runners → artifacts
- Build system → package registries

## 4) Abuse cases
- Auth bypass
- Injection (SQL/command/template)
- SSRF (internal metadata endpoints)
- Deserialization attacks
- ReDoS
- Zip bombs / decompression bombs
- Rate limit bypass
- Supply chain compromise (malicious dep update)

## 5) Controls
- You must validate inputs + size limits
- AuthZ checks with tests
- Timeouts + bounded retries
- Egress allowlists
- Dependency pinning + audits
- Logging redaction
- Least-privilege execution

## 6) Tests as controls
For each major abuse case, add at least one regression test that proves the control exists:
- Invalid input → 400 with clear message (no stack traces)
- Unauthorized → 401/403 (no data leaks)
- SSRF attempt → blocked by allowlist (or private-IP block) with a safe error
- Oversized payload → 413/400, fast fail

## Outputs
- A short list of top risks and mitigations.
- Concrete “where to implement” notes (files/modules/middleware).
- At least one negative test per major abuse case.

See also:
- `overview.md`
- `review-hardening.md`
- `$CODEX_HOME/index/core/security.md`
