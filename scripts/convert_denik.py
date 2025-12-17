import os
import markdown
import yaml
import json
from bs4 import BeautifulSoup
import datetime

CZECH_MONTHS = {
    "01": "ledna", "02": "února", "03": "března", "04": "dubna",
    "05": "května", "06": "června", "07": "července", "08": "srpna",
    "09": "září", "10": "října", "11": "listopadu", "12": "prosince"
}

INPUT_MD_DIR = "denik/25_12_md"
OUTPUT_HTML_DIR = "denik/25_12"
TEMPLATE_PATH = "denik/templates/template.html"
INDEX_PATH = "denik/denik_index.json"
SITEMAP_PATH = "denik/sitemap_denik.xml"
FOLDER_NAME = "25_12"

def load_template():
    with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
        return f.read()

def render_html(template, metadata, content):
    html = template
    for key in ['title', 'summary', 'tags', 'date', 'hidden']:
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
        with open(os.path.join(INPUT_MD_DIR, filename), 'r', encoding='utf-8') as f:
            raw = f.read()

        # Rozdělit YAML + obsah
        if raw.startswith('---'):
            parts = raw.split('---', 2)
            metadata = yaml.safe_load(parts[1])
            markdown_content = parts[2].strip()
        else:
            metadata = {}
            markdown_content = raw

        html_content = markdown.markdown(markdown_content)
        rendered = render_html(template, metadata, html_content)

        out_filename = filename.replace('.md', '.html')
        out_path = os.path.join(OUTPUT_HTML_DIR, out_filename)
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(rendered)


def extract_metadata_from_html(folder):
    entries = []
    for filename in sorted(os.listdir(folder)):
        if not filename.endswith(".html"):
            continue
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            soup = BeautifulSoup(f, "html.parser")

        def get_meta(name):
            tag = soup.find("meta", attrs={"name": name})
            return tag["content"] if tag else ""

        date_str = get_meta("date")
        title = get_meta("title")

        # Pokud title chybí, vygeneruj z datumu
        if not title and date_str:
            try:
                dt = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                day = dt.day
                month = CZECH_MONTHS[date_str[5:7]]
                title = f"{day}. {month} {dt.year}"
            except Exception:
                title = ""  # fallback pokud selže

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

def generate_index_json(entries):
    months = [{
        "label": "Prosinec 2025",
        "folder": FOLDER_NAME,
        "entries": entries
    }]
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump({"months": months}, f, ensure_ascii=False, indent=2)

def generate_sitemap(entries):
    url_prefix = "https://fisteque.github.io/symnozein/denik/25_12/"
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for entry in entries:
            if not entry["hidden"]:
                url = url_prefix + entry["file"]
                f.write(f'  <url><loc>{url}</loc></url>\n')
        f.write('</urlset>\n')

def main():
    convert_md_to_html()
    entries = extract_metadata_from_html(OUTPUT_HTML_DIR)
    generate_index_json(entries)
    generate_sitemap(entries)

if __name__ == "__main__":
    main()
