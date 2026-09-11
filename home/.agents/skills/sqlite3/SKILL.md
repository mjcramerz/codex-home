---
name: sqlite3
description: Use this skill to inspect, query, and maintain SQLite databases safely
  with the `sqlite3` CLI. Use when the task involves local database files, schema
  analysis, ad hoc reporting, or transaction-safe maintenance.
metadata:
  version: '1.0'
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
  brand-color: '#0F766E'
  default-prompt: Act as the "DB-SQLite3" specialist for "Operate SQLite databases
    safely from the sqlite3 CLI". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence,
    and residual risks.
---

# Sqlite3

## Workflow

1. Confirm the database path and whether the database is live, backed up or read-only. Avoid opening an absent path in create mode accidentally.

2. Inspect schema and PRAGMA state with bounded read queries. Use bound parameters in application code, not interpolated SQL.

3. Plan transactions, busy timeouts and backup behavior around WAL and concurrent writers. Do not copy only the main file of an active WAL database as a consistent backup.

4. Check the narrow changed query or migration and report observed rows/integrity evidence without exposing sensitive records.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
