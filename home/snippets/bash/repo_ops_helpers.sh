# shellcheck shell=bash
# Repo automation safety helpers.
# Intended to be sourced into repo scripts.
#
# Notes:
# - Use with strict mode and explicit confirmations.
# - Avoid destructive defaults; support --dry-run/ASSUME_YES.
#
# References: docs/workflows/repo-ops.md, Use skill repo-ops.

require_cmd() {
  command -v "$1" >/dev/null 2>&1 || {
    printf 'ERROR: missing required command: %s\n' "$1" >&2
    exit 127
  }
}

require_git_repo() {
  require_cmd git
  git rev-parse --is-inside-work-tree >/dev/null 2>&1 || {
    printf 'ERROR: not inside a git repository\n' >&2
    exit 2
  }
}

git_repo_root() {
  require_git_repo
  git rev-parse --show-toplevel
}

git_is_clean() {
  require_git_repo
  [[ -z "$(git status --porcelain=v1 --untracked-files=normal)" ]]
}

require_clean_worktree() {
  git_is_clean && return 0
  printf 'ERROR: working tree is not clean\n' >&2
  git status --porcelain=v1 --untracked-files=normal >&2 || true
  exit 2
}

git_current_branch() {
  require_git_repo
  git rev-parse --abbrev-ref HEAD
}

git_current_commit() {
  require_git_repo
  git rev-parse --verify HEAD
}

confirm_or_die() {
  local prompt="${1:-Are you sure?}"

  # Non-interactive guardrails:
  # - Set ASSUME_YES=1 to auto-confirm in automation.
  # - Otherwise refuse to prompt when stdin isn't a TTY.
  if [[ "${ASSUME_YES:-}" == "1" || "${ASSUME_YES:-}" == "true" ]]; then
    return 0
  fi
  if [[ ! -t 0 && ! -r /dev/tty ]]; then
    printf 'ERROR: refusing to prompt in non-interactive mode; set ASSUME_YES=1 to proceed\n' >&2
    exit 1
  fi

  local ans=""
  if [[ -r /dev/tty ]]; then
    read -r -p "${prompt} [y/N] " ans </dev/tty
  else
    read -r -p "${prompt} [y/N] " ans
  fi

  case "${ans}" in
    y|Y|yes|YES) return 0 ;;
    *) printf 'Aborted.\n' >&2; exit 1 ;;
  esac
}
