# Vagrant + libvirt skeleton (overview)
Purpose: tell the Codex coding agent how to use `templates/virtualization/vagrant-libvirt-skeleton/overview.md` as a runtime-pack surface and when to stop browsing.
Minimal Vagrantfile scaffold targeting the libvirt provider (Linux).

## Requirements (host)
- Vagrant installed
- libvirt configured and accessible for your user
- libvirt provider plugin (installation varies by distro/Vagrant version)

## Quickstart
```bash
export VAGRANT_BOX="generic/debian12"   # choose a box compatible with your environment
export VAGRANT_BOX_VERSION="4.3.12"    # optional pin for reproducibility
vagrant up --provider=libvirt
vagrant ssh
```

## Network templates
The Vagrantfile includes a private network (DHCP). Adjust as needed:
- NAT only (default) for simpler isolation
- Private network for host↔VM dev access
- Bridged networking only when you explicitly need LAN exposure

## Notes
- You must treat provisioning scripts as privileged code inside the VM.
- Pin box versions and verify provenance when your policy requires it.

## Inputs
- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs
- Files copied from this template directory.
- `Vagrantfile`

## Next steps
1) Copy files into deterministic repository paths.
2) Replace placeholders and pin versions/images before first commit.
3) Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, you must check related files
- Docs: `$CODEX_HOME/docs/virtualization/overview.md`
