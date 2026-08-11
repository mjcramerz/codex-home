# Performance playbook
Purpose: tell the Codex coding agent how to use `docs/perf/overview.md` as a runtime-pack surface and when to stop browsing.
Performance playbook for Codex-driven changes.


## Contents
<!-- BEGIN:contents -->
- `$CODEX_HOME/docs/perf/profiling.md` — Profiling playbook
- `$CODEX_HOME/docs/perf/python-perf.md` — Python performance notes
- `$CODEX_HOME/docs/perf/rust-perf.md` — Rust performance notes
<!-- END:contents -->


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Philosophy
- Optimize **after** correctness and safety.
- Measure first. Prefer profiling over speculation.
- Focus on asymptotics and I/O before micro-optimizations.

## Checklist
### Hot path identification
- [ ] Identify critical request paths / loops.
- [ ] Confirm with profiling (CPU) and tracing (latency).

### Algorithmic / structural
- [ ] Avoid quadratic growth (nested scans, repeated parsing).
- [ ] Use indexes/maps/sets appropriately.
- [ ] Stream large data instead of buffering.
- [ ] Reduce allocations and copies.

### Concurrency
- [ ] Choose async vs threads intentionally.
- [ ] Bound concurrency (semaphores/worker pools).
- [ ] Avoid shared mutable state; keep locks tight.

### I/O
- [ ] Add timeouts to network and filesystem I/O.
- [ ] Use buffered I/O for many small writes.
- [ ] Prefer batched DB writes/reads.

### Rust-specific
- [ ] Avoid needless `clone()`.
- [ ] Consider `Cow`, `Bytes`, or borrowed views on hot paths.
- [ ] Use `tracing` with level gating.

### Python-specific
- [ ] Avoid per-item Python overhead in loops (vectorize or batch).
- [ ] Prefer `orjson`/`ujson` only with justification; stdlib is fine often.
- [ ] Use `asyncio` correctly; avoid blocking calls on event loop.

### Web/frontend
- [ ] Avoid large bundles; code split.
- [ ] Cache static assets; use HTTP caching headers.
- [ ] Prevent N+1 queries to backend.

## Deliverables for a perf task
- Before/after numbers (benchmark or representative run).
- Root cause analysis.
- Regression test / benchmark if feasible.

## When to skip
- No measurable baseline and no user-visible performance issue.
- Changes are purely structural and do not affect hot paths.

See also:
- `profiling.md`
- `rust-perf.md`
- `python-perf.md`
- `$CODEX_HOME/index/core/perf.md`
- `../workflows/overview.md`
- You must use skill perf-profiling.
