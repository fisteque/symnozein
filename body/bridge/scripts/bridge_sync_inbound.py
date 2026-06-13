#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import sys
from datetime import UTC, datetime
from pathlib import Path

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


RUNTIME_INBOX_MESSAGES = Path("inbox/messages")
PROCESSED_FILE = Path("state/processed_messages.json")
SYNC_STATE_FILE = Path("state/bridge_sync_state.json")
TERMINAL_AGENT_STATUSES = {"ok", "ignored", "pending_codex", "error"}


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def load_json(path: Path) -> dict:
    if not path.exists():
        return {"version": 1}
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return {"version": 1}
    if not isinstance(data, dict):
        return {"version": 1}
    data.setdefault("version", 1)
    return data


def atomic_write_json(path: Path, data: dict, runtime_root: Path) -> None:
    safe_path = ensure_inside(path, runtime_root)
    safe_path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = ensure_inside(safe_path.with_name(f".{safe_path.name}.tmp-{os.getpid()}"), runtime_root)
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    tmp_path.replace(safe_path)


def record_inbound_sync(runtime_root: Path, *, status: str, hydrated: int | None = None, error: str | None = None) -> None:
    path = ensure_inside(runtime_root / SYNC_STATE_FILE, runtime_root)
    state = load_json(path)
    state["last_inbound_sync"] = utc_iso()
    state["last_inbound_sync_status"] = status
    if hydrated is not None:
        state["last_inbound_hydrated_count"] = hydrated
    if error:
        state["last_inbound_error"] = error
    else:
        state.pop("last_inbound_error", None)
    atomic_write_json(path, state, runtime_root)


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


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_message_id(path: Path) -> str | None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None
    try:
        frontmatter_block, _body = text[4:].split("\n---\n", 1)
    except ValueError:
        return None
    try:
        import yaml

        frontmatter = yaml.safe_load(frontmatter_block) or {}
    except Exception:
        return None
    if not isinstance(frontmatter, dict):
        return None
    message_id = frontmatter.get("id")
    if message_id is None:
        return None
    return str(message_id)


def load_processed(runtime_root: Path) -> dict:
    path = ensure_inside(runtime_root / PROCESSED_FILE, runtime_root)
    if not path.exists():
        return {"version": 1, "messages": {}, "pending": {}, "errors": []}
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SyncError(f"Invalid processed state: {path}")
    data.setdefault("messages", {})
    data.setdefault("pending", {})
    data.setdefault("errors", [])
    return data


def is_terminal_processed(processed: dict, message_id: str | None, sha256: str) -> bool:
    if message_id:
        entry = processed.get("messages", {}).get(message_id)
        if (
            isinstance(entry, dict)
            and entry.get("sha256") == sha256
            and entry.get("status") in TERMINAL_AGENT_STATUSES
        ):
            return True
    for error in processed.get("errors", []):
        if isinstance(error, dict) and error.get("sha256") == sha256:
            return True
    return False


def hydrate_runtime_inbox(repo_root: Path, runtime_root: Path, *, dry_run: bool) -> int:
    mirror_root = ensure_inside(repo_root / INBOX_MESSAGES, repo_root)
    runtime_inbox = ensure_inside(runtime_root / RUNTIME_INBOX_MESSAGES, runtime_root)
    processed = load_processed(runtime_root)
    if not mirror_root.exists():
        print(f"Runtime inbox hydration skipped; mirror source missing: {mirror_root}")
        return 0

    copied = 0
    for source in sorted(mirror_root.glob("*.md")):
        if not source.is_file() or source.name.startswith("."):
            continue
        sha256 = sha256_file(source)
        message_id = parse_message_id(source)
        if is_terminal_processed(processed, message_id, sha256):
            continue

        target = ensure_inside(runtime_inbox / source.name, runtime_inbox)
        if target.exists():
            if target.read_bytes() == source.read_bytes():
                continue
            raise SyncError(f"Runtime inbox already has different content for {target}")

        print(f"{'Would hydrate' if dry_run else 'Hydrating'} runtime inbox: {source} -> {target}")
        if not dry_run:
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        copied += 1

    print(f"Runtime inbox hydration complete. New files: {copied}")
    return copied


def main() -> int:
    args = parse_args()
    runtime_root = args.runtime_root.resolve()
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
                hydrated = hydrate_runtime_inbox(repo_root, runtime_root, dry_run=args.dry_run)
                if not args.dry_run:
                    record_inbound_sync(runtime_root, status="ok", hydrated=hydrated)
                print(f"Local inbound mirror pruned under {path}.")
                return 0
            if local_status:
                print("Local inbound files are already present and match FETCH_HEAD:")
                print(local_status)
                if args.dry_run:
                    print(f"Would restore local inbound mirror from FETCH_HEAD under {path}.")
                else:
                    run_git(repo_root, ["restore", "--source", "FETCH_HEAD", "--worktree", "--", path])
                    prune_empty_dirs(repo_root / path)
                    print(f"Restored local inbound mirror from FETCH_HEAD under {path}.")
            print(f"No inbound changes for {path}.")
            hydrated = hydrate_runtime_inbox(repo_root, runtime_root, dry_run=args.dry_run)
            if not args.dry_run:
                record_inbound_sync(runtime_root, status="ok", hydrated=hydrated)
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
        hydrated = hydrate_runtime_inbox(repo_root, runtime_root, dry_run=False)
        record_inbound_sync(runtime_root, status="ok", hydrated=hydrated)
        return 0
    except SyncError as exc:
        try:
            if not args.dry_run:
                record_inbound_sync(runtime_root, status="error", error=str(exc))
        except Exception as state_exc:
            print(f"WARN: failed to write inbound sync state: {state_exc}", file=sys.stderr)
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
