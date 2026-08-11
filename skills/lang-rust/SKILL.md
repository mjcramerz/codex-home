---
name: lang-rust
description: Build Rust workspaces with cargo fmt, clippy, locked builds, and targeted test guidance.
metadata:
  version: '1.0'
  short-description: Build Rust workspaces with cargo defaults
  tags:
  - rust
  - cargo
  - workspace
  - release
interface:
  display-name: LANG-Rust
  short-description: Build Rust workspaces with cargo defaults
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#C44A2A'
  default-prompt: Act as the "LANG-Rust" specialist for "Build Rust workspaces with cargo defaults". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# LANG-Rust

## Use this skill when
- editing Rust crates or Cargo workspace configuration
- mapping release/build commands into CI or docs
- tightening Rust validation defaults before handoff

## Workflow
1) Confirm the crate/workspace scope and toolchain pin.
2) Run fast formatting and lint gates first.
3) Use locked, targeted builds/tests before broader release checks.
4) Keep packaging, schema generation, and release mutation steps explicit.

## Agent orchestration
- Delegate read-only discovery only.
- Keep one owner for final code edits and validation output.

## Validation and testing
- Run `cargo fmt --check`.
- Run `cargo clippy --workspace --all-targets -- -D warnings` when applicable.
- Run targeted `cargo test` or `cargo nextest` for impacted crates.

## Outputs
- Reviewable Rust/Cargo changes with explicit validation evidence.

## References
- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/docs/style/rust.md`
- `$CODEX_HOME/docs/workflows/testing.md`
