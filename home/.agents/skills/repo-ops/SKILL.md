---
name: repo-ops
description: Use this skill to plan and implement safe repository operations, git
  automation, release workflows, and CI helper tooling with deterministic contracts.
  Use when the user asks for repo automation, release hygiene, branch promotion, or
  tooling that touches git state.
metadata:
  version: '1.0'
  short-description: Drive safe repo automation, branch promotion, release flows,
    and git hygiene
  tags:
  - git
  - repo
  - automation
  - release
  - ci
  - workflow
interface:
  display-name: REPO-Ops
  short-description: Drive safe repo automation, branch promotion, release flows,
    and git hygiene
  icon-small: assets/icon-32.png
  icon-large: assets/icon-128.png
  brand-color: '#327FCC'
  default-prompt: Act as the "REPO-Ops" specialist for "Drive safe repo automation,
    branch promotion, release flows, and git hygiene". Deliver focused, deterministic
    results with minimal, reviewable changes and explicit assumptions. Validate untrusted
    inputs and bounded I/O, run the narrowest relevant checks, and report concrete
    actions, evidence, and residual risks.
---

# Repo Ops

## Workflow

1. Inspect status, branch, remotes and the intended comparison base without changing user-owned work. Treat remote URLs as sensitive if they contain credentials.

2. Keep revisions and pathspecs separate using -- where supported. Quote arguments and avoid constructing shell fragments from branch names or filenames.

3. Do not reset, clean, force-push, rewrite history, create commits or publish tags unless the task authorizes the action. Preserve unrelated staged and unstaged changes.

4. Read CI and release scripts before invocation; protect signing and registry credentials. Verify the exact destination branch, tag and account before publication.

5. Check the diff for unintended paths, whitespace and generated artifacts. Report the actual commands, references and checks, not an assumed clean or pushed state.

## Boundaries and completion

Follow the active instruction hierarchy, preserve unrelated work and use only tools actually available in this session. Read the selected reference only when it resolves a concrete question. Keep secrets out of prompts, logs and artifacts. Finish with the requested result, changed paths, checks actually run and unresolved risks; do not claim live success from static evidence.

## References

- `$CODEX_HOME/AGENTS.md`
- `$CODEX_HOME/docs/workflows/repo-ops.md`
- `$CODEX_HOME/docs/workflows/release.md`
- `$CODEX_HOME/index/core/repo-ops.md`
- `$CODEX_HOME/docs/style/bash.md`
- `references/latest-sources.md`
- `rules/rules.md`
- `rules/framework.md`
