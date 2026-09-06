# Upgrade the custom Codex configuration

Use the schema emitted by the actual custom binary, not a newer upstream release.
The current target is the supplied custom build based on 0.147.0. Preserve all
custom instruction overrides, catalogs, provider/model settings and original
profile/feature choices unless the user explicitly requests a semantic change.
Experimental does not mean deprecated. Schema acceptance and live lifecycle status
are separate: remove only documented deprecated/removed compatibility entries or
keys rejected by the exact supplied schema. Record every change.

Validate home, system defaults and all profile/agent config layers against that
schema. Check requirements separately; config.schema.json does not describe the
managed-requirements format. Verify referenced instruction/catalog files, full
home/etc synchronization and original-file preservation. The generator only
updates mirrors; it does not replace the full main config or instruction tree.

Back up existing configuration, preserve opaque desktop settings, auth, sessions,
state and plugin files. Source or cache presence does not prove product installation
or authentication. Finish with actual custom-binary, desktop-resource, hook,
MCP and wrapper-namespace checks on the target. Do not report a static validation
as live product certification.
