# Next.js app scaffold (overview)
Purpose: tell the Codex coding agent how to use `templates/web/nextjs-app/overview.md` as a runtime-pack surface and when to stop browsing.
This template is a wrapper around the official Next.js scaffold.

## Recommended approach
1) Pick a pinned Next.js version approved by your org.
2) Run `npx create-next-app@<version>`.
3) Add CI workflows from `$CODEX_HOME/templates/ci/github-actions/` or `$CODEX_HOME/templates/ci/gitlab-ci/`.

## Notes
- Pin Node.js and Next.js versions.
- You must keep server/client boundaries explicit.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- No additional files are currently defined in this template directory.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
