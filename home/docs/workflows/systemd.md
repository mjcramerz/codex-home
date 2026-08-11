# systemd workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-systemd.md` before executing this workflow.
Purpose: design, harden, and install systemd services and timers for the Codex coding agent.
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
1) **Clarify intent**: system vs user service, ExecStart, user/group, working dir, dependencies, restart policy.
2) **Draft unit**: service file with explicit timeouts and environment file.
3) **Harden**: add safe defaults (`NoNewPrivileges`, `ProtectSystem`, etc.).
4) **Validate**: `systemd-analyze verify` if available.
5) **Install**: copy to `/etc/systemd/system/` (or `~/.config/systemd/user/` for user units), `daemon-reload`, `enable --now`.
6) **Observe**: check `journalctl -u <unit>`, ensure clean startup/shutdown.
7) **Timers** (if needed): create `.timer`, enable, and verify with `list-timers`.

## Safety rules
- Avoid `sh -c` and shell pipelines in `ExecStart=`.
- You must run as non-root unless explicitly required.
- You must keep secrets in env files or secret managers, not unit files.

## Security checkpoints
- You must require least-privilege unit settings (`User=`, capabilities, filesystem protection).
- You must verify secret handling via protected env files instead of inline unit values.
- Review dependency graph to avoid unintended privileged execution paths.

## Testing checkpoints
- You must run `systemd-analyze verify` and resolve warnings before enabling units.
- Test start/stop/restart cycles and confirm clean status and exit codes.
- For timers, validate schedule firing and missed-run behavior with `list-timers`.

## Deployment checkpoints
- Deploy to canary host/user first, then `enable --now` after soak success.
- You must keep previous unit revisions and documented `daemon-reload` rollback steps.
- Monitor journal output and restart counters during initial runtime window.

## Multi-agent handoff
- Coordinator specifies unit purpose, runtime identity, and hardening baseline.
- Executor hands off unit/timer diffs, verify output, and runtime logs.
- Receiver confirms ownership docs, alert routes, and pending hardening follow-ups.
## References
- `overview.md`
- `../systemd/overview.md`
- `../systemd/service-units.md`
- `../systemd/timers.md`
- `../systemd/hardening.md`
- `../systemd/user-units.md`
- `$CODEX_HOME/templates/systemd/service-skeleton/`
- `$CODEX_HOME/templates/systemd/user-service-skeleton/`
- `$CODEX_HOME/snippets/systemd/service.unit`
- `$CODEX_HOME/snippets/systemd/timer.unit`
- `$CODEX_HOME/snippets/systemd/user-service.unit`
- You must use skill `infra-systemd`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/system/systemd.md`
