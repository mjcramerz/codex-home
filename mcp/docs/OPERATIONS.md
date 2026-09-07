# Operations and recovery

## Credential inventory

The following names are accepted by `codex-mcp-admin credential --name NAME`. Master files are `/etc/codex/mcp/credentials/NAME`. Do not put secret values in `.env` or TOML.

| Credential name | Consumer | Requirement |
| --- | --- | --- |
| postgres-dsn | PostgreSQL DBHub | Required, real database and TLS DSN |
| context7-api-key | Context7 | Optional authenticated quota/access |
| semgrep-app-token | Semgrep | Optional platform-dependent features |
| openai-api-key | MarkItDown | Optional provider-dependent conversion |
| azure-openai-api-key | MarkItDown | Optional Azure credentials |
| azure-openai-endpoint | MarkItDown | Optional Azure endpoint |
| azure-openai-api-version | MarkItDown | Optional Azure API version |
| fetch-proxy-url | Fetch | Optional proxy URL, potentially secret-bearing |
| github-token | Git askpass | Optional; local Git mode remains network-disabled |

Provision with a hidden prompt:

```sh
sudo make credential NAME=postgres-dsn
sudo make credential NAME=context7-api-key
```

For controlled import, use a pre-existing mode-0600 regular file:

```sh
sudo codex-mcp-admin credential --name postgres-dsn --file /root/secure/postgres-dsn
```

A DSN has the general form `postgresql://ROLE:URL_ENCODED_PASSWORD@HOST:5432/DATABASE?sslmode=verify-full`. Do not use container `localhost` to mean the desktop host. This code deploys the **PostgreSQL MCP adapter**, not a PostgreSQL database server. Provision an appropriate database, role, network route and certificates separately. Optional credential projection does not prove every upstream conversion option will use a provider automatically; verify the required feature in the actual server version.

Updates are atomic, but a running service retains its old systemd credential snapshot and container process. Reconnect affected clients or run `sudo make restart` to drain all sessions. Revocation must also occur at the provider when a secret is compromised. There is intentionally no command that prints secrets back to the operator.

## Day-to-day commands

```sh
sudo make status
sudo make logs
sudo make doctor
sudo make down
sudo make up
sudo make restart
```

`down` and `restart` interrupt tool sessions; coordinate with users. Logs contain session identifiers, server names, lifecycle and byte counts rather than raw prompts or upstream error payloads. Use the actual service units for more lifecycle detail: `journalctl -u 'codex-mcp@*'` and `systemctl status codex-mcp-sshd.service`. Suppressed upstream stderr protects credentials but reduces diagnostics. Reproduce a problem with a nonsecret test configuration in a controlled environment instead of logging production DSNs.

`make smoke` checks initialize/tools-list for every server and creates, reads, edits from the desktop and removes only a uniquely named Workspace test file. It does not make paid provider calls or demonstrate every possible server tool. Run `make smoke-ssh` separately from a native desktop shell. Check there are no abandoned managed containers after clients disconnect. The GC timer handles normal retryable cleanup; an engine outage is not proof cleanup succeeded.

## Upgrade and rollback

Close clients; preserve source/config backups and persistent state. The target is the custom build based on 0.147.0; retain its supplied schema and instruction bindings. `python3 scripts/refresh_schema.py` fetches only pinned 0.147.0 upstream reference material and never changes the custom schema. A future custom-binary update requires its actual schema and a reviewed lifecycle policy, not automatic migration to a newer stock release.

For an MCP code or image change, review `.env`, run tests, then `sudo make deploy DESKTOP_USER=YOUR_DESKTOP_USER`. Installs are serialized and stop the target. Protected previous releases remain under `/usr/local/libexec/codex-mcp/releases/`. Matching image build inputs allow the installer to retain the old immutable image ID, but deploy still executes a build. The resulting ID and dependency evidence live under `/etc/codex/mcp/`.

Rollback is explicit, not an automatic reverse transaction: stop the target, restore a matching backed-up runtime/client configuration and unit set, atomically repoint `current` to the corresponding protected release, run `systemctl daemon-reload`, verify the referenced image is still present, and rerun acceptance before reopening clients. Reinstalling the previously reviewed source is usually safer than hand-editing hashes. Never rollback only code while leaving an incompatible runtime schema/image or changed database state.

## State backup and restore

```sh
sudo make backup FILE=/root/codex-mcp-state.tar.gz
# Services remain stopped. Copy the private backup to approved protected storage.
sudo make up
```

Backup stops the target and verifies no managed containers remain. It reads only memory/SQLite state as devops, writes an exclusive mode-0600 archive and rejects links/special files. No master credentials, desktop Workspace or PostgreSQL database contents are included. Back up those separately with the proper owners and database-native tools.

Restore is allowed only to empty memory/SQLite state:

```sh
sudo make restore FILE=/root/codex-mcp-state.tar.gz
sudo make up
```

Restore rejects traversal, links, special files, unexpected paths and archives above 10 GiB uncompressed. It does not trust archived ownership. It is not a cross-database atomic migration: preserve an old-state backup and keep clients closed until validation succeeds.

## Uninstall

`sudo make uninstall` stops/disables the target, removes its unit files, client links and managed AppArmor include, and reloads affected configuration. It deliberately retains credentials, state, images, network, protected releases, desktop SSH key and ACL backups. This avoids destructive surprise and allows recovery.

ACL snapshots are under `/etc/codex/mcp/acl-backups/`. Review and restore the applicable snapshots using `setfacl --restore=FILE` only after stopping clients and comparing any intentional ACL changes since installation. A stale ACL backup can undo later legitimate access changes. New Workspace files did not exist in the snapshot; review their inherited ACLs separately. Revoke the dedicated SSH authorization and delete its desktop private/public key only after confirming no consumer still uses it. Remove retained secrets and state under a separate explicit retention/destruction decision; never run a blanket Podman prune.

Client startup/tool deadlines are explicit in home/config.toml (currently 120/180 seconds). Broker startup is 90 seconds in .env. Edit the relevant client values deliberately when changing broker timing, then run root make generate to synchronize the complete etc mirror. Generation never overwrites user config from .env. An alternate ENV_FILE does not rewrite client TOML; the broker lifetime/startup/idle controls remain independent from client deadlines.

## Backup publication and import limits

Backup destinations must be in a dedicated root-owned protected directory. A
mode-0600 temporary archive is flushed before atomic no-overwrite publication;
partial data is never published under the requested backup name. Restore rejects
links, special files, path traversal, more than 100000 members and data above
10 GiB. Restore remains a stopped-service, per-state-directory operation, not a
whole-host transaction. Preserve an independent verified backup first.
