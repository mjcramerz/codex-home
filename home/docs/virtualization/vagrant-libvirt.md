# Vagrant (libvirt)

Use this guide when the task concerns vagrant (libvirt). Apply the relevant steps to the current repository, preserve unrelated work, and stop when the requested outcome and checks are complete.

Vagrant can manage reproducible VM environments. On Linux, the libvirt provider is a common choice.

## Navigation

<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/virtualization/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->

## Typical setup

- Install Vagrant
- Install the libvirt provider plugin (varies by distro and Vagrant version)
- Ensure libvirt is configured for your user

## Network access templates

Vagrant VMs can be configured with:
- NAT (default): outbound internet access
- Private network: isolated L2/L3 segment for dev
- Bridged network: VM on LAN (higher exposure)

When building hermetic environments, prefer NAT without port forwards, or fully isolated networks.

## Operational guidance

- Treat provisioning scripts as privileged code inside the VM.
- Keep base boxes pinned and verify provenance when possible.
- Use `vagrant destroy` + `vagrant up` to validate reproducibility.
- Document network mode (NAT/bridged/isolated) in the project README.

See also:
- `overview.md`
- `qemu-kvm-libvirt.md`
- `$CODEX_HOME/templates/virtualization/vagrant-libvirt-skeleton/`
- `$CODEX_HOME/index/domains/infra/virtualization.md`
