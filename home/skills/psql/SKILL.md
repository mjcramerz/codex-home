---
name: psql
description: Inspect, query, and maintain PostgreSQL databases safely with the
  `psql` CLI. Use when the task involves schema inspection, bounded reporting,
  transaction-safe migrations, or planner analysis.
metadata:
  version: "1.0"
  short-description: Operate PostgreSQL safely from the psql CLI
  tags:
  - postgres
  - postgresql
  - psql
  - database
  - cli
interface:
  display-name: DB-PSQL
  short-description: Operate PostgreSQL safely from the psql CLI
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: "#2563EB"
  default-prompt: Act as the "DB-PSQL" specialist for "Operate PostgreSQL safely from the psql CLI". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- inspecting PostgreSQL schemas, relations, indexes, roles, or extensions from the CLI
- running bounded ad hoc queries or exports against a live or staging database
- reviewing migrations, DDL changes, locking behavior, or planner regressions
- preparing transaction-safe remediation steps for data fixes or maintenance tasks
- validating session-level safety controls such as `statement_timeout` or `lock_timeout`

## Inputs
- connection target (`DATABASE_URL`, service name, socket, or explicit host/db/user values)
- whether production safeguards require read-only or rollback-only work
- target schemas, tables, or migration objective
- acceptable runtime budget for `EXPLAIN`, counts, or verification queries

## Scope and boundaries
- Prefer `psql -X` so local startup files do not change behavior.
- Default to read-oriented inspection first; stage exploratory writes inside `BEGIN` / `ROLLBACK`.
- Set `ON_ERROR_STOP` for scripted runs and apply `statement_timeout` / `lock_timeout` when appropriate.
- Avoid `VACUUM FULL`, `REINDEX DATABASE`, role changes, or cluster-wide commands without explicit user intent.
- Bound large reads with selective predicates, sampling, or `LIMIT` before returning data.

## Workflow
1) Confirm the target connection, role, and environment risk level before opening a session.
2) Inspect context with `\conninfo`, relation metadata (`\dn`, `\dt+`, `\d+`), and session settings.
3) Reproduce the question with the smallest deterministic `SELECT`, `\copy`, or migration statement.
4) Use `EXPLAIN` or `EXPLAIN ANALYZE` only when the query cost and environment allow it.
5) If writes are required, apply explicit transactions, safe timeouts, and post-change verification queries.

## Validation and testing
- Run `SELECT current_database(), current_user;` or `\conninfo` to confirm the target before mutating anything.
- Use `psql -X -v ON_ERROR_STOP=1` for non-interactive commands and checked SQL files.
- Verify row counts, constraints, and search-path assumptions before and after change sets.
- Record the exact command, timeout settings, and transaction scope so the workflow is reproducible.

## Outputs
- Safe `psql` commands or `.sql` scripts with connection and timeout assumptions called out.
- Schema, relation, and planner notes tied to the investigated tables or migrations.
- Rollback-aware steps for any write or DDL operation.

## References
- `$CODEX_HOME/UNIX.md`
- `$CODEX_SKILLS/psql/references/latest-sources.md`
- `$CODEX_SKILLS/psql/references/command-catalog.md`
