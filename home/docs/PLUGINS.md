# Restored plugins and skills

All original plugin source marketplaces, versioned runtime mirrors, standalone
skills, `.agents` metadata and 54 plugin configuration entries are retained at
their original paths. The earlier replacement that reduced this to a new
source-only marketplace is superseded. Original browser/REPL instructions are
restored; the desktop node_repl MCP remains configured.

The local `codex-home` and `repo-local` marketplace sources and their corresponding
versioned mirrors can be checked offline. `openai-curated` is the original git
marketplace configuration. `openai-bundled` points to the original app-generated
`.tmp/bundled-marketplaces/openai-bundled` location; its browser-service and Node
resources are supplied by the desktop installation. They are not synthesized or
misrepresented as present in this archive. Run target runtime checks before using
those integrations.

Configured/enabled does not mean authenticated or installed by the running
product. Source metadata, app installation state, cached payloads, tool approvals
and OAuth authorization are distinct. The installer backs up changed source
assets and does not delete unrelated cache entries. It preserves existing opaque
desktop preferences. Review conflicting user edits before deploying.

The original standalone `skills/` collection and all instruction/catalog sources
remain. The preseed supplies CODEX_HOME/CODEX_AGENTS/CODEX_SKILLS; actual discovery
must be verified with the matching custom binary and desktop application.
