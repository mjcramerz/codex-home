# Crystal Dock workflow

Use this guide when the task concerns crystal dock workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-crystal-dock.md` before executing this workflow.

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

1. Confirm the dock command, PID-file path, and the Labwc autostart entrypoint first.
2. Keep start, stop, and restart behavior deterministic with explicit timeout handling.
3. Validate only the affected PID or restart path before widening to the broader desktop session.
4. Recheck Labwc or Waybar interactions only when the dock change actually affects them.

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

## After that, check related files

- `$CODEX_HOME/docs/desktop/crystal-dock.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/index/domains/desktop/crystal-dock.md`
- Read the `crystal-dock` skill only when its trigger matches this task and the skill is available.
