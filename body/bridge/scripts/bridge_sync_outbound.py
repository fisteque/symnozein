#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import shutil
import sys
from pathlib import Path

from bridge_sync_common import (
    FORBIDDEN_REPO_PATHS,
    INBOX_MESSAGES,
    LOGS,
    OUTBOX_CODEX,
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
RUNTIME_LOG_NAME = "bridge.log"
REPO_LOG_TAIL_NAME = "bridge_tail.log"
LOG_TAIL = LOGS / REPO_LOG_TAIL_NAME
LEGACY_REPO_LOG = LOGS / RUNTIME_LOG_NAME
STATE_SUMMARY_LATEST = STATE_SUMMARY / "latest.md"
ALLOWED_REPO_PATHS = (OUTBOX_MESSAGES, OUTBOX_CODEX, STATE_SUMMARY, SCRIPTS)
REMOVED_REPO_PATHS = (LOG_TAIL,)
LOCAL_ONLY_REPO_PATHS = (INBOX_MESSAGES,)


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
        (runtime_root / "state_summary", repo_root / STATE_SUMMARY),
    )
    for source, target in pairs:
        ensure_inside(target, repo_root)
        changed = copy_tree_without_delete(source, target, dry_run=dry_run)
        if source.exists():
            print(f"Mirrored {source} -> {target}. Changed files: {changed}")
        else:
            print(f"Optional source missing, skipped: {source}")

    print(
        "Log tail mirror disabled; runtime log remains local and public tail is "
        f"available through {repo_root / STATE_SUMMARY_LATEST}."
    )
    mirror_scripts(runtime_root, repo_root, dry_run=dry_run)


def ensure_no_forbidden_status(repo_root: Path) -> None:
    status = porcelain_status(repo_root, FORBIDDEN_REPO_PATHS)
    if status:
        raise SyncError(f"Forbidden bridge state paths have git changes:\n{status}")


def is_allowed_staged_change(status: str, name: str) -> bool:
    path = Path(name)
    if any(path == allowed or allowed in path.parents for allowed in ALLOWED_REPO_PATHS):
        return True
    return status.startswith("D") and is_removed_repo_path(name)


def ensure_no_disallowed_staged_paths(repo_root: Path) -> None:
    staged = run_git(repo_root, ["diff", "--cached", "--name-status"]).stdout.splitlines()
    disallowed: list[str] = []
    for line in staged:
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        names = parts[1:]
        if not names or not all(is_allowed_staged_change(status, name) for name in names):
            disallowed.append(line)
    if disallowed:
        raise SyncError(
            "Refusing outbound sync because staged paths outside the bridge outbound whitelist exist:\n"
            + "\n".join(disallowed)
        )


def path_exists_or_tracked(repo_root: Path, path: Path) -> bool:
    if (repo_root / path).exists():
        return True
    result = run_git(repo_root, ["ls-files", "--error-unmatch", repo_rel(path)], check=False)
    return result.returncode == 0


def working_tree_status(repo_root: Path) -> str:
    return run_git(repo_root, ["status", "--porcelain", "--untracked-files=all"]).stdout.strip()


def working_tree_status_for_paths(repo_root: Path, paths: tuple[Path, ...]) -> str:
    return run_git(
        repo_root,
        ["status", "--porcelain", "--untracked-files=all", "--", *[repo_rel(path) for path in paths]],
    ).stdout.strip()


def is_allowed_worktree_path(name: str) -> bool:
    path = Path(name)
    allowed_paths = (*ALLOWED_REPO_PATHS, *LOCAL_ONLY_REPO_PATHS)
    return any(path == allowed or allowed in path.parents for allowed in allowed_paths)


def is_removed_repo_path(name: str) -> bool:
    path = Path(name)
    return any(path == removed for removed in REMOVED_REPO_PATHS)


def is_allowed_worktree_status_line(line: str) -> bool:
    status = line[:2]
    name = line[3:] if len(line) > 2 and line[2] == " " else line[2:]
    if " -> " in name:
        old_name, new_name = name.split(" -> ", 1)
        return is_allowed_worktree_path(old_name) and is_allowed_worktree_path(new_name)
    if "D" in status and is_removed_repo_path(name):
        return True
    return is_allowed_worktree_path(name)


def ensure_only_allowed_worktree_changes(repo_root: Path) -> None:
    status = working_tree_status(repo_root)
    if not status:
        return
    disallowed = [
        line
        for line in status.splitlines()
        if not is_allowed_worktree_status_line(line)
    ]
    if disallowed:
        raise SyncError(
            "Refusing outbound sync because worktree has changes outside the bridge outbound whitelist:\n"
            + "\n".join(disallowed)
        )


def stage_allowed_paths(repo_root: Path) -> None:
    existing = [path for path in ALLOWED_REPO_PATHS if path_exists_or_tracked(repo_root, path)]
    if existing:
        run_git(repo_root, ["add", "--", *[repo_rel(path) for path in existing]])
    removed = [
        path
        for path in REMOVED_REPO_PATHS
        if not (repo_root / path).exists() and path_exists_or_tracked(repo_root, path)
    ]
    if removed:
        run_git(repo_root, ["add", "--", *[repo_rel(path) for path in removed]])


def show_pending(repo_root: Path) -> str:
    existing = [
        path
        for path in (*ALLOWED_REPO_PATHS, *REMOVED_REPO_PATHS)
        if path_exists_or_tracked(repo_root, path)
    ]
    if not existing:
        return ""
    return run_git(
        repo_root,
        ["diff", "--cached", "--name-status", "--", *[repo_rel(path) for path in existing]],
    ).stdout.strip()


