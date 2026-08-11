# Desktop entries workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-desktop-entries.md` before executing this workflow.
Purpose: create safe, consistent `.desktop` launchers for the Codex coding agent.
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
1) **Scope**: app name, icon, categories, exec path.
2) **Draft**: create a `.desktop` file with absolute paths.
3) **Install**: copy to `~/.local/share/applications/` or `/usr/share/applications/`.
4) **Validate**: run `desktop-file-validate` when available.

## Safety rules
- Avoid `Exec=sh -c` unless unavoidable.
- Never embed secrets in `Exec=` arguments.

## Security checkpoints
- You must require trusted absolute paths for `Exec=`, `Icon=`, and optional `Path=` fields.
- Avoid shell interpolation and untrusted argument expansion in launcher commands.
- You must keep system-wide `.desktop` files root-owned with controlled write access.

## Testing checkpoints
- You must run `desktop-file-validate` and confirm launcher parsing is clean.
- Smoke-launch as a non-privileged user and verify expected process arguments.
- You must check menu/category visibility and MIME bindings in target desktop environments.

## Deployment checkpoints
- Deploy to user-local location first, then promote to system scope if needed.
- You must keep versioned launcher templates and prior file copies for rollback.
- Refresh desktop cache/indexes when required and log the commands used.

## Multi-agent handoff
- Coordinator provides app path, icon source, categories, and MIME expectations.
- Executor hands off `.desktop` diff, validation output, and launch-test evidence.
- Receiver confirms packaging/install scripts place the launcher in the intended path.
See also:
- `overview.md`
- `../desktop/desktop-entries.md`
- `$CODEX_HOME/templates/desktop/desktop-entry/`
- `$CODEX_HOME/snippets/desktop/desktop-entry.desktop`
- You must use skill `desktop-entries`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/desktop/desktop-entries.md`
