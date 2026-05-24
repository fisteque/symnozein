#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import os
import sys
from datetime import UTC, datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1]
DEFAULT_RUNTIME_ROOT = Path("/home/fiste/Noema/bridge")
DEFAULT_REPO_ROOT = Path("/home/fiste/Noema/symnozein")
DEFAULT_REMOTE = "origin"
DEFAULT_BRANCH = "main"


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def load_module(filename: str, module_name: str):
    module_path = SCRIPT_DIR / filename
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load sync module: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(SCRIPT_DIR))
    spec.loader.exec_module(module)
    return module


def main() -> int:
    if sys.argv[1:]:
        print("sync_body_without_bridge task does not accept arguments", file=sys.stderr)
        return 2

    runtime_root = Path(os.environ.get("NOEMA_BRIDGE_ROOT", DEFAULT_RUNTIME_ROOT)).resolve()
    repo_root = Path(os.environ.get("NOEMA_REPO_ROOT", DEFAULT_REPO_ROOT)).resolve()
    remote = os.environ.get("NOEMA_SYNC_REMOTE", DEFAULT_REMOTE)
    branch = os.environ.get("NOEMA_SYNC_BRANCH", DEFAULT_BRANCH)

    module = load_module("sync_body_without_bridge.py", "noema_sync_body_without_bridge")
    old_argv = sys.argv[:]
    try:
        sys.argv = [
            "sync_body_without_bridge.py",
            "--runtime-root",
            str(runtime_root),
            "--repo-root",
            str(repo_root),
            "--remote",
            remote,
            "--branch",
            branch,
        ]
        exit_code = int(module.main())
    finally:
        sys.argv = old_argv

    print(
        json.dumps(
            {
                "task": "sync_body_without_bridge",
                "run_id": os.environ.get("NOEMA_TASK_RUN_ID"),
                "runtime_root": str(runtime_root),
                "repo_root": str(repo_root),
                "remote": remote,
                "branch": branch,
                "exit_code": exit_code,
                "completed_at": utc_iso(),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
