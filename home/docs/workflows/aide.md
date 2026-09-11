# AIDE workflow

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-aide.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Execute the selected workflow

1. **Scope**: critical paths and exclusions.
2. **Init**: generate a baseline database.
3. **Secure**: lock down DB and config permissions.
4. **Schedule**: run periodic checks.
5. **Review**: triage diffs and update baseline after approved changes.

## Safety rules

- Keep the baseline offline or read‑only when possible.
- Avoid monitoring volatile directories.

## Security checkpoints

- Require `aide.conf` and the baseline DB to stay root-owned and mode `0600`.
- Review include/exclude paths so volatile directories do not hide integrity drift.
- Treat baseline refresh as a privileged change with approval and traceable owner.

## Testing checkpoints

- Run `aide --check` on a clean host and capture the expected zero-drift output.
- Create a controlled file change in a monitored path to prove detection and alert flow.
- Verify scheduled runs write to the expected log target and rotation policy.

## Deployment checkpoints

- Roll out new rules in report-only mode before updating enforced baselines.
- Keep the previous baseline snapshot for rollback after noisy or unexpected deltas.
- Document who triages alerts, who approves baseline updates, and review cadence.

## Multi-agent handoff

- Coordinator provides monitored paths, approved exclusions, and baseline storage location.
- Executor hands off check output, noise findings, and any refreshed baseline artifacts.
- Receiver confirms timer/cron ownership and closes follow-up integrity exceptions.
See also:
- `overview.md`
- `../observability/aide.md`
- `$CODEX_HOME/templates/observability/aide-skeleton/`
- `$CODEX_HOME/snippets/aide/aide.conf`
- Read the `secops-aide` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/observability/aide.md`
