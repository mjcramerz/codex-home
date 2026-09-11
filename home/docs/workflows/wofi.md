# Wofi workflow

Use this guide when the task concerns wofi workflow. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-wofi.md` before executing this workflow.

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

1. Confirm launcher mode, desktop entry source, and keybinding integration first.
2. Keep launcher config, styling, and wrapper commands explicit and reviewable.
3. Validate only the affected search, launch, or command-safety behavior.
4. Recheck Labwc integration only when the Wofi change affects the session entrypoint directly.

## Safety rules

- Prefer desktop entries or direct argv wrappers over inline shell command strings.
- Avoid privileged launch actions in launcher entries.

## Security checkpoints

- Validate command invocation boundaries and quoting.
- Review any wrapper scripts for unsafe interpolation or environment leakage.

## Testing checkpoints

- Test launcher invocation and the affected command path.
- Run the narrowest repo-local launcher smoke checks when available.

## Deployment checkpoints

- Keep a known-good launcher config snapshot for rollback.
- Call out any user-visible launch or search behavior changes that still need live confirmation.

## After that, check related files

- `$CODEX_HOME/docs/desktop/wofi.md`
- `$CODEX_HOME/docs/workflows/desktop-wayland.md`
- `$CODEX_HOME/index/domains/desktop/wofi.md`
- Read the `wofi` skill only when its trigger matches this task and the skill is available.
