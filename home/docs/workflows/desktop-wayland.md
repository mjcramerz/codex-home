# Wayland desktop workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-desktop-wayland.md` before executing this workflow.
Purpose: configure a minimal Wayland desktop with Labwc and companion tools for the Codex coding agent.
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
1) Scope the stack: Labwc, Waybar, Wofi, lock or idle helpers, display manager, terminals, and any dock or notifier helpers.
2) Keep session ownership explicit: user-owned compositor helpers, system-owned greeter services, and no privileged commands in desktop autostart.
3) Configure minimal, versioned files under `~/.config/` or the designated system service locations.
4) Validate login, lock or unlock, monitor hotplug, launcher behavior, bar restart logic, and dock start or restart behavior with a fallback TTY available.

## Safety rules
- Keep a fallback TTY or alternate session.
- Avoid autostart scripts that run privileged commands.
- Prefer direct argv wrappers or desktop entries over shell-string launchers.

## Security checkpoints
- Ensure session config and startup scripts are user-owned and not group/world writable.
- Review autostart entries for privileged commands or unsafe environment injection.
- Confirm lock-screen and idle behavior protect active sessions.

## Testing checkpoints
- Test login, lock/unlock, monitor hotplug, and session recovery from a TTY fallback.
- Verify portal, clipboard, and screenshot permissions for allowed applications.
- Validate Labwc helper flows such as bar start, dock restart, launcher invocation, and output refresh using the narrowest repo-local smoke tests when available.

## Deployment checkpoints
- Roll out by host profile with backups of previous compositor configs.
- Keep a known-good config snapshot for quick restore after regressions.
- Schedule session restarts and communicate expected user impact.

## Multi-agent handoff
- Coordinator specifies compositor stack versions, display topology, and must-have apps.
- Executor shares config diffs plus login, lock, output, and launcher test results.
- Receiver manages per-user overrides and unresolved hardware quirks.

## See also
- `overview.md`
- `../desktop/wayland.md`
- `$CODEX_HOME/docs/desktop/labwc.md`
- `$CODEX_HOME/docs/desktop/waybar.md`
- `$CODEX_HOME/docs/desktop/wofi.md`
- `$CODEX_HOME/docs/desktop/crystal-dock.md`
- `$CODEX_HOME/templates/desktop/wayland-skeleton/`
- `$CODEX_HOME/snippets/desktop/`
- You must use skill `desktop-wayland`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/desktop/stack.md`
- `$CODEX_HOME/index/domains/desktop/wayland.md`
