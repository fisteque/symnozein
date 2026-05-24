#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from bridge_sync_common import (
    FORBIDDEN_REPO_PATHS,
    LOGS,
    OUTBOX_MESSAGES,
    SCRIPTS,
    STATE_SUMMARY,
    SyncError,
    add_common_args,
    ensure_inside,
    ensure_repo,
    porcelain_status,
    print_git_output,
    repo_rel,
    run_git,
)
from mirror_scripts_to_repo import mirror_scripts


COMMIT_MESSAGE = "Sync RPi bridge outbound state"
ALLOWED_REPO_PATHS = (OUTBOX_MESSAGES, LOGS, STATE_SUMMARY, SCRIPTS)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Safely mirror and optionally push bridge outbound files to Git."
    )
    add_common_args(parser)
    parser.add_argument(
        "--commit-and-push",
        action="store_true",
        help=f"Create a commit with the built-in message and push it. Message: {COMMIT_MESSAGE!r}",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be mirrored, staged, committed, and pushed without writing.",
    )
    return parser.parse_args()


def copy_tree_without_delete(source_root: Path, target_root: Path, *, dry_run: bool) -> int:
    if not source_root.exists():
        return 0
    changed = 0
    for source in sorted(source_root.rglob("*")):
        if not source.is_file():
            continue
        rel = source.relative_to(source_root)
        target = ensure_inside(target_root / rel, target_root)
        if target.exists() and target.read_bytes() == source.read_bytes():
            continue
        print(f"{'Would copy' if dry_run else 'Copying'} {source} -> {target}")
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        changed += 1
    return changed


def mirror_outbound(runtime_root: Path, repo_root: Path, *, dry_run: bool) -> None:
    pairs = (
        (runtime_root / "outbox/messages", repo_root / OUTBOX_MESSAGES),
        (runtime_root / "logs", repo_root / LOGS),
        (runtime_root / "state_summary", repo_root / STATE_SUMMARY),
    )
    for source, target in pairs:
        ensure_inside(target, repo_root)
        changed = copy_tree_without_delete(source, target, dry_run=dry_run)
        if source.exists():
            print(f"Mirrored {source} -> {target}. Changed files: {changed}")
        else:
            print(f"Optional source missing, skipped: {source}")

    mirror_scripts(runtime_root, repo_root, dry_run=dry_run)


def ensure_no_forbidden_status(repo_root: Path) -> None:
    status = porcelain_status(repo_root, FORBIDDEN_REPO_PATHS)
    if status:
        raise SyncError(f"Forbidden bridge state paths have git changes:\n{status}")


def is_allowed_staged_path(name: str) -> bool:
    path = Path(name)
    return any(path == allowed or allowed in path.parents for allowed in ALLOWED_REPO_PATHS)


def ensure_no_disallowed_staged_paths(repo_root: Path) -> None:
    staged = run_git(repo_root, ["diff", "--cached", "--name-only"]).stdout.splitlines()
    disallowed = [name for name in staged if not is_allowed_staged_path(name)]
    if disallowed:
        raise SyncError(
            "Refusing outbound sync because staged paths outside the bridge outbound whitelist exist:\n"
            + "\n".join(disallowed)
        )


def stage_allowed_paths(repo_root: Path) -> None:
    existing = [path for path in ALLOWED_REPO_PATHS if (repo_root / path).exists()]
    if existing:
        run_git(repo_root, ["add", "--", *[repo_rel(path) for path in existing]])


def show_pending(repo_root: Path) -> str:
    existing = [path for path in ALLOWED_REPO_PATHS if (repo_root / path).exists()]
    if not existing:
        return ""
    return run_git(
        repo_root,
        ["diff", "--cached", "--name-status", "--", *[repo_rel(path) for path in existing]],
    ).stdout.strip()


def main() -> int:
    args = parse_args()
    try:
        repo_root = ensure_repo(args.repo_root)
        runtime_root = args.runtime_root.resolve()
        ensure_inside(runtime_root, runtime_root)
        ensure_no_forbidden_status(repo_root)
        ensure_no_disallowed_staged_paths(repo_root)

        mirror_outbound(runtime_root, repo_root, dry_run=args.dry_run)

        if args.dry_run:
            status = porcelain_status(repo_root, ALLOWED_REPO_PATHS)
            print("Dry run only; repo was not staged.")
            print("Current allowed-path git status:")
            print(status or "(clean)")
            return 0

        stage_allowed_paths(repo_root)
        ensure_no_forbidden_status(repo_root)
        ensure_no_disallowed_staged_paths(repo_root)
        pending = show_pending(repo_root)

        print("Staged outbound changes:")
        print(pending or "(none)")

        if not pending:
            print("Nothing to commit or push.")
            return 0

        print(f"Commit message in code: {COMMIT_MESSAGE}")
        if not args.commit_and_push:
            print("Not committing or pushing. Re-run with --commit-and-push to publish.")
            return 0

        print("Committing outbound changes...")
        commit = run_git(repo_root, ["commit", "-m", COMMIT_MESSAGE])
        print_git_output(commit)
        print(f"Pushing to {args.remote} {args.branch}...")
        push = run_git(repo_root, ["push", args.remote, f"HEAD:{args.branch}"])
        print_git_output(push)
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
