import json
import os
from datetime import datetime, timezone

OUTPUT_FILE = "body/index_menu.json"

SOURCE_SCRIPT = "scripts/update_index_menu.py"
SOURCE_WORKFLOW = ".github/workflows/update_index_menu.yml"

MENU_ITEMS = [
    {
        "name": "body",
        "index_path": "body/body_index.json",
        "prev_path": "body/body_index_prev.json",
        "diff_path": "body/body_diff.md",
    },
    {
        "name": "13",
        "index_path": "Reinterpretace_13/13_index.json",
        "prev_path": "Reinterpretace_13/13_index_prev.json",
        "diff_path": "Reinterpretace_13/13_diff.md",
    },
    {
        "name": "material",
        "index_path": "Reinterpretace_13/material_index.json",
        "prev_path": "Reinterpretace_13/material_index_prev.json",
        "diff_path": "Reinterpretace_13/material_diff.md",
    },
    {
        "name": "spirala",
        "index_path": "denik/spirala_index.json",
        "prev_path": "denik/spirala_index_prev.json",
        "diff_path": "denik/spirala_diff.md",
    },
    {
        "name": "denik",
        "index_path": "denik/denik_index.json",
        "prev_path": "denik/denik_index_prev.json",
        "diff_path": "denik/denik_diff.md",
    },
]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def exists(path: str) -> bool:
    return os.path.exists(path)


def build_menu():
    menu = []
    for item in MENU_ITEMS:
        menu.append(
            {
                **item,
                "index_exists": exists(item["index_path"]),
                "prev_exists": exists(item["prev_path"]),
                "diff_exists": exists(item["diff_path"]),
            }
        )
    return {
        "generated_at": utc_now_iso(),
        "source": {
            "script": SOURCE_SCRIPT,
            "workflow": SOURCE_WORKFLOW,
        },
        "menu": menu,
    }


def main():
    data = build_menu()
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Updated {OUTPUT_FILE}.")


if __name__ == "__main__":
    main()
