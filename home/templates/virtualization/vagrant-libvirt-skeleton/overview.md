# Vagrant + libvirt skeleton (overview)

Use this template when you need vagrant + libvirt skeleton (overview) in the authorized project. Replace placeholders, adapt the examples to the detected toolchain, and preserve the requested output contract. Do not treat sample values or commands as verified deployment settings.

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

- Treat provisioning scripts as privileged code inside the VM.
- Pin box versions and verify provenance when your policy requires it.

## Inputs

- Destination repository path for this template.
- Exact runtime/toolchain versions and pinning policy.
- Repository-specific values for placeholders, secrets, and host paths.

## Outputs

- Files copied from this template directory.
- `Vagrantfile`

## Next steps

1. Copy files into deterministic repository paths.
2. Replace placeholders and pin versions/images before first commit.
3. Run the narrowest relevant checks (lint/test/build or dry-run) before commit.

## After that, check related files

- Docs: `$CODEX_HOME/docs/virtualization/overview.md`
