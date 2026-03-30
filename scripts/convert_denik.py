import datetime
import json
import os
import re
import shutil
from datetime import timezone

import markdown
import yaml
from bs4 import BeautifulSoup

CZECH_MONTHS = {
    "01": "leden", "02": "únor", "03": "březen", "04": "duben",
    "05": "květen", "06": "červen", "07": "červenec", "08": "srpen",
    "09": "září", "10": "říjen", "11": "listopad", "12": "prosinec"
}

TEMPLATE_PATH = "denik/templates/template.html"
INDEX_PATH = "denik/denik_index.json"
INDEX_PREV_PATH = "denik/denik_index_prev.json"
DIFF_PATH = "denik/denik_diff.md"
SITEMAP_PATH = "denik/sitemap_denik.xml"
DENIK_DIR = "denik"

SOURCE_SCRIPT = "scripts/convert_denik.py"
SOURCE_WORKFLOW = ".github/workflows/update_denik_index.yml"
MAX_DIFF_ENTRIES = 50


def utc_now_iso() -> str:
    return datetime.datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def discover_month_folders():
    month_folders = []
    pattern = re.compile(r"^\d{2}_\d{2}_md$")

    if not os.path.exists(DENIK_DIR):
        return month_folders

    for name in os.listdir(DENIK_DIR):
        full_path = os.path.join(DENIK_DIR, name)
        if os.path.isdir(full_path) and pattern.match(name):
            month_folders.append(name[:-3])

    return sorted(month_folders)


FOLDERS = discover_month_folders()


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


def convert_md_to_html(input_md_dir, output_html_dir):
    template = load_template()

    if not os.path.exists(input_md_dir):
        print(f"Přeskakuji neexistující vstupní složku: {input_md_dir}")
        return

    if not os.path.exists(output_html_dir):
        os.makedirs(output_html_dir)

    for filename in os.listdir(input_md_dir):
        if not filename.endswith(".md"):
            continue

        with open(os.path.join(input_md_dir, filename), "r", encoding="utf-8") as f:
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
        with open(os.path.join(output_html_dir, out_filename), "w", encoding="utf-8") as f:
            f.write(rendered)


def extract_metadata_from_html(folder):
    entries = []

    if not os.path.exists(folder):
        return entries

    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".html"):
            continue

        filepath = os.path.join(folder, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        def get_meta(name):
            tag = soup.find("meta", attrs={"name": name})
            return tag["content"] if tag else ""

        date_str = get_meta("date")
        title = get_meta("title")

        if not title and date_str:
            try:
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                day = dt.day
                month = CZECH_MONTHS[date_str[5:7]]
                title = f"{day}. {month} {dt.year}"
            except Exception:
                title = ""

        entry = {
            "title": title,
            "summary": get_meta("summary"),
            "tags": get_meta("tags").split(", ") if get_meta("tags") else [],
            "date": date_str,
            "hidden": get_meta("hidden").strip().lower() == "true",
            "file": filename
        }
        entries.append(entry)

    return entries


def backup_previous_index():
    if os.path.exists(INDEX_PATH):
        shutil.copy2(INDEX_PATH, INDEX_PREV_PATH)


def generate_index_json(all_months):
    data = {
        "generated_at": utc_now_iso(),
        "source": {
            "script": SOURCE_SCRIPT,
            "workflow": SOURCE_WORKFLOW,
        },
        "months": all_months
    }

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def generate_sitemap(all_months):
    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for month in all_months:
            folder = month["folder"]
            for entry in month["entries"]:
                if not entry["hidden"]:
                    url = f"https://fisteque.github.io/symnozein/denik/{folder}/{entry['file']}"
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

    result = {}
    for month in index_data.get("months", []):
        for entry in month.get("entries", []):
            result[entry["file"]] = entry
    return result


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

    if parts[0].startswith("# deník diff"):
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
        "# deník diff",
        "",
        "Automaticky generovaný přehled posledních změn v deníku.",
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

    for folder in FOLDERS:
        input_md_dir = f"denik/{folder}_md"
        output_html_dir = f"denik/{folder}"
        convert_md_to_html(input_md_dir, output_html_dir)

    backup_previous_index()

    all_months = []

    if not FOLDERS:
        print("Nenalezeny žádné deníkové složky ve formátu YY_MM_md.")

    for folder in FOLDERS:
        output_html_dir = f"denik/{folder}"
        entries = extract_metadata_from_html(output_html_dir)

        if entries and entries[0]["date"]:
            try:
                dt = datetime.datetime.strptime(entries[0]["date"], "%Y-%m-%d")
                month_label = f"{CZECH_MONTHS[entries[0]['date'][5:7]].capitalize()} {dt.year}"
            except Exception:
                month_label = folder
        else:
            month_label = folder

        all_months.append({
            "label": month_label,
            "folder": folder,
            "entries": entries
        })

    generate_index_json(all_months)
    generate_sitemap(all_months)

    current_index = load_json(INDEX_PATH)
    diff = compute_diff(previous_index, current_index)
    write_diff_file(diff, DIFF_PATH, MAX_DIFF_ENTRIES)


if __name__ == "__main__":
    main()
