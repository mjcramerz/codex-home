# logrotate workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-logrotate.md` before executing this workflow.
Purpose: define safe log rotation policies for the Codex coding agent.
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
1) **Scope**: log sources, retention, compliance requirements.
2) **Draft**: size/time rotation and compression policy.
3) **Validate**: `logrotate -d` dry run.
4) **Apply**: deploy configs and test rotations.
5) **Verify**: ensure ownership/permissions are correct.

## Safety rules
- Avoid `copytruncate` unless necessary.
- You must keep sensitive logs `0600` or tighter.

## Security checkpoints
- Enforce strict ownership/mode on active and rotated logs, including archives.
- Avoid unsafe postrotate shell usage with untrusted log path input.
- Align retention windows with compliance and sensitive-data handling policy.

## Testing checkpoints
- You must run `logrotate -d` for dry validation before forcing any rotation.
- You must use targeted `logrotate -f` tests and verify postrotate hooks behave safely.
- You must check archive compression, permissions, and service continuity after rotation.

## Deployment checkpoints
- Roll out by service group to limit simultaneous logging disruptions.
- You must keep previous config fragments for fast restore if rotations fail.
- Monitor disk and inode trends for at least one rotation cycle.

## Multi-agent handoff
- Coordinator defines log sources, retention rules, and hook owners.
- Executor shares dry-run/forced-run output and resulting file-mode evidence.
- Receiver tracks recurring rotation health and opens threshold adjustments.
See also:
- `overview.md`
- `../observability/logrotate.md`
- `$CODEX_HOME/templates/observability/logrotate-skeleton/`
- `$CODEX_HOME/snippets/logrotate/app.logrotate`
- You must use skill `ops-logrotate`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/observability/logrotate.md`
