# Dependency update workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-dependency-updates.md` before executing this workflow.
Purpose: update dependencies safely with minimal risk for the Codex coding agent.
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

## Steps
1) Batch by ecosystem (Cargo, pip, npm).
2) Review changelogs and breaking changes.
3) Run unit + integration tests.
4) Run security audits.
5) Prefer small PRs with tight scope.
6) Roll out with monitoring if runtime dependencies change.


## Hygiene checklist
- Ensure lockfiles are updated and committed.
- Watch for new transitive deps and risky install scripts (Node `postinstall`, etc.).
- For CI: prefer pinned actions (at least major version; pin to SHA for high assurance).
- You must re-run vulnerability scans after the update (`cargo audit`, OSV, `pip-audit`).

## Security checkpoints
- Review advisories, signatures, and installer behavior for each bumped dependency group.
- Block updates that add unreviewed install hooks, binaries, or high-risk transitive packages.
- Track temporary suppressions with advisory/CVE ID, owner, and expiry.

## Testing checkpoints
- You must run package-scoped tests first, then full regression for shared/runtime-critical dependencies.
- Review lockfile diffs for unexpected transitive changes and validate ABI/API compatibility.
- You must re-run vulnerability scans after merge-ready lockfiles are finalized.

## Deployment checkpoints
- Roll out runtime dependency bumps via canary or staged environments when blast radius is high.
- You must keep previous lockfile and artifact references ready for quick rollback.
- Monitor error, latency, and security signals with predefined rollback thresholds.

## Multi-agent handoff
- Updater provides changelog highlights, risk rank, and affected services per dependency.
- Tester hands minimal repro and failing evidence to the owning implementer.
- Release owner confirms lockfiles, scan reports, and rollout plan are attached to the PR.
See also:
- `overview.md`
- `ci-cd.md`
- `../security/supply-chain-controls.md`
- `$CODEX_HOME/index/pack/workflows.md`
