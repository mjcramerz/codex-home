# Rust CLI Template (overview)
Purpose: tell the Codex coding agent how to use `templates/rust/cli-app/overview.md` as a runtime-pack surface and when to stop browsing.

## Quickstart
```bash
cargo run -- --help
cargo run -- --version
cargo test
```

## Logging
- `RUST_LOG=debug` (EnvFilter)
- `--log-format json` for structured logs
- `LOG_LEVEL` as a fallback when `RUST_LOG` is unset
- `LOG_FORMAT` can be set to `json` or `compact`

## Notes
- You must keep dependencies minimal and pinned.
- You must prefer typed errors and explicit exit codes.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- `.gitignore`
- `Cargo.toml`
- `rust-toolchain.toml`
- `src/`
- `tests/`

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/style/rust.md`
- Snippets: `$CODEX_HOME/snippets/rust/`
