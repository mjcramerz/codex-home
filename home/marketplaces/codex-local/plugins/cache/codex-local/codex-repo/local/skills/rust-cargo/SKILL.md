---
name: rust-cargo
description: Edit Rust/Cargo projects with explicit Cargo, rustc, rustup, fmt, clippy, test, locked-build, and release packaging guidance.
metadata:
  version: '1.0'
  short-description: Cargo workspace, release, and validation workflows
  tags:
  - rust-cargo
interface:
  display-name: Rust Cargo
  short-description: Cargo workspace, release, and validation workflows
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C2410C'
  default-prompt: Act as the "Rust Cargo" specialist for "Cargo workspace, release, and validation workflows". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- the task directly targets the Rust or Cargo repository/domain surface
- repo contracts, CI, compiler, or toolchain behavior must stay aligned with the active source tree
- validation evidence is needed for a cross-file operational change

## Workflow
1) Read the repo anchors in `references/latest-sources.md`.
2) Confirm the smallest affected surface before editing.
3) Keep secrets, runtime-only state, and generated artifacts out of source-controlled changes.
4) Run the narrowest Cargo, rustc, or rustup checks that prove the change.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final edits and verification output.

## Validation and testing
- Reparse structured config after mutation.
- Run repo-local lint/test/build commands when the touched surface ships them.
- Record residual gaps when external credentials or infrastructure are required for deeper verification.

## Outputs
- Reviewable changes with explicit validation evidence.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rust-cargo/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/codex-repo/local/skills/rust-cargo/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/lang/cargo.md`
- `$CODEX_HOME/docs/lang/rustc.md`
- `$CODEX_HOME/docs/lang/rustup.md`
- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/docs/workflows/codex-manager.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- `$CODEX_HOME/docs/workflows/codex-mcp.md`
