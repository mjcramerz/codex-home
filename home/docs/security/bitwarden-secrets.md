# Bitwarden Secrets Manager (BWS)
Purpose: tell the Codex coding agent how to use `docs/security/bitwarden-secrets.md` as a runtime-pack surface and when to stop browsing.
Guidance for using Bitwarden Secrets Manager in repos and CI.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


For local-host operation guidance, use `$CODEX_HOME/docs/security/bitwarden-secrets-local.md`.


## Baseline
- Store the access token as a masked/protected secret.
- Map the CI secret to the environment variable expected by your BWS tooling.
- Fetch secrets by ID and keep them in memory; avoid writing to disk.
- Never log secret values or full JSON payloads.

## CI usage pattern
1) Add masked/protected secrets named `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID`.
2) Validate both variables are present before running BWS commands.
3) Fetch required secrets at runtime and pass them to the process that needs them.

## Hardening checklist
- Scope tokens to read-only and to the minimal project/collection.
- Rotate tokens regularly and after suspected exposure.
- You must use separate tokens for prod vs non-prod.
- Avoid passing secrets through command arguments when possible.

See also:
- `bitwarden-secrets-local.md`
- `secrets.md`
- `key-management.md`
- `overview.md`
- `$CODEX_HOME/snippets/ci/bitwarden_bws_env.sh`
- `$CODEX_HOME/index/core/security.md`
