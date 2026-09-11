# Configure the active Codex runtime

Use this guide when you change Codex settings, diagnose configuration precedence, or compare client versions. Do not load configuration files or schemas for unrelated coding tasks.

## Establish the effective configuration

Identify the actual Codex executable and version, the process's `CODEX_HOME`, its selected profile, and any command-line or managed-policy overrides. Treat this repository's `home/` as the future `$CODEX_HOME`, not as proof that it has already been installed. Inspect only the settings needed for the task; never print authentication files, complete environments, or secret-valued headers.

Preserve every existing key in `home/config.toml`. The supplied model/provider IDs, absolute `/data/codex` paths, instruction overrides and model catalogues are deployment inputs, not a guarantee of entitlement or installed files. Confirm those paths and the custom client's behavior before launch. Do not replace a complete custom model catalogue with an incomplete fragment.

In this scoped revision, `home/config.toml` is intentionally newer than the unchanged `etc/config.toml`. Do not claim they are byte-identical, run an assumed synchronizer, or overwrite either direction without an explicitly authorized synchronization task. No root Makefile or generator is guaranteed to exist.

## Apply version-aware settings

Use the selected release's public configuration reference, tagged schema and feature registry together. This configuration records supported settings from the inspected 0.147.0, 0.153.0 and 0.154.0 surfaces; that is not a promise that every setting works in every historical or future client. A schema can retain aliases and removed no-op flags. Preserve existing compatibility entries, but do not add deprecated aliases as new features.

Keep supported, meaningful settings active. Keep alternatives commented when they require a real account identifier, trusted executable, credential source, collector, origin or application ID. Do not activate placeholder examples merely to make a table nonempty. Do not activate every experimental flag: capability declarations, installed tools and backend support are separate facts.

The `default_permissions` and older `sandbox_mode`/`sandbox_workspace_write` mechanisms are alternatives. Do not combine them in one effective configuration. Likewise, keep one compaction-prompt source and one provider authentication mechanism. A valid TOML parse does not prove semantic or cross-version compatibility.

## Preserve broad networking without confusing it with trust

The selected `full` permission profile grants full local filesystem access. All three supplied profiles enable outbound networking; `workspace` and `readonly` retain their different local filesystem rules. Read-only local access does not prevent a remote API write.

The Codex command proxy remains disabled, so command traffic uses direct networking or the host's configured proxy environment. Domain rules in the permission profiles are dormant in this mode, including the retained metadata-deny entries. Do not describe these entries as an enforced security boundary while the proxy is off. Host firewalls, DNS, managed requirements and upstream policies can still constrain connectivity.

For a future explicitly mediated setup, each profile includes `"*" = "allow"` and named Git, source-hosting, registry, language-package, cloud, vendor and Filen destinations. The wildcard covers unlisted and self-hosted names; no finite vendor list is exhaustive. Keep listeners on loopback and preserve explicit socket permissions. Do not expose proxy listeners to the network or disable TLS verification to solve a connection problem.

Web-search domain filtering remains unrestricted. App/connector traffic and remote service authorization are separate from command-proxy policy. Connectivity never authorizes publishing code, uploading private data, using unrelated credentials or mutating production.

## Keep context and hooks separate from schemas

`hooks.json` owns the active command hooks. The inline `[hooks]` arrays are empty intentionally; registering the same handlers in both places would duplicate them. Read [the hook contract](HOOKS.md) before changing lifecycle behavior.

Do not inject `config.toml`, configuration schemas, model catalogue bodies, full transcripts or complete tool responses into ambient context. Consult a small relevant schema section only during an actual configuration task. Keep all authoritative tool results in the normal conversation instead of replaying them through hooks.

## Configure desktop settings from public contracts

Treat `[desktop]` as opaque to the CLI. Its documented `custom_file_handlers.<id>` table exposes `command`, `args`, `label`, `icon`, `input` and `supports_ssh`. The supplied Debian handler uses those fields. Check that the executable and icon exist and that the selected app supports the handler contract; a handler entry does not establish Debian desktop-app support.

Do not invent private desktop keys or treat managed desktop feature gates as ordinary user-config overrides. Do not grant browser-history, full CDP or desktop-application access just because a network operation is allowed.

## Check the changed contract

Parse the edited TOML, compare retained keys, and inspect only the applicable schema definitions and release notes. Check actual file paths and tool availability on the target host. Exercise the relevant client startup or config command only when the client is installed and the action is authorized. Report parsing, fixture behavior, client acceptance, authentication and live service access separately.

## Primary references

Consult these sources only for a configuration task, and select the actual installed release rather than assuming the newest branch is compatible:

- [Configuration reference](https://developers.openai.com/codex/config-reference)
- [Permissions](https://developers.openai.com/codex/permissions)
- [Hooks](https://developers.openai.com/codex/hooks)
- [Tagged 0.154.0 configuration schema](https://raw.githubusercontent.com/openai/codex/rust-v0.154.0/codex-rs/core/config.schema.json)
- [Tagged 0.154.0 feature registry](https://raw.githubusercontent.com/openai/codex/rust-v0.154.0/codex-rs/features/src/lib.rs)
