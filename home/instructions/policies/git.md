# Git and change ownership
Inspect status and diff before edits. Preserve unrelated changes and do not reset, clean, overwrite, rebase, force-push, commit, tag or publish without the user's authorization for that operation. Never infer authorization from a script name or historical plan.

The retained repo.sh has repository-specific GitOps conventions. The branch `mcr/main` is not a universal requirement for other repositories. Respect the active repository's actual branch policy, upstream and working-tree state. Review staged and unstaged changes separately before preparing a final summary.
