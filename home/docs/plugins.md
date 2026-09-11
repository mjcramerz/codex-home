# Plugins runtime overview

Purpose: tell the Codex coding agent how to inspect and maintain portable local
plugin bundles inside this managed Codex home. Read only the section needed for the
current task.

## Runtime and authoring roots

- Plugin enablement lives in `$CODEX_HOME/config.toml` under `[plugins]`.
- Each local marketplace owns `.agents/plugins/marketplace.json` and its curated
  ordering plus install/authentication policy.
- `codex-home` authoring bundles live at repository source path
  `home/plugins/<plugin>/`; installed marketplace-local mirrors live below
  `$CODEX_HOME/marketplaces/codex-home/plugins/cache/codex-home/<plugin>/local/`.
- Repo-local authoring bundles live directly below
  `home/marketplaces/repo-local/plugins/cache/repo-local/<plugin>/local/`.
- Installed versioned bundles live below
  `$CODEX_HOME/plugins/cache/<marketplace>/<plugin>/<version>/`.
- The managed Codex marketplace projection is
  `$CODEX_HOME/.agents/plugins/marketplace.json`.
- Plugin ids use `<plugin>@<marketplace>`.

```text
root plugin.json (canonical Agent Plugins 1.0 manifest)
  -> .codex-plugin/plugin.json (Codex 0.147.0 compatibility fallback)
  -> marketplace-local bundle
  -> plugins/cache/<marketplace>/<plugin>/1.1.0
```

Do not edit a generated fallback, marketplace-local mirror, managed marketplace
projection, or versioned cache. Update the canonical source and run `make generate`.
Marketplace policy and ordering remain marketplace-owned rather than being inferred
from a plugin manifest.

## Bundle structure

- `plugin.json` - portable canonical manifest using the Agent Plugins 1.0 schema.
- `.codex-plugin/plugin.json` - generated legacy-compatible overlay only.
- `skills/<skill>/SKILL.md` - immediate skill entrypoints discovered by the portable
  package format.
- `skills/<skill>/agents/openai.yaml` - OpenAI UI, invocation policy, and required
  remote MCP dependency metadata.
- `mcp.json` - optional portable bundled MCP declaration when a plugin actually
  ships a server. Do not rename legacy `.mcp.json` blindly; the portable transport
  format differs.
- `.app.json` - optional registered app mapping referenced by
  `extensions.com.openai.apps`.
- Optional assets and lifecycle hooks referenced from the portable manifest.

This pack intentionally keeps its image-backed local MCP servers in the global
`home/config.toml` registry. Plugin skill metadata declares only genuine required
remote MCP servers and must not duplicate local broker commands.

## Invocation and routing

- Plugins do not appear in `/` slash-command lists.
- Bundle mentions use the `$` picker and store `plugin://<plugin@marketplace>`
  bindings.
- Plugin-local skills, tools, and apps use the same picker and store `skill://...`
  or `app://...` bindings.
- Selecting the picker entry creates the hidden bound mention; plain typed text is
  not equivalent.

High-value routes include `codex-runtime` for managed runtime configuration,
`cloudflare-workers` for Worker delivery, and `system-infra` for Debian and host
operations. Load only the bundle whose signals match the active task.

## Validation

From the source repository:

```sh
make generate
python3 generate/scripts/plugin_catalog_coverage.py
python3 -m unittest -v tests.test_plugin_catalog
```

The validator proves portable/fallback identity, accepted OpenAI categories,
marketplace metadata parity, source/local/runtime byte-and-mode parity, exact
version paths, current `agents/openai.yaml` shape, grounded remote MCP URLs, core
skill mirror parity, and absence of stale local-cache or wrapper references. It does
not prove external marketplace safety, registered-app eligibility, authentication,
network reachability, or live desktop loading.

## References

- [OpenAI: Package your plugin](https://developers.openai.com/plugins/build/plugins)
- [OpenAI: Build skills](https://developers.openai.com/plugins/build/skills)
- [OpenAI: Plugin submission errors](https://developers.openai.com/plugins/deploy/submission-errors)
- `$CODEX_HOME/docs/operations/PLUGINS.md`
- `$CODEX_HOME/config.toml`
- `$CODEX_HOME/index/pack/plugins.md`
