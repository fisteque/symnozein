#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import stat
import sys
from pathlib import Path

from bridge_sync_common import (
    SCRIPTS,
    SyncError,
    add_common_args,
    ensure_inside,
    ensure_repo,
)


EXCLUDED_DIRS = {"__pycache__", ".git"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mirror local bridge scripts into the repo copy without deleting repo files."
    )
    add_common_args(parser)
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show copied files without writing them.",
    )
    return parser.parse_args()


def should_skip(path: Path) -> bool:
    if any(part in EXCLUDED_DIRS for part in path.parts):
        return True
    if path.suffix in EXCLUDED_SUFFIXES:
        return True
    if path.name.startswith(".") and ".tmp-" in path.name:
        return True
    return False


def copy_changed_file(source: Path, target: Path, *, dry_run: bool) -> bool:
    if target.exists() and target.read_bytes() == source.read_bytes():
        return False
    print(f"{'Would copy' if dry_run else 'Copying'} {source} -> {target}")
    if dry_run:
        return True
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    if source.stat().st_mode & stat.S_IXUSR:
        target.chmod(target.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return True


def mirror_scripts(runtime_root: Path, repo_root: Path, *, dry_run: bool = False) -> int:
    repo_root = ensure_repo(repo_root)
    source_root = ensure_inside(runtime_root / "scripts", runtime_root)
    target_root = ensure_inside(repo_root / SCRIPTS, repo_root)

    if not source_root.exists():
        raise SyncError(f"Runtime scripts directory does not exist: {source_root}")

    changed = 0
    for source in sorted(source_root.rglob("*")):
        if not source.is_file() or should_skip(source.relative_to(source_root)):
            continue
        rel = source.relative_to(source_root)
        target = ensure_inside(target_root / rel, target_root)
        if copy_changed_file(source, target, dry_run=dry_run):
            changed += 1

    print(f"Scripts mirror complete. Changed files: {changed}")
    return changed


def main() -> int:
    args = parse_args()
    try:
        mirror_scripts(args.runtime_root.resolve(), args.repo_root.resolve(), dry_run=args.dry_run)
        return 0
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())

