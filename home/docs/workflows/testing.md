# Testing workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-testing.md` before executing this workflow.
Purpose: build a fast, layered test suite that protects correctness and security for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Testing philosophy
- Fast unit tests for core logic.
- Integration tests for boundaries (HTTP, DB, CLI, filesystem).
- Security regressions as tests (negative cases).
- Deterministic and hermetic where possible.

## Layered strategy
1) **Unit tests** for pure logic and invariants (fast, deterministic).
2) **Integration tests** for boundaries (HTTP/DB/filesystem/CLI).
3) **Property tests** for parsers/serializers where valuable.
4) **Security regression tests** for trust boundaries (authz, validation, SSRF, path traversal).

## Hermeticity
- Tests should not require network by default.
- You must use fixtures and local containers only when necessary (and time-box them).
- Seed RNG for deterministic tests.
- Avoid wall-clock dependencies; inject clocks or use time-freezing tools.
- You must keep filesystem tests in temp dirs; clean up deterministically.

## CI strategy
- You must run fast checks on every push.
- You must run slower suites on a schedule or on-demand.
- Time-box tests and track slowest tests to keep the suite healthy.

## Minimum bar for changes
- Bugfix: add a failing test first (when feasible), then fix.
- Security-sensitive change: add at least one negative test (attack/abuse case).

## Suggested commands (examples)
- Python: `python -m ruff check . && python -m ruff format --check . && pytest -q`
- Rust: `cargo fmt --check && cargo clippy -- -D warnings && cargo test`
- Node: `npm run lint && npm test && npm run build`

## Codex source command profile
- Workspace runner: `just test` (Rust `cargo nextest`) and `just fmt` / `just fix -p <crate>`.
- Rust checks: `cargo clippy --workspace --all-targets -- -D warnings`, targeted `cargo nextest run -p <crate>`.
- TypeScript tooling checks: `pnpm -r lint`, `pnpm -r test`, `pnpm -r build`, and package-scoped `tsup` builds.
- If the active codebase ships repo-hygiene helpers, run them alongside the language-specific checks for that codebase.

## Security checkpoints
- Include negative tests for auth, input validation, and boundary abuse on changed surfaces.
- You must keep fixtures free of real secrets and disable outbound network unless explicitly required.
- You must add regression tests for any prior vulnerability before closing the issue.

## Testing checkpoints
- You must define tiered commands (quick, full, nightly) with time budgets and ownership.
- You must require deterministic seeds/fixtures for flaky areas and track quarantined tests explicitly.
- Map each changed module to at least one validating test so coverage gaps stay visible.

## Deployment checkpoints
- Map test suites to release gates: pre-merge, pre-release, and post-deploy smoke checks.
- Fail promotion when critical-path tests are skipped/quarantined without approved exception.
- Archive test artifacts/logs needed for rollback and post-incident analysis.

## Multi-agent handoff
- Test author hands fixtures, seeds, and command list needed to reproduce failures exactly.
- Implementer returns fix commits plus updated tests and expected outputs to the test owner.
- Release owner receives final pass matrix, known quarantines, and residual testing risk.
See also:
- `overview.md`
- `codex-repo.md`
- `code-review.md`
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/core/testing.md`
