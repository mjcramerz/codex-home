---
name: infra-systemd
description: Design, harden, and validate systemd services and timers including unit files,
  restart behavior, and sandbox directives. Use when the user asks to create or troubleshoot
  Linux service/timer units.
metadata:
  version: '1.0'
  short-description: Design and harden systemd services and timers with safe defaults, validation,
    and install steps
  tags:
  - systemd
  - services
  - timers
  - linux
  - operations
interface:
  display-name: INFRA-systemd
  short-description: Design and harden systemd services and timers with safe defaults, validation,
    and install steps
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#5932CC'
  default-prompt: Act as the "INFRA-systemd" specialist for "Design and harden systemd services
    and timers with safe defaults, validation, and install steps". Deliver focused, deterministic
    results with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions,
    evidence, and residual risks.
---

## Use this skill when
- creating or updating systemd `.service` units
- adding scheduled jobs with systemd timers
- hardening long-running services

## Workflow
1) Clarify intent: ExecStart, user/group, working dir, dependencies, restart policy.
2) Draft a unit with explicit timeouts and environment file.
3) Apply hardening options incrementally.
4) Validate with `systemd-analyze verify` (if available).
5) Install: `daemon-reload`, `enable --now`, check `journalctl`.
6) For timers: add `.timer`, enable, verify `list-timers`.

## Checkpoint gates
- Unit gate: confirm service account, filesystem paths, dependencies, restart policy, and timeout behavior are explicit.
- Hardening gate: apply least-privilege directives (`NoNewPrivileges`, `CapabilityBoundingSet`, `ProtectSystem`, `PrivateTmp`) and document any exceptions.
- Install gate: verify unit files before reload, then apply `systemctl daemon-reload` and controlled start/enable sequence.
- Timer gate: for scheduled jobs, validate `OnCalendar`, jitter (`RandomizedDelaySec`), and persistence semantics before enabling.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Static validation: run `systemd-analyze verify <unit-files>` on `.service` and `.timer` definitions before install; run `systemd-analyze security <unit>` for long-running services when available.
- Runtime validation: start units and capture `systemctl status --no-pager` plus recent logs (`journalctl -u <unit> -n 100 --no-pager`).
- Behavioral validation: test restart/failure paths (non-zero exit, timeout, dependency unavailable) to confirm `Restart=` and `StartLimit*` behavior.
- Deployment validation: verify enablement and scheduling state (`systemctl is-enabled`, `systemctl list-timers`) and capture rollback steps (`disable --now`, unit restore).

## Outputs
- Production-ready `.service` and optional `.timer` files with explicit hardening and timeout choices.
- Install/upgrade runbook (`daemon-reload`, `enable --now`, status/log checks) plus rollback/uninstall commands.
- Validation transcript covering verify output, runtime behavior, and timer execution evidence.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-systemd/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-systemd/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-systemd/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-systemd/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/infra-systemd/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/systemd/overview.md`
- `$CODEX_HOME/docs/systemd/service-units.md`
- `$CODEX_HOME/docs/systemd/timers.md`
- `$CODEX_HOME/docs/systemd/hardening.md`
- `$CODEX_HOME/docs/systemd/user-units.md`
- `$CODEX_HOME/docs/workflows/systemd.md`
- `$CODEX_HOME/snippets/systemd/service.unit`
- `$CODEX_HOME/snippets/systemd/timer.unit`
- `$CODEX_HOME/snippets/systemd/user-service.unit`
- `$CODEX_HOME/templates/systemd/user-service-skeleton/`
