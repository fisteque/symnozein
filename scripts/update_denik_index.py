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

        summary = ""
        meta_summary = soup.find("meta", attrs={"name": "summary"})
        if meta_summary and meta_summary.get("content"):
            summary = meta_summary["content"].strip()
        else:
            first_p = soup.select_one(".zaznam p")
            if first_p:
                summary = first_p.text.strip()

        hidden = False
        meta_hidden = soup.find("meta", attrs={"name": "hidden"})
        if meta_hidden and meta_hidden.get("content", "").lower() == "true":
            hidden = True

        tags = []
        meta_tags = soup.find("meta", attrs={"name": "tags"})
        if meta_tags and meta_tags.get("content"):
            tags = [tag.strip() for tag in meta_tags["content"].split(",")]

        meta_date = soup.find("meta", attrs={"name": "date"})
        if meta_date and meta_date.get("content"):
            meta_date_value = meta_date["content"].strip()
            match = re.match(r"(\d{4})-(\d{2})-(\d{2})", meta_date_value)
            if match:
                y, m, d = match.groups()
                return summary, hidden, tags, f"{d}. {m}. {y}", meta_date_value

        # fallback – pokus z title
        title_tag = soup.find("title")
        if title_tag:
            match = re.search(r"(\d{1,2})\.\s?(\d{1,2})\.\s?(20\d\d)", title_tag.text)
            if match:
                d, m, y = match.groups()
                d = d.zfill(2)
                m = m.zfill(2)
                return summary, hidden, tags, f"{d}. {m}. {y}", f"{y}-{m}-{d}"

        return summary, hidden, tags, None, None
    except Exception as e:
        print(f"⚠️ Chyba při čtení {path}: {e}")
        return "", False, [], None, None

for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)
    if not os.path.isdir(folder_path):
        continue

    match_folder = re.match(r"(\d{2})_(\d{2})", folder)
    if not match_folder:
        continue

    year_short, month_num = match_folder.groups()
    year_prefix = "20"
    folder_year = int(year_short)

    label_year = f"{year_prefix}{year_short}"
    label = f"{MONTH_LABELS.get(month_num, 'Neznámý')} {label_year}"

    entries = []

    for file in sorted(os.listdir(folder_path)):
        if not file.endswith(".html") or not file.startswith("Noe_"):
            continue

        match_file = re.match(r"Noe_(\d{2})_(\d{2})_(\d{2})([a-z]*)\.html", file)
        if not match_file:
            print(f"[WARN] Nerozpoznán název souboru: {file}")

