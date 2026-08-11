# Python performance notes
Purpose: tell the Codex coding agent how to use `docs/perf/python-perf.md` as a runtime-pack surface and when to stop browsing.
- Avoid Python-level per-item overhead in tight loops; batch.
- You must prefer local variables inside loops; avoid repeated global lookups.
- You must use `asyncio.to_thread` for blocking I/O if async.
- You must keep JSON encoding/decoding bounded; stream if possible.
- You must prefer `time.perf_counter()` for timing and profiling harnesses.
- You must use `pytest -q` for fast feedback; identify and quarantine slow tests.
- You must add timeouts to network clients; avoid unbounded retries on hot paths.
- You must prefer deterministic runs by pinning input sizes and seeding RNGs when benchmarking.


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
