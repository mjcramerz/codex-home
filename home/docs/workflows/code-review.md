# Code review workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-code-review.md` before executing this workflow.
Purpose: consistent, high-signal reviews with minimal noise for the Codex coding agent.
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

## Review steps
1) Read intent (issue/PR description).
2) Validate diff is minimal and cohesive.
3) Run targeted tests (or propose the minimal set).
4) Perform security pass (`../security/review-hardening.md`).
5) Perform perf pass (`../perf/overview.md`) if the change touches hot paths.

## Output format
- Summary (intent vs diff)
- Must-fix issues (correctness/security)
- Suggestions (maintainability/perf)
- Tests to run (exact commands)
- Security notes
- Perf notes

## High-signal checks
- **Correctness**: edge cases, error paths, invariants, backwards compatibility.
- **Security**: trust boundaries, input validation, timeouts, secrets handling, injection risks.
- **Reliability**: retries/backoff, cancellation, resource bounds, graceful shutdown.
- **Maintainability**: readability, modularity, clear ownership of responsibilities.


## Security checkpoints
- Review auth, input parsing, subprocess, and secret-touching diffs first; escalate must-fix issues.
- You must verify CI/workflow permission changes use least privilege and document any broad scope.
- You must require explicit rationale and expiry for waived security findings before approval.

## Testing checkpoints
- Reviewer states exact commands run (or required) and maps them to changed risk areas.
- Request targeted regression tests for uncovered paths instead of approving on green CI alone.
- Flag flaky or skipped tests as blockers when they hide impacted behavior.

## Deployment checkpoints
- Call out required migrations, feature flags, or runbook updates before approving risky diffs.
- Ensure rollback path is documented for user-visible or data-shape changes.
- Block approval when release impact is unknown or ownership is unclear.

## Multi-agent handoff
- Primary reviewer assigns owners for must-fix comments and tracks closure by commit reference.
- Author responds with evidence per comment (tests, logs, rationale), not "fixed" only.
- Final approver confirms security/testing/deploy blockers are closed before merge.
See also:
- `overview.md`
- `../security/review-hardening.md`
- `../perf/overview.md`
- `$CODEX_HOME/index/pack/workflows.md`
