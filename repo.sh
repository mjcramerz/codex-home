#!/usr/bin/env bash
set -Eeuo pipefail

export LC_ALL=C
export TZ=UTC

readonly REMOTE_NAME="origin"
readonly REMOTE_URL="git@gitlab.com:computes/misc/codex-home.git"
readonly MAIN_BRANCH="mcr/main"
readonly REMOTE_MAIN="${REMOTE_NAME}/${MAIN_BRANCH}"
readonly REMOTE_FETCH_REFSPEC='+refs/heads/*:refs/remotes/origin/*'
readonly GITOPS_BIN="${HOME:?HOME must be set}/.local/bin/gitops"
# Keep this repository-local alias aligned with gitops/config/gitconfig.aliases.
# $HOME and the positional parameters expand later, when Git runs the alias.
# shellcheck disable=SC2016
readonly MCR_BRANCH_PUSH_ALIAS='!f() { cmd="$HOME/.local/bin/gitops"; [ -x "$cmd" ] || { echo "error: missing gitops binary: $cmd" >&2; exit 1; }; "$cmd" mcr-branch-push "$@"; }; f'

dry_run=false

usage() {
  cat <<'USAGE'
usage: ./repo.sh [--dry-run]

Prepare this clone for normal development after the managed installer leaves
it at a pinned detached HEAD. The script:

  1. configures origin as the managed GitLab SSH repository,
  2. fetches all branches and reconciles the pinned commit into mcr/main,
  3. sets mcr/main to track origin/mcr/main, and
  4. configures the repository-local `git mcr-branch-push` GitOps alias.

The script never pushes. Use --dry-run to validate local prerequisites and
print the intended mutations without changing the repository or using network.
USAGE
}

die() {
  printf 'error: %s\n' "$*" >&2
  exit 1
}

log() {
  printf '%s\n' "$*"
}

restore_config_values() {
  local key="$1"
  shift

  git config --local --unset-all "$key" >/dev/null 2>&1 || true
  while [ "$#" -gt 0 ]; do
    git config --local --add "$key" "$1"
    shift
  done
}

incorporate_ref() {
  local ref="$1"
  local description="$2"

  if git merge-base --is-ancestor "$ref" HEAD; then
    log "already contains ${description}: $(git rev-parse --short "$ref")"
    return
  fi

  if git merge-base --is-ancestor HEAD "$ref"; then
    git merge --ff-only "$ref" >/dev/null
    log "fast-forwarded to ${description}: $(git rev-parse --short "$ref")"
    return
  fi

  if ! git merge --no-edit -m "chore: reconcile ${description} into ${MAIN_BRANCH}" "$ref" >/dev/null; then
    git merge --abort >/dev/null 2>&1 || true
    die "${description} conflicts with the managed ${MAIN_BRANCH}; resolve it on a temporary branch"
  fi
  log "merged ${description}: $(git rev-parse --short "$ref")"
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --dry-run)
      dry_run=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      usage >&2
      die "unknown option: $1"
      ;;
  esac
done

SCRIPT_DIR="$(CDPATH='' cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd -P)" ||
  die "failed to resolve the repository script directory"
readonly SCRIPT_DIR
REPO_ROOT="$(git -C "$SCRIPT_DIR" rev-parse --show-toplevel 2>/dev/null)" ||
  die "repo.sh must be run from inside its Git repository"
readonly REPO_ROOT
[ "$REPO_ROOT" = "$SCRIPT_DIR" ] ||
  die "repo.sh must remain at the repository root: ${REPO_ROOT}"
cd -- "$REPO_ROOT"

[ "$(git rev-parse --is-inside-work-tree)" = true ] ||
  die "not inside a Git worktree"
[ -z "$(git status --porcelain=v1 --untracked-files=all)" ] ||
  die "the worktree must be clean before branch reconciliation"

