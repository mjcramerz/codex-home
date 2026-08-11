---
name: infra-kernel
description: Build and validate custom Linux kernel configurations with reproducible compile
  and boot validation steps. Use when the user asks for custom kernel config, compile, or
  test guidance.
metadata:
  version: '1.0'
  short-description: Plan and validate custom Linux kernel builds
  tags:
  - kernel
  - linux
  - build
  - system
interface:
  display-name: INFRA-Kernel
  short-description: Plan and validate custom Linux kernel builds
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC3296'
  default-prompt: Act as the "INFRA-Kernel" specialist for "Plan and validate custom Linux
    kernel builds". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- compiling or customizing a kernel
- applying config fragments

## Workflow
1) Scope hardware and policy requirements
2) Start from distro config
3) Apply minimal config deltas
4) Build, install, and verify

## Checkpoint gates
- Baseline gate: start from distro kernel config (`/boot/config-$(uname -r)`) and record toolchain/kernel source versions.
- Config gate: apply only scoped config fragments, then run `make olddefconfig` to resolve dependencies deterministically.
- Build gate: compile with bounded parallelism, capture build logs, and fail on warnings promoted by policy.
- Install gate: install new kernel alongside existing versions and keep bootloader fallback entry intact.
- Boot gate: verify first boot with `uname -r`, module load checks, and critical subsystem smoke tests (storage, network, virtualization).

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Config validation: diff `.config` against baseline, and verify required options via the kernel source tree helper scripts/config with `--file .config --state <OPTION>`.
- Build validation: run `make olddefconfig`, `make -j<N> bzImage modules`, and confirm artifacts/signing outputs exist before install.
- Runtime validation: after boot, inspect `dmesg -l err,crit,alert,emerg` and confirm required modules/services load cleanly.
- Rollback validation: document and test kernel fallback selection (GRUB/systemd-boot) before declaring deployment complete.

## Outputs
- Kernel config fragment set plus concise delta summary from baseline config.
- Build/install command sequence with artifact paths and expected outputs.
- Post-boot verification checklist and explicit rollback procedure to prior kernel.

## Local resources
- `references/latest-sources.md`
- `references/operations-checklist.md`
- `references/risk-register.md`
- `assets/rollback-checklist.md`
- `scripts/skill_helper.py`

## References
- `$CODEX_HOME/index/domains/system/kernel.md`
- `$CODEX_HOME/docs/system/kernel.md`
- `$CODEX_HOME/docs/workflows/kernel-build.md`
- `$CODEX_HOME/templates/system/kernel-build-skeleton/`
- `$CODEX_HOME/snippets/system/kernel-config.fragment`
