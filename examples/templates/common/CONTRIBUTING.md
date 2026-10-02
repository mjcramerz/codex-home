# Contributing (template)

Use this template when you need contributing (template) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

## Principles

- Keep PRs small, cohesive, and reviewable.
- Preserve existing behavior unless the change is intentional and documented.
- Prefer correctness first, then security, then performance, then polish.

## Before opening a PR

- Run format + lint + tests locally (or document why not).
- Add tests for behavior changes (including negative/security cases where applicable).
- Update project runbooks/docs when user-visible behavior changes.
- Commit lockfile updates when dependencies change.

## PR description checklist

- What changed and why (link issue/ticket)
- How to test (exact commands)
- Risk assessment (security/perf/reliability)
- Rollout/migration notes (if applicable)

## Security

- Treat all inputs as untrusted; validate and bound sizes/timeouts at trust boundaries.
- Never log secrets or request bodies by default.
- Avoid `eval`, shell interpolation with untrusted input, and unsafe deserialization.

## Support

- For security issues, follow the process in `SECURITY.md` (do not open a public issue).

Reference: `$CODEX_HOME/docs/security/review-hardening.md` and `$CODEX_HOME/docs/security/`.
