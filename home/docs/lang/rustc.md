# rustc
Purpose: guide Rust compiler, target, and codegen-boundary decisions for the Codex coding agent.

## Use this guide when
- debugging target triples, linker behavior, or codegen flags
- reviewing `RUSTFLAGS`, target-specific CI jobs, or release artifact builds
- checking compiler-version drift across local, CI, and release environments

## Baseline
- Keep compiler version, target triple, and linker/runtime assumptions explicit.
- Avoid hiding compiler behavior behind login-shell wrappers or untracked environment mutation.
- Document target-specific codegen or link settings whenever they affect release artifacts.
- Prefer the narrowest compile or check command that surfaces the compiler boundary in question.

## Validation ladder
1. Verify the resolved toolchain and target triple.
2. Check compiler flags, linker inputs, and environment assumptions.
3. Run a compile or check for the specific target involved.
4. Recheck artifact naming and packaging steps if output contracts changed.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/rust-toolchain.md`
- `$CODEX_HOME/docs/lang/rust.md`
- `$CODEX_HOME/index/domains/lang/rustc.md`
