---
title: Tuning rollback matrix
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-optimizations
- references
- tuning-rollback-matrix-md
- tuning-rollback-matrix
- user
- infra
updated: '2026-02-20'
---
# Tuning rollback matrix

| Tuning domain | Change example | Risk | Rollback command | Validation after rollback |
| --- | --- | --- | --- | --- |
| CPU scheduler | `sched_*` sysctl | Throughput regression | `sysctl -w <key>=<old>` | Re-run latency and throughput probes |
| VM memory | `vm.*` sysctl | OOM / swap storms | Restore saved sysctl profile | Confirm memory pressure recovery |
| Network | `net.*` sysctl | Packet loss / latency | Restore backup config and restart stack if needed | Check RTT and error counters |
| Filesystem | mount option changes | Data integrity/perf tradeoff | Revert mount options and remount | Validate IO benchmarks and fs health |
