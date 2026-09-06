---
title: redis-cli command catalog
status: active
owner: Matthew Cramer
tags:
- skills
- redis-cli
- references
- commands
updated: '2026-03-11'
---
# redis-cli command catalog

## Session-safe inspection
```bash
redis-cli -u "$REDIS_URL" PING
redis-cli -u "$REDIS_URL" INFO server
redis-cli -u "$REDIS_URL" ACL WHOAMI
redis-cli -u "$REDIS_URL" DBSIZE
```

## Key discovery without KEYS *
```bash
redis-cli -u "$REDIS_URL" --scan --pattern 'session:*'
redis-cli -u "$REDIS_URL" --scan --pattern 'job:*' | head -n 50
```

## Key-type and TTL checks
```bash
redis-cli -u "$REDIS_URL" TYPE session:123
redis-cli -u "$REDIS_URL" TTL session:123
redis-cli -u "$REDIS_URL" MEMORY USAGE session:123
redis-cli -u "$REDIS_URL" HGETALL job:42
```

## Operational diagnostics
```bash
redis-cli -u "$REDIS_URL" SLOWLOG GET 10
redis-cli -u "$REDIS_URL" LATENCY LATEST
redis-cli -u "$REDIS_URL" INFO persistence
```

## Targeted write template
```bash
redis-cli -u "$REDIS_URL" <<'EOF'
MULTI
SETEX cache:key 60 updated-value
TTL cache:key
EXEC
EOF
```
