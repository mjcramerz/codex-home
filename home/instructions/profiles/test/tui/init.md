Generate a file named `AGENTS.override.md` that serves as a local repository-specific override guide for this repository.
Before writing, check whether `AGENTS.override.md` already exists in the current working directory. If it does, do not overwrite or modify it.
The document should extend the existing repository instructions with concrete local rules, not restate generic boilerplate.
Write a compact, operational guide that another coding agent can follow immediately with minimal interpretation.

Document Requirements

- Title the document `Repository Override Guidelines`.
- Use Markdown headings (`#`, `##`, etc.) for structure.
- Target roughly 250-500 words.
- Keep wording direct, repo-specific, and action-oriented.
- Include short examples for commands, paths, branch names, and validation steps when helpful.
- Prefer imperative language and concrete constraints over narrative explanation.

Required Coverage

Project Structure & Ownership

- Summarize the key directories that matter locally: source, tests, packaging, release automation, generated assets, and runtime mirrors.
- Call out any source-of-truth vs mirrored-file relationships.
- If both source and runtime-mirror files exist, require the override guide to name the authoritative source path and the mirrored paths explicitly.

Build, Test, and Validation Commands

- List the exact local commands used most often for this repository.
- Include narrow validation first, then broader validation.
- Mention any commands that must be run after config, catalog, packaging, or installer changes.

Editing & Safety Rules

- State any branch restrictions, release-path restrictions, generated-file handling, and protected areas.
- If the repository is a fork or mirror topology, explicitly describe the allowed working branch and any read-only branches.
- Include any repo-local constraints for secrets, backups, packaging, release scripts, or installer paths.

Testing Expectations

- Identify the test framework and test naming patterns.
- Explain what must be validated before finalizing changes.

Change Management

- Describe commit and patch expectations only if they are visible from repo history or explicit repo docs.
- If specific paths are the only safe mutation surface in fork mode, list them explicitly.

Important Repository Rule

- If `gitlab/*` or `github/*` branches exist, treat the repository as a fork or mirror topology.
- In that case, work must always be done on `mcr/main`.
- In that mode, direct codebase edits are disallowed by default except for:
  - `.gitlab-ci.yml`
  - `Makefile`
  - `scripts/release/**`
  - `debian/**`
  - `.bazelversion`
  - `.bazelignore`
  - `.bazelrc`
  - `bazel/**`

The output should feel like a high-signal local override file for experienced maintainers and coding agents, not a generic contributor template.
