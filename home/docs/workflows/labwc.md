# Labwc workflow

Use this guide when the task concerns labwc workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-labwc.md` before executing this workflow.

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

1. Confirm the Labwc session owner, fallback TTY path, and compositor entrypoint first.
2. Keep compositor config, keybindings, and autostart helpers separated by responsibility.
3. Validate only the affected session helpers, output refresh, lock, or keybinding behavior.
4. Recheck related Waybar, Wofi, or Crystal Dock assumptions only when the Labwc change affects them directly.

## Safety rules

- Keep a fallback TTY or alternate session available.
- Avoid privileged commands in compositor or autostart helpers.

## Security checkpoints

- Ensure session config and helper scripts are user-owned and not group/world writable.
- Review environment injection and command invocation boundaries for autostart helpers.

## Testing checkpoints

- Test login/session start, keybindings, output refresh, and session restart behavior.
- Run the narrowest repo-local smoke checks for the changed Labwc helper path when available.

## Deployment checkpoints

- Keep a known-good session config snapshot for rollback.
- Communicate expected user impact before restarting active sessions.

## After that, check related files

- `$CODEX_HOME/docs/desktop/labwc.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/index/domains/desktop/labwc.md`
- Read the `labwc` skill only when its trigger matches this task and the skill is available.
