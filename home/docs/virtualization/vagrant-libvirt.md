# Vagrant (libvirt)
Purpose: tell the Codex coding agent how to use `docs/virtualization/vagrant-libvirt.md` as a runtime-pack surface and when to stop browsing.
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
- You must treat provisioning scripts as privileged code inside the VM.
- You must keep base boxes pinned and verify provenance when possible.
- You must use `vagrant destroy` + `vagrant up` to validate reproducibility.
- You must document network mode (NAT/bridged/isolated) in the project README.

See also:
- `overview.md`
- `qemu-kvm-libvirt.md`
- `$CODEX_HOME/templates/virtualization/vagrant-libvirt-skeleton/`
- `$CODEX_HOME/index/domains/infra/virtualization.md`
