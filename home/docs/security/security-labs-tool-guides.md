# Security tool guides
Purpose: tell the Codex coding agent how to use `docs/security/security-labs-tool-guides.md` as a runtime-pack surface and when to stop browsing.
Defensive and scoped-simulation guide set for high-risk security tools.


## Navigation
<!-- BEGIN:nav -->
- Parent: `$CODEX_HOME/docs/security/overview.md`
- Pack index: `$CODEX_HOME/INDEX.md`
- Routing guide: `$CODEX_HOME/index/OVERVIEW.md`
<!-- END:nav -->


## Global guardrails
- Execute only within a documented scope manifest with a named owner and environment class.
- You must use lab/staging environments for high-risk simulations.
- You must keep deterministic command logs, hashes, and rollback notes.
- Exclude weaponized or uncontrolled exploitation procedures.

## Cobalt Strike (defense and detection)
### Objective
Detect beacon-like behavior, validate redirector controls, and harden telemetry coverage.

### Operator workflow
1) Validate ingress boundaries and proxy policy.
2) Capture callback cadence/jitter patterns.
3) Tune detections for profile drift and low-and-slow traffic.
4) Validate SOC containment workflow.

### Defensive command examples
```bash
LC_ALL=C rg -n --color=never "POST|GET" /var/log/nginx/access.log | head -n 200
tshark -r capture.pcapng -Y "tls && tcp.dstport==443" -T fields -e frame.time_epoch -e ip.dst | head -n 200
```

## Wifite / wireless attack-surface defense
### Objective
Assess wireless exposure and validate monitoring/containment in the documented RF boundary.

### Defensive command examples
```bash
nmcli dev wifi list
iw dev
```

## Wireshark / tshark
### Objective
Collect packet evidence for threat hunting and control validation.

### Defensive command examples
```bash
timeout 300 tshark -i eth0 -w incident-capture.pcapng
tshark -r incident-capture.pcapng -Y "dns.flags.response==0" -T fields -e ip.src -e dns.qry.name | head -n 200
```

## Nmap (scoped inventory)
### Objective
Enumerate exposed services in the documented ranges and track remediation progress.

### Defensive command examples
```bash
nmap -sn 10.10.20.0/24
nmap -Pn -sV --top-ports 200 --host-timeout 90s 10.10.20.15
```

## Reverse-shell detection and containment
### Objective
Identify suspicious egress command channels and isolate affected hosts.

### Defensive command examples
```bash
ss -tpan
lsof -nP -iTCP -sTCP:ESTABLISHED
```

## SharpKatz (Mimikatz-port behavior) defensive coverage
### Objective
Validate credential-access detections and hardening around LSASS/credential stores.

### Defensive command examples
```powershell
Get-WinEvent -LogName "Microsoft-Windows-Sysmon/Operational" -MaxEvents 200 |
  Where-Object { $_.Message -match "lsass.exe" } |
  Select-Object TimeCreated, Id, Message
```

## NetHunter Pixel 9a lab operations
### Objective
Build reproducible NetHunter artifacts and execute rooted-device validation with rollback.

### Workspace setup (no hardcoded mirror paths)
```bash
export NH_KERNEL_BUILDER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-kernel-builder.git"
export NH_INSTALLER_REPO_URL="https://gitlab.com/kalilinux/nethunter/build-scripts/kali-nethunter-installer.git"

git clone "$NH_KERNEL_BUILDER_REPO_URL"
git clone "$NH_INSTALLER_REPO_URL"
```

### Controlled sequence
1) Validate scope via `nethunter-pixel9a/scripts/nethunter_scope_guard.py`.
2) Run preflight evidence collection:
   `nethunter_pixel9a_preflight.sh --scope-file <scope.json> --device-id <id> --out-dir <dir>`.
3) Verify toolchain compatibility from the current Platform-Tools release notes.
4) Capture fingerprint and align Google kernel baseline.
5) Build artifacts with NetHunter builder + installer and hash outputs.
6) Run root/flash preview first:
   `nethunter_pixel9a_root_sequence.sh ... --slot a`.
7) Before apply, verify mode and slot (`fastboot getvar is-userspace`, `fastboot getvar current-slot`).
8) Apply only in a documented change window using `--apply --confirm I_UNDERSTAND_DATA_RISK`.
9) Execute rollback drill using stock boot image.

### Deterministic helper commands
```bash
# Validate builder script syntax
bash -n kali-nethunter-kernel-builder/build.sh

# List installer options
python3 kali-nethunter-installer/build.py -h

# Record commit IDs
git -C kali-nethunter-kernel-builder rev-parse HEAD
git -C kali-nethunter-installer rev-parse HEAD

# Record platform-tools and mode/slot state
adb version
fastboot --version
fastboot getvar is-userspace
fastboot getvar current-slot
```

## Rooting Google phones (documented device workflow)
### Objective
Control risk while preparing mobile research devices for sanctioned testing.

### Workflow controls
1) Use dedicated lab devices, never employee production phones.
2) Capture inventory, bootloader state, and owner record before changes.
3) Preserve rollback images and factory restore steps before unlock.
4) Isolate rooted devices from production identities and networks.

## Source set
- Kali NetHunter build docs: https://www.kali.org/docs/nethunter/building-nethunter/
- NetHunter kernel-builder porting docs: https://www.kali.org/docs/nethunter/porting-nethunter-kernel-builder/
- NetHunter manual porting docs: https://www.kali.org/docs/nethunter/porting-nethunter/
- Android bootloader locking/unlocking: https://source.android.com/docs/core/architecture/bootloader/locking_unlocking
- Android fastbootd architecture: https://source.android.com/docs/core/architecture/bootloader/fastbootd
- Android platform-tools release notes: https://developer.android.com/tools/releases/platform-tools