def staged_allowed_paths(repo_root: Path) -> list[str]:
    existing = [
        path
        for path in (*ALLOWED_REPO_PATHS, *REMOVED_REPO_PATHS)
        if path_exists_or_tracked(repo_root, path)
    ]
    if not existing:
        return []
    output = run_git(
        repo_root,
        ["diff", "--cached", "--name-only", "--", *[repo_rel(path) for path in existing]],
    ).stdout
    return [line for line in output.splitlines() if line]


def has_substantive_staged_change(repo_root: Path) -> bool:
    quiet_paths = (repo_rel(STATE_SUMMARY_LATEST),)
    for path in staged_allowed_paths(repo_root):
        if not any(path == quiet or path.startswith(f"{quiet}/") for quiet in quiet_paths):
            return True
    return False


def unstage_allowed_paths(repo_root: Path) -> None:
    staged = staged_allowed_paths(repo_root)
    if staged:
        run_git(repo_root, ["restore", "--staged", "--", *staged])


def existing_allowed_paths(repo_root: Path) -> list[Path]:
    return [
        path
        for path in (*ALLOWED_REPO_PATHS, *REMOVED_REPO_PATHS)
        if path_exists_or_tracked(repo_root, path)
    ]


def local_only_untracked_paths(repo_root: Path) -> list[Path]:
    status = working_tree_status_for_paths(repo_root, LOCAL_ONLY_REPO_PATHS)
    paths: list[Path] = []
    for line in status.splitlines():
        if not line.startswith("?? "):
            continue
        path = Path(line[3:])
        if any(path == local_only or local_only in path.parents for local_only in LOCAL_ONLY_REPO_PATHS):
            paths.append(path)
    return paths


def fetch_head_file_bytes(repo_root: Path, path: Path) -> bytes | None:
    result = run_git(repo_root, ["show", f"FETCH_HEAD:{repo_rel(path)}"], check=False)
    if result.returncode != 0:
        return None
    return result.stdout.encode("utf-8")


def clear_matching_local_only_untracked_files(repo_root: Path) -> None:
    for path in local_only_untracked_paths(repo_root):
        full_path = ensure_inside(repo_root / path, repo_root)
        remote_bytes = fetch_head_file_bytes(repo_root, path)
        if remote_bytes is None or not full_path.is_file():
            continue
        if full_path.read_bytes() != remote_bytes:
            continue
        full_path.unlink()
        print(f"Removed local-only untracked file already present in FETCH_HEAD: {repo_rel(path)}")


def branch_divergence(repo_root: Path) -> tuple[int, int]:
    output = run_git(repo_root, ["rev-list", "--left-right", "--count", "HEAD...FETCH_HEAD"]).stdout
    left, right = output.strip().split()
    return int(left), int(right)


def safe_rebase_onto_fetch_head(repo_root: Path, remote: str, branch: str) -> None:
    ensure_only_allowed_worktree_changes(repo_root)
    fetch = run_git(repo_root, ["fetch", "--no-tags", remote, branch])
    print_git_output(fetch)
    ahead, behind = branch_divergence(repo_root)
    if behind == 0:
        print("Local branch is not behind remote; no pre-push rebase needed.")
        return

    print(f"Local branch divergence before push: ahead={ahead} behind={behind}")
    clear_matching_local_only_untracked_files(repo_root)
    allowed_dirty = bool(working_tree_status_for_paths(repo_root, ALLOWED_REPO_PATHS))
    stash_ref = None
    if allowed_dirty:
        stash = run_git(
            repo_root,
            [
                "stash",
                "push",
                "-m",
                "bridge-outbound-pre-rebase",
                "--",
                *[repo_rel(path) for path in existing_allowed_paths(repo_root)],
            ],
        )
        print_git_output(stash)
        stash_ref = "stash@{0}"

    try:
        rebase = run_git(repo_root, ["rebase", "FETCH_HEAD"])
        print_git_output(rebase)
    finally:
        if stash_ref is not None:
            pop = run_git(repo_root, ["stash", "pop", stash_ref])
            print_git_output(pop)
    ensure_only_allowed_worktree_changes(repo_root)


def git_push_env() -> dict[str, str]:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    if env.get("GITHUB_USER") and env.get("GITHUB_TOKEN"):
        env["GIT_ASKPASS"] = str(Path(__file__).resolve().with_name("git_askpass.py"))
    return env


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

        safe_rebase_onto_fetch_head(repo_root, args.remote, args.branch)
        unstage_allowed_paths(repo_root)
        stage_allowed_paths(repo_root)
        ensure_no_forbidden_status(repo_root)
        ensure_no_disallowed_staged_paths(repo_root)
        pending = show_pending(repo_root)
        if not pending:
            print("Nothing to commit or push after pre-push rebase.")
            return 0
        if not has_substantive_staged_change(repo_root):
            unstage_allowed_paths(repo_root)
            print("Only logs/state_summary changed; not committing this cycle.")
            return 0

        print("Committing outbound changes...")
        commit = run_git(repo_root, ["commit", "-m", COMMIT_MESSAGE])
        print_git_output(commit)
        print(f"Pushing to {args.remote} {args.branch}...")
        push = run_git(
            repo_root,
            ["push", args.remote, f"HEAD:{args.branch}"],
            env=git_push_env(),
        )
        print_git_output(push)
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
