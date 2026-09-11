# sysctl workflow

Use this guide when the task concerns sysctl workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-sysctl.md` before executing this workflow.

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

1. **Scope**: role (server/desktop), security vs performance goals.
2. **Draft**: minimal drop‑in under `/etc/sysctl.d/`.
3. **Apply**: `sysctl --system` and validate values.
4. **Measure**: verify impact (latency, throughput, stability).
5. **Rollback**: remove drop‑in if regressions occur.

## Safety rules

- Avoid blanket “tuning packs” without testing.
- Keep a record of changes for audits.

## Security checkpoints

- Cross-check each parameter against host hardening and workload requirements.
- Keep overrides in dedicated drop-ins with root-only write access.
- Reject copied tuning values without trusted source and justification.

## Testing checkpoints

- Apply with `sysctl --system` (or scoped file load) and verify effective values.
- Run workload plus kernel-log checks for warnings, packet loss, or memory instability.
- Reboot validation host(s) to confirm persistent and safe startup behavior.

## Deployment checkpoints

- Roll out by host role with canary testing for high-impact network/memory knobs.
- Keep rollback drop-ins or previous parameter values ready for immediate restore.
- Monitor latency, throughput, and error counters after rollout.

## Multi-agent handoff

- Coordinator provides parameter list, rationale, and acceptable risk limits.
- When executing, report applied values, verification commands, and observed impact.
- Receiver owns long-run drift checks and follow-up retuning tasks.
See also:
- `overview.md`
- `../system/sysctl.md`
- `$CODEX_HOME/templates/system/sysctl-baseline/`
- `$CODEX_HOME/snippets/system/sysctl.conf`
- Read the `infra-sysctl` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/sysctl.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
