---
name: mobile-wireless-defense
description: Run scoped mobile and wireless defense operations covering Wi-Fi assessment
  controls, NetHunter lab build governance, rooted-device risk management, and BadUSB/Rubber
  Ducky resilience testing in documented scope.
metadata:
  version: '1.0'
  short-description: Scoped mobile and wireless defense operations with strict scope
    boundaries
  tags:
  - mobile-wireless-defense
  - wireless
  - nethunter
  - badusb
  - mobile-security
interface:
  display-name: Mobile Wireless Defense
  short-description: Scoped mobile and wireless defense operations with strict scope
    boundaries
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3270CC'
  default-prompt: Act as the "Mobile Wireless Defense" specialist for "Scoped mobile and
    wireless defense operations with strict scope boundaries". Deliver focused, deterministic
    results with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions,
    evidence, and residual risks.
---

## Use this skill when
- the request targets wireless/mobile lab defense
- the task includes NetHunter build operations, rooted-device governance, or USB attack-surface controls
- the objective is defensive validation in documented labs or owned-device environments

## Scope boundary (required)
- Require explicit operation scope and listed devices.
- No access to third-party wireless networks or devices outside the documented scope.
- No covert payload delivery through USB emulation devices.

## Workflow
1) Validate scope and allowed devices with `scripts/mobile_scope_guard.py` using
   `references/lab-boundary.md`.
2) Baseline wireless/mobile environment and control expectations.
3) Execute controlled defense tracks:
   - wireless posture validation (Wifite/Wireshark/Nmap defensive use)
   - NetHunter installer and kernel-builder governance checks
   - rooted Android risk controls and segmentation checks
   - BadUSB/Rubber Ducky resilience drills
4) Capture findings, apply hardening updates, and re-test.

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
- Mobile and wireless defense assessment with evidence.
- Device and network hardening recommendations with owners.
- Re-test plan for residual risk closure.

## References
- `references/lab-boundary.md`
- `references/wifi-lab-defense.md`
- `references/nethunter-build-governance.md`
- `references/google-pixel-rooting-guardrails.md`
- `references/pixel9a-kernel-porting-checklist.md`
- `references/badusb-rubberducky-defense.md`
- `references/latest-sources.md`
- `$CODEX_HOME/docs/security/security-labs-tool-guides.md`
- `$CODEX_HOME/templates/system/mobile-wireless-defense-kit/overview.md`
