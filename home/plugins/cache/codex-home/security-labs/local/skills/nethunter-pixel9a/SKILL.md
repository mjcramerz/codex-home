---
name: nethunter-pixel9a
description: Run scoped Kali NetHunter Pixel 9a kernel-porting and Android rooting lab
  operations, including Google kernel alignment, boot-image patch validation, and rollback-safe
  deployment checks.
metadata:
  version: '1.0'
  short-description: Pixel 9a NetHunter kernel port + Android root lab operations with
    strict scope controls
  tags:
  - nethunter-pixel9a
  - nethunter
  - pixel9a
  - android-root
  - kernel-porting
interface:
  display-name: NetHunter Pixel9a
  short-description: Pixel 9a NetHunter kernel port + Android root lab operations with
    strict scope controls
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC4A32'
  default-prompt: Act as the "NetHunter Pixel9a" specialist for "Pixel 9a NetHunter kernel
    port + Android root lab operations with strict scope controls". Deliver focused, deterministic
    results with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions,
    evidence, and residual risks.
---

## Use this skill when
- the request specifically targets Kali NetHunter on Google Pixel 9a
- you need controlled kernel-porting steps tied to a documented lab scope
- you need rooted-device preparation for permitted testing with rollback safeguards

## Scope boundary (required)
- Require explicit documented scope and owned test devices.
- No rooting or flashing on third-party devices without documented owner authorization.
- No bypass attempts for locked bootloaders, FRP, carrier locks, or anti-theft controls.
- No persistence or covert tooling outside the documented lab objective.

## Workflow
1) Validate the scope manifest with `scripts/nethunter_scope_guard.py`.
2) Capture baseline device state (`adb` properties, slot info, bootloader state, and build fingerprint).
3) Align Google kernel source/branch to the exact device build baseline.
4) Prepare NetHunter builder + installer repositories and record commit IDs.
5) Apply porting changes in reviewable commits and keep patch history deterministic.
6) Build and verify artifacts (kernel images, installer zip, checksums, and logs).
7) Execute rooted-device lab sequence (unlock, patch boot image, flash, validate).
8) Run post-flash validation and rollback drills.
9) Publish evidence and residual risk summary.

## Topic map
- Scope and legal controls: `references/lab-boundary.md`
- Pixel 9a kernel porting stages: `references/pixel9a-porting-phases.md`
- Rooting sequence in controlled labs: `references/android-root-lab-sequence.md`
- Builder/installer command baselines: `references/nethunter-builder-installer-commands.md`
- Recovery and rollback: `references/rollback-and-recovery.md`

## Companion skills
- `mobile-wireless-defense` for broader wireless/mobile controls.
- `offsec-defense` for cross-domain evidence, detection, and remediation reporting.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- Scope-validated Pixel 9a NetHunter execution runbook with commands and artifact paths.
- Rooting + flashing evidence package (hashes, logs, build IDs, rollback proof).
- Risk-ranked findings and hardening actions with re-test criteria.

## References
- `references/lab-boundary.md`
- `references/pixel9a-porting-phases.md`
- `references/android-root-lab-sequence.md`
- `references/nethunter-builder-installer-commands.md`
- `references/rollback-and-recovery.md`
- `references/latest-sources.md`
- `$CODEX_HOME/docs/workflows/nethunter-pixel9a.md`
- `$CODEX_HOME/docs/security/nethunter-pixel9a.md`
- `$CODEX_HOME/docs/security/security-labs-index.md`
- `$CODEX_HOME/templates/system/nethunter-pixel9a-kit/overview.md`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_preflight.sh`
- `$CODEX_HOME/snippets/bash/nethunter_pixel9a_root_sequence.sh`
