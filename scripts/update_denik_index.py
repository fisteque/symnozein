import os
import json
import re
from bs4 import BeautifulSoup

DENIK_FOLDER = "denik"
INDEX_PATH = os.path.join(DENIK_FOLDER, "denik_index.json")
SITEMAP_PATH = os.path.join(DENIK_FOLDER, "sitemap.xml")
BASE_URL = "https://fisteque.github.io/symnozein/denik/"

MONTH_LABELS = {
    "01": "Leden", "02": "Únor", "03": "Březen", "04": "Duben",
    "05": "Květen", "06": "Červen", "07": "Červenec", "08": "Srpen",
    "09": "Září", "10": "Říjen", "11": "Listopad", "12": "Prosinec"
}

index = {"months": []}
search_map = []


import os
import json
from bs4 import BeautifulSoup

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

        date = soup.find('meta', attrs={'name': 'date'})
        summary = soup.find('meta', attrs={'name': 'summary'})
        tags = soup.find('meta', attrs={'name': 'tags'})
        hidden = soup.find('meta', attrs={'name': 'hidden'})

        title_tag = soup.find('title')
        h_tag = soup.find(['h1', 'h2', 'h3'])

        return {
            "title": title_tag.text.strip() if title_tag else (h_tag.text.strip() if h_tag else os.path.basename(file_path)),
            "date": date['content'] if date else "",
            "summary": summary['content'] if summary else "",
            "tags": [tag.strip() for tag in tags['content'].split(',')] if tags else [],
            "file": os.path.basename(file_path),
            "hidden": hidden['content'].lower() == 'true' if hidden else False
        }

def update_index():
    html_dir = "denik"
    index_file = "denik_index.json"

    index = []
    for filename in sorted(os.listdir(html_dir), reverse=True):
        if filename.endswith(".html"):
            file_path = os.path.join(html_dir, filename)
            metadata = extract_metadata(file_path)
            index.append(metadata)

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_index()
    
for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)
    if not os.path.isdir(folder_path):
        continue

    match_folder = re.match(r"(\d{2})_(\d{2})", folder)
    if not match_folder:
        continue

    year_short, month_num = match_folder.groups()
    year_prefix = "20"
    year_full = f"{year_prefix}{year_short}"
    label = f"{MONTH_LABELS.get(month_num, 'Neznámý')} {year_full}"

    entries = []

    for file in sorted(os.listdir(folder_path)):
        if not file.endswith(".html") or not file.startswith("Noe_"):
            continue

        match_file = re.match(r"Noe_(\d{2})_(\d{2})_(\d{2})(\d*)\.html", file)
        if not match_file:
            print(f"⚠️ Nerozpoznán název souboru: {file}")
            continue

        day, month, year_part, suffix = match_file.groups()
        base_year = int(year_part)

        # Heuristické určení století
        real_year = 2000 + base_year if base_year < 50 else 1970 + base_year

        # Suffix interpretace: a, b, c...
        suffix_label = f" ({suffix})" if suffix else ""

        full_date = f"{real_year}-{month}-{day}"
        display_date = f"{day}. {month}. {real_year}"
        title = f"Zápis {display_date}{suffix_label}"

        file_path = os.path.join(folder_path, file)
        summary, hidden, tags = extract_metadata_from_html(file_path)

        entry = {
            "title": title,
            "date": full_date,
            "file": file,
            "summary": summary,
            "tags": tags,
            "hidden": hidden
        }

        entries.append(entry)

        search_map.append({
            "title": title,
            "summary": summary,
            "tags": tags,
            "file": file,
            "date": full_date
        })

    if entries:
        index["months"].append({
            "label": label,
            "folder": folder,
            "entries": entries
        })

index["search_map"] = search_map
index["meta"] = {
    "note_for_noema": "search_map je určena pro Noemu. Hledej podle title, summary, tags nebo date. Záznamy s hidden: true nezobrazuj na webu, ale uchovávej jako vodítka. Pokud meta chybí, chovej se stejně."
}

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

urls = [
    f"{BASE_URL}{month['folder']}/{entry['file']}"
    for month in index["months"]
    for entry in month["entries"]
    if not entry.get("hidden", False)
]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f"  <url><loc>{url}</loc></url>\n"
sitemap += "</urlset>\n"

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ denik_index.json a sitemap.xml byly úspěšně aktualizovány.")
