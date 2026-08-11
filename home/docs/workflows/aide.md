# AIDE workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-aide.md` before executing this workflow.
Purpose: establish and monitor a file‑integrity baseline for the Codex coding agent.
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

## You must follow this workflow
1) **Scope**: critical paths and exclusions.
2) **Init**: generate a baseline database.
3) **Secure**: lock down DB and config permissions.
4) **Schedule**: run periodic checks.
5) **Review**: triage diffs and update baseline after approved changes.

## Safety rules
- You must keep the baseline offline or read‑only when possible.
- Avoid monitoring volatile directories.

## Security checkpoints
- You must require `aide.conf` and the baseline DB to stay root-owned and mode `0600`.
- Review include/exclude paths so volatile directories do not hide integrity drift.
- You must treat baseline refresh as a privileged change with approval and traceable owner.

## Testing checkpoints
- You must run `aide --check` on a clean host and capture the expected zero-drift output.
- You must create a controlled file change in a monitored path to prove detection and alert flow.
- You must verify scheduled runs write to the expected log target and rotation policy.

## Deployment checkpoints
- Roll out new rules in report-only mode before updating enforced baselines.
- You must keep the previous baseline snapshot for rollback after noisy or unexpected deltas.
- You must document who triages alerts, who approves baseline updates, and review cadence.

## Multi-agent handoff
- Coordinator provides monitored paths, approved exclusions, and baseline storage location.
- Executor hands off check output, noise findings, and any refreshed baseline artifacts.
- Receiver confirms timer/cron ownership and closes follow-up integrity exceptions.
See also:
- `overview.md`
- `../observability/aide.md`
- `$CODEX_HOME/templates/observability/aide-skeleton/`
- `$CODEX_HOME/snippets/aide/aide.conf`
- You must use skill `secops-aide`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/observability/aide.md`
