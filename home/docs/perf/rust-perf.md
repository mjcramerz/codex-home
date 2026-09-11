# Rust performance notes

Use this guide when you change Rust crates, workspaces, build tooling or async services. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Prefer `Bytes` for large buffers and zero-copy slicing.
- Minimize `clone()` and intermediate allocations.
- Avoid per-request global locks; use sharding or lock-free where possible.
- Use `tracing` spans with sampling/levels to avoid overhead.
- Prefer `&str`/slices over allocating `String`/`Vec` when lifetimes allow.
- Use `tokio::task::spawn_blocking` for CPU-bound work in async servers.
- Benchmark in `--release`; avoid drawing conclusions from debug builds.
- Validate with `cargo bench` or a reproducible load test when possible.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/perf/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

See also:
- `overview.md`
- `profiling.md`
- `$CODEX_HOME/index/core/perf.md`
