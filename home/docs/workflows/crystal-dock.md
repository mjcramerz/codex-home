# Crystal Dock workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-crystal-dock.md` before executing this workflow.
Purpose: guide Crystal Dock-specific startup, restart, and PID-file behavior for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) Confirm the dock command, PID-file path, and the Labwc autostart entrypoint first.
2) Keep start, stop, and restart behavior deterministic with explicit timeout handling.
3) Validate only the affected PID or restart path before widening to the broader desktop session.
4) Recheck Labwc or Waybar interactions only when the dock change actually affects them.

## Safety rules
- Keep the dock process user-owned and avoid privileged restart helpers.
- Do not use ambiguous shell wrappers when the dock command can be invoked directly.

## Security checkpoints
- Validate PID-file ownership and location.
- Review restart helpers for unsafe process matching or unbounded kill behavior.

## Testing checkpoints
- Test start, stop, and restart behavior with the narrowest dock smoke checks available.
- Confirm restart waits for the previous process to exit when that contract exists.

## Deployment checkpoints
- Keep a known-good dock launcher config snapshot for rollback.
- Note any user-visible launch timing or restart behavior that still needs live confirmation.

## After that, you must check related files
- `$CODEX_HOME/docs/desktop/crystal-dock.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/index/domains/desktop/crystal-dock.md`
- You must use skill `crystal-dock`.
