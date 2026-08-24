# Plugins runtime overview
Purpose: tell the Codex coding agent how to use `docs/plugins.md` as a runtime-pack surface and when to stop browsing.

You must use this guide when working with runtime plugin bundles inside an installed Codex home.

## What exists at runtime
- Plugin enablement lives in `$CODEX_HOME/config.toml` under `[plugins]`.
- Each local marketplace root carries its own `.agents/plugins/marketplace.json`.
- The configured `codex-home` marketplace root lives at `$CODEX_HOME/marketplaces/codex-home/`.
- Additional configured Git marketplaces can point at external plugin repos such as the official `openai-curated` source at `https://github.com/openai/plugins`.
- The managed in-place runtime snapshot still lives at `$CODEX_HOME/.agents/plugins/marketplace.json`.
- Installed plugin bundles live under `$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/local/`.
- Marketplace source paths must resolve from a marketplace root's `.agents/plugins/marketplace.json`
  back to that root's `plugins/cache/<marketplace>/<plugin>/local/`.
- Plugin bundle ids use `<plugin>@<marketplace>`.

## Current high-value bundles
- `codex-runtime` for runtime configuration and hook/runtime work.
- `cloudflare-workers` for Worker plus shared delivery workflows.
- `system-infra` for host hardening, preseed, and low-level runtime operations.

## How to invoke plugins and skills
- Plugins do not appear in `/` slash-command lists.
- Plugin bundle mentions use the `$` mention picker and store `plugin://<plugin@marketplace>` bindings.
- Plugin-local skills, tools, and apps also use the `$` mention picker and `skill://...` or `app://...` bindings.
- Select the popup entry so Codex stores the hidden bound mention for that turn.
- Typing plain `$plugin-name`, `$skill-name`, or `$app-name` text without selecting the popup is not the same as inserting the bound mention.

## What a bundle contains
- `.codex-plugin/plugin.json` — plugin manifest and interface metadata.
- `skills/` — plugin-local skills exposed by the bundle.
- `.mcp.json` — plugin-scoped MCP server definitions when present.
- `.app.json` — plugin-scoped app definitions when present.

## Runtime checks
- Inspect enabled plugins with `rg -n "^\[plugins\]" "$CODEX_HOME/config.toml"` and `rg -n "enabled =" "$CODEX_HOME/config.toml"`.
- Inspect the configured `codex-home` marketplace with `python3 -m json.tool "$CODEX_HOME/marketplaces/codex-home/.agents/plugins/marketplace.json"`.
- Inspect configured Git marketplace sources with `rg -n "^\[marketplaces\." "$CODEX_HOME/config.toml"`.
- Inspect the marketplace with `python3 -m json.tool "$CODEX_HOME/.agents/plugins/marketplace.json"`.
- Inspect one installed bundle with `find "$CODEX_HOME/plugins/cache" -maxdepth 5 -type f | sort`.

## Related runtime paths
- `$CODEX_HOME/config.toml`
- `$CODEX_HOME/marketplaces/codex-home/.agents/plugins/marketplace.json`
- `$CODEX_HOME/.agents/plugins/marketplace.json`
- `$CODEX_HOME/plugins/cache/`
- `$CODEX_HOME/index/pack/plugins.md`
