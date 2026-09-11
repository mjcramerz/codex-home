---
name: desktop-entries
description: Create and validate safe .desktop launchers with correct Exec fields, metadata, and desktop integration. Use when the user asks to add or repair Linux desktop entries.
metadata:
  version: '1.0'
  short-description: Create safe and consistent .desktop launchers
  tags:
  - desktop
  - launcher
  - linux
interface:
  display-name: DESKTOP-.desktop Entries
  short-description: Create safe and consistent .desktop launchers
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#CC4232'
  default-prompt: Act as the "DESKTOP-.desktop Entries" specialist for "Create safe and consistent .desktop launchers". Deliver focused, deterministic results with minimal, reviewable changes and explicit assumptions. Validate untrusted inputs and bounded I/O, run the narrowest relevant checks, and report concrete actions, evidence, and residual risks.
---

# SKILL

## Execute the scoped task

1. Confirm system versus user manager, service identity, working directories and runtime paths. A locked service account does not imply a running user manager.

2. Use explicit ExecStart argument semantics rather than shell assumptions. Apply sandboxing compatible with required access; keep credentials in the intended credential mechanism, not unit text or command lines.

3. Define bounded startup, stop and restart behavior. Use RuntimeDirectory, StateDirectory and appropriate ownership where they match the service lifecycle.

4. Inspect unit dependencies, socket activation and restart implications before daemon-reload, enable, restart or stop. Treat each as a live host operation requiring scope and authority.

5. Check unit syntax with available tools, then inspect actual unit state and journal evidence only in the authorized environment. Never equate a parsed unit with a running service.

## Task-specific details and resources

## Use this skill when

- adding application launchers
- wiring scripts into desktop menus

## Workflow

1. Define Exec/Name/Icon
2. Validate with `desktop-file-validate`
3. Install to user/system path

## Agent orchestration

- Confirm that the request fits this skill and state boundaries if other skills are needed.
- For multi-step work, keep a concise plan, execute in small reversible steps, and surface assumptions early.
- Delegate only independent discovery tasks, then reconcile findings before making edits.

## Validation and testing

- Validate critical inputs and bound external I/O (size, retries, and timeouts) before applying changes.
- Run the narrowest relevant checks that prove behavior (tests, lint, or build as applicable).
- Include risk-based negative or edge-case coverage for security-sensitive, parsing, or automation changes.
- Report verification commands, outcomes, and any follow-up checks that remain.

## Outputs

- Actionable steps or artifacts aligned to the skill.
- References to relevant files, commands, or templates.

## References

- `$CODEX_HOME/index/domains/desktop/desktop-entries.md`
- `$CODEX_HOME/docs/desktop/desktop-entries.md`
- `$CODEX_HOME/docs/workflows/desktop-entries.md`
- `$CODEX_HOME/templates/desktop/desktop-entry/`
- `$CODEX_HOME/snippets/desktop/desktop-entry.desktop`
