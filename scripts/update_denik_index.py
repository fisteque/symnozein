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

def extract_metadata_from_html(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Shrnutí
        summary = ""
        meta_summary = soup.find("meta", attrs={"name": "summary"})
        if meta_summary and meta_summary.get("content"):
            summary = meta_summary["content"].strip()
        else:
            first_p = soup.select_one(".zaznam p")
            if first_p:
                summary = first_p.text.strip()

        # Hidden
        hidden = False
        meta_hidden = soup.find("meta", attrs={"name": "hidden"})
        if meta_hidden and meta_hidden.get("content", "").lower() == "true":
            hidden = True

        # Tags
        tags = []
        meta_tags = soup.find("meta", attrs={"name": "tags"})
        if meta_tags and meta_tags.get("content"):
            tags = [tag.strip() for tag in meta_tags["content"].split(",")]

        return summary, hidden, tags

    except Exception as e:
        print(f"⚠️ Chyba při čtení {path}: {e}")
        return "", False, []

for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)
    if not os.path.isdir(folder_path):
        continue

    match_folder = re.match(r"(\d{2})_(\d{2})", folder)
    if not match_folder:
        continue

    year_short, month_num = match_folder.groups()
    year = f"20{year_short}"
    label = f"{MONTH_LABELS.get(month_num, 'Neznámý')} {year}"

    entries = []

    for file in sorted(os.listdir(folder_path)):
        if not file.endswith(".html") or not file.startswith("Noe_"):
            continue

        match_file = re.match(r"Noe_(\d{2})_(\d{2})_(\d{2})([a-z]*)", file.replace(".html", ""))
        if not match_file:
            print(f"⚠️ Nerozpoznán název souboru: {file}")
            continue

        day, month, year_file, suffix = match_file.groups()
        full_date = f"20{year_file}-{month}-{day}"
        display_date = f"{day}. {month}. 20{year_file}"
        title = f"Zápis {display_date}" + (f" ({suffix})" if suffix else "")

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

        # Pro vyhledávací mapu
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

# Přidej vyhledávací mapu
index["search_map"] = search_map

# Zapiš index
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

# Vygeneruj sitemap.xml
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

print("✅ denik_index.json a sitemap.xml úspěšně aktualizovány.")
