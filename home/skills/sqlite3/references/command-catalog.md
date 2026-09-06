---
title: sqlite3 command catalog
status: active
owner: Matthew Cramer
tags:
- skills
- sqlite3
- references
- commands
updated: '2026-03-11'
---
# sqlite3 command catalog

## Read-only inspection
```bash
sqlite3 -readonly "$DB_PATH" '.databases'
sqlite3 -readonly "$DB_PATH" '.tables'
sqlite3 -readonly "$DB_PATH" '.schema users'
sqlite3 -readonly "$DB_PATH" 'PRAGMA foreign_keys;'
```

## Bounded query examples
```bash
sqlite3 -readonly "$DB_PATH" "SELECT id, created_at FROM events ORDER BY created_at DESC LIMIT 50;"
sqlite3 -readonly "$DB_PATH" "SELECT type, COUNT(*) FROM events GROUP BY type ORDER BY COUNT(*) DESC LIMIT 20;"
```

## Query-plan inspection
```bash
sqlite3 -readonly "$DB_PATH" "EXPLAIN QUERY PLAN SELECT * FROM events WHERE user_id = 42 LIMIT 10;"
sqlite3 -readonly "$DB_PATH" "PRAGMA index_list('events');"
sqlite3 -readonly "$DB_PATH" "PRAGMA index_info('idx_events_user_id');"
```

## Integrity checks
```bash
sqlite3 -readonly "$DB_PATH" 'PRAGMA quick_check;'
sqlite3 -readonly "$DB_PATH" 'PRAGMA integrity_check;'
```

## Transaction-safe write template
```sql
BEGIN IMMEDIATE;
-- make targeted UPDATE / INSERT / DELETE statements here
SELECT changes();
ROLLBACK;
```
