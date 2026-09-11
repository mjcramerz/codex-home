# Security overview

Use this guide when you review authentication, authorization, trust boundaries or defensive security controls. Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/OVERVIEW.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Start here

- Review hardening: `review-hardening.md`
- Threat modeling: `threat-model.md`
- Secrets and key handling: `secrets.md` (includes `codex-login` and managed MCP operator flow), `key-management.md`
- Supply chain: `supply-chain.md`, `supply-chain-controls.md`
- Logging and data hygiene: `logging.md`
- Security-labs references: `security-labs-index.md`, `security-labs-repo-catalog.md`, `security-labs-tool-guides.md`

## Baseline expectations

- Validate and bound untrusted input.
- Keep least privilege explicit across code, CI, containers, and host access.
- Treat dependency provenance and release integrity as part of the security surface.
- Keep secrets and sensitive logs out of repo-managed artifacts.

## Adjacent routing

- App/service hardening -> `web-hardening.md` and `review-hardening.md`
- CI/release trust -> `../workflows/ci-cd.md` and `../workflows/release.md`
- Host/device hardening -> `../system/overview.md`
