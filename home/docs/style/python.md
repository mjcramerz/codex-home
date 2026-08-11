# Python style guide
Purpose: tell the Codex coding agent how to use `docs/style/python.md` as a runtime-pack surface and when to stop browsing.
Canonical Python guidance for this pack. Follow repo-specific conventions first.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/style/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline
- Target Python 3.11+ unless repo constraints say otherwise.
- You must prefer type hints everywhere; use `mypy` or `pyright` when the repo supports it.
- You must prefer `ruff` for linting and formatting; keep configuration in `pyproject.toml`.

## Structure
- You must prefer explicit packages/modules; avoid circular imports.
- You must keep I/O at the edges; keep core logic pure and testable.
- You must use `pydantic`/`pydantic-settings` only when it meaningfully improves validation.

## Errors
- Raise specific exceptions.
- Map internal exceptions to safe external errors (don’t leak internals).
- For APIs: centralize error mapping (HTTP status + redacted message) and log the internal error.

## Security
- No `eval`, no `pickle` for untrusted input.
- You must validate inputs at boundaries; enforce size limits.
- You must use `secrets` for tokens; use `hashlib`/`hmac` correctly; no custom crypto.
- HTTP clients must set timeouts and avoid redirect surprises; prefer `trust_env=False` unless you control the environment.
- Avoid SSRF: never fetch arbitrary user-provided URLs without host allowlists and private-IP blocking.

## Performance
- Avoid quadratic string concatenation; prefer `''.join(...)`.
- Stream large files instead of buffering whole content.
- You must add timeouts to requests; keep retries bounded.
- You must prefer context managers for resources (`with open(...)`, `with httpx.Client(...)`).

## Logging
- Default to structured logs to stderr; keep stdout for machine output.
- Include request-id/correlation-id when applicable.
- Never log secrets or request bodies by default.

## References
- `overview.md`
- Snippets: `$CODEX_HOME/snippets/python/`
- Docs: `../security/logging.md`, `../security/web-hardening.md`
- Skill: Use skill backend-fastapi. (when building APIs)
- `$CODEX_HOME/index/pack/style.md`
- `$CODEX_HOME/index/style/python.md`
