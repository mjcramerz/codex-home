# Review hardening checklist
Purpose: tell the Codex coding agent how to use `docs/security/review-hardening.md` as a runtime-pack surface and when to stop browsing.
A practical, high-signal hardening checklist for code reviews.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Threat model (2 minutes)
- What is the trust boundary?
- Who can call this?
- What is the worst plausible abuse?
- What secrets exist and where do they flow?

## Web/API safety
- [ ] AuthN/AuthZ is explicit, minimal, and tested.
- [ ] CSRF protections for cookie-based auth.
- [ ] CORS is restrictive (no `*` with credentials).
- [ ] All inputs validated (schema + size limits).
- [ ] Output encoding / escaping (XSS-safe templates).
- [ ] Rate limits / quotas (or documented rationale for none).
- [ ] Safe file upload handling (type allowlist, size, storage path).
- [ ] SSRF defenses for outbound fetches (allowlist hosts, block link-local).
- [ ] Request body limits and timeouts configured to prevent slowloris/DoS.

## Secrets & privacy
- [ ] No secrets in logs.
- [ ] No secrets in config files / repo history.
- [ ] Errors don’t leak internal details to clients.
- [ ] PII handling is explicit (what is stored/logged/returned), with retention considerations.

## Dependency and supply chain
- [ ] Lockfile committed.
- [ ] Versions pinned.
- [ ] No new dependency without justification.
- [ ] No install scripts executed silently.
- [ ] Dependency audit integrated (npm/pip/cargo).

## OS / shell / subprocess
- [ ] No shell injection (avoid `sh -c`; prefer exec args).
- [ ] Paths normalized; no traversal.
- [ ] Atomic writes; avoid TOCTOU.
- [ ] File permissions sensible (no world-writable).
- [ ] No unsafe temp file handling; use `mktemp` and cleanup traps.

## Crypto
- [ ] No custom crypto.
- [ ] Secure RNG for tokens/keys.
- [ ] Password hashing uses argon2/bcrypt/scrypt with sane parameters.

## Observability
- [ ] Structured logs.
- [ ] Correlation IDs / request IDs.
- [ ] Metrics/tracing hooks for critical paths.

## Containers / CI
- [ ] Containers run as non-root; no privileged flags or docker-socket mounts.
- [ ] Network use is explicit (offline where possible).
- [ ] CI permissions are minimal and actions are pinned.

## Performance & reliability
- [ ] Timeouts on all I/O.
- [ ] Bounded retries with backoff + jitter.
- [ ] Resource limits (memory, concurrency).
- [ ] Avoids pathological big‑O and unbounded loops.
- [ ] Graceful shutdown / cancellation is considered for long-running tasks.

## Tests
- [ ] Added/updated tests cover success and failure cases.
- [ ] At least one integration test for cross-module flows.
- [ ] Negative tests for security boundaries.

See also:
- `overview.md`
- `threat-model.md`
- `../workflows/code-review.md`
- `$CODEX_HOME/index/core/security.md`
- `$CODEX_HOME/index/core/review-hardening.md`
