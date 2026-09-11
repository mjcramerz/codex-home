# Plugins (entrypoint)
Purpose: route portable plugin, marketplace, compatibility, and runtime-cache work for the Codex coding agent.
You must read only the smallest section that resolves the current task and stop broad browsing once the source and validator are known.

## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/index/pack/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

Canonical guidance: `$CODEX_HOME/docs/plugins.md` and
`$CODEX_HOME/docs/operations/PLUGINS.md`.

Use when:
- editing canonical Agent Plugins 1.0 root manifests
- tracing marketplace policy, source paths, generated compatibility fallbacks, or
  versioned runtime caches
- validating plugin skills, OpenAI metadata, registered apps, hooks, or grounded
  MCP dependencies

Source ownership:
- `home/plugins/<plugin>/` is canonical for `codex-home` bundles.
- `home/marketplaces/repo-local/.../<plugin>/local/` is canonical for repo-local
  bundles.
- `skills/<skill>/` is canonical for the mirrored core skill catalog.
- `.codex-plugin/plugin.json`, marketplace-local copies, `home/.agents/plugins/`,
  `home/skills/`, `home/.agents/skills/`, and versioned caches are generated.

Required check: `python3 generate/scripts/plugin_catalog_coverage.py`.

Related:
- `$CODEX_HOME/config.toml`
- `$CODEX_HOME/.agents/plugins/marketplace.json`
- `$CODEX_HOME/plugins/cache/`
- [OpenAI plugin packaging](https://developers.openai.com/plugins/build/plugins)
