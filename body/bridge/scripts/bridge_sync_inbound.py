#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from bridge_sync_common import (
    INBOX_MESSAGES,
    SyncError,
    add_common_args,
    ensure_repo,
    print_git_output,
    repo_rel,
    require_clean_paths,
    run_git,
    updatable_paths_from_name_status,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Safely sync only bridge inbound message files from Git into the repo copy."
    )
    add_common_args(parser)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Fetch and show the inbound path diff without updating the working tree.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        repo_root = ensure_repo(args.repo_root)
        require_clean_paths(repo_root, [INBOX_MESSAGES])

        print(f"Fetching {args.remote} {args.branch}...")
        fetch = run_git(repo_root, ["fetch", "--no-tags", args.remote, args.branch])
        print_git_output(fetch)

        path = repo_rel(INBOX_MESSAGES)
        diff = run_git(
            repo_root,
            ["diff", "--name-status", f"HEAD..FETCH_HEAD", "--", path],
        ).stdout.strip()

        if not diff:
            print(f"No inbound changes for {path}.")
            return 0

        print("Inbound changes detected:")
        print(diff)
        update_paths, skipped_delete = updatable_paths_from_name_status(diff)
        if skipped_delete:
            print("Remote deletes are intentionally skipped:")
            for skipped in skipped_delete:
                print(f"  {skipped}")
        if not update_paths:
            print("No inbound additions or modifications to apply.")
            return 0

        if args.dry_run:
            print("Dry run only; working tree was not updated.")
            return 0

        run_git(repo_root, ["restore", "--source", "FETCH_HEAD", "--worktree", "--", *update_paths])
        print(f"Updated inbound files only under {path}.")
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
