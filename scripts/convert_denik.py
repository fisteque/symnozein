import os
import markdown
import yaml
import json
from datetime import datetime, date as date_type

# Cílové složky deníku
TARGETS = {
    "25_12": {
        "input_dir": "denik/25_12_md",
        "output_dir": "denik/25_12",
        "template_path": "denik/templates/template.html",
    },
    "26_01": {
        "input_dir": "denik/26_01_md",
        "output_dir": "denik/26_01",
        "template_path": "denik/templates/template.html",
    }
}

INDEX_PATH = "denik_index.json"
SITEMAP_PATH = "sitemap_denik.xml"
URL_PREFIX = "https://fisteque.github.io/symnozein/denik"

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

def main():
    index_entries = []
    sitemap_urls = []

    for period_key, config in TARGETS.items():
        input_dir = config["input_dir"]
        output_dir = config["output_dir"]
        template = ""

        if os.path.exists(config["template_path"]):
            with open(config["template_path"], 'r', encoding='utf-8') as f:
                template = f.read()

        os.makedirs(output_dir, exist_ok=True)

        # 1. PŘEVOD .md → .html
        for filename in os.listdir(input_dir):
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(input_dir, filename)
            metadata, content = load_metadata(filepath)

            base_name = os.path.splitext(filename)[0]
            html_filename = base_name + ".html"
            output_path = os.path.join(output_dir, html_filename)
            url = f"{URL_PREFIX}/{period_key}/{html_filename}"
            hidden = metadata.get("hidden", False)

            # HTML render
            html_body = markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
            final_html = template.replace("{{ content }}", html_body)
            for key, value in metadata.items():
                final_html = final_html.replace(f"{{{{ {key} }}}}", str(value))

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)

        # 2. PRŮCHOD CELÉ .html SLOŽKY → zápis do indexu/sitemap
        for filename in os.listdir(output_dir):
            if not filename.endswith('.html'):
                continue

            filepath = os.path.join(output_dir, filename)
            url = f"{URL_PREFIX}/{period_key}/{filename}"
            hidden = False
            metadata = {
                "title": os.path.splitext(filename)[0],
                "summary": "",
                "tags": [],
                "date": "",
            }

            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if '<meta name="title"' in line:
                        metadata["title"] = line.split('content="')[1].split('"')[0]
                    elif '<meta name="summary"' in line:
                        metadata["summary"] = line.split('content="')[1].split('"')[0]
                    elif '<meta name="tags"' in line:
                        raw = line.split('content="')[1].split('"')[0]
                        metadata["tags"] = [tag.strip() for tag in raw.split(',')]
                    elif '<meta name="date"' in line:
                        metadata["date"] = line.split('content="')[1].split('"')[0]
                    elif '<meta name="hidden"' in line:
                        value = line.split('content="')[1].split('"')[0].lower()
                        hidden = value == "true"

            index_entries.append({
                "title": metadata["title"],
                "file": filename,
                "date": normalize_date(metadata["date"]),
                "summary": metadata["summary"],
                "tags": metadata["tags"],
                "hidden": hidden,
                "folder": period_key
            })

            if not hidden:
                sitemap_urls.append(url)

    # Zápis JSON indexu
    with open(INDEX_PATH, 'w', encoding='utf-8') as f:
        json.dump(index_entries, f, indent=2, ensure_ascii=False)

    # Zápis sitemap
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write('</urlset>\n')

if __name__ == "__main__":
    main()
