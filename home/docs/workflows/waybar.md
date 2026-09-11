# Waybar workflow

Use this guide when the task concerns waybar workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-waybar.md` before executing this workflow.

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

1. Confirm the Waybar startup path, config owner, and whether custom module helpers are involved.
2. Keep JSONC config, CSS, and helper scripts separated so regressions stay local.
3. Validate only the affected modules, restart behavior, and duplicate-process prevention.
4. Recheck Labwc or launcher assumptions only when bar startup depends on them.

## Safety rules

- Avoid shell-string module commands when direct executables or dedicated helpers will work.
- Keep bar restart logic idempotent.

## Security checkpoints

- Bound custom module script input and output.
- Review helper script execution and environment inheritance for unsafe behavior.

## Testing checkpoints

- Test startup, restart, and module rendering for the touched modules.
- Run the narrowest repo-local Waybar or session smoke checks when available.

## Deployment checkpoints

- Keep a known-good bar config snapshot for rollback.
- Note any user-visible module or style regressions that still need live confirmation.

## After that, check related files

- `$CODEX_HOME/docs/desktop/waybar.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/index/domains/desktop/waybar.md`
- Read the `waybar` skill only when its trigger matches this task and the skill is available.
