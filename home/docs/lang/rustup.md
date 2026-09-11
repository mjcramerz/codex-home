# rustup

Use this guide when you change Rust crates, workspaces, build tooling or async services. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Use this guide when

- pinning or updating Rust channels and components
- reviewing repo-local toolchain overrides versus user-global defaults
- checking how toolchain selection affects Cargo or rustc validation paths

## Baseline

- Prefer repo-local toolchain declarations such as `rust-toolchain.toml` over ad-hoc shell exports.
- Keep required components (`rustfmt`, `clippy`, targets) explicit and versioned with the repo.
- Avoid mutating a user-global toolchain when a repo-local override is sufficient.
- Document any CI-specific toolchain installation differences alongside local developer expectations.

## Validation ladder

1. Verify the resolved toolchain and components.
2. Check target and component requirements for the touched commands.
3. Run the smallest follow-up Cargo or rustc check that depends on the updated toolchain.
4. Recheck release or CI docs when toolchain pinning changes.

## After that, check related files

- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/index/domains/lang/rustup.md`
