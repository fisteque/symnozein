import json
import os
import shutil
import hashlib
from datetime import date as date_type
from datetime import datetime, timezone

import yaml

CONFIG = {
    "input_dir": "Symnozein",
    "index_path": "Symnozein/index.json",
    "index_prev_path": "Symnozein/index_prev.json",
    "diff_path": "Symnozein/diff.md",
    "source_script": "scripts/update_symnozein_index.py",
    "source_workflow": ".github/workflows/update_symnozein_index.yml",
    "diff_title": "# Symnozein diff",
    "diff_description": "Automaticky generovaný přehled posledních změn v materiálech Symnozein.",
}

MAX_DIFF_ENTRIES = 50


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def normalize_date(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, datetime):
        return value.date().isoformat()
    if isinstance(value, date_type):
        return value.isoformat()
    return ""


def load_metadata(md_file: str):
    with open(md_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines or lines[0].strip() != "---":
        return {}, "".join(lines)

    meta_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == "---":
            break
        meta_lines.append(lines[i])
        i += 1

    metadata = yaml.safe_load("".join(meta_lines)) or {}
    content = "".join(lines[i + 1 :])
    return metadata, content

def file_sha256(path: str) -> str:
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()
    
def backup_previous_index(index_path: str, index_prev_path: str):
    if os.path.exists(index_path):
        shutil.copy2(index_path, index_prev_path)


def ensure_prev_exists(index_prev_path: str):
    if not os.path.exists(index_prev_path):
        empty_prev = {
            "generated_at": utc_now_iso(),
            "source": {
                "script": CONFIG["source_script"],
                "workflow": CONFIG["source_workflow"],
            },
            "entries": [],
        }
        with open(index_prev_path, "w", encoding="utf-8") as f:
            json.dump(empty_prev, f, indent=2, ensure_ascii=False)


def load_json(path: str):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def build_index_data(index_entries):
    return {
        "generated_at": utc_now_iso(),
        "source": {
            "script": CONFIG["source_script"],
            "workflow": CONFIG["source_workflow"],
        },
        "kind": "content",
        "entries": index_entries,
    }

def get_entries_map(index_data):
    if not index_data:
        return {}

    if isinstance(index_data, list):
        entries = index_data
    elif isinstance(index_data, dict):
        entries = index_data.get("entries", [])
    else:
        return {}

    return {
        entry["file"]: entry
        for entry in entries
        if isinstance(entry, dict) and "file" in entry
    }


def compute_diff(prev_index, current_index):
    prev_map = get_entries_map(prev_index)
    curr_map = get_entries_map(current_index)

    prev_files = set(prev_map.keys())
    curr_files = set(curr_map.keys())

    added = sorted(curr_files - prev_files)
    removed = sorted(prev_files - curr_files)

    changed = []
    for file in sorted(curr_files & prev_files):
        prev_entry = prev_map[file]
        curr_entry = curr_map[file]

        prev_hash = prev_entry.get("content_sha256")
        curr_hash = curr_entry.get("content_sha256")

        if prev_hash and curr_hash:
            if prev_hash != curr_hash:
                changed.append(file)
            continue

        # Backward-compatible fallback for the first run after adding hashes.
        # This avoids marking every existing file as changed only because
        # the new content_sha256 field was added to the index.
        prev_compare = {
            key: value
            for key, value in prev_entry.items()
            if key != "content_sha256"
        }
        curr_compare = {
            key: value
            for key, value in curr_entry.items()
            if key != "content_sha256"
        }

        if prev_compare != curr_compare:
            changed.append(file)
    return {
        "generated_at": current_index.get("generated_at", utc_now_iso()),
        "source": current_index.get("source", {}),
        "added": added,
        "removed": removed,
        "changed": changed,
        "count_added": len(added),
        "count_removed": len(removed),
        "count_changed": len(changed),
    }


def parse_existing_diff_entries(path: str, diff_title: str):
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

    if parts[0].startswith(diff_title):
        return parts[1:]

    return parts


def format_list(items, empty_text="nic"):
    if not items:
        return [f"- {empty_text}"]
    return [f"- `{item}`" for item in items]


def format_diff_entry(diff):
    source = diff.get("source", {})
    lines = [
        f"## {diff['generated_at']}",
        "",
        "Zdroj změn:",
        f"- skript: `{source.get('script', CONFIG['source_script'])}`",
        f"- workflow: `{source.get('workflow', CONFIG['source_workflow'])}`",
        "",
        f"➕ přidáno: **{diff['count_added']}**",
        *format_list(diff["added"]),
        "",
        f"🔄 změněno: **{diff['count_changed']}**",
        *format_list(diff["changed"]),
        "",
        f"❌ odebráno: **{diff['count_removed']}**",
        *format_list(diff["removed"]),
    ]
    return "\n".join(lines).strip()


def write_diff_file(diff):
    path = CONFIG["diff_path"]
    existing_entries = parse_existing_diff_entries(path, CONFIG["diff_title"])
    new_entry = format_diff_entry(diff)

    entries = [new_entry] + existing_entries
    entries = entries[:MAX_DIFF_ENTRIES]

    lines = [
        CONFIG["diff_title"],
        "",
        CONFIG["diff_description"],
        f"Uchovává posledních **{MAX_DIFF_ENTRIES}** záznamů.",
        "",
        "---",
        "",
        "\n\n---\n\n".join(entries),
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

def title_from_filename(filename: str) -> str:
    base_name = os.path.splitext(os.path.basename(filename))[0]
    return base_name.replace("_", " ").replace("-", " ").strip()

def ensure_list(value):
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [item.strip() for item in value.split(",") if item.strip()]
    return []

def build_entry(filename: str):
    # filename is a path relative to Symnozein/, for example:
    # Co_stavime.md or legacy/what_we_build.md
    filepath = os.path.join(CONFIG["input_dir"], filename)
    metadata, _content = load_metadata(filepath)

    title = metadata.get("title") or title_from_filename(filename)
    summary = metadata.get("summary", "") or ""
    tags = ensure_list(metadata.get("tags"))
    date_value = normalize_date(metadata.get("date"))

    return {
        "title": title,
        "file": filename.replace("\\", "/"),
        "path": filepath.replace("\\", "/"),
        "date": date_value,
        "summary": summary,
        "tags": tags,
        "content_sha256": file_sha256(filepath),
    }

def main():
    input_dir = CONFIG["input_dir"]
    index_path = CONFIG["index_path"]
    index_prev_path = CONFIG["index_prev_path"]

    previous_index = load_json(index_path)
    backup_previous_index(index_path, index_prev_path)
    ensure_prev_exists(index_prev_path)

    index_entries = []
    skip_files = {"diff.md"}

    for root, _dirs, files in os.walk(input_dir):
        for filename in sorted(files):
            if not filename.endswith(".md"):
                continue

            full_path = os.path.join(root, filename)
            rel_path = os.path.relpath(full_path, input_dir).replace("\\", "/")

            if rel_path in skip_files:
                continue

            index_entries.append(build_entry(rel_path))

    index_data = build_index_data(index_entries)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    current_index = load_json(index_path)
    diff = compute_diff(previous_index, current_index)
    write_diff_file(diff)

    print(
        f"Aktualizováno: {CONFIG['index_path']}, "
        f"{CONFIG['index_prev_path']} a {CONFIG['diff_path']}"
    )


if __name__ == "__main__":
    main()
