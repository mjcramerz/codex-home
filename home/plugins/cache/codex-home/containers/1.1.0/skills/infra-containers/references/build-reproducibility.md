---
title: Build reproducibility
status: active
owner: Matthew Cramer
tags:
- skills
- all
- infra-containers
- references
- build-reproducibility-md
- build-reproducibility
- user
- infra
updated: '2026-02-20'
---
# Build reproducibility

## Pinning checklist
- Use immutable image references (digest or pinned version tags).
- Pin language and package manager versions.
- Keep lockfiles in version control and fail builds when lockfiles drift.
- Record build arguments that affect output artifacts.

## Deterministic build commands
```bash
docker build --pull=false --build-arg BUILDKIT_INLINE_CACHE=1 -t app:local .
docker buildx bake --print
podman build --pull-never -t app:local .
```

## Verification
- Compare resulting image digest across two local builds with unchanged sources.
- Diff SBOM output before/after dependency updates.
- Verify runtime UID/GID behavior against bind mounts.
