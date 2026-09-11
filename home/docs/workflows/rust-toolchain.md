# Rust toolchain workflow

Use this guide when you change Rust crates, workspaces, build tooling or async services. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Start with `$CODEX_HOME/plans/workflows/workflow-rust-toolchain.md` before executing this workflow.

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

1. Confirm toolchain version, Cargo workspace root, required components, target triples, and lockfile policy first.
2. Keep repo-local overrides explicit and avoid silent user-global toolchain mutation.
3. Treat Cargo manifests and release flags as part of the same toolchain contract, then separate compiler/debugging checks from broader workspace validation or release actions.
4. Validate with the narrowest cargo or rustc commands that prove the changed contract.

## Safety rules

- Preserve behavior unless the task explicitly changes it.
- Keep secrets, tokens, and machine-specific state out of tracked assets.

## Security checkpoints

- Confirm trust boundaries, credentials, and least-privilege assumptions before execution.
- Validate input bounds, timeout or retry limits, and failure behavior for risky operations.
- Record any approved exception, owner, and expiry before proceeding.

## Testing checkpoints

- Define fast-path and deep validation commands before making changes.
- Re-run impacted checks after major changes and before final handoff.

## Deployment checkpoints

- Document rollout order, blast-radius controls, and rollback conditions.
- Record post-deploy verification owners and evidence.

## Multi-agent handoff

- When coordinating, hand off scope, constraints, and stop condition with the target entrypoint.
- When executing, report touched files, commands run, evidence, blockers, and next action.
- When receiving work, acknowledge handoff completeness before continuing execution.

## After that, check related files

- $CODEX_HOME/docs/lang/rust.md
- $CODEX_HOME/docs/lang/cargo.md
- $CODEX_HOME/docs/lang/rustc.md
- $CODEX_HOME/docs/lang/rustup.md
- $CODEX_HOME/index/domains/lang/cargo.md
- $CODEX_HOME/index/domains/lang/rustc.md
- $CODEX_HOME/index/domains/lang/rustup.md
