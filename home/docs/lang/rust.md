# Rust
Purpose: guide Rust, Cargo, rustc, and rustup work across release flows and
validation-heavy runtime integrations for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

## Use this guide when
- working in a Rust repo where Cargo workspace or rustup behavior matters
- mapping source-repo commands into pack docs or CI templates
- reviewing compiler, toolchain, lint, or packaging expectations for Rust projects

## Baseline
- Prefer pinned toolchains via `rust-toolchain.toml`.
- Keep `cargo fmt --check`, `cargo clippy -- -D warnings`, and targeted tests in the default validation path.
- Use `cargo --locked` in CI and release flows when a lockfile exists.
- Keep `rustc` target, linker, and codegen assumptions explicit when they affect artifacts.
- Keep `rustup` component and target selection explicit; prefer repo-local overrides over user-global shell mutation.
- Treat Cargo manifests, lockfiles, and command flags as part of the same Rust toolchain surface, not a separate operational silo.
- Keep release packaging and schema/config regeneration steps explicit in docs and plans.

## Validation ladder
1. `cargo fmt --check`
2. `cargo clippy --workspace --all-targets -- -D warnings`
3. targeted `cargo test` or `cargo nextest`
4. target-specific `rustc` or build checks only when the task touches compiler, target, or packaging behavior
5. release or package checks only when the task touches publishing

## After that, you must check related files
- `$CODEX_HOME/docs/style/rust.md`
- `$CODEX_HOME/docs/lang/cargo.md`
- `$CODEX_HOME/docs/lang/rustc.md`
- `$CODEX_HOME/docs/lang/rustup.md`
- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/index/domains/lang/rust.md`
