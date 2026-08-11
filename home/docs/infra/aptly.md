# Aptly
Purpose: guide Aptly publication, snapshot retention, and signed channel operations for the Codex coding agent.

## Use this guide when
- reviewing Aptly publish helpers, queue layout, or snapshot cleanup policy
- mapping stable/testing/unstable channels to deterministic release or promote flows
- checking how package publication integrates with GitLab delivery jobs or Cloudflare front-ends

## Baseline
- Keep publish endpoints, prefixes, and channel names explicit; do not rely on implicit default repos.
- Separate queue, working state, cache, and secrets directories so operators can audit retention and ownership independently.
- Prefer append-only snapshot publication and explicit retention windows over mutable in-place repository edits.
- Keep signing key material and passphrases out of tracked config; inject them through protected runtime state only.

## Validation ladder
1. Verify channel definitions and publish endpoints.
2. Check signing, snapshot naming, and retention inputs.
3. Run focused functional checks for the managed publish helper or cleanup contract.
4. Revalidate any operator docs or env snippets touched by the change.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/aptly.md`
- `$CODEX_HOME/docs/workflows/cloudflare-r2.md`
- `$CODEX_HOME/index/domains/infra/aptly.md`
- `$CODEX_HOME/snippets/ci/gitlab_delivery_vars.env`
