# Apply a scoped Ansible change

Use this workflow when you change playbooks, roles or inventory and need a safe
path from local edits to an explicitly authorized rollout. Read
`$CODEX_HOME/docs/infra/ansible.md`; use the linked plan only for a multi-step change.

## Inspect and edit

Identify the inventory, exact host subset, connection identity, privilege boundary,
variable precedence and collection lock/pin policy. Read affected tasks, handlers
and role defaults. Prefer idempotent modules and make changed/failed conditions
explicit where command execution is unavoidable. Preserve unrelated hosts and roles.

## Check without overstating evidence

Use the repository's syntax and lint commands. Check mode is not a complete safety
or idempotence proof; modules and plugins differ, and some operations can still run.
Use `--diff` only when output cannot reveal secrets. Do not invoke an inventory
plugin or external lookup without understanding its access and side effects.

## Apply only within authorization

Confirm the canary host set, backup or rollback method and acceptance criteria.
Apply to the explicit limit, inspect failed/unreachable/changed results and service
health, and expand only through the approved batch plan. Reapplying to establish
idempotence is a live operation and requires the same authority as the first run.

## Handoff and stop

Report the changed files, selected inventory/limit without credentials, commands,
observed host outcomes and remaining drift. Do not claim a rollout from lint output
or open unrelated tasks. Stop when the authorized scope is complete.

## Optional resources

Read `$CODEX_HOME/plans/workflows/workflow-ansible.md` for a larger rollout plan.
Adapt `$CODEX_HOME/templates/infra/ansible-role-skeleton/` or
`$CODEX_HOME/snippets/ansible/playbook.yml` only when a new artifact is requested.
Discover the available Ansible plugin skill before invoking it.
