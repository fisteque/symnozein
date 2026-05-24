#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import sys
import importlib.util
from datetime import UTC, datetime
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1]

DEFAULT_RUNTIME_ROOT = Path("/home/fiste/Noema/bridge")
DEFAULT_REPO_ROOT = Path("/home/fiste/Noema/symnozein")


def load_mirror_function():
    module_path = SCRIPT_DIR / "mirror_scripts_to_repo.py"
    spec = importlib.util.spec_from_file_location("noema_mirror_scripts_to_repo", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load mirror module: {module_path}")
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(SCRIPT_DIR))
    spec.loader.exec_module(module)
    return module.mirror_scripts


def utc_iso() -> str:
    return datetime.now(UTC).isoformat().replace("+00:00", "Z")


def main() -> int:
    if sys.argv[1:]:
        print("mirror_scripts_to_repo task does not accept arguments", file=sys.stderr)
        return 2

    runtime_root = Path(os.environ.get("NOEMA_BRIDGE_ROOT", DEFAULT_RUNTIME_ROOT)).resolve()
    repo_root = Path(os.environ.get("NOEMA_REPO_ROOT", DEFAULT_REPO_ROOT)).resolve()
    mirror_scripts = load_mirror_function()
    changed = mirror_scripts(runtime_root, repo_root, dry_run=False)

    print(
        json.dumps(
            {
                "task": "mirror_scripts_to_repo",
                "run_id": os.environ.get("NOEMA_TASK_RUN_ID"),
                "runtime_root": str(runtime_root),
                "repo_root": str(repo_root),
                "changed_files": changed,
                "completed_at": utc_iso(),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
