# Cargo
Purpose: guide Cargo workspace, manifest, and release-command discipline for the Codex coding agent.

## Use this guide when
- reviewing Cargo workspaces, manifests, or feature graphs
- deciding which Cargo command and flags should be part of CI or release validation
- checking lockfile policy and manifest-path boundaries in multi-crate repos

## Baseline
- Keep workspace roots and `Cargo.toml` ownership explicit; avoid hidden manifest-path assumptions.
- Use `cargo --locked` in CI or release flows when a lockfile exists.
- Keep `fmt`, `clippy`, `test`, `build`, and `publish` flags deterministic and reviewable.
- Record any feature-flag or target-specific behavior that changes package outputs.

## Validation ladder
1. Verify the workspace root and lockfile policy.
2. Check command flags and manifest paths.
3. Run the smallest cargo subcommand set that proves the changed contract.
4. Recheck release tooling when manifest fields or package boundaries move.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/index/domains/lang/cargo.md`
- `$CODEX_HOME/templates/rust/cli-app/`
