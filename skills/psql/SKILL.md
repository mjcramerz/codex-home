---
name: psql
description: Use this skill to inspect, query, and maintain PostgreSQL databases safely
  with the `psql` CLI. Use when the task involves schema inspection, bounded reporting,
  transaction-safe migrations, or planner analysis.
metadata:
  version: '1.0'
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
  brand-color: '#2563EB'
  default-prompt: Act as the "DB-PSQL" specialist for "Operate PostgreSQL safely from
    the psql CLI". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Psql

## Workflow

1. Confirm host, database, role, schema and read/write authorization without printing connection secrets. Start with read-only metadata queries.

2. Use parameterized SQL or safely quoted psql variables; set statement and lock timeouts appropriate to the operation.

3. Review transaction scope, locks, row counts and rollback for writes. EXPLAIN ANALYZE executes the statement; do not treat it as a harmless plan.

4. Limit result size and redact personal data. Report actual query outcomes and stop before unrelated maintenance or destructive SQL.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
