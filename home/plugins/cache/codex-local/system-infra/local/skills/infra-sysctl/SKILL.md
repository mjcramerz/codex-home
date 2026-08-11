---
name: infra-sysctl
description: Apply kernel sysctl parameter changes with safe rollout, verification, and rollback
  guidance. Use when the user asks to tune /proc/sys values or persistent sysctl settings.
metadata:
  version: '1.0'
  short-description: Apply sysctl tuning with safety and rollback
  tags:
  - sysctl
  - linux
  - performance
  - security
interface:
  display-name: INFRA-sysctl
  short-description: Apply sysctl tuning with safety and rollback
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC54'
  default-prompt: Act as the "INFRA-sysctl" specialist for "Apply sysctl tuning with safety
    and rollback". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- adjusting kernel parameters
- building baseline hardening profiles

## Workflow
1) Scope role and goals
2) Draft minimal sysctl drop-ins
3) Apply and measure
4) Roll back if needed

## Checkpoint gates
- Scope gate: map host role and kernel version to allowed tunables; reject keys that conflict with workload or security baseline.
- Staging gate: write versioned drop-in files under `/etc/sysctl.d/` with comments for intent and rollback owner.
- Apply gate: validate file syntax and apply with `sysctl --system` (or scoped `sysctl -p <file>`); confirm systemd-sysctl ordering when boot-time dependencies matter.
- Persistence gate: verify tuned keys survive reboot and do not depend on transient runtime state.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Key validation: confirm each expected key/value pair with `sysctl -n <key>` before and after apply.
- Workload validation: run relevant smoke/perf checks (network throughput, connection churn, memory pressure) tied to changed keys.
- Safety validation: inspect kernel logs for side effects (`dmesg`) and verify no critical service regressions.
- Rollback validation: test restoration of prior values/drop-in file and capture commands for emergency revert.

## Outputs
- Sysctl drop-in file(s) with rationale for each key and host-role constraints.
- Apply/verify/rollback command set, including reboot persistence checks.
- Before/after key snapshot plus workload impact notes and residual risk.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-sysctl/scripts/skill_helper.py`

## References
- `$CODEX_HOME/index/domains/system/sysctl.md`
- `$CODEX_HOME/docs/system/sysctl.md`
- `$CODEX_HOME/docs/workflows/sysctl.md`
- `$CODEX_HOME/templates/system/sysctl-baseline/`
- `$CODEX_HOME/snippets/system/sysctl.conf`
