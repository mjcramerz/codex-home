# Bitwarden Secrets Manager (BWS) for local hosts
Purpose: tell the Codex coding agent how to use `docs/security/bitwarden-secrets-local.md` as a runtime-pack surface and when to stop browsing.
Guidance for using BWS on local Debian systems with OS keyring storage.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Local-only objective
- You must keep `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` in the user keyring for local development and operator tasks.
- Expose `bws` through deterministic system PATH wiring.
- Enforce non-root invocation with explicit sudo only for privileged filesystem/package steps.

## Baseline controls
- You must validate token/project ID structure before any write operation.
- Write secrets only through keyring tooling (Secret Service/libsecret), not persistent shell files.
- You must keep keyring service/account identifiers constrained to safe character sets.
- Avoid command patterns that print secret values to stdout/stderr.

## Lifecycle
1) Install pinned `bws` binary and verify SHA256.
2) Configure user-scoped PATH snippet under `~/.profile.d`.
3) Store `BWS_ACCESS_TOKEN` and `BWS_PROJECT_ID` in keyring.
4) Retrieve values on demand via keyring-aware helper commands.
5) Rotate keyring entries when credentials change.

## Operational checks
- `bws --version` resolves from PATH in a new shell session.
- Keyring status checks pass after install and after rotation updates.
- No secret values appear in command output, shell history, or logs.

## Local vs CI/CD
- Use this document only when the task targets a local host.
- For CI-oriented BWS patterns, use `$CODEX_HOME/docs/security/bitwarden-secrets.md`.

See also:
- `$CODEX_HOME/docs/workflows/bws-local.md`
- `$CODEX_HOME/docs/security/secrets.md`
- `$CODEX_HOME/index/domains/system/bws-local.md`
