# Profiling playbook

Use this guide when the task concerns profiling playbook. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

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
- Use `tokio-console` for async visibility (if available).
- Use `perf`/`dtrace`/`Instruments` depending on OS.
- Add criterion benchmarks for critical algorithms.
- Prefer flamegraphs for CPU hot paths; keep profiles attached to a reproducible input.

## Python

- Use `cProfile` and `pstats` for CPU.
- Use `py-spy` for sampling profiling.
- Use `tracemalloc` for allocations.
- For async: identify blocking calls.
- For services: measure p50/p95/p99 latencies and error rates before/after.

## Output

- Before/after numbers
- The bottleneck you removed
- Why it was bottlenecking (allocations, lock contention, I/O)
- A regression guard (test/benchmark)

## Notes

- Keep profiling inputs reproducible and stored in the repo when feasible.

See also:
- `overview.md`
- `python-perf.md`
- `rust-perf.md`
- Read the `perf-profiling` skill only when its trigger matches this task and the skill is available.
- `$CODEX_HOME/index/core/perf.md`
