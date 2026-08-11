# sysctl workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-sysctl.md` before executing this workflow.
Purpose: apply sysctl changes safely and measurably for the Codex coding agent.
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
1) **Scope**: role (server/desktop), security vs performance goals.
2) **Draft**: minimal drop‑in under `/etc/sysctl.d/`.
3) **Apply**: `sysctl --system` and validate values.
4) **Measure**: verify impact (latency, throughput, stability).
5) **Rollback**: remove drop‑in if regressions occur.

## Safety rules
- Avoid blanket “tuning packs” without testing.
- You must keep a record of changes for audits.

## Security checkpoints
- Cross-check each parameter against host hardening and workload requirements.
- You must keep overrides in dedicated drop-ins with root-only write access.
- Reject copied tuning values without trusted source and justification.

## Testing checkpoints
- Apply with `sysctl --system` (or scoped file load) and verify effective values.
- You must run workload plus kernel-log checks for warnings, packet loss, or memory instability.
- Reboot validation host(s) to confirm persistent and safe startup behavior.

## Deployment checkpoints
- Roll out by host role with canary testing for high-impact network/memory knobs.
- You must keep rollback drop-ins or previous parameter values ready for immediate restore.
- Monitor latency, throughput, and error counters after rollout.

## Multi-agent handoff
- Coordinator provides parameter list, rationale, and acceptable risk limits.
- Executor reports applied values, verification commands, and observed impact.
- Receiver owns long-run drift checks and follow-up retuning tasks.
See also:
- `overview.md`
- `../system/sysctl.md`
- `$CODEX_HOME/templates/system/sysctl-baseline/`
- `$CODEX_HOME/snippets/system/sysctl.conf`
- You must use skill `infra-sysctl`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/sysctl.md`
- `$CODEX_HOME/index/domains/system/hardening.md`
