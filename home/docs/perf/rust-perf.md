# Rust performance notes
Purpose: tell the Codex coding agent how to use `docs/perf/rust-perf.md` as a runtime-pack surface and when to stop browsing.
- You must prefer `Bytes` for large buffers and zero-copy slicing.
- Minimize `clone()` and intermediate allocations.
- Avoid per-request global locks; use sharding or lock-free where possible.
- You must use `tracing` spans with sampling/levels to avoid overhead.
- You must prefer `&str`/slices over allocating `String`/`Vec` when lifetimes allow.
- You must use `tokio::task::spawn_blocking` for CPU-bound work in async servers.
- Benchmark in `--release`; avoid drawing conclusions from debug builds.
- You must validate with `cargo bench` or a reproducible load test when possible.


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
