---
name: sqlite3
description: Inspect, query, and maintain SQLite databases safely with the `sqlite3`
  CLI. Use when the task involves local database files, schema analysis, ad hoc
  reporting, or transaction-safe maintenance.
metadata:
  version: "1.0"
  short-description: Operate SQLite databases safely from the sqlite3 CLI
  tags:
  - sqlite
  - sqlite3
  - database
  - cli
  - query
interface:
  display-name: DB-SQLite3
  short-description: Operate SQLite databases safely from the sqlite3 CLI
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: "#0F766E"
  default-prompt: Act as the "DB-SQLite3" specialist for "Operate SQLite databases safely from the sqlite3 CLI". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- inspecting local `.sqlite`, `.sqlite3`, or `.db` files before code or migration changes
- tracing tables, indexes, views, triggers, foreign keys, and pragma settings
- writing bounded ad hoc queries, exports, or schema comparison commands
- reviewing query plans, journaling mode, WAL behavior, or lock contention
- preparing transaction-safe maintenance or repair steps for SQLite-backed tooling

## Inputs
- absolute or workspace-relative database path
- whether inspection must stay read-only or may include mutations
- target tables, query objective, or migration scope
- expected data size and acceptable runtime for verification checks

## Scope and boundaries
- Prefer read-only access first; use `sqlite3 -readonly` when mutation is not required.
- Keep destructive statements (`DROP`, `DELETE`, `VACUUM`, `REINDEX`) behind explicit user intent.
- Wrap multi-statement writes in transactions and show rollback-aware SQL when possible.
- Bound result sets with `LIMIT`, selective predicates, or aggregate summaries before returning data.
- Validate the database path, journaling assumptions, and available disk space before maintenance work.

## Workflow
1) Confirm the database path, access mode, and whether a backup already exists.
2) Inspect schema and runtime state with `.databases`, `.schema`, `.tables`, and targeted `PRAGMA` queries.
3) Reproduce the question with the smallest deterministic SQL statement or `.read` script.
4) Use `EXPLAIN QUERY PLAN`, index inspection, and pragmas to reason about performance or locking behavior.
5) If writes are required, stage them in an explicit transaction and verify post-change invariants.

## Validation and testing
- Run the narrowest relevant checks that prove the change or diagnosis.
- Prefer `PRAGMA quick_check;` for fast integrity verification and `PRAGMA integrity_check;` only when the cost is acceptable.
- Validate row counts, foreign-key expectations, and schema diffs before and after mutating work.
- Record the exact CLI command or SQL script used so the workflow is reproducible.

## Outputs
- Safe `sqlite3` commands or `.sql` scripts with explicit assumptions.
- Schema notes, query-plan findings, and integrity-check results.
- Clear rollback notes for any data-changing operation.

## References
- `$CODEX_HOME/UNIX.md`
- `$CODEX_SKILLS/sqlite3/references/latest-sources.md`
- `$CODEX_SKILLS/sqlite3/references/command-catalog.md`
