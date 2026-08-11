# Ansible workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-ansible.md` before executing this workflow.
Purpose: apply configuration changes safely and repeatably for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- Start from the linked workflow plan template above, then tailor scope, constraints, and validation commands before editing.
- You must keep the plan updated as execution progresses, including risk and rollback notes for any sensitive change.

## You must follow this workflow
1) **Scope**: hosts, inventory, roles, credentials.
2) **Check**: run lint and `--check` where possible.
3) **Apply**: run playbooks with limited batch size.
4) **Verify**: validate service health and idempotence.

## Safety rules
- Avoid broad host globs without confirmation.
- You must prefer idempotent modules over shell commands.

## Security checkpoints
- You must confirm inventory boundaries, vault secret sources, and `become` scope before execution.
- Reject ad-hoc shell-heavy tasks unless a module cannot meet the requirement.
- Pin role/collection versions and verify trusted upstream sources.

## Testing checkpoints
- You must run `ansible-lint` and syntax validation for every changed playbook or role.
- You must run `--check --diff` on a canary inventory slice and review task-level drift.
- You must re-run apply on the same slice to confirm idempotence expectations.

## Deployment checkpoints
- You must use staged rollout controls (`serial`, `--limit`) with health checks between batches.
- You must keep rollback playbook or config backup references per changed service.
- You must record final host set, failed hosts, and accepted drift exceptions.

## Multi-agent handoff
- Coordinator passes inventory subset, credential path, and rollout batch plan.
- Executor provides exact commands, host outcomes, and remediation actions taken.
- Receiver validates post-run idempotence and opens follow-up tasks for unresolved hosts.
See also:
- `overview.md`
- `../infra/ansible.md`
- `$CODEX_HOME/templates/infra/ansible-role-skeleton/`
- `$CODEX_HOME/snippets/ansible/playbook.yml`
- You must use skill `iac-ansible`.
- `$CODEX_HOME/index/pack/workflows.md`
