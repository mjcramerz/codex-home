# Docker Buildx
Purpose: tell the Codex coding agent how to use `docs/containers/buildx.md` as a runtime-pack surface and when to stop browsing.
Buildx enables multi-platform builds and advanced caching via BuildKit.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/containers/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## When to use
- building multi-arch images (e.g., `linux/amd64`, `linux/arm64`)
- using cache exports/imports in CI
- consistent builds across hosts

## Determinism and safety
- Avoid `:latest` base images; prefer pinned versions (or image digests for high assurance).
- You must use lockfiles inside builds (e.g., `Cargo.lock`, `requirements.txt` / lockfile).
- You must keep network use explicit. When possible, build with restricted network or vendor dependencies.
- If a build requires outbound network, document why and keep it bounded (proxies, retries).

## Common pitfalls
- Cross-arch emulation may be slow (QEMU); prefer native builders for high-volume CI.
- Some images require binfmt/qemu registration on the host; treat that as privileged host configuration.

## Buildah (Podman builds)
If you are on Podman:
- `podman build` and Buildah both accept Dockerfile/Containerfile inputs; Buildah offers more granular control.
- For daemonless builds outside Podman, use `buildah bud` with the same Dockerfile.

See also:
- `overview.md`
- `docker-compose.md`
- `dockerfile.md`
- `../workflows/containers.md`
- `$CODEX_HOME/templates/containers/docker-compose-skeleton/`
- `$CODEX_HOME/templates/containers/dockerfile-skeleton/`
- `$CODEX_HOME/index/domains/infra/containers.md`
