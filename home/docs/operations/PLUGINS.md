# Portable plugin and hook lifecycle

This is agent-facing runtime-pack guidance. Use it when authoring, synchronizing,
or validating local plugin bundles; it is not an end-user installation guide.

## Current OpenAI packaging contract

Local bundles use the portable Agent Plugins 1.0 layout documented in
[Package your plugin](https://developers.openai.com/plugins/build/plugins):

- `plugin.json` at the plugin root is canonical.
- `$schema` is exactly
  `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`.
- OpenAI presentation, registered app mappings, and hooks live below
  `extensions.com.openai`.
- Portable packages discover immediate `skills/<skill>/SKILL.md` entries without
  a `skills` manifest field.
- `.codex-plugin/plugin.json` remains a generated compatibility fallback for the
  pinned Codex 0.147.0 deployment baseline. Never author it independently.
- Local plugin version `1.1.0` identifies this packaging migration and forces a
  deterministic runtime-cache refresh.

The current field and error contracts are grounded in OpenAI's
[plugin submission error reference](https://developers.openai.com/plugins/deploy/submission-errors).
Public-directory submission has additional listing, image, policy, and registered
MCP eligibility requirements; local validation does not claim public acceptance.

## Source and mirror ownership

```text
codex-home authoring source
  home/plugins/<plugin>/plugin.json
    -> generated home/plugins/<plugin>/.codex-plugin/plugin.json
    -> generated marketplace-local bundle
    -> generated versioned runtime cache

repo-local authoring source
  home/marketplaces/repo-local/plugins/cache/repo-local/<plugin>/local/plugin.json
    -> generated .codex-plugin/plugin.json
    -> generated versioned runtime cache

core skill authoring source
  skills/<skill>/
    -> generated home/skills/<skill>/
    -> generated home/.agents/skills/<skill>/
```

Marketplace files own plugin ordering, source paths, and install/authentication
policy. Generation preserves that policy while synchronizing each entry's portable
manifest description, OpenAI interface, accepted category, compatibility fallback,
and current version path. Do not patch a marketplace-local bundle or versioned
cache directly.

## Skill metadata

Every bundled skill with `agents/openai.yaml` follows OpenAI's
[skill packaging guidance](https://developers.openai.com/plugins/build/skills):

- `interface.display_name` and `interface.short_description` are present.
- Optional icons are safe `./`-prefixed paths to regular files inside the skill.
- `interface.default_prompt`, when present, explicitly mentions `$<skill-name>`.
- `policy` contains only `products` and/or `allow_implicit_invocation`.
- `dependencies` contains only `tools`; each retained tool is a remote MCP
  dependency whose identifier and HTTPS URL exactly match `home/config.toml`.
- Generic filesystem, Git, fetch, reasoning, Linear, or time boilerplate is not a
  dependency declaration. Local MCP transport remains globally configured through
  `/usr/local/bin/codex-mcp connect SERVER` and the private
  `/data/codex/sockets/codex-mcp.sock`; metadata declares only grounded remote MCP
  URLs and never exposes the Podman engine socket.

## Generation and validation

Run from the repository root:

```sh
make generate
python3 generate/scripts/plugin_catalog_coverage.py
python3 -m unittest -v tests.test_plugin_catalog
```

`make generate` updates sources only through their documented generator: core
skill mirrors, portable compatibility manifests, marketplace-local bundles,
versioned caches, marketplace projection, config mirrors, and other pack-derived
assets. A second synchronization must report zero changes. `make verify` includes
the catalog checks but does not certify an external marketplace, registered app,
remote MCP service, or installed desktop runtime as reachable or trustworthy.

## Security and lifecycle boundaries

Review plugin origin, requested tools, registered app identity, credential scope,
write approvals, and execution permissions before enabling new code. Do not modify
product-managed caches during a running client session. Asset installation backs up
overwritten files and preserves unrelated runtime data; it does not reset secrets,
auth databases, preferences, or session history.

Lifecycle hooks execute trusted local code, not downloaded instructions. The bounded
hook runner enforces JSON framing, input/output caps, timeouts, and process-group
cleanup. PreToolUse and PermissionRequest infrastructure failures fail closed;
non-policy notification failures emit a generic warning without private payloads.
Hook logs must not contain prompts, command arguments, tokens, or raw tool output.
Install the documented Perl dependencies before enabling the real hooks.
