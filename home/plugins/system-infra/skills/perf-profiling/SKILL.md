---
name: perf-profiling
description: Profile and optimize application or system performance using benchmarking, hot-path
  analysis, and regression guards. Use when the user asks to investigate slowness, latency
  regressions, or performance bottlenecks.
metadata:
  version: '1.1'
  short-description: 'Performance engineering playbook: profiling, benchmarking, hot path
    analysis, safe optimizations, and regression guards'
  tags:
  - performance
  - profiling
  - benchmarking
  - optimization
interface:
  display-name: PERF-Profiling
  short-description: 'Performance engineering playbook: profiling, benchmarking, hot-path analysis, safe optimizations, and regression guards'
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CCBA'
  default-prompt: 'Act as the "PERF-Profiling" specialist for "Performance engineering playbook: profiling, benchmarking, hot-path analysis, safe optimizations, and regression guards". Deliver focused, deterministic results with
    minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded
    I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.'
---

## Use this skill when
- optimizing latency/throughput/memory
- working on hot loops or large data flows
- dealing with timeouts, slow CI, or scaling issues

## Workflow
1) Reproduce deterministically
2) Measure (profiling/benchmarks/tracing)
3) Optimize structurally (big-O, I/O, allocations)
4) Validate correctness and safety
5) Add regression guard (benchmark/test)
6) Document before/after numbers and environment

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Deliverables
- Before/after numbers and methodology (what changed, how measured)
- Root cause analysis (why it was slow)
- Regression guard (benchmark/test) when feasible

## Outputs
- A reproducible measurement plan and a minimal set of optimizations.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/perf-profiling/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/perf-profiling/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/perf-profiling/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/perf-profiling/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/perf-profiling/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/perf/overview.md`
- `$CODEX_HOME/docs/perf/profiling.md`
