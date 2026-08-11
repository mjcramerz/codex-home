# VS Code overview
Purpose: route editor, devcontainer, settings, and extension-related work to the correct guide for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Scope
- Shared `settings.json` and workspace policy
- Devcontainers and remote/container development
- Theming and UX consistency
- Extension and marketplace hygiene

## Quick map
- Devcontainers: `devcontainer.md`
- Settings: `settings.md`
- Theming: `theming.md`
- Extension delivery/review workflow: `../workflows/vscode-extensions.md`

## You must enforce these guardrails
- You must keep workspace trust explicit.
- You must keep settings minimal and intentional.
- You must treat devcontainers as code: pin images, review mounts, and keep secrets out.
