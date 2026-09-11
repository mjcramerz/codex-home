# Python performance notes

Use this guide when you implement or review Python modules, CLIs, packaging or automation. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

- Avoid Python-level per-item overhead in tight loops; batch.
- Prefer local variables inside loops; avoid repeated global lookups.
- Use `asyncio.to_thread` for blocking I/O if async.
- Keep JSON encoding/decoding bounded; stream if possible.
- Prefer `time.perf_counter()` for timing and profiling harnesses.
- Use `pytest -q` for fast feedback; identify and quarantine slow tests.
- Add timeouts to network clients; avoid unbounded retries on hot paths.
- Prefer deterministic runs by pinning input sizes and seeding RNGs when benchmarking.

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
