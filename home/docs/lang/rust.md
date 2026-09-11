# Rust

Use this guide when you change Rust crates, workspaces, build tooling or async services. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Read Cargo.toml, Cargo.lock, rust-toolchain.toml, feature flags and MSRV before choosing APIs. Preserve the workspace's dependency and error-handling conventions.

**2.** Model invalid states explicitly with enums and Result. Propagate useful errors, avoid unwrap on external input, and keep unsafe blocks minimal with written invariants.

**3.** Bound allocation, channel sizes, retries and external I/O. Handle cancellation and deadlines in async tasks; do not hold blocking locks across await.

**4.** Use tracing fields for structured, redacted diagnostics. Keep secrets out of Debug output, panics and error chains.

**5.** Run the repository's targeted cargo fmt, clippy, build and tests with the selected feature set and lockfile policy. Do not equate one host build with cross-platform or all-feature coverage.

## Select related guidance

- `$CODEX_HOME/docs/style/rust.md`
- `$CODEX_HOME/docs/lang/cargo.md`
- `$CODEX_HOME/docs/lang/rustc.md`
- `$CODEX_HOME/docs/lang/rustup.md`
- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/index/domains/lang/rust.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
