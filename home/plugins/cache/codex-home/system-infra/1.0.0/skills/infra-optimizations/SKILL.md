---
name: infra-optimizations
description: Tune host performance and security settings with measurement-first baselines
  and rollback controls. Use when the user asks to improve host throughput, latency, or system
  hardening posture.
metadata:
  version: '1.0'
  short-description: Plan host performance/security tuning with measurement and rollback
  tags:
  - performance
  - security
  - tuning
  - linux
interface:
  display-name: INFRA-Optimizations
  short-description: Plan host performance/security tuning with measurement and rollback
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#BCCC32'
  default-prompt: Act as the "INFRA-Optimizations" specialist for "Plan host performance/security
    tuning with measurement and rollback". Deliver focused, deterministic results with minimal,
    reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O,
    run the narrowest relevant checks, and report concrete actions, evidence, and residual
    risks.
---

## Use this skill when
- tuning sysctl or kernel settings
- adjusting host performance knobs

## Workflow
1) Capture baseline metrics
2) Apply one change at a time
3) Measure and compare
4) Roll back if needed

## Checkpoint gates
- Baseline gate: capture before metrics for CPU, memory, I/O, latency, and security posture in the same sampling window.
- Change-budget gate: define one hypothesis per change, success threshold, and abort threshold before applying tunables.
- Soak gate: run representative workload for a fixed duration after each change before moving to the next knob.
- Rollback gate: pre-stage exact revert commands/files and trigger rollback immediately on regression beyond thresholds.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Measurement validation: use consistent tools and windows (`vmstat`, `iostat`, `sar`, `perf`, service latency probes) before/after each change.
- Functional validation: confirm workload behavior under expected and peak load; include at least one adverse-path check (resource pressure or burst traffic).
- Security validation: ensure hardening controls are not weakened unintentionally (firewall, audit, isolation, cgroup limits).
- Reporting validation: include raw metric snapshots plus normalized deltas so decisions are reproducible.

## Outputs
- Tuning plan table (change, hypothesis, metric target, abort threshold, rollback command).
- Before/after metrics summary with interpretation and confidence caveats.
- Deployment sequence for staged rollout and monitoring hooks to watch after change.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/scripts/skill_helper.py`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/references/perf-experiment-template.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/references/tuning-rollback-matrix.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/assets/experiment-sheet.md`
- `$CODEX_HOME/plugins/cache/codex-home/system-infra/1.0.0/skills/infra-optimizations/assets/sysctl-rollback.conf`

## References
- `$CODEX_HOME/index/domains/system/optimizations.md`
- `$CODEX_HOME/docs/system/optimizations.md`
- `$CODEX_HOME/docs/workflows/optimizations.md`
