# Local BWS workflow

You must start with `$CODEX_HOME/plans/workflows/workflow-bws-local.md` before executing this workflow.
Purpose: provide a local-only playbook for Bitwarden Secrets Manager CLI (`bws`) on Debian workstations and servers for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/workflows/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Plan
- You must use `$CODEX_HOME/plans/workflows/workflow-bws-local.md`.

## Scope
- In scope: local installation, PATH wiring, keyring storage, and token rotation.
- Out of scope: CI/CD secret injection, hosted runner setup, and GitHub/GitLab pipeline wiring.

## Skill routing
- You must use skill `bws-local`.

## Baseline workflow
1) Validate local prerequisites (Debian, sudo availability, DBus/session keyring readiness).
2) Install or verify pinned `bws` binary and integrity hash.
3) Configure system-wide PATH exposure (shell startup snippet + interactive shell source path).
4) Store `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` in local keyring only.
5) Verify local read path (`bws --version`, keyring status, local command execution).
6) Rotate keyring values on token/project changes.

## Operational guidance
- You must keep token material out of shell history and logs.
- You must prefer keyring retrieval over persistent plaintext env files.
- You must keep path mutation deterministic and scoped to dedicated marker blocks.
- You must require explicit sudo elevation only for privileged writes.

## Security checkpoints
- You must confirm `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` are never printed, logged, or committed.
- You must validate keyring target attributes (service/account names) against strict allowlists.
- Ensure scripts are run as a non-root user and only elevate specific privileged commands.

## Testing checkpoints
- You must validate syntax/static checks for shell scripts before execution.
- Test install, update-keyring, keyring-status, and read-path flows in a non-prod shell session.

## Deployment checkpoints
- Sequence local changes as install -> keyring update -> verification in one session.
- When the task includes host migration, move only required env metadata (never secret values) and re-enroll keyring at destination.
- Track follow-up verification steps for binary/path visibility and keyring read-path checks.

## Multi-agent handoff
- Planner provides target host baseline (Debian version, shell, privilege model) and stop conditions.
- Executor records changed files/commands and key verification outputs without secret values.
- Reviewer confirms local-only scope stayed isolated from CI/CD workflows.

See also:
- `$CODEX_HOME/docs/security/bitwarden-secrets-local.md`
- `$CODEX_HOME/docs/security/bitwarden-secrets.md`
- `$CODEX_HOME/docs/prompt-writing.md`
- `$CODEX_HOME/index/domains/system/bws-local.md`
