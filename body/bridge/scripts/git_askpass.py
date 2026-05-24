#!/usr/bin/env python3

from __future__ import annotations

import os
import sys


def main() -> int:
    prompt = " ".join(sys.argv[1:]).lower()
    if "username" in prompt:
        print(os.environ.get("GITHUB_USER", ""))
        return 0
    if "password" in prompt:
        print(os.environ.get("GITHUB_TOKEN", ""))
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
