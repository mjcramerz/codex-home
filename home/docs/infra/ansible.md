# Ansible
Purpose: tell the Codex coding agent how to use `docs/infra/ansible.md` as a runtime-pack surface and when to stop browsing.
Guidance for idempotent, reviewable configuration automation.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/infra/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Baseline practices
- You must prefer modules over raw shell.
- You must use `check` mode for dry runs when possible.
- You must keep secrets in Ansible Vault or external secret managers.
- Structure reusable logic into roles.

## Inventory & roles
- You must keep inventory explicit and scoped.
- You must use group vars and role defaults for safe defaults.

## Safety
- Avoid running on broad host globs without confirmation.
- You must add `serial` or `max_fail_percentage` for safer rollouts.

See also:
- `overview.md`
- `../workflows/ansible.md`
- `$CODEX_HOME/templates/infra/ansible-role-skeleton/`
- `$CODEX_HOME/snippets/ansible/playbook.yml`
- `$CODEX_HOME/snippets/ansible/ansible.cfg`
- You must use skill iac-ansible.
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/ansible.md`
