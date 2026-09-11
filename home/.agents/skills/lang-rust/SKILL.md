---
name: lang-rust
description: Use this skill to build Rust workspaces with cargo fmt, clippy, locked
  builds, and targeted test guidance.
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
  default-prompt: Act as the "LANG-Rust" specialist for "Build Rust workspaces with
    cargo defaults". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Lang Rust

## Workflow

1. Read Cargo.toml, Cargo.lock, rust-toolchain.toml, feature flags and MSRV before choosing APIs. Preserve the workspace's dependency and error-handling conventions.

2. Model invalid states explicitly with enums and Result. Propagate useful errors, avoid unwrap on external input, and keep unsafe blocks minimal with written invariants.

3. Bound allocation, channel sizes, retries and external I/O. Handle cancellation and deadlines in async tasks; do not hold blocking locks across await.

4. Use tracing fields for structured, redacted diagnostics. Keep secrets out of Debug output, panics and error chains.

5. Run the repository's targeted cargo fmt, clippy, build and tests with the selected feature set and lockfile policy. Do not equate one host build with cross-platform or all-feature coverage.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/docs/style/rust.md`
- `$CODEX_HOME/docs/workflows/testing.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