START_HEAD="$(git rev-parse --verify HEAD)" || die "repository HEAD is invalid"
readonly START_HEAD
START_BRANCH="$(git symbolic-ref --quiet --short HEAD 2>/dev/null || true)"
readonly START_BRANCH
case "$START_BRANCH" in
  ""|"$MAIN_BRANCH") ;;
  *) die "expected detached HEAD or ${MAIN_BRANCH}, found ${START_BRANCH}" ;;
esac

[ -x "$GITOPS_BIN" ] ||
  die "missing GitOps executable: ${GITOPS_BIN}; install the neighboring gitops repository first"

mapfile -t original_remote_urls < <(git config --local --get-all "remote.${REMOTE_NAME}.url" || true)
mapfile -t original_remote_fetches < <(git config --local --get-all "remote.${REMOTE_NAME}.fetch" || true)
mapfile -t original_remote_pushurls < <(git config --local --get-all "remote.${REMOTE_NAME}.pushurl" || true)
mapfile -t original_alias_values < <(git config --local --get-all alias.mcr-branch-push || true)
mapfile -t original_branch_remotes < <(git config --local --get-all "branch.${MAIN_BRANCH}.remote" || true)
mapfile -t original_branch_merges < <(git config --local --get-all "branch.${MAIN_BRANCH}.merge" || true)

[ "${#original_remote_urls[@]}" -le 1 ] ||
  die "${REMOTE_NAME} has multiple URLs; refusing to choose one implicitly"

main_existed=false
original_main_head=""
if git show-ref --verify --quiet "refs/heads/${MAIN_BRANCH}"; then
  main_existed=true
  original_main_head="$(git rev-parse "refs/heads/${MAIN_BRANCH}")"
fi

remote_main_existed=false
original_remote_main_head=""
if git show-ref --verify --quiet "refs/remotes/${REMOTE_MAIN}"; then
  remote_main_existed=true
  original_remote_main_head="$(git rev-parse "refs/remotes/${REMOTE_MAIN}")"
fi

if [ "$dry_run" = true ]; then
  log "repository: ${REPO_ROOT}"
  log "current HEAD: ${START_HEAD} (${START_BRANCH:-detached})"
  log "would configure ${REMOTE_NAME}.url=${REMOTE_URL}"
  log "would configure ${REMOTE_NAME}.fetch=${REMOTE_FETCH_REFSPEC}"
  log "would fetch all branches from ${REMOTE_NAME} and unshallow when required"
  log "would reconcile ${REMOTE_MAIN}, existing ${MAIN_BRANCH}, and pinned HEAD into ${MAIN_BRANCH}"
  log "would set ${MAIN_BRANCH} upstream to ${REMOTE_MAIN}"
  log "would configure repository-local alias.mcr-branch-push via ${GITOPS_BIN}"
  log "would not push any refs"
  exit 0
fi

origin_existed=false
if git remote get-url "$REMOTE_NAME" >/dev/null 2>&1; then
  origin_existed=true
fi

rollback() {
  local status=$?
  trap - EXIT INT TERM
  set +e

  git merge --abort >/dev/null 2>&1 || true
  git switch --quiet --detach "$START_HEAD" >/dev/null 2>&1 || true

  if [ "$main_existed" = true ]; then
    git update-ref "refs/heads/${MAIN_BRANCH}" "$original_main_head" >/dev/null 2>&1 || true
  else
    git update-ref -d "refs/heads/${MAIN_BRANCH}" >/dev/null 2>&1 || true
  fi
  if [ "$remote_main_existed" = true ]; then
    git update-ref "refs/remotes/${REMOTE_MAIN}" "$original_remote_main_head" >/dev/null 2>&1 || true
  else
    git update-ref -d "refs/remotes/${REMOTE_MAIN}" >/dev/null 2>&1 || true
  fi

  if [ "$origin_existed" = true ]; then
    restore_config_values "remote.${REMOTE_NAME}.url" "${original_remote_urls[@]}"
    restore_config_values "remote.${REMOTE_NAME}.fetch" "${original_remote_fetches[@]}"
    restore_config_values "remote.${REMOTE_NAME}.pushurl" "${original_remote_pushurls[@]}"
  else
    git remote remove "$REMOTE_NAME" >/dev/null 2>&1 || true
  fi
  restore_config_values alias.mcr-branch-push "${original_alias_values[@]}"
  restore_config_values "branch.${MAIN_BRANCH}.remote" "${original_branch_remotes[@]}"
  restore_config_values "branch.${MAIN_BRANCH}.merge" "${original_branch_merges[@]}"
  if [ -n "$START_BRANCH" ]; then
    git switch --quiet "$START_BRANCH" >/dev/null 2>&1 || true
  fi

  printf 'error: repository bootstrap failed; original branch and configuration were restored\n' >&2
  exit "$status"
}
trap rollback EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

