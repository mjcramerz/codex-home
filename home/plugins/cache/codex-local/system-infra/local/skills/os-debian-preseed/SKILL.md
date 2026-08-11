---
name: os-debian-preseed
description: Create and review Debian preseed automation files for unattended installations with deterministic installer behavior, class-driven profiles, and staged runtime helpers. Use when the user asks for Debian auto-install, desktop/service role provisioning, or image delivery via preseed.
metadata:
  version: '1.1'
  short-description: Class-driven Debian preseed files for unattended installations
  tags:
  - debian
  - preseed
  - unattended
  - install
  - virtualization
interface:
  display-name: OS-Debian Preseed
  short-description: Class-driven Debian preseed files for unattended installations
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#3265CC'
  default-prompt: Act as the "OS-Debian Preseed" specialist for "Class-driven Debian preseed files for unattended installations". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- generating or updating Debian preseed files
- automating unattended Debian installs for desktop or service roles
- grounding changes against the active `debian-preseed-di` repository contract
- checking how Labwc desktops, GitLab Runner services, Aptly publication, or addon classes are staged through the installer

## Workflow
1) Collect requirements (class set, storage, network, users, packages, and service or desktop addons).
2) Confirm destructive storage targets, kernel cmdline inputs, and split-file include boundaries.
3) Keep class metadata, host profiles, and staged helper scripts separated by responsibility.
4) Host the preseed securely and validate both install and first-boot behavior in a VM before widening scope.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for destructive storage, class expansion, or late-command automation.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs
- A preseed or helper change set with safe defaults and explicit class or role impact.
- Clear installation and validation steps for the touched class, service, or desktop contract.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/os-debian-preseed/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/os-debian-preseed/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/os-debian-preseed/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/os-debian-preseed/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-local/system-infra/local/skills/os-debian-preseed/scripts/skill_helper.py`

## References
- `$CODEX_HOME/index/domains/system/debian-preseed.md`
- `$CODEX_HOME/docs/workflows/debian-preseed.md`
- `$CODEX_HOME/docs/virtualization/debian-preseed.md`
- `$CODEX_HOME/docs/workflows/gitlab-runner.md`
- `$CODEX_HOME/docs/desktop/wayland.md`
- `$CODEX_HOME/templates/virtualization/debian-preseed/`
- `$CODEX_HOME/snippets/virtualization/preseed_boot_params.txt`
