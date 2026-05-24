#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import subprocess
from pathlib import Path


DEFAULT_PROJECT_ROOT = Path("/home/fiste/Noema")
DEFAULT_RUNTIME_ROOT = DEFAULT_PROJECT_ROOT / "bridge"
DEFAULT_REPO_ROOT = DEFAULT_PROJECT_ROOT / "symnozein"
DEFAULT_REMOTE = "origin"
DEFAULT_BRANCH = "main"

BRIDGE_REPO_ROOT = Path("body/bridge")
INBOX_MESSAGES = BRIDGE_REPO_ROOT / "inbox/messages"
OUTBOX_MESSAGES = BRIDGE_REPO_ROOT / "outbox/messages"
OUTBOX_CODEX = BRIDGE_REPO_ROOT / "outbox/codex"
LOGS = BRIDGE_REPO_ROOT / "logs"
STATE_SUMMARY = BRIDGE_REPO_ROOT / "state_summary"
SCRIPTS = BRIDGE_REPO_ROOT / "scripts"

FORBIDDEN_REPO_PATHS = (
    BRIDGE_REPO_ROOT / "state",
    Path("body/bridge/processed_messages.json"),
    Path("body/bridge/event_state.json"),
    Path("body/bridge/lock.json"),
)


class SyncError(RuntimeError):
    pass


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--runtime-root",
        type=Path,
        default=DEFAULT_RUNTIME_ROOT,
        help=f"Local bridge runtime root. Default: {DEFAULT_RUNTIME_ROOT}",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=DEFAULT_REPO_ROOT,
        help=f"Git repo root. Default: {DEFAULT_REPO_ROOT}",
    )
    parser.add_argument(
        "--remote",
        default=os.environ.get("NOEMA_SYNC_REMOTE", DEFAULT_REMOTE),
        help=f"Git remote name or URL. Default: {DEFAULT_REMOTE}",
    )
    parser.add_argument(
        "--branch",
        default=os.environ.get("NOEMA_SYNC_BRANCH", DEFAULT_BRANCH),
        help=f"Git branch. Default: {DEFAULT_BRANCH}",
    )


def ensure_repo(repo_root: Path) -> Path:
    repo_root = repo_root.resolve()
    if not (repo_root / ".git").exists():
        raise SyncError(f"Not a git repo: {repo_root}")
    return repo_root


def ensure_inside(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise SyncError(f"Unsafe path outside allowed root: {path}")
    return resolved_path


def repo_rel(path: Path) -> str:
    return path.as_posix()


def run_git(
    repo_root: Path,
    args: list[str],
    *,
    check: bool = True,
    capture: bool = True,
    env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    cmd = ["git", "-C", str(repo_root), *args]
    try:
        return subprocess.run(
            cmd,
            check=check,
            text=True,
            stdout=subprocess.PIPE if capture else None,
            stderr=subprocess.PIPE if capture else None,
            env=env,
        )
    except subprocess.CalledProcessError as exc:
        stderr = (exc.stderr or "").strip()
        stdout = (exc.stdout or "").strip()
        detail = stderr or stdout or f"exit code {exc.returncode}"
        raise SyncError(f"Git command failed: {' '.join(cmd)}\n{detail}") from exc


def porcelain_status(repo_root: Path, paths: list[Path] | tuple[Path, ...]) -> str:
    args = ["status", "--porcelain", "--", *[repo_rel(path) for path in paths]]
    return run_git(repo_root, args).stdout.strip()


def require_clean_paths(repo_root: Path, paths: list[Path] | tuple[Path, ...]) -> None:
    status = porcelain_status(repo_root, paths)
    if status:
        joined = ", ".join(repo_rel(path) for path in paths)
        raise SyncError(f"Refusing to sync because repo paths are dirty ({joined}):\n{status}")


def require_clean_path_names(repo_root: Path, paths: list[str]) -> None:
    if not paths:
        return
    status = run_git(repo_root, ["status", "--porcelain", "--", *paths]).stdout.strip()
    if status:
        raise SyncError(f"Refusing to sync because target paths are dirty:\n{status}")


def print_git_output(result: subprocess.CompletedProcess[str]) -> None:
    if result.stdout:
        print(result.stdout.rstrip())
    if result.stderr:
        print(result.stderr.rstrip())


def parse_name_status(output: str) -> list[tuple[str, list[str]]]:
    changes: list[tuple[str, list[str]]] = []
    for line in output.splitlines():
        if not line:
            continue
        parts = line.split("\t")
        status = parts[0]
        paths = parts[1:]
        changes.append((status, paths))
    return changes


def updatable_paths_from_name_status(output: str) -> tuple[list[str], list[str]]:
    update: list[str] = []
    skipped_delete: list[str] = []
    for status, paths in parse_name_status(output):
        kind = status[0]
        if kind == "D":
            skipped_delete.extend(paths)
        elif kind == "R" and len(paths) >= 2:
            skipped_delete.append(paths[0])
            update.append(paths[-1])
        elif paths:
            update.append(paths[-1])
    return update, skipped_delete
