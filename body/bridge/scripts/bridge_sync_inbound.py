#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from bridge_sync_common import (
    INBOX_MESSAGES,
    SyncError,
    add_common_args,
    ensure_inside,
    ensure_repo,
    print_git_output,
    porcelain_status,
    repo_rel,
    run_git,
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


def remote_inbound_paths(repo_root, path: str) -> set[str]:
    output = run_git(repo_root, ["ls-tree", "-r", "--name-only", "FETCH_HEAD", "--", path]).stdout
    return {line for line in output.splitlines() if line}


def local_inbound_paths(repo_root, path: str) -> set[str]:
    root = ensure_inside(repo_root / path, repo_root)
    if not root.exists():
        return set()
    paths: set[str] = set()
    for item in root.rglob("*"):
        if not item.is_file():
            continue
        rel = item.resolve().relative_to(repo_root.resolve()).as_posix()
        paths.add(rel)
    return paths


def remove_stale_local_files(repo_root, paths: list[str], *, dry_run: bool) -> None:
    for path in paths:
        local_path = ensure_inside(repo_root / path, repo_root)
        if not local_path.exists():
            continue
        if not local_path.is_file():
            raise SyncError(f"Refusing to remove non-file inbound path: {path}")
        print(f"{'Would remove' if dry_run else 'Removing'} local inbound file absent from FETCH_HEAD: {path}")
        if not dry_run:
            local_path.unlink()


def prune_empty_dirs(root) -> None:
    if not root.exists():
        return
    for item in sorted(root.rglob("*"), reverse=True):
        if item.is_dir() and not any(item.iterdir()):
            item.rmdir()


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
        remote_paths = remote_inbound_paths(repo_root, path)
        local_paths = local_inbound_paths(repo_root, path)
        stale_local_paths = sorted(local_paths - remote_paths)

        if not diff:
            if stale_local_paths:
                print("Local inbound files absent from FETCH_HEAD detected:")
                for stale in stale_local_paths:
                    print(f"  {stale}")
                remove_stale_local_files(repo_root, stale_local_paths, dry_run=args.dry_run)
                if not args.dry_run:
                    prune_empty_dirs(repo_root / path)
                print(f"Local inbound mirror pruned under {path}.")
                return 0
            if local_status:
                print("Local inbound files are already present and match FETCH_HEAD:")
                print(local_status)
            print(f"No inbound changes for {path}.")
            return 0

        print("Inbound changes detected:")
        print(diff)
        if stale_local_paths:
            print("Local inbound files absent from FETCH_HEAD detected:")
            for stale in stale_local_paths:
                print(f"  {stale}")

        if args.dry_run:
            print("Dry run only; working tree was not updated.")
            return 0

        remove_stale_local_files(repo_root, stale_local_paths, dry_run=False)
        if remote_paths:
            run_git(repo_root, ["restore", "--source", "FETCH_HEAD", "--worktree", "--", path])
        prune_empty_dirs(repo_root / path)
        print(f"Updated inbound mirror to match FETCH_HEAD under {path}.")
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
