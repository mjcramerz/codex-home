# HTMX app skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/web/htmx-app/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal HTML + HTMX starter.

## Outputs
- `index.html`

## Notes
- Serve with any static server.
- Vendor `htmx.min.js` or pin the version explicitly.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.
