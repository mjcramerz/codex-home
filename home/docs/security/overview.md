# Security overview
Purpose: route security work to the right checklist, threat-model, or defensive operations guide for the Codex coding agent.
You must read only the smallest section that resolves the current task, follow the first matching route, and stop broad browsing once the next concrete file or command is clear.

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
- You must validate and bound untrusted input.
- You must keep least privilege explicit across code, CI, containers, and host access.
- You must treat dependency provenance and release integrity as part of the security surface.
- You must keep secrets and sensitive logs out of repo-managed artifacts.

## Adjacent routing
- App/service hardening -> `web-hardening.md` and `review-hardening.md`
- CI/release trust -> `../workflows/ci-cd.md` and `../workflows/release.md`
- Host/device hardening -> `../system/overview.md`
