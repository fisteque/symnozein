import hashlib
import json
import os
import shutil
from datetime import datetime, timezone

BODY_DIR = "body"
OUTPUT_FILE = os.path.join(BODY_DIR, "body_index.json")
PREV_FILE = os.path.join(BODY_DIR, "body_index_prev.json")
DIFF_FILE = os.path.join(BODY_DIR, "body_diff.md")

SOURCE_SCRIPT = "scripts/update_body_index.py"
SOURCE_WORKFLOW = ".github/workflows/update_body_index.yml"
DIFF_TITLE = "# body diff"
DIFF_DESCRIPTION = "Automaticky generovaný přehled posledních změn ve složce `body/`."

MAX_DIFF_ENTRIES = 50


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_file(path: str) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def scan_directory(base_path: str) -> list[dict]:
    result = []

    skip_names = {"body_index.json", "body_index_prev.json", "body_diff.md"}

    for root, dirs, files in os.walk(base_path):
        dirs.sort()
        files.sort()

        for file in files:
            if file in skip_names:
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path).replace("\\", "/")

            result.append(
                {
                    "path": rel_path,
                    "size": os.stat(full_path).st_size,
                    "sha256": sha256_file(full_path),
                }
            )

    return sorted(result, key=lambda x: x["path"])


def load_json_file(path: str) -> dict | None:
    if not os.path.exists(path):
        return None

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def backup_previous_index() -> None:
    if os.path.exists(OUTPUT_FILE):
        shutil.copy2(OUTPUT_FILE, PREV_FILE)


def build_index(files: list[dict]) -> dict:
    return {
        "generated_at": utc_now_iso(),
        "source": {
            "script": SOURCE_SCRIPT,
            "workflow": SOURCE_WORKFLOW,
        },
        "kind": "state",
        "count": len(files),
        "files": files,
    }


def write_json_file(path: str, data: dict) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def map_files(index_data: dict | None) -> dict[str, dict]:
    if not index_data:
        return {}
    return {item["path"]: item for item in index_data.get("files", [])}


def compute_diff(prev_index: dict | None, current_index: dict) -> dict:
    prev_map = map_files(prev_index)
    curr_map = map_files(current_index)

    prev_paths = set(prev_map.keys())
    curr_paths = set(curr_map.keys())

    added = sorted(curr_paths - prev_paths)
    removed = sorted(prev_paths - curr_paths)

    changed = []
    for path in sorted(curr_paths & prev_paths):
        prev_item = prev_map[path]
        curr_item = curr_map[path]
        if (
            prev_item.get("size") != curr_item.get("size")
            or prev_item.get("sha256") != curr_item.get("sha256")
        ):
            changed.append(path)

    return {
        "generated_at": current_index["generated_at"],
        "source": current_index.get(
            "source",
            {
                "script": SOURCE_SCRIPT,
                "workflow": SOURCE_WORKFLOW,
            },
        ),
        "added": added,
        "removed": removed,
        "changed": changed,
        "count_added": len(added),
        "count_removed": len(removed),
        "count_changed": len(changed),
    }


def parse_existing_diff_entries(path: str) -> list[str]:
    if not os.path.exists(path):
        return []

    with open(path, "r", encoding="utf-8") as f:
        content = f.read().strip()

    if not content:
        return []

    parts = content.split("\n---\n")
    parts = [p.strip() for p in parts if p.strip()]

    if not parts:
        return []

    if parts[0].startswith(DIFF_TITLE):
        return parts[1:]

    return parts


def format_list(items: list[str], empty_text: str) -> list[str]:
    if not items:
        return [f"- {empty_text}"]
    return [f"- `{item}`" for item in items]


def format_diff_entry(diff: dict) -> str:
    source = diff.get("source", {})
    lines = [
        f"## {diff['generated_at']}",
        "",
        "Zdroj změn:",
        f"- skript: `{source.get('script', SOURCE_SCRIPT)}`",
        f"- workflow: `{source.get('workflow', SOURCE_WORKFLOW)}`",
        "",
        f"➕ přidáno: **{diff['count_added']}**",
        *format_list(diff["added"], "nic"),
        "",
        f"🔄 změněno: **{diff['count_changed']}**",
        *format_list(diff["changed"], "nic"),
        "",
        f"❌ odebráno: **{diff['count_removed']}**",
        *format_list(diff["removed"], "nic"),
    ]
    return "\n".join(lines).strip()


def write_diff_file(diff: dict, path: str, max_entries: int) -> None:
    existing_entries = parse_existing_diff_entries(path)
    new_entry = format_diff_entry(diff)

    entries = [new_entry] + existing_entries
    entries = entries[:max_entries]

    lines = [
        DIFF_TITLE,
        "",
        DIFF_DESCRIPTION,
        f"Uchovává posledních **{max_entries}** záznamů.",
        "",
        "---",
        "",
        "\n\n---\n\n".join(entries),
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main() -> None:
    previous_index = load_json_file(OUTPUT_FILE)

    backup_previous_index()

    files = scan_directory(BODY_DIR)
    current_index = build_index(files)
    write_json_file(OUTPUT_FILE, current_index)

    diff = compute_diff(previous_index, current_index)
    write_diff_file(diff, DIFF_FILE, MAX_DIFF_ENTRIES)

    print(f"Updated {OUTPUT_FILE} with {len(files)} files.")
    print(f"Updated {PREV_FILE}.")
    print(f"Updated {DIFF_FILE}.")


if __name__ == "__main__":
    main()
