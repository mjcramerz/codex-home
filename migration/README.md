# Restoration inventory

The earlier stock-oriented refactor is superseded. All 6,802 original files are
restored in the live tree, with all 491 original instruction files byte-identical.
Original prompts, catalogs, hook scripts, docs, plans, snippets, templates, plugin
sources and runtime mirrors are not relegated to an inactive reference directory.
The retained Podman MCP deployment and additional validation tooling are additive.

`original-files.json` maps every original path to its SHA-256. `original-home-config.toml`
and `original-requirements.toml` preserve comparison baselines; do not activate
these unfiltered historical configs. `generate/restoration-changes.json` records
config migrations. `validation/RESTORATION.md`, `static-report.json` and
`home-config.diff` show the actual corrected tree and changes. The supplied schema
is unchanged. The active validator fails if any original file goes missing or any
original instruction source changes.

`legacy-source.tar.gz`, `input-manifest.json` and `input-artifacts.json` are retained
historical evidence from the prior package. The legacy archive is not the only
copy of the original assets. Do not extract it over a running install or restore
its obsolete feature switches. No generated target private SSH keys, provisioned
MCP API secrets or live database state are added to this source package.
