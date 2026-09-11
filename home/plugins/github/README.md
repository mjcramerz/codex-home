# GitHub task routing

Read this plugin only when its listed skills match the current task. Discover the actual client tools, account access and permission requirements before invoking anything. Treat this directory as bundled source, not proof of an installed or authenticated integration.

## Select one entrypoint

| Skill | Apply it to |
| --- | --- |
| [ci-github-actions](skills/ci-github-actions/SKILL.md) | Design or update GitHub Actions pipelines with pinned tooling, least-privilege permissions, caching strategy, and reproducible CI gates |
| [ci-github-actions-fix](skills/ci-github-actions-fix/SKILL.md) | Debug failing GitHub Actions checks by inspecting PR statuses and logs with gh, then propose and implement fixes after approval |
| [gh-address-comments](skills/gh-address-comments/SKILL.md) | Use this skill for help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in. |
| [gh-fix-ci](skills/gh-fix-ci/SKILL.md) | Use when a user asks to debug or fix failing GitHub PR checks that run in GitHub Actions; use `gh` to inspect checks and logs, summarize failure context, draft a fix plan, and implement only after explicit approval |
| [github-pr-comments](skills/github-pr-comments/SKILL.md) | Work through open GitHub PR review comments using gh CLI, map each comment to code changes, and post or prepare responses |
| [yeet](skills/yeet/SKILL.md) | Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`). |

## Preserve the integration boundary

Read only the references required by the selected skill. Inspect bundled scripts before execution; retain their argument and output contracts. Keep credentials and private payloads out of examples, logs and ambient hook context.

Do not install, enable, trust, publish or update a remote integration merely because you edit these files. Keep canonical and authorized bundled mirrors coherent, preserve existing resource paths and license notices, and report the checks you actually performed. Local packaging does not assert vendor endorsement.
