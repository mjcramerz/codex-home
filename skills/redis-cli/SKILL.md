---
name: redis-cli
description: Use this skill to inspect and operate Redis safely with the `redis-cli`
  shell. Use when the task involves keyspace inspection, TTL analysis, operational
  checks, or bounded remediation against Redis instances.
metadata:
  version: '1.0'
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
  brand-color: '#DC2626'
  default-prompt: Act as the "DB-Redis CLI" specialist for "Operate Redis safely from
    the redis-cli shell". Deliver focused, deterministic results with minimal, reviewable
    changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run
    the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

# Redis Cli

## Workflow

1. Confirm the instance, logical database, TLS/auth method and read/write authority without placing secrets on command lines.

2. Inspect a bounded key sample using SCAN rather than a broad KEYS operation on a live instance. Treat values and key names as potentially sensitive.

3. Understand TTL, type, transaction and persistence effects before mutation. Avoid FLUSHALL, FLUSHDB or broad deletion unless explicitly authorized.

4. Use bounded reads/timeouts and report exact scope and observed outcomes; do not treat a successful PING as application-level correctness.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
