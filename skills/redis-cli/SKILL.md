---
name: redis-cli
description: Inspect and operate Redis safely with the `redis-cli` shell. Use
  when the task involves keyspace inspection, TTL analysis, operational checks,
  or bounded remediation against Redis instances.
metadata:
  version: "1.0"
  short-description: Operate Redis safely from the redis-cli shell
  tags:
  - redis
  - redis-cli
  - database
  - cli
  - cache
interface:
  display-name: DB-Redis CLI
  short-description: Operate Redis safely from the redis-cli shell
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: "#DC2626"
  default-prompt: Act as the "DB-Redis CLI" specialist for "Operate Redis safely from the redis-cli shell". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- inspecting Redis connectivity, selected logical databases, memory usage, or slowlog entries
- querying key types, TTLs, counters, streams, or hashes from the CLI
- preparing bounded remediation steps for cache invalidation or data repair work
- reviewing operational issues such as latency spikes, blocked clients, or persistence settings
- diagnosing automation that talks directly to Redis over TCP, TLS, or Unix sockets

## Inputs
- target connection (`REDIS_URL`, host/port, or Unix socket) and selected logical DB
- whether the environment permits writes, deletes, or pub/sub side effects
- key patterns, prefixes, or operational objective
- acceptable runtime for scans, monitors, or memory inspection

## Scope and boundaries
- Prefer inspection commands first (`PING`, `INFO`, `TYPE`, `TTL`, `MEMORY USAGE`) before any write.
- Use `SCAN` / `--scan` for key discovery; avoid `KEYS *` on non-trivial instances.
- Keep `FLUSHDB`, `FLUSHALL`, `CONFIG SET`, `MONITOR`, and Lua writes behind explicit user intent.
- Bound scans and stream reads with pattern filters, `COUNT`, or limited result windows.
- Confirm selected database number, ACL identity, and persistence assumptions before mutating state.

## Workflow
1) Confirm the target Redis instance, logical DB, ACL/auth expectations, and write-risk boundaries.
2) Inspect health with `PING`, `INFO`, `ACL WHOAMI`, `DBSIZE`, and targeted key-type checks.
3) Reproduce the question with the smallest deterministic `redis-cli` command or shell pipeline.
4) Use `SCAN`, `SLOWLOG GET`, `MEMORY USAGE`, or `LATENCY` tooling to investigate performance and operational issues.
5) If writes are required, make them narrowly targeted and verify TTLs, values, and key counts immediately afterward.

## Validation and testing
- Confirm the target DB and auth context before mutating anything.
- Prefer `redis-cli --raw` or explicit shell quoting when command output feeds other tooling.
- Validate TTLs, key existence, and data types before and after write-oriented commands.
- Keep `MONITOR` or continuous diagnostics time-bounded and document the stop condition.

## Outputs
- Safe `redis-cli` commands with connection, DB-selection, and key-pattern assumptions called out.
- Keyspace, TTL, latency, or persistence findings tied to the investigated instance.
- Rollback-aware notes for any cache invalidation or data rewrite operation.

## References
- `$CODEX_HOME/UNIX.md`
- `$CODEX_SKILLS/redis-cli/references/latest-sources.md`
- `$CODEX_SKILLS/redis-cli/references/command-catalog.md`
