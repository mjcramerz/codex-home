# VS Code extensions

Use this guide when the task concerns vs code extensions. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-vscode-extensions.md` before executing this workflow.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Plan

- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- Keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## Baseline structure

- `package.json` with `engines.vscode`, `activationEvents`, and `contributes`.
- `src/extension.ts` (or `extension.js`) as the entrypoint.
- `vscode:prepublish` script for build steps.
- `.vscodeignore` to avoid shipping dev files.

## Security and safety

- Avoid executing shell commands with user input.
- Validate and bound all external data.
- Keep telemetry opt-in and minimal, or omit entirely.
- Never log secrets or tokens.

## Testing

- Unit tests for helpers and parsers.
- Integration tests using the VS Code test runner.
- Ensure tests run headless in CI.

## Packaging and release

- Use a pinned Node.js version and lockfile.
- Package with `vsce` or the official VS Code tooling.
- Sign or checksum release artifacts if required by policy.

## Security checkpoints

- Review activation events/commands for untrusted workspace input handling.
- Limit shell/process execution and sanitize any user-controlled arguments.
- Ensure telemetry and logs never contain tokens, secrets, or sensitive file paths.

## Testing checkpoints

- Run unit tests plus VS Code integration tests on supported engine versions.
- Test in untrusted workspace and remote/container development scenarios.
- Package once and verify `.vscodeignore` excludes development-only artifacts.

## Deployment checkpoints

- Build and package with pinned Node/toolchain versions and lockfile install.
- Publish pre-release channel first, then promote to stable after error review.
- Archive VSIX checksum, package metadata, and rollback version pointer.

## Multi-agent handoff

- Coordinator defines target `engines.vscode` range and release channel strategy.
- When executing, provide test matrix results, VSIX metadata, and changelog updates.
- Receiver owns marketplace publish decision, rollback trigger, and support triage.
See also:
- `overview.md`
- `../vscode/overview.md`
- Read the `devtools-vscode-extension` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/pack/workflows.md`
- `$CODEX_HOME/index/domains/vscode/vscode-extension.md`
