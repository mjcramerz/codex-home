# Contributing (template)
Purpose: tell the Codex coding agent how to use `templates/common/CONTRIBUTING.md` as a runtime-pack surface and when to stop browsing.

## Principles
- You must keep PRs small, cohesive, and reviewable.
- Preserve existing behavior unless the change is intentional and documented.
- You must prefer correctness first, then security, then performance, then polish.

## Before opening a PR
- You must run format + lint + tests locally (or document why not).
- You must add tests for behavior changes (including negative/security cases where applicable).
- You must update project runbooks/docs when user-visible behavior changes.
- Commit lockfile updates when dependencies change.

## PR description checklist
- What changed and why (link issue/ticket)
- How to test (exact commands)
- Risk assessment (security/perf/reliability)
- Rollout/migration notes (if applicable)

## Security
- You must treat all inputs as untrusted; validate and bound sizes/timeouts at trust boundaries.
- Never log secrets or request bodies by default.
- Avoid `eval`, shell interpolation with untrusted input, and unsafe deserialization.

## Support
- For security issues, follow the process in `SECURITY.md` (do not open a public issue).

Reference: `$CODEX_HOME/docs/security/review-hardening.md` and `$CODEX_HOME/docs/security/`.
