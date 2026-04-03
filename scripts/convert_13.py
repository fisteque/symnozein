import json
import os
import shutil
import sys
from datetime import datetime, date as date_type, timezone

import markdown
import yaml

TARGETS = {
    "13": {
        "input_dir": "Reinterpretace_13/13_md",
        "output_dir": "Reinterpretace_13/13",
        "template_path": "Reinterpretace_13/templates/template.html",
        "index_path": "Reinterpretace_13/13_index.json",
        "index_prev_path": "Reinterpretace_13/13_index_prev.json",
        "diff_path": "Reinterpretace_13/13_diff.md",
        "sitemap_path": "Reinterpretace_13/sitemap_13.xml",
        "url_prefix": "https://fisteque.github.io/symnozein/Reinterpretace_13/13/",
        "source_script": "scripts/convert_13.py",
        "source_workflow": ".github/workflows/update_13_index.yml",
        "diff_title": "# 13 diff",
        "diff_description": "Automaticky generovaný přehled posledních změn v mapitolách 13.",
    },
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


def load_metadata(md_file):
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


def backup_previous_index(index_path, index_prev_path):
    if os.path.exists(index_path):
        shutil.copy2(index_path, index_prev_path)


def load_json(path):
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

    # starý formát: index je přímo list entries
    if isinstance(index_data, list):
        entries = index_data

    # nový formát: objekt s klíčem "entries"
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
        if prev_map[file] != curr_map[file]:
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


def parse_existing_diff_entries(path, diff_title):
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


def format_diff_entry(diff, config):
    source = diff.get("source", {})
    lines = [
        f"## {diff['generated_at']}",
        "",
        "Zdroj změn:",
        f"- skript: `{source.get('script', config['source_script'])}`",
        f"- workflow: `{source.get('workflow', config['source_workflow'])}`",
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


def write_diff_file(diff, config):
    path = config["diff_path"]
    existing_entries = parse_existing_diff_entries(path, config["diff_title"])
    new_entry = format_diff_entry(diff, config)

    entries = [new_entry] + existing_entries
    entries = entries[:MAX_DIFF_ENTRIES]

    lines = [
        config["diff_title"],
        "",
        config["diff_description"],
        f"Uchovává posledních **{MAX_DIFF_ENTRIES}** záznamů.",
        "",
        "---",
        "",
        "\n\n---\n\n".join(entries),
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def process_target(target_name):
    if target_name not in TARGETS:
        print(f"Unknown target: {target_name}")
        return

    config = TARGETS[target_name]
    input_dir = config["input_dir"]
    output_dir = config["output_dir"]
    index_path = config["index_path"]
    index_prev_path = config["index_prev_path"]
    sitemap_path = config["sitemap_path"]
    url_prefix = config["url_prefix"]
    template = ""

    previous_index = load_json(index_path)
    backup_previous_index(index_path, index_prev_path)

    if config["template_path"] and os.path.exists(config["template_path"]):
        with open(config["template_path"], "r", encoding="utf-8") as f:
            template = f.read()

    index_entries = []
    sitemap_urls = []

    for filename in os.listdir(input_dir):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(input_dir, filename)
        metadata, content = load_metadata(filepath)

        hidden = metadata.get("hidden", False)

        base_name = os.path.splitext(filename)[0]
        html_filename = base_name + ".html"
        html_url = url_prefix + html_filename

        html_body = markdown.markdown(content, extensions=["extra", "codehilite", "toc"])
        final_html = template.replace("{{ content }}", html_body)
        for key, value in metadata.items():
            final_html = final_html.replace(f"{{{{ {key} }}}}", str(value))

        output_path = os.path.join(output_dir, html_filename)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_html)

        size = os.path.getsize(output_path) if os.path.exists(output_path) else 0

        index_entry = {
            "title": metadata.get("title", base_name),
            "file": html_filename,
            "date": normalize_date(metadata.get("date")),
            "summary": metadata.get("summary", ""),
            "tags": metadata.get("tags", []),
            "hidden": hidden,
            "size": size,
        }
        index_entries.append(index_entry)

        if not hidden:
            sitemap_urls.append(html_url)

    index_entries = sorted(index_entries, key=lambda x: x["file"])
    index_data = build_index_data(index_entries, config)

    with open(index_path, "w", encoding="utf-8") as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write("</urlset>")

    current_index = load_json(index_path)
    diff = compute_diff(previous_index, current_index)
    write_diff_file(diff, config)


def main():
    if len(sys.argv) == 1:
        for target in TARGETS:
            process_target(target)
    elif len(sys.argv) == 3 and sys.argv[1] == "--only":
        process_target(sys.argv[2])
    else:
        print("Použití: python convert_13.py --only [13]")
        sys.exit(1)


if __name__ == "__main__":
    main()
