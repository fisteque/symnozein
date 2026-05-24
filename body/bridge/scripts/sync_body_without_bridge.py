#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from bridge_sync_common import (
    BRIDGE_REPO_ROOT,
    SyncError,
    add_common_args,
    ensure_repo,
    print_git_output,
    require_clean_path_names,
    run_git,
    updatable_paths_from_name_status,
)


BODY_ROOT = Path("body")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch and restore body/ content except body/bridge.")
    add_common_args(parser)
    parser.add_argument("--dry-run", action="store_true", help="Show body changes without updating the working tree.")
    return parser.parse_args()


def is_body_non_bridge(path: str) -> bool:
    return path.startswith("body/") and not (path == BRIDGE_REPO_ROOT.as_posix() or path.startswith(f"{BRIDGE_REPO_ROOT.as_posix()}/"))


def main() -> int:
    args = parse_args()
    try:
        repo_root = ensure_repo(args.repo_root)
        fetch = run_git(repo_root, ["fetch", "--no-tags", args.remote, args.branch])
        print_git_output(fetch)
        output = run_git(repo_root, ["diff", "--name-status", "HEAD..FETCH_HEAD", "--", BODY_ROOT.as_posix()]).stdout
        update_paths, skipped_delete = updatable_paths_from_name_status(output)
        paths = update_paths + skipped_delete
        bridge_paths = [path for path in paths if path == BRIDGE_REPO_ROOT.as_posix() or path.startswith(f"{BRIDGE_REPO_ROOT.as_posix()}/")]
        if bridge_paths:
            print("Bridge body changes exist remotely and will be ignored:")
            for path in bridge_paths:
                print(f"  {path}")
        allowed = [path for path in update_paths if is_body_non_bridge(path)]
        skipped_delete = [path for path in skipped_delete if is_body_non_bridge(path)]
        if skipped_delete:
            print("Remote deletes are intentionally skipped:")
            for path in skipped_delete:
                print(f"  {path}")
        if not allowed:
            print("No non-bridge body changes to sync.")
            return 0
        print("Non-bridge body changes:")
        for path in allowed:
            print(f"  {path}")
        if args.dry_run:
            print("Dry run only; working tree was not updated.")
            return 0
        require_clean_path_names(repo_root, allowed)
        run_git(repo_root, ["restore", "--source", "FETCH_HEAD", "--worktree", "--", *allowed])
        print("Updated non-bridge body paths only.")
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
