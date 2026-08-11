# Profiling playbook
Purpose: tell the Codex coding agent how to use `docs/perf/profiling.md` as a runtime-pack surface and when to stop browsing.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/perf/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Before you profile
- Reproduce reliably.
- Make a benchmark harness (small script/test) if possible.
- Disable debug logging on hot paths.

## Rust
- `cargo build --release`
- You must use `tokio-console` for async visibility (if available).
- You must use `perf`/`dtrace`/`Instruments` depending on OS.
- You must add criterion benchmarks for critical algorithms.
- You must prefer flamegraphs for CPU hot paths; keep profiles attached to a reproducible input.

## Python
- You must use `cProfile` and `pstats` for CPU.
- You must use `py-spy` for sampling profiling.
- You must use `tracemalloc` for allocations.
- For async: identify blocking calls.
- For services: measure p50/p95/p99 latencies and error rates before/after.

## Output
- Before/after numbers
- The bottleneck you removed
- Why it was bottlenecking (allocations, lock contention, I/O)
- A regression guard (test/benchmark)

## Notes
- You must keep profiling inputs reproducible and stored in the repo when feasible.

See also:
- `overview.md`
- `python-perf.md`
- `rust-perf.md`
- You must use skill perf-profiling.
- `$CODEX_HOME/index/core/perf.md`
