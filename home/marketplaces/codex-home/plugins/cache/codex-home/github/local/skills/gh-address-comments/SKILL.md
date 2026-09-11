---
name: gh-address-comments
description: Use this skill for help address review/issue comments on the open GitHub PR for the current branch using gh CLI; verify gh auth first and prompt the user to authenticate if not logged in.
metadata:
  short-description: Address comments in a GitHub PR review
---

# PR Comment Handler

## Execute the scoped task

1. Inspect status, branch, remotes and the intended comparison base without changing user-owned work. Treat remote URLs as sensitive if they contain credentials.

2. Keep revisions and pathspecs separate using -- where supported. Quote arguments and avoid constructing shell fragments from branch names or filenames.

3. Do not reset, clean, force-push, rewrite history, create commits or publish tags unless the task authorizes the action. Preserve unrelated staged and unstaged changes.

4. Read CI and release scripts before invocation; protect signing and registry credentials. Verify the exact destination branch, tag and account before publication.

5. Check the diff for unintended paths, whitespace and generated artifacts. Report the actual commands, references and checks, not an assumed clean or pushed state.

## Task-specific details and resources

Guide to find the open PR for the current branch and address its comments with gh CLI. Run all `gh` commands with elevated network access.

Prereq: ensure `gh` is authenticated (for example, run `gh auth login` once), then run `gh auth status` with escalated permissions (include workflow/repo scopes) so `gh` commands succeed. If sandboxing blocks `gh auth status`, rerun it with `sandbox_permissions=require_escalated`.

## 1) Inspect comments needing attention

- Run scripts/fetch_comments.py which will print out all the comments and review threads on the PR

## 2) Ask the user for clarification

- Number all the review threads and comments and provide a short summary of what would be required to apply a fix for it
- Ask the user which numbered comments should be addressed

## 3) If user chooses comments

- Apply fixes for the selected comments

Notes:
- If gh hits auth/rate issues mid-run, prompt the user to re-authenticate with `gh auth login`, then retry.
