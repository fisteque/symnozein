import os
import sys
import markdown
import yaml
from datetime import datetime, date as date_type
import json

TEMPLATE_PATH = "denik/templates/template.html"
INDEX_PATH = "denik/denik_index.json"
SITEMAP_PATH = "denik/sitemap_denik.xml"
URL_ROOT = "https://fisteque.github.io/symnozein/denik/"

PERIODS = {
    "25_12": {
        "input_dir": "denik/25_12_md",
        "output_dir": "denik/25_12",
        "url_prefix": URL_ROOT + "25_12/"
    },
    "26_01": {
        "input_dir": "denik/26_01_md",
        "output_dir": "denik/26_01",
        "url_prefix": URL_ROOT + "26_01/"
    }
}

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
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    if not lines or lines[0].strip() != '---':
        return {}, ''.join(lines)
    meta_lines, i = [], 1
    while i < len(lines) and lines[i].strip() != '---':
        meta_lines.append(lines[i])
        i += 1
    metadata = yaml.safe_load(''.join(meta_lines))
    content = ''.join(lines[i+1:])
    return metadata or {}, content

def find_metadata_for_html(html_filename, input_dir):
    base_name = os.path.splitext(html_filename)[0]
    md_path = os.path.join(input_dir, base_name + ".md")
    if os.path.exists(md_path):
        metadata, _ = load_metadata(md_path)
        return metadata
    else:
        return {
            "title": base_name,
            "summary": "",
            "tags": [],
            "date": "",
            "hidden": False
        }

def process_period(period_key):
    config = PERIODS[period_key]
    input_dir = config['input_dir']
    output_dir = config['output_dir']
    url_prefix = config['url_prefix']

    index_entries = []
    sitemap_urls = []

    if not os.path.exists(output_dir):
        print(f"Složka neexistuje: {output_dir}")
        return [], []

    for filename in os.listdir(output_dir):
        if not filename.endswith(".html"):
            continue

        metadata = find_metadata_for_html(filename, input_dir)
        hidden = metadata.get("hidden", False)
        html_url = url_prefix + filename

        index_entry = {
            "title": metadata.get("title", filename),
            "file": filename,
            "date": normalize_date(metadata.get("date")),
            "summary": metadata.get("summary", ""),
            "tags": metadata.get("tags", []),
            "hidden": hidden
        }
        index_entries.append(index_entry)

        if not hidden:
            sitemap_urls.append(html_url)

    return index_entries, sitemap_urls

def main():
    args = sys.argv[1:]
    selected_periods = list(PERIODS.keys())

    if len(args) == 2 and args[0] == "--only":
        if args[1] in PERIODS:
            selected_periods = [args[1]]
        else:
            print(f"Neznámé období: {args[1]}")
            sys.exit(1)

    all_index = []
    all_urls = []

    for period_key in selected_periods:
        index_entries, urls = process_period(period_key)
        all_index.extend(index_entries)
        all_urls.extend(urls)

    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_index, f, indent=2, ensure_ascii=False)

    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in all_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write('</urlset>\n')

if __name__ == "__main__":
    main()
