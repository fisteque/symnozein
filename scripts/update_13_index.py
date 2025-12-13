# scripts/update_13_index.py

import os
import json
from bs4 import BeautifulSoup
from datetime import datetime

BASE_DIR = "Reinterpretace_13/13"
INDEX_FILE = "Reinterpretace_13/13_index.json"


def extract_metadata_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        title = soup.title.string.strip() if soup.title else "Bez názvu"
        meta = soup.find("meta", attrs={"name": "tags"})
        tags = meta["content"].split(",") if meta and meta.get("content") else []

        meta_description = soup.find("meta", attrs={"name": "description"})
        description = meta_description["content"].strip() if meta_description else ""

        meta_hidden = soup.find("meta", attrs={"name": "hidden"})
        hidden = meta_hidden["content"].strip().lower() == "true" if meta_hidden else False

        # Fallback summary: use first paragraph
        if not description:
            p = soup.find("p")
            if p:
                description = p.get_text().strip()

    return title, tags, description, hidden


def build_index():
    entries = []

    for filename in sorted(os.listdir(BASE_DIR)):
        if filename.endswith(".html"):
            filepath = os.path.join(BASE_DIR, filename)
            title, tags, description, hidden = extract_metadata_from_file(filepath)

            date_str = filename.replace("Noe_", "").replace(".html", "")
            try:
                date_obj = datetime.strptime(date_str, "%d_%m_%y")
                date = date_obj.strftime("%Y-%m-%d")
            except ValueError:
                date = ""

            entries.append({
                "title": title,
                "tags": tags,
                "description": description,
                "file": f"13/{filename}",
                "date": date,
                "hidden": hidden
            })

    # Připojená mapa pojmů a vysvětlení struktury indexu
    metadata_map = {
        "_map": {
            "title": "Název mapitoly",
            "tags": "Seznam štítků (klíčová slova)",
            "description": "Krátké shrnutí nebo první odstavec",
            "file": "Cesta k HTML souboru",
            "date": "Datum ve formátu YYYY-MM-DD",
            "hidden": "True = nebude veřejně vidět, jen pro AI"
        }
    }

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump({"mapitoly": entries, **metadata_map}, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    build_index()
