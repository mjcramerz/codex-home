# Secrets handling
Purpose: tell the Codex coding agent how to use `docs/security/secrets.md` as a runtime-pack surface and when to stop browsing.
- Do not commit secrets.
- You must prefer environment variables or a secrets manager.
- Never log secrets.
- Redact sensitive values in error paths.
- For local dev, use `.env` but keep it out of git.
- Rotate credentials regularly and design for rotation (short-lived tokens where possible).
- Apply least privilege: scoped tokens, minimal IAM permissions.
- For CI, prefer a dedicated secrets manager (e.g., Bitwarden Secrets Manager).
- For local hosts, prefer keyring-backed storage and retrieval patterns (`bitwarden-secrets-local.md`).
- Store private keys in a secrets manager; see `key-management.md`.
- For managed MCP config, keep `bearer_token_env_var` on URL transports only; stdio / `command` transports must use wrapper `env_vars` instead.
- You must treat `secrets.toml` as the managed-secret allow-list: only entries set to `true` are exported into runtime wrapper launches.
- For stdio / `command` MCP servers, any keyring-backed token must appear both in that server's `env_vars` list and under the matching server name in `secrets.toml`.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Runtime workflows

### `codex-login`
- You must use `codex-login` from PATH for Codex access-token login; the default managed wrapper path is `/data/bin/codex-login`.
- The wrapper runs `codex logout` first, then reads the token from either a hidden prompt or a one-shot `CODEX_ACCESS_TOKEN` environment value.
- You must prefer a one-shot environment assignment instead of a long-lived shell export, for example `CODEX_ACCESS_TOKEN='at-…' codex-login`.
- Do not add `CODEX_ACCESS_TOKEN` to shell profiles, dotfiles, or shared scripts.
- The wrapper removes `CODEX_ACCESS_TOKEN` from the child process environment and sends the token to `codex login --with-access-token` only over stdin.
- Managed Codex login accounts are configured in `/data/codex/lookup/auth.toml`.
- Valid TOML for email-style account names uses quoted keys, for example:

```toml
version = 1
service = "codex-login"

[codex_login."copilots@jcra.io"]
CODEX_ACCESS_TOKEN = true

[codex_login."matthew@gmail.com"]
CODEX_ACCESS_TOKEN = true
```

- You must run `codex-login --init` to prompt for each enabled account in `/data/codex/lookup/auth.toml` and store the corresponding `CODEX_ACCESS_TOKEN` values in the local keyring.
- On a normal `codex-login` run, enabled accounts that already have stored keyring tokens are listed for selection before login proceeds.

### Managed MCP token enablement
- You must treat the installed managed secret file, typically `/data/codex/lookup/secrets.toml`, as the runtime allow-list for MCP token injection.
- You must keep token values out of that file; it must contain booleans only.
- A token is exported into a wrapper launch only when both conditions are true:
  1. the matching `secrets.toml` entry is set to `true`
  2. the matching MCP server is enabled in `$CODEX_HOME/config.toml`
- URL MCP servers use `bearer_token_env_var`; stdio / `command` servers use `env_vars`.
- During installer-driven setup, the managed runtime can prompt securely for any enabled MCP token that is still missing from the local keyring.
- You must use `codex-mcp-token <SECRET_NAME> <TOKEN>` for explicit rotation or first-write of enabled managed MCP tokens.

Example enablement for Context7:

```toml
[mcp_servers.context7]
CONTEXT7_API_KEY = true
```

Example secure keyring store for Context7:

```sh
read -r -s CONTEXT7_API_KEY
printf '%s\n' "$CONTEXT7_API_KEY" | secret-tool store \
  --label='Codex managed secret: mcp_servers.context7 (CONTEXT7_API_KEY)' \
  service codex-mcp name mcp_servers.context7
unset CONTEXT7_API_KEY
```

### Rotation and disablement
- Rotate a managed MCP token with `codex-mcp-token`, for example `codex-mcp-token CONTEXT7_API_KEY new-token-value`.
- The wrapper only accepts keys that exist in `/data/codex/lookup/secrets.toml` and are currently set to `true`.
- If a key exists but is disabled, the wrapper exits with `Please enable secret first and try again later`.
- Writing a new value for the same `service` + `name` pair is enough; the next wrapper launch picks it up automatically.
- Disable runtime injection by setting the matching entry in `/data/codex/lookup/secrets.toml` to `false`.

Patterns:
- Python: load via pydantic-settings; validate at startup.
- Rust: load via env + typed config; fail-fast on missing required secrets.

## CI/CD notes
- You must keep workflow permissions minimal and avoid long-lived deploy keys.
- You must prefer OIDC (`id-token: write`) to exchange for short-lived cloud creds when supported.
- Do not print environment dumps in CI logs.
- You must add secret scanning in CI when available.

See also:
- `overview.md`
- `bitwarden-secrets.md`
- `bitwarden-secrets-local.md`
- `key-management.md`
- `../workflows/ci-cd.md`
- `$CODEX_HOME/index/core/security.md`