if [ "$origin_existed" = true ]; then
  git remote set-url "$REMOTE_NAME" "$REMOTE_URL"
else
  git remote add "$REMOTE_NAME" "$REMOTE_URL"
fi
git config --local --replace-all "remote.${REMOTE_NAME}.fetch" "$REMOTE_FETCH_REFSPEC"
git config --local --unset-all "remote.${REMOTE_NAME}.pushurl" >/dev/null 2>&1 || true

if [ "$(git rev-parse --is-shallow-repository)" = true ]; then
  git fetch --no-tags --unshallow "$REMOTE_NAME"
else
  git fetch --no-tags "$REMOTE_NAME"
fi
git show-ref --verify --quiet "refs/remotes/${REMOTE_MAIN}" ||
  die "${REMOTE_NAME} does not advertise ${MAIN_BRANCH}"
git remote set-head "$REMOTE_NAME" "$MAIN_BRANCH"

git switch --quiet --detach "$REMOTE_MAIN"
if [ "$main_existed" = true ]; then
  incorporate_ref "$original_main_head" "existing local ${MAIN_BRANCH}"
fi
incorporate_ref "$START_HEAD" "pinned detached HEAD"
INTEGRATED_HEAD="$(git rev-parse HEAD)" || die "failed to resolve the reconciled HEAD"
readonly INTEGRATED_HEAD

git config --local --replace-all alias.mcr-branch-push "$MCR_BRANCH_PUSH_ALIAS"
if [ "$main_existed" = true ]; then
  git update-ref "refs/heads/${MAIN_BRANCH}" "$INTEGRATED_HEAD" "$original_main_head"
else
  git update-ref "refs/heads/${MAIN_BRANCH}" "$INTEGRATED_HEAD"
fi
git switch --quiet "$MAIN_BRANCH"
git branch --set-upstream-to="$REMOTE_MAIN" "$MAIN_BRANCH" >/dev/null

[ "$(git config --local --get "remote.${REMOTE_NAME}.url")" = "$REMOTE_URL" ] ||
  die "failed to persist the managed SSH remote"
[ "$(git config --local --get "remote.${REMOTE_NAME}.fetch")" = "$REMOTE_FETCH_REFSPEC" ] ||
  die "failed to persist the all-branches fetch refspec"
[ "$(git rev-parse --abbrev-ref --symbolic-full-name '@{upstream}')" = "$REMOTE_MAIN" ] ||
  die "failed to configure ${MAIN_BRANCH} upstream"
git merge-base --is-ancestor "$START_HEAD" "$MAIN_BRANCH" ||
  die "${MAIN_BRANCH} does not contain the original pinned HEAD"
git merge-base --is-ancestor "$REMOTE_MAIN" "$MAIN_BRANCH" ||
  die "${MAIN_BRANCH} does not contain ${REMOTE_MAIN}"
[ "$(git config --local --get alias.mcr-branch-push)" = "$MCR_BRANCH_PUSH_ALIAS" ] ||
  die "failed to configure git mcr-branch-push"

trap - EXIT INT TERM

log "repository ready"
log "  branch:   ${MAIN_BRANCH}"
log "  upstream: ${REMOTE_MAIN}"
log "  remote:   ${REMOTE_URL}"
log "  HEAD:     ${INTEGRATED_HEAD}"
log "  push:     run 'git mcr-branch-push' when you are ready"
