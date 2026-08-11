# USB lab policy baseline
Purpose: tell the Codex coding agent how to use `templates/system/mobile-wireless-defense-kit/usb-lab-policy.md` as a runtime-pack surface and when to stop browsing.

## Purpose
Reduce risk from USB emulation tools (BadUSB/Rubber Ducky class) during scoped lab exercises.

## Controls
- Allowlist documented USB VID/PID where feasible.
- Enforce endpoint alerts for rapid HID keystroke bursts.
- Block unknown USB mass-storage in sensitive zones.
- You must require supervised physical access during exercise windows.

## Response
- Isolate endpoint on suspected USB-injection behavior.
- Preserve USB event and endpoint telemetry artifacts.
- Execute containment + credential hygiene playbook.
