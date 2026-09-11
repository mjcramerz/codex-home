# Nuxt app scaffold (overview)

Use this template when you need nuxt app scaffold (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

Wrapper around the official Nuxt scaffold.

## Recommended approach

1. Pick a pinned Nuxt version approved by your org.
2. Run `npx nuxi@<version> init <app>`.
3. Add CI workflows from `$CODEX_HOME/templates/ci/github-actions/` or `$CODEX_HOME/templates/ci/gitlab-ci/`.

## Notes

- Pin Node.js and Nuxt versions.
- Keep runtime config explicit.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs

- Files copied from this template directory.
- No additional files are currently defined in this template directory.

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
