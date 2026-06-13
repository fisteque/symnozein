#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

from bridge_cycle_lock import DEFAULT_LOCK_TTL_SECONDS, bridge_cycle_lock, update_lock_progress
from bridge_sync_common import (
    DEFAULT_PROJECT_ROOT,
    STATE_SUMMARY,
    SyncError,
    add_common_args,
    ensure_inside,
    ensure_repo,
    print_git_output,
    repo_rel,
    run_git,
)


SCRIPT_DIR = Path(__file__).resolve().parent
LATEST = STATE_SUMMARY / "latest.md"
COMMIT_MESSAGE = "Pulse body state to tape"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish a scheduled body health pulse by committing latest.md only.")
    add_common_args(parser)
    parser.add_argument(
        "--project-root",
        type=Path,
        default=DEFAULT_PROJECT_ROOT,
        help=f"Project root containing state/body_state.json. Default: {DEFAULT_PROJECT_ROOT}",
    )
    parser.add_argument("--lock-ttl-seconds", type=int, default=DEFAULT_LOCK_TTL_SECONDS)
    parser.add_argument("--dry-run", action="store_true", help="Refresh latest.md and show what would be committed.")
    return parser.parse_args()


def git_push_env() -> dict[str, str]:
    env = os.environ.copy()
    env["GIT_TERMINAL_PROMPT"] = "0"
    if env.get("GITHUB_USER") and env.get("GITHUB_TOKEN"):
        env["GIT_ASKPASS"] = str(SCRIPT_DIR / "git_askpass.py")
    return env


def run_step(name: str, args: list[str], *, env: dict[str, str] | None = None) -> None:
    print(f"== {name} ==")
    result = subprocess.run(
        args,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
        check=False,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip(), file=sys.stderr)
    if result.returncode != 0:
        raise SyncError(f"Step failed ({name}) with exit code {result.returncode}")


def porcelain(repo_root: Path, args: list[str]) -> str:
    return run_git(repo_root, ["status", "--porcelain", *args]).stdout.strip()


def ensure_no_unrelated_dirty(repo_root: Path) -> None:
    status = porcelain(repo_root, ["--untracked-files=all"])
    if not status:
        return
    allowed = {f" M {repo_rel(LATEST)}", f"M  {repo_rel(LATEST)}", f"MM {repo_rel(LATEST)}"}
    disallowed = [line for line in status.splitlines() if line not in allowed]
    if disallowed:
        raise SyncError(
            "Refusing body pulse because repo has unrelated dirty paths:\n"
            + "\n".join(disallowed)
        )


def branch_divergence(repo_root: Path) -> tuple[int, int]:
    output = run_git(repo_root, ["rev-list", "--left-right", "--count", "HEAD...FETCH_HEAD"]).stdout
    ahead, behind = output.strip().split()
    return int(ahead), int(behind)


def fetch_and_rebase(repo_root: Path, remote: str, branch: str) -> None:
    fetch = run_git(repo_root, ["fetch", "--no-tags", remote, branch])
    print_git_output(fetch)
    ahead, behind = branch_divergence(repo_root)
    if behind == 0:
        print("Local branch is not behind remote.")
        return
    print(f"Local branch divergence before pulse push: ahead={ahead} behind={behind}")
    latest_status = porcelain(repo_root, ["--", repo_rel(LATEST)])
    stash_ref = None
    if latest_status:
        stash = run_git(repo_root, ["stash", "push", "-m", "body-pulse-pre-rebase", "--", repo_rel(LATEST)])
        print_git_output(stash)
        stash_ref = "stash@{0}"
    try:
        rebase = run_git(repo_root, ["rebase", "FETCH_HEAD"])
        print_git_output(rebase)
    finally:
        if stash_ref is not None:
            pop = run_git(repo_root, ["stash", "pop", stash_ref])
            print_git_output(pop)
    ensure_no_unrelated_dirty(repo_root)


def staged_paths(repo_root: Path) -> list[str]:
    output = run_git(repo_root, ["diff", "--cached", "--name-only"]).stdout
    return [line for line in output.splitlines() if line]


def refresh_latest(runtime_root: Path, repo_root: Path, project_root: Path) -> None:
    run_step(
        "write bridge summary",
        [
            sys.executable,
            str(SCRIPT_DIR / "write_bridge_summary.py"),
            "--runtime-root",
            str(runtime_root),
            "--repo-root",
            str(repo_root),
            "--project-root",
            str(project_root),
        ],
    )


def pulse(args: argparse.Namespace) -> dict[str, object]:
    runtime_root = args.runtime_root.resolve()
    repo_root = ensure_repo(args.repo_root)
    project_root = args.project_root.resolve()
    latest_path = ensure_inside(repo_root / LATEST, repo_root)

    with bridge_cycle_lock(runtime_root, ttl_seconds=args.lock_ttl_seconds) as lock_path:
        print(f"Bridge lock acquired: {lock_path}")
        update_lock_progress(lock_path, runtime_root, "body pulse fetch")
        fetch_and_rebase(repo_root, args.remote, args.branch)

        update_lock_progress(lock_path, runtime_root, "body pulse summary")
        refresh_latest(runtime_root, repo_root, project_root)
        ensure_no_unrelated_dirty(repo_root)

        status = porcelain(repo_root, ["--", repo_rel(LATEST)])
        if not status:
            print("No latest.md change to pulse.")
            return {"status": "no_change", "path": repo_rel(LATEST)}

        if args.dry_run:
            print("Dry run only; latest.md would be committed and pushed.")
            print(status)
            return {"status": "would_commit", "path": repo_rel(LATEST)}

        update_lock_progress(lock_path, runtime_root, "body pulse commit")
        run_git(repo_root, ["add", "--", repo_rel(LATEST)])
        staged = staged_paths(repo_root)
        if staged != [repo_rel(LATEST)]:
            raise SyncError(f"Refusing body pulse because staged paths are not exactly latest.md: {staged}")

        commit = run_git(repo_root, ["commit", "-m", COMMIT_MESSAGE])
        print_git_output(commit)
        commit_hash = run_git(repo_root, ["rev-parse", "--short", "HEAD"]).stdout.strip()

        update_lock_progress(lock_path, runtime_root, "body pulse push")
        push = run_git(
            repo_root,
            ["push", args.remote, f"HEAD:{args.branch}"],
            env=git_push_env(),
        )
        print_git_output(push)
        return {
            "status": "pushed",
            "path": str(latest_path),
            "commit": commit_hash,
            "message": COMMIT_MESSAGE,
        }


def main() -> int:
    args = parse_args()
    try:
        result = pulse(args)
        print(result)
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
