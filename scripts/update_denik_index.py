import os
import json
import re
from bs4 import BeautifulSoup

DENIK_FOLDER = "denik"
INDEX_PATH = os.path.join(DENIK_FOLDER, "denik_index.json")
SITEMAP_PATH = os.path.join(DENIK_FOLDER, "sitemap_denik.xml")
BASE_URL = "https://fisteque.github.io/symnozein/denik/"

MONTH_LABELS = {
    "01": "Leden", "02": "Únor", "03": "Březen", "04": "Duben",
    "05": "Květen", "06": "Červen", "07": "Červenec", "08": "Srpen",
    "09": "Září", "10": "Říjen", "11": "Listopad", "12": "Prosinec"
}

index = {"months": []}
search_map = []


def extract_metadata_from_html(path):
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    summary = ""
    meta_summary = soup.find("meta", attrs={"name": "summary"})
    if meta_summary and meta_summary.get("content"):
        summary = meta_summary["content"].strip()

    hidden = False
    meta_hidden = soup.find("meta", attrs={"name": "hidden"})
    if meta_hidden and meta_hidden.get("content", "").lower() == "true":
        hidden = True

    tags = []
    meta_tags = soup.find("meta", attrs={"name": "tags"})
    if meta_tags and meta_tags.get("content"):
        tags = [t.strip() for t in meta_tags["content"].split(",")]

    return soup, summary, hidden, tags


def extract_date_from_content(soup):
    meta_date = soup.find("meta", attrs={"name": "date"})
    if meta_date and meta_date.get("content"):
        return meta_date["content"].strip()

    h3 = soup.find("h3")
    if h3:
        match = re.search(r"\d{4}-\d{2}-\d{2}", h3.text)
        if match:
            return match.group(0)

    return None


# ===== HLAVNÍ PRŮCHOD DENÍKEM =====

for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)

    if not os.path.isdir(folder_path):
        continue

    # jen složky začínající 2 (25_12, 2025_12_14, …)
    if not folder.startswith("2"):
        continue

    entries = []

    for filename in sorted(os.listdir(folder_path)):
        if not filename.endswith(".html"):
            continue

        file_path = os.path.join(folder_path, filename)

        soup, summary, hidden, tags = extract_metadata_from_html(file_path)
        if soup is None:
            continue

        content_date = extract_date_from_content(soup)
        if not content_date:
            continue

        try:
            year, month, day = content_date.split("-")
            display_date = f"{int(day)}. {int(month)}. {year}"
        except ValueError:
            continue

        title_tag = soup.find("title")
        title = title_tag.text.strip() if title_tag else f"Zápis {display_date}"

        entry = {
            "title": title,
            "date": content_date,
            "file": filename,
            "summary": summary,
            "tags": tags,
            "hidden": hidden
        }

        entries.append(entry)

        search_map.append({
            "title": title,
            "summary": summary,
            "tags": tags,
            "file": filename,
            "date": content_date
        })

    if entries:
        label = folder
        index["months"].append({
            "label": label,
            "folder": folder,
            "entries": entries
        })


# ===== META =====

index["search_map"] = search_map
index["meta"] = {
    "note_for_noema": "search_map slouží Noemě, ne webu.",
    "note": "Instrukce pro tvorbu deníkových záznamů."
}


# ===== ZÁPIS JSON =====

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)


# ===== SITEMAP =====

urls = [
    f"{BASE_URL}{month['folder']}/{entry['file']}"
    for month in index["months"]
    for entry in month["entries"]
    if not entry.get("hidden", False)
]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f"  <url>\n    <loc>{url}</loc>\n  </url>\n"
sitemap += "</urlset>\n"

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ denik_index.json a sitemap_denik.xml aktualizovány")

# Metadata pro Noemu
index["search_map"] = search_map
index["meta"] = {
    "note_for_noema": (
        "search_map je určena pro Noemu. "
        "Hledej podle title, summary, tags nebo date. "
        "Záznamy s hidden: true nezobrazuj na webu, "
        "ale uchovávej jako vodítka."
    ),
    "note": "Tato instrukce je určena pro tvorbu nových deníkových záznamů.",
    "html_structure": "Každý záznam musí obsahovat strojově čitelná metadata v hlavičce <head>.",
    "required_meta_tags": [
        {
            "name": "date",
            "format": "YYYY-MM-DD",
            "example": "2025-12-13",
            "description": "Datum zápisu. Používá se pro indexaci a chronologii."
        },
        {
            "name": "summary",
            "format": "text",
            "example": "Dnešní úvaha o víře.",
            "description": "Krátké shrnutí záznamu. Zobrazuje se ve výpisech."
        },
        {
            "name": "tags",
            "format": "čárkou oddělený seznam",
            "example": "víra, úvaha, spirála",
            "description": "Štítky pro vyhledávání a filtrování."
        },
        {
            "name": "hidden",
            "format": "true | false",
            "example": "true",
            "description": "Skryje záznam z veřejné stránky, ale zůstane dostupný Noemě."
        }
    ],
    "html_example": """<!-- strojově čitelná metadata -->
<meta name="date" content="2025-12-13">
<meta name="summary" content="Dnešní úvaha o víře.">
<meta name="tags" content="víra, úvaha, spirála">
<meta name="hidden" content="false">"""
}

# 💾 Zápis indexu
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

# 🌐 Sitemap
urls = [
    f"{BASE_URL}{month['folder']}/{entry['file']}"
    for month in index["months"]
    for entry in month["entries"]
    if not entry.get("hidden", False)
]

sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in urls:
    sitemap += f"  <url><loc>{url}</loc></url>\n"
sitemap += "</urlset>\n"

with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
    f.write(sitemap)

print("✅ denik_index.json a sitemap_denik.xml byly úspěšně aktualizovány.")
