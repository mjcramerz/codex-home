#!/usr/bin/env python3
"""
Fetch all PR conversation comments + reviews + review threads (inline threads)
for the PR associated with the current git branch, by shelling out to:

  gh api graphql

Requires:
  - `gh auth login` already set up
  - current branch has an associated (open) PR

Usage:
  python fetch_comments.py > pr_comments.json
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from typing import Any

QUERY = """\
query(
  $owner: String!,
  $repo: String!,
  $number: Int!,
  $commentsCursor: String,
  $reviewsCursor: String,
  $threadsCursor: String
) {
  repository(owner: $owner, name: $repo) {
    pullRequest(number: $number) {
      number
      url
      title
      state

      # Top-level "Conversation" comments (issue comments on the PR)
      comments(first: 100, after: $commentsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          body
          createdAt
          updatedAt
          author { login }
        }
      }

      # Review submissions (Approve / Request changes / Comment), with body if present
      reviews(first: 100, after: $reviewsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          state
          body
          submittedAt
          author { login }
        }
      }

      # Inline review threads (grouped), includes resolved state
      reviewThreads(first: 100, after: $threadsCursor) {
        pageInfo { hasNextPage endCursor }
        nodes {
          id
          isResolved
          isOutdated
          path
          line
          diffSide
          startLine
          startDiffSide
          originalLine
          originalStartLine
          resolvedBy { login }
          comments(first: 100) {
            nodes {
              id
              body
              createdAt
              updatedAt
              author { login }
            }
          }
        }
      }
    }
  }
}
"""

DEFAULT_TIMEOUT_SEC = 45
MAX_TIMEOUT_SEC = 300
DEFAULT_MAX_PAGES = 30
MAX_MAX_PAGES = 200
MAX_TOTAL_ITEMS = 10000
MAX_COMMAND_ERROR_CHARS = 1200


def _deterministic_env() -> dict[str, str]:
    env = dict(os.environ)
    env.setdefault("LC_ALL", "C")
    env.setdefault("TZ", "UTC")
    return env


def _truncate(text: str, limit: int = MAX_COMMAND_ERROR_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[: limit - 3] + "..."


def _run(cmd: list[str], stdin: str | None = None, timeout_sec: int = DEFAULT_TIMEOUT_SEC) -> str:
    try:
        p = subprocess.run(
            cmd,
            input=stdin,
            capture_output=True,
            text=True,
            timeout=timeout_sec,
            env=_deterministic_env(),
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(
            f"Command timed out after {timeout_sec}s: {' '.join(cmd)}"
        ) from exc
    if p.returncode != 0:
        stderr = _truncate((p.stderr or "").strip())
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{stderr}")
    return p.stdout


def _run_json(
    cmd: list[str], stdin: str | None = None, timeout_sec: int = DEFAULT_TIMEOUT_SEC
) -> dict[str, Any]:
    out = _run(cmd, stdin=stdin, timeout_sec=timeout_sec)
    try:
        return json.loads(out)
    except json.JSONDecodeError as e:
        raise RuntimeError(
            f"Failed to parse JSON from command output: {e}\nRaw:\n{_truncate(out)}"
        ) from e


def _ensure_gh_authenticated(timeout_sec: int) -> None:
    try:
        _run(["gh", "auth", "status"], timeout_sec=timeout_sec)
    except RuntimeError:
        print("run `gh auth login` to authenticate the GitHub CLI", file=sys.stderr)
        raise RuntimeError(
            "gh auth status failed; run `gh auth login` to authenticate the GitHub CLI"
        ) from None


def gh_pr_view_json(fields: str, timeout_sec: int) -> dict[str, Any]:
    # fields is a comma-separated list like: "number,headRepositoryOwner,headRepository"
    return _run_json(["gh", "pr", "view", "--json", fields], timeout_sec=timeout_sec)


def get_current_pr_ref(timeout_sec: int) -> tuple[str, str, int]:
    """
    Resolve the PR for the current branch (whatever gh considers associated).
    Works for cross-repo PRs too, by reading head repository owner/name.
    """
    pr = gh_pr_view_json("number,headRepositoryOwner,headRepository", timeout_sec=timeout_sec)
    owner = (((pr.get("headRepositoryOwner") or {}).get("login")) or "").strip()
    repo = (((pr.get("headRepository") or {}).get("name")) or "").strip()
    number_raw = pr.get("number")
    if not owner or not repo:
        raise RuntimeError("Unable to resolve PR head repository owner/name from gh output")
    try:
        number = int(number_raw)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"Invalid PR number from gh output: {number_raw!r}") from exc
    if number <= 0:
        raise RuntimeError(f"Invalid PR number from gh output: {number}")
    return owner, repo, number


def gh_api_graphql(
    owner: str,
    repo: str,
    number: int,
    comments_cursor: str | None = None,
    reviews_cursor: str | None = None,
    threads_cursor: str | None = None,
    timeout_sec: int = DEFAULT_TIMEOUT_SEC,
) -> dict[str, Any]:
    """
    Call `gh api graphql` using -F variables, avoiding JSON blobs with nulls.
    Query is passed via stdin using query=@- to avoid shell newline/quoting issues.
    """
    cmd = [
        "gh",
        "api",
        "graphql",
        "-F",
        "query=@-",
        "-F",
        f"owner={owner}",
        "-F",
        f"repo={repo}",
        "-F",
        f"number={number}",
    ]
    if comments_cursor:
        cmd += ["-F", f"commentsCursor={comments_cursor}"]
    if reviews_cursor:
        cmd += ["-F", f"reviewsCursor={reviews_cursor}"]
    if threads_cursor:
        cmd += ["-F", f"threadsCursor={threads_cursor}"]

    return _run_json(cmd, stdin=QUERY, timeout_sec=timeout_sec)


def _assert_item_limits(
    conversation_comments: list[dict[str, Any]],
    reviews: list[dict[str, Any]],
    review_threads: list[dict[str, Any]],
) -> None:
    total_items = len(conversation_comments) + len(reviews) + len(review_threads)
    if total_items > MAX_TOTAL_ITEMS:
        raise RuntimeError(
            f"Exceeded max item cap ({MAX_TOTAL_ITEMS}); narrow PR scope or reduce page limit"
        )


def fetch_all(
    owner: str, repo: str, number: int, *, max_pages: int, timeout_sec: int
) -> dict[str, Any]:
    conversation_comments: list[dict[str, Any]] = []
    reviews: list[dict[str, Any]] = []
    review_threads: list[dict[str, Any]] = []

    comments_cursor: str | None = None
    reviews_cursor: str | None = None
    threads_cursor: str | None = None

    pr_meta: dict[str, Any] | None = None

    page_count = 0
    previous_cursor_state: tuple[str | None, str | None, str | None] | None = None

    while True:
        if page_count >= max_pages:
            raise RuntimeError(
                f"Reached page cap ({max_pages}) while fetching comments; increase --max-pages if needed"
            )
        page_count += 1

        payload = gh_api_graphql(
            owner=owner,
            repo=repo,
            number=number,
            comments_cursor=comments_cursor,
            reviews_cursor=reviews_cursor,
            threads_cursor=threads_cursor,
            timeout_sec=timeout_sec,
        )

        if "errors" in payload and payload["errors"]:
            raise RuntimeError(f"GitHub GraphQL errors:\n{json.dumps(payload['errors'], indent=2)}")

        pr = payload["data"]["repository"]["pullRequest"]
        if pr_meta is None:
            pr_meta = {
                "number": pr["number"],
                "url": pr["url"],
                "title": pr["title"],
                "state": pr["state"],
                "owner": owner,
                "repo": repo,
            }

        c = pr["comments"]
        r = pr["reviews"]
        t = pr["reviewThreads"]

        conversation_comments.extend(c.get("nodes") or [])
        reviews.extend(r.get("nodes") or [])
        review_threads.extend(t.get("nodes") or [])
        _assert_item_limits(conversation_comments, reviews, review_threads)

        comments_cursor = c["pageInfo"]["endCursor"] if c["pageInfo"]["hasNextPage"] else None
        reviews_cursor = r["pageInfo"]["endCursor"] if r["pageInfo"]["hasNextPage"] else None
        threads_cursor = t["pageInfo"]["endCursor"] if t["pageInfo"]["hasNextPage"] else None

        current_cursor_state = (comments_cursor, reviews_cursor, threads_cursor)
        if previous_cursor_state is not None and current_cursor_state == previous_cursor_state:
            raise RuntimeError("GraphQL pagination cursor stalled; aborting to avoid infinite loop")
        previous_cursor_state = current_cursor_state

        if not (comments_cursor or reviews_cursor or threads_cursor):
            break

    assert pr_meta is not None
    return {
        "pull_request": pr_meta,
        "conversation_comments": conversation_comments,
        "reviews": reviews,
        "review_threads": review_threads,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch GitHub PR comments/reviews/threads")
    parser.add_argument(
        "--max-pages",
        type=int,
        default=DEFAULT_MAX_PAGES,
        help=f"Maximum GraphQL pages to fetch (default: {DEFAULT_MAX_PAGES})",
    )
    parser.add_argument(
        "--timeout-sec",
        type=int,
        default=DEFAULT_TIMEOUT_SEC,
        help=f"Per-command timeout in seconds (default: {DEFAULT_TIMEOUT_SEC})",
    )
    parser.add_argument(
        "--compact",
        action="store_true",
        help="Emit compact JSON instead of pretty-printed output",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_pages < 1 or args.max_pages > MAX_MAX_PAGES:
        print(
            f"ERROR: --max-pages must be between 1 and {MAX_MAX_PAGES}",
            file=sys.stderr,
        )
        return 2
    if args.timeout_sec < 1 or args.timeout_sec > MAX_TIMEOUT_SEC:
        print(
            f"ERROR: --timeout-sec must be between 1 and {MAX_TIMEOUT_SEC}",
            file=sys.stderr,
        )
        return 2

    try:
        _ensure_gh_authenticated(timeout_sec=args.timeout_sec)
        owner, repo, number = get_current_pr_ref(timeout_sec=args.timeout_sec)
        result = fetch_all(
            owner,
            repo,
            number,
            max_pages=args.max_pages,
            timeout_sec=args.timeout_sec,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if args.compact:
        print(json.dumps(result, separators=(",", ":")))
    else:
        print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
