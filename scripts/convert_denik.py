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

TEMPLATE_PATH = "denik/templates/template.html"
INDEX_PATH = "denik/denik_index.json"
SITEMAP_PATH = "denik/sitemap_denik.xml"
FOLDERS = ["25_10", "25_12"]  # přidej další podle potřeby

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

def convert_md_to_html(input_md_dir, output_html_dir):
    template = load_template()
    if not os.path.exists(output_html_dir):
        os.makedirs(output_html_dir)
    for filename in os.listdir(input_md_dir):
        if not filename.endswith(".md"):
            continue
        with open(os.path.join(input_md_dir, filename), 'r', encoding='utf-8') as f:
            raw = f.read()
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
        with open(os.path.join(output_html_dir, out_filename), 'w', encoding='utf-8') as f:
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

def generate_index_json(all_months):
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump({"months": all_months}, f, ensure_ascii=False, indent=2)

def generate_sitemap(all_months):
    with open(SITEMAP_PATH, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for month in all_months:
            folder = month["folder"]
            for entry in month["entries"]:
                if not entry["hidden"]:
                    url = f"https://fisteque.github.io/symnozein/denik/{folder}/{entry['file']}"
                    f.write(f'  <url><loc>{url}</loc></url>\n')
        f.write('</urlset>\n')

def main():
    all_months = []
    for folder in FOLDERS:
        input_md_dir = f"denik/{folder}_md"
        output_html_dir = f"denik/{folder}"
        convert_md_to_html(input_md_dir, output_html_dir)
        entries = extract_metadata_from_html(output_html_dir)

        # Odvodit měsíc a rok z první položky
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

if __name__ == "__main__":
    main()
