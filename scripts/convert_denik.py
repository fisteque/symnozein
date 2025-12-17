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
    # další období můžeš přidat tady
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

    if lines[0].strip() != '---':
        return {}, ''.join(lines)

    meta_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == '---':
            break
        meta_lines.append(lines[i])
        i += 1

    metadata = yaml.safe_load(''.join(meta_lines))
    content = ''.join(lines[i+1:])
    return metadata, content

def process_period(period_key, template):
    config = PERIODS[period_key]
    input_dir = config['input_dir']
    output_dir = config['output_dir']
    url_prefix = config['url_prefix']

    index_entries = []
    sitemap_urls = []

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(input_dir, filename)
            metadata, content = load_metadata(filepath)

            hidden = metadata.get('hidden', False)
            base_name = os.path.splitext(filename)[0]
            html_filename = base_name + '.html'
            html_url = url_prefix + html_filename

            index_entry = {
                "title": metadata.get("title", base_name),
                "file": html_filename,
                "date": normalize_date(metadata.get("date")),
                "summary": metadata.get("summary", ""),
                "tags": metadata.get("tags", []),
                "hidden": hidden
            }
            index_entries.append(index_entry)

            if not hidden:
                sitemap_urls.append(html_url)

            # Render HTML
            html_body = markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
            final_html = template.replace("{{ content }}", html_body)
            for key, value in metadata.items():
                final_html = final_html.replace(f"{{{{ {key} }}}}", str(value))

            output_path = os.path.join(output_dir, html_filename)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)

    return index_entries, sitemap_urls

def main():
    args = sys.argv[1:]
    selected_periods = list(PERIODS.keys())  # default: all

    if len(args) == 2 and args[0] == "--only":
        if args[1] in PERIODS:
            selected_periods = [args[1]]
        else:
            print(f"Neznámé období: {args[1]}")
            sys.exit(1)

    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        template = f.read()

    all_index = []
    all_urls = []

    for period_key in selected_periods:
        index_entries, urls = process_period(period_key, template)
        all_index.extend(index_entries)
        all_urls.extend(urls)

    # Uložení denik_index.json
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(all_index, f, indent=2, ensure_ascii=False)

    # Uložení sitemap
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in all_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write('</urlset>\n')

if __name__ == "__main__":
    main()
