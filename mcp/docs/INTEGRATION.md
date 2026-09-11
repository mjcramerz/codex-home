# Supplied Debian preseed integration

## Existing identities and services

The reviewed preseed has a locked, no-login `devops:devops` system account whose passwd home is the absent `/nonexistent` sentinel. It has subordinate IDs, no linger record, no user manager, and no user runtime directory. PID 1 owns `podman-devops-bootstrap.service`; the rootless API socket is `/run/podman-devops/podman.sock`, devops:devops mode 0660. The desktop is a trusted devops-group member. This project uses the installed `/usr/local/bin/podman` policy wrapper and that fixed socket; it does not create a competing rootful engine or change the main SSH policy.

The preflight checks the existing engine is rootless, reports Podman >=5.8.6, and has cgroup v2, expected account identities, protected socket/runtime directories, required executables and the audited profile. It also validates the private `/data/codex/sockets` directory and the app-server control directory, startup lock, and control-socket symlink created by the preseed. A changed profile fails closed because automatically sourcing arbitrary shell code or silently expanding mounts is not acceptable. Re-review `integration/71-devops-de.sh.reference` and the mapping before accepting an upstream preseed change.

## Profile paths

`lib/toolchain.py` enumerates every explicit PATH root from `71-devops-de.sh`: OBS/aptly helper roots; OpenTufo; Ansible; Deno; yt-dlp; Terraform/Packer; Wrangler; aptly; osc/obs-build; rustup; Node 26; Bazelisk; LLVM 24; CUDA 12.8, 12.9 and 13.1; Codex and llama binaries; plus per-desktop Python, uv, Go, Deno, Cargo, npm, pnpm, Yarn, rustup and mise installations. `/usr/local/bin` is visible at `/opt/host/bin` rather than overmounting the image's own entrypoints.

The supplied environment exports are parsed as a restricted, audited literal subset, never evaluated as shell. `/pool/build/<desktop>`, `/pool/cache/<desktop>` and `/pool/db/<desktop>` exist at the same paths inside the container but default to private per-session scratch; explicit tool installation roots overlay them read-only. The container identity variables remain devops. Home/config/history variables point to private directories, not desktop authentication state.

`/etc/codex/mcp/toolchain-coverage.json` records all mounts, profile PATH entries, environment values and missing roots. `TOOLCHAIN_REQUIRE_ALL=true` makes missing installation roots a deployment-session error and missing probed tools a probe failure; default false supports machines that omit some optional toolchains. The explicit host Node executable is `/usr/local/lib/node-26/bin/node`. The MCP Python/Node packages deliberately start with the image's pinned runtimes so host PATH order cannot accidentally replace their interpreter.

Visibility is not ABI compatibility. The supplied image is Trixie-based while the host is Forky. A host ELF binary may need newer libraries than the image has. `sudo make toolchain-check` executes fixed, non-mutating version probes, reports missing/failed tools and fails for an unavailable host Node or failed executable. It is a representative probe, not a full test of every profile tool. The image also installs compatible in-image base development tools. Do not overmount host `/usr` or libc as a shortcut; add a reviewed compatible package/runtime layer and rerun target tests when a required tool fails.

## Codex wrapper and AppArmor

The supplied Codex wrapper uses Bubblewrap plus a separate slirp network namespace, masks `/run`, and exposes the private `/data/codex` tree. The broker listener therefore uses `/data/codex/sockets/codex-mcp.sock`, beside but distinct from `app-server-control.sock` and `app-server-backend.sock`. The app-server startup lock remains `/data/codex/usr/home/app-server-control/app-server-startup.lock`; MCP session, capacity, and GC locks are volatile below `/run/podman-devops/codex-mcp`. Neither subsystem reuses or removes the other subsystem's socket or lock. The wrapper retains the actual desktop UID, so Unix peer authorization still works despite synthetic environment identity variables.

The installer adds the `codex-mcp-client` abstraction to the existing `managed-codex-runtime` abstraction and reloads `managed-desktop-wrappers` and `chatgpt` when present. It permits the exact MCP client socket, protected client release, known_hosts and desktop automation key. It does not grant `/run/podman-devops/podman.sock` to the app. Missing shared abstraction is a preflight/integration error, not a reason to disable AppArmor. The real host parser and confined client launch remain acceptance tests.

`home/config.toml` covers supported local Codex engine settings used by the CLI and covered desktop capabilities. It is not a universal ChatGPT cloud configuration, does not register a cloud-accessible stdio service, and cannot grant workspace features, account seats, app logins or private desktop preferences. Check the actual desktop-embedded engine independently from the CLI version.

The supplied manifest is a single OCI image manifest, not a multi-architecture index. Its architecture must match the target; image pull/build and the runtime identity probe must succeed before activation. No cross-architecture emulation is configured.
