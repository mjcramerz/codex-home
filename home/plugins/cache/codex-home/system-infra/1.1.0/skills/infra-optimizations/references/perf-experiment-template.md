---
title: Performance experiment template
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-optimizations
- references
- perf-experiment-template-md
- perf-experiment-template
- user
- infra
updated: '2026-02-20'
---

# Performance experiment template

Consult this reference when performance experiment template is relevant to the selected task. Extract the specific constraint or example you need, verify version-sensitive behavior against the active toolchain, and return to the task rather than loading unrelated references.

## Hypothesis

- Change:
- Expected effect:
- Success metric and threshold:
- Abort threshold:

## Baseline capture

- Sampling window:
- Workload profile:
- Metrics captured (latency, CPU, memory, I/O):

## Post-change capture

- Same workload and window:
- Delta summary:
- Confidence caveats:

## Decision

- Keep / rollback:
- Follow-up actions:
