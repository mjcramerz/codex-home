# Cloudflare R2
Purpose: guide Cloudflare R2-backed artifact publication and readback contracts for the Codex coding agent.

## Use this guide when
- reviewing bucket, prefix, or object layout for published artifacts
- checking how a Worker or other front-end serves data from R2
- validating that CI publication and runtime reads agree on naming and retention

## Baseline
- Keep bucket names, prefixes, and publication paths explicit and deterministic.
- Prefer immutable object keys and append-only publication semantics over silent overwrites.
- Keep access keys, secret keys, and signing material out of tracked config and out of early-evaluated CI surfaces.
- Record which layer owns metadata normalization: publisher, worker, or downstream client.

## Validation ladder
1. Verify bucket, prefix, and endpoint inputs.
2. Check that publication and readback use the same path contract.
3. Run the smallest artifact upload/readback test that proves the change.
4. Revalidate CI includes and runtime docs when the storage contract changes.

## After that, you must check related files
- `$CODEX_HOME/docs/workflows/cloudflare-r2.md`
- `$CODEX_HOME/docs/workflows/cloudflare-delivery.md`
- `$CODEX_HOME/index/domains/infra/cloudflare-r2.md`
