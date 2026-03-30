import json
import os
import shutil
from datetime import datetime, timezone

import markdown
import yaml
from bs4 import BeautifulSoup

INPUT_MD_DIR = "denik/spirala_vedomi_md"
OUTPUT_HTML_DIR = "denik/spirala_vedomi"
TEMPLATE_PATH = "denik/templates/template.html"

INDEX_PATH = "denik/spirala_index.json"
INDEX_PREV_PATH = "denik/spirala_index_prev.json"
DIFF_PATH = "denik/spirala_diff.md"
SITEMAP_PATH = "denik/sitemap_spirala.xml"

FOLDER_NAME = "spirala_vedomi"
SOURCE_SCRIPT = "scripts/convert_spirala.py"
SOURCE_WORKFLOW = ".github/workflows/update_spirala_index.yml"

MAX_DIFF_ENTRIES = 50


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()


def render_html(template, metadata, content):
    html = template
    for key in ["title", "summary", "tags", "date", "hidden"]:
        value = metadata.get(key, "")
        if isinstance(value, list):
            value = ", ".join(value)
        html = html.replace(f"{{{{ {key} }}}}", str(value))
    html = html.replace("{{ content }}", content)
    return html


def convert_md_to_html():
    template = load_template()
    for filename in os.listdir(INPUT_MD_DIR):
        if not filename.endswith(".md"):
            continue

        with open(os.path.join(INPUT_MD_DIR, filename), "r", encoding="utf-8") as f:
            raw = f.read()

        if raw.startswith("---"):
            parts = raw.split("---", 2)
            metadata = yaml.safe_load(parts[1]) or {}
            markdown_content = parts[2].strip()
        else:
            metadata = {}
            markdown_content = raw

        html_content = markdown.markdown(markdown_content)
        rendered = render_html(template, metadata, html_content)

        out_filename = filename.replace(".md", ".html")
        out_path = os.path.join(OUTPUT_HTML_DIR, out_filename)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rendered)


def extract_metadata_from_html(folder):
    entries = []
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".html"):
            continue

        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else filename.replace(".html", "")

        summary_tag = soup.find("meta", attrs={"name": "summary"})
        summary = summary_tag["content"].strip() if summary_tag else ""

        def get_meta(name):
            tag = soup.find("meta", attrs={"name": name})
            return tag["content"].strip() if tag else ""

        tags_raw = get_meta("tags")
        tags = tags_raw.split(", ") if tags_raw else []
        date = get_meta("date")
        hidden = get_meta("hidden").lower() == "true" if get_meta("hidden") else False

        entry = {
            "title": title,
            "summary": summary,
            "tags": tags,
            "date": date,
            "hidden": hidden,
            "file": filename,
        }
        entries.append(entry)

    return entries


def backup_previous_index():
    if os.path.exists(INDEX_PATH):
        shutil.copy2(INDEX_PATH, INDEX_PREV_PATH)


def generate_index_json(entries):
    data = {
        "generated_at": utc_now_iso(),
        "source": {
            "script": SOURCE_SCRIPT,
            "workflow": SOURCE_WORKFLOW,
        },
        "months": [
            {
                "label": "Spirála",
                "folder": FOLDER_NAME,
                "entries": entries,
            }
        ],
    }

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_sitemap(entries):
    url_prefix = "https://fisteque.github.io/symnozein/denik/spirala_vedomi/"
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for entry in entries:
            if not entry["hidden"]:
                url = url_prefix + entry["file"]
                f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write("</urlset>\n")


def load_json(path):
    if not os.path.exists(path):
        return None
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_entries_map(index_data):
    if not index_data:
        return {}
    months = index_data.get("months", [])
    entries = []
    for month in months:
        entries.extend(month.get("entries", []))
    return {entry["file"]: entry for entry in entries}


def compute_diff(prev_index, current_index):
    prev_map = get_entries_map(prev_index)
    curr_map = get_entries_map(current_index)

    prev_files = set(prev_map.keys())
    curr_files = set(curr_map.keys())

    added = sorted(curr_files - prev_files)
    removed = sorted(prev_files - curr_files)

    changed = []
    for file in sorted(curr_files & prev_files):
        prev_item = prev_map[file]
        curr_item = curr_map[file]
        if prev_item != curr_item:
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


def parse_existing_diff_entries(path):
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

    if parts[0].startswith("# spirála diff"):
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
        f"- skript: `{source.get('script', SOURCE_SCRIPT)}`",
        f"- workflow: `{source.get('workflow', SOURCE_WORKFLOW)}`",
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


def write_diff_file(diff, path, max_entries):
    existing_entries = parse_existing_diff_entries(path)
    new_entry = format_diff_entry(diff)

    entries = [new_entry] + existing_entries
    entries = entries[:max_entries]

    lines = [
        "# spirála diff",
        "",
        "Automaticky generovaný přehled posledních změn ve spirále vědomí.",
        f"Uchovává posledních **{max_entries}** záznamů.",
        "",
        "---",
        "",
        "\n\n---\n\n".join(entries),
        "",
    ]

    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))


def main():
    previous_index = load_json(INDEX_PATH)

    convert_md_to_html()
    backup_previous_index()

    entries = extract_metadata_from_html(OUTPUT_HTML_DIR)
    generate_index_json(entries)
    generate_sitemap(entries)

    current_index = load_json(INDEX_PATH)
    diff = compute_diff(previous_index, current_index)
    write_diff_file(diff, DIFF_PATH, MAX_DIFF_ENTRIES)


if __name__ == "__main__":
    main()
