#!/usr/bin/env python3

from __future__ import annotations

import json
import os
import sys
from datetime import UTC, datetime


def main() -> int:
    payload = {
        "task": "example_task",
        "run_id": os.environ.get("NOEMA_TASK_RUN_ID"),
        "received_args": sys.argv[1:],
        "completed_at": datetime.now(UTC).isoformat().replace("+00:00", "Z"),
    }
    print(json.dumps(payload, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
