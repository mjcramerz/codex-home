# Ansible

Use this guide when you change Ansible inventories, roles, playbooks or collection dependencies. Inspect the project's declared versions and existing conventions before selecting a command or API.

## Apply these practices

**1.** Inspect the inventory, selected hosts, collection versions, role defaults and variable precedence before editing. State the exact host limit and required privilege escalation.

**2.** Prefer idempotent modules, fully qualified collection names, explicit ownership and modes, and handlers triggered only by actual changes. Use command or shell only where a module cannot express the operation; define changed_when and failed_when from real outcomes.

**3.** Keep secrets in the approved secret store or Vault. Apply no_log to secret-bearing tasks and disable diff where it could reveal sensitive values. Never embed credentials in inventory, example files or logs.

**4.** Run syntax and lint checks with the repository's declared toolchain. Treat check mode as partial evidence: module support varies, and lookups or delegated actions may still have side effects.

**5.** Apply only to an authorized canary host set, review health and changed/failed/unreachable results, and expand batches only after the canary meets the acceptance criteria. Re-running for idempotence is a live change, not a harmless inspection.

## Select related guidance

- `$CODEX_HOME/docs/infra/overview.md`
- `$CODEX_HOME/INDEX.md`
- `$CODEX_HOME/index/OVERVIEW.md`
- `$CODEX_HOME/templates/infra/ansible-role-skeleton/`
- `$CODEX_HOME/snippets/ansible/playbook.yml`
- `$CODEX_HOME/snippets/ansible/ansible.cfg`
- `$CODEX_HOME/index/domains/infra/tooling.md`
- `$CODEX_HOME/index/domains/infra/ansible.md`

Read only the matching skill or workflow. Stop when the requested change and its narrowest permitted checks are complete.
