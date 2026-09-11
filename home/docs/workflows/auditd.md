# auditd workflow

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-auditd.md` before executing this workflow.

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

1. **Scope**: systems, log destinations, retention.
2. **Draft**: minimal ruleset focused on auth/privilege/integrity.
3. **Validate**: load rules in audit‑only mode.
4. **Apply**: enable enforcement and restart auditd.
5. **Verify**: check event volume and false positives.

## Safety rules

- Avoid broad syscall rules without filters.
- Keep audit logs rotated and protected.

## Security checkpoints

- Protect `/etc/audit/rules.d` and service controls so only privileged admins can modify rules.
- Ensure rules cover auth, privilege, and integrity events with explicit noise filters.
- Verify remote forwarding and storage targets use trusted, access-controlled channels.

## Testing checkpoints

- Validate rule load with `augenrules --check` and confirm active rules via `auditctl -l`.
- Trigger representative events (for example `sudo` and protected file edits) and verify records.
- Check backlog and drop counters to confirm sustained event throughput.

## Deployment checkpoints

- Stage by host class with an observation window before stricter enforcement.
- Keep prior rulesets ready for immediate rollback if noise spikes.
- Confirm retention and logrotate settings can absorb projected event volume.

## Multi-agent handoff

- Coordinator defines required event classes and acceptable false-positive levels.
- Executor hands off loaded rules, sample event IDs, and noise analysis.
- Receiver owns whitelist tuning decisions and tracks follow-up rule changes.
See also:
- `overview.md`
- `../observability/auditd.md`
- `$CODEX_HOME/templates/observability/auditd-rules-skeleton/`
- `$CODEX_HOME/snippets/auditd/audit.rules`
- Read the `secops-auditd` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/observability/auditd.md`
