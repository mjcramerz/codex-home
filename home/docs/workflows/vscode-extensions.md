# VS Code extensions

You must start with `$CODEX_HOME/plans/workflows/workflow-vscode-extensions.md` before executing this workflow.
Purpose: guide creation and maintenance of VS Code extensions with secure, reproducible defaults for the Codex coding agent.
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

## Baseline structure
- `package.json` with `engines.vscode`, `activationEvents`, and `contributes`.
- `src/extension.ts` (or `extension.js`) as the entrypoint.
- `vscode:prepublish` script for build steps.
- `.vscodeignore` to avoid shipping dev files.

## Security and safety
- Avoid executing shell commands with user input.
- You must validate and bound all external data.
- You must keep telemetry opt-in and minimal, or omit entirely.
- Never log secrets or tokens.

## Testing
- Unit tests for helpers and parsers.
- Integration tests using the VS Code test runner.
- Ensure tests run headless in CI.

## Packaging and release
- You must use a pinned Node.js version and lockfile.
- Package with `vsce` or the official VS Code tooling.
- Sign or checksum release artifacts if required by policy.

## Security checkpoints
- Review activation events/commands for untrusted workspace input handling.
- Limit shell/process execution and sanitize any user-controlled arguments.
- Ensure telemetry and logs never contain tokens, secrets, or sensitive file paths.

## Testing checkpoints
- You must run unit tests plus VS Code integration tests on supported engine versions.
- Test in untrusted workspace and remote/container development scenarios.
- Package once and verify `.vscodeignore` excludes development-only artifacts.

## Deployment checkpoints
- Build and package with pinned Node/toolchain versions and lockfile install.
- Publish pre-release channel first, then promote to stable after error review.
- Archive VSIX checksum, package metadata, and rollback version pointer.

## Multi-agent handoff
- Coordinator defines target `engines.vscode` range and release channel strategy.
- Executor provides test matrix results, VSIX metadata, and changelog updates.
- Receiver owns marketplace publish decision, rollback trigger, and support triage.
See also:
- `overview.md`
- `../vscode/overview.md`
- You must use skill `devtools-vscode-extension`.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/vscode/vscode-extension.md`
