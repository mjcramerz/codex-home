# Rust CLI Template (overview)

Use this template when you need rust cli template (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

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

- Keep dependencies minimal and pinned.
- Prefer typed errors and explicit exit codes.

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

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, check related files

- Docs: `$CODEX_HOME/docs/style/rust.md`
- Snippets: `$CODEX_HOME/snippets/rust/`
