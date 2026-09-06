---
name: iac-ansible
description: Author or refactor idempotent Ansible playbooks, roles, inventories, and handlers
  with safe defaults. Use when the user asks for Ansible-based provisioning or configuration
  automation.
metadata:
  version: '1.0'
  short-description: Build idempotent Ansible playbooks and roles safely
  tags:
  - ansible
  - infra
  - automation
  - security
interface:
  display-name: IAC-Ansible
  short-description: Build idempotent Ansible playbooks and roles safely
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#32CC49'
  default-prompt: Act as the "IAC-Ansible" specialist for "Build idempotent Ansible playbooks
    and roles safely". Deliver focused, deterministic results with minimal, reviewable changes
    and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest
    relevant checks, and report concrete actions, evidence, and residual risks.
---

## Use this skill when
- writing Ansible roles or playbooks
- planning safe rollouts

## Workflow
1) Scope inventory and privileges.
2) Prefer modules over shell.
3) Use check mode and limited batch sizes.
4) Verify idempotence.

## Checkpoint gates
- Pre-change: confirm inventory scope (`--limit`), privilege model (`become`), maintenance window, and rollback path (backup/snapshot or package downgrade).
- Dry-run: require `ansible-playbook --syntax-check` and `ansible-playbook --check --diff --limit <canary>` before broader execution.
- Rollout: use canary-first batching (`serial` and/or `--limit`) with explicit failure bounds (`max_fail_percentage`) before fleet-wide runs.
- Post-change: rerun the same playbook and capture idempotence; second pass should converge with no unexpected `changed` tasks.

## Agent orchestration
- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing
- Static validation: run `ansible-lint` and `ansible-playbook --syntax-check <playbook.yml>`.
- Functional validation: run `ansible-playbook --check --diff --limit <host-or-group> <playbook.yml>` plus service smoke checks (health endpoint, `systemctl`, open port).
- Auth/secret validation: fail closed when required vault vars, credentials, or `become` permissions are missing.
- Report per-host recap (`ok/changed/failed/unreachable`) and the exact inventory limits used for every test or rollout command.

## Outputs
- Updated role/playbook bundle with inventory targeting, tags, and privilege assumptions documented.
- Rollout runbook with canary command, full deployment command, and rollback command.
- Validation evidence block with lint/syntax/check/idempotence results and any accepted residual risk.

## Local resources
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-ansible/references/latest-sources.md`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-ansible/references/operations-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-ansible/references/risk-register.md`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-ansible/assets/rollback-checklist.md`
- `$CODEX_HOME/plugins/cache/codex-home/iac/1.0.0/skills/iac-ansible/scripts/skill_helper.py`

## References
- `$CODEX_HOME/docs/workflows/ansible.md`
- `$CODEX_HOME/docs/infra/ansible.md`
- `$CODEX_HOME/templates/infra/ansible-role-skeleton/`
- `$CODEX_HOME/snippets/ansible/playbook.yml`
