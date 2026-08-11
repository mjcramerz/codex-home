---
title: psql command catalog
status: active
owner: Matthew Cramer
tags:
- skills
- psql
- references
- commands
updated: '2026-03-11'
---
# psql command catalog

## Session-safe inspection
```bash
psql -X "$DATABASE_URL" -c '\conninfo'
psql -X "$DATABASE_URL" -c '\dn'
psql -X "$DATABASE_URL" -c '\dt+'
psql -X "$DATABASE_URL" -c '\d+ public.events'
```

## Bounded query examples
```bash
psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c "SELECT id, created_at FROM public.events ORDER BY created_at DESC LIMIT 50;"
psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c "SELECT status, COUNT(*) FROM public.jobs GROUP BY status ORDER BY COUNT(*) DESC LIMIT 20;"
```

## Session guardrails
```bash
psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c "SET statement_timeout = '5s'; SET lock_timeout = '2s'; SELECT current_database(), current_user;"
```

## Planner inspection
```bash
psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c "EXPLAIN SELECT * FROM public.events WHERE user_id = 42 LIMIT 10;"
psql -X -v ON_ERROR_STOP=1 "$DATABASE_URL" -c "EXPLAIN (ANALYZE, BUFFERS, VERBOSE) SELECT * FROM public.events WHERE user_id = 42 LIMIT 10;"
```

## Transaction-safe write template
```sql
BEGIN;
SET LOCAL statement_timeout = '5s';
SET LOCAL lock_timeout = '2s';
-- make targeted UPDATE / INSERT / DELETE statements here
SELECT pg_backend_pid();
ROLLBACK;
```
