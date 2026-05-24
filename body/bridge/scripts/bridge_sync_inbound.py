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
    porcelain_status,
    repo_rel,
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


def remote_file_text(repo_root, path: str) -> str | None:
    result = run_git(repo_root, ["show", f"FETCH_HEAD:{path}"], check=False)
    if result.returncode != 0:
        return None
    return result.stdout


def inbound_updates_match_local_files(repo_root, update_paths: list[str]) -> bool:
    for path in update_paths:
        local_path = repo_root / path
        if not local_path.exists() or not local_path.is_file():
            return False
        remote_text = remote_file_text(repo_root, path)
        if remote_text is None:
            return False
        local_text = local_path.read_text(encoding="utf-8", errors="replace")
        if local_text != remote_text:
            return False
    return True


def main() -> int:
    args = parse_args()
    try:
        repo_root = ensure_repo(args.repo_root)
        local_status = porcelain_status(repo_root, [INBOX_MESSAGES])

        print(f"Fetching {args.remote} {args.branch}...")
        fetch = run_git(repo_root, ["fetch", "--no-tags", args.remote, args.branch])
        print_git_output(fetch)

        path = repo_rel(INBOX_MESSAGES)
        diff = run_git(
            repo_root,
            ["diff", "--name-status", f"HEAD..FETCH_HEAD", "--", path],
        ).stdout.strip()

        if not diff:
            if local_status:
                print("Local inbound files are already present and will be left untouched:")
                print(local_status)
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

        if local_status and not inbound_updates_match_local_files(repo_root, update_paths):
            raise SyncError(
                f"Refusing to sync because local inbound paths are dirty while remote inbound changes exist ({path}):\n"
                f"{local_status}"
            )
        if local_status:
            print("Local inbound files match remote inbound updates; accepting them as already present.")

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
