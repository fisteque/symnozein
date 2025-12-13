import os
import json
from bs4 import BeautifulSoup
from datetime import datetime

MAPITOL_DIR = "Reinterpretace_13/13"
INDEX_FILE = "Reinterpretace_13/13_index.json"


def extract_metadata(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    title_tag = soup.find("title")
    title = title_tag.text.strip() if title_tag else os.path.basename(file_path)

    meta_desc = soup.find("meta", attrs={"name": "description"})
    if meta_desc and meta_desc.get("content"):
        summary = meta_desc["content"].strip()
    else:
        first_p = soup.find("p")
        summary = first_p.text.strip() if first_p else ""

    tags = []
    tag_meta = soup.find("meta", attrs={"name": "tags"})
    if tag_meta and tag_meta.get("content"):
        tags = [tag.strip() for tag in tag_meta["content"].split(",")]

    hidden = False
    hidden_meta = soup.find("meta", attrs={"name": "hidden"})
    if hidden_meta and hidden_meta.get("content", "").lower() == "true":
        hidden = True

    return {
        "title": title,
        "summary": summary,
        "tags": tags,
        "file": file_path.replace("\\", "/"),
        "date": extract_date_from_filename(file_path),
        "hidden": hidden
    }


def extract_date_from_filename(file_path):
    base = os.path.basename(file_path)
    try:
        parts = base.replace(".html", "").split("_")
        return f"{parts[1]}.{parts[2]}.20{parts[3]}"
    except:
        return ""


def build_index():
    index = []
    for fname in sorted(os.listdir(MAPITOL_DIR)):
        if fname.endswith(".html"):
            path = os.path.join(MAPITOL_DIR, fname)
            entry = extract_metadata(path)
            index.append(entry)

    index.append({
        "_map": {
            "title": "Název mapitoly",
            "summary": "Automaticky získané shrnutí",
            "tags": "Štítky pro vyhledávání",
            "file": "Cesta k HTML souboru",
            "date": "Datum vytvoření z názvu souboru",
            "hidden": "true/false – zda se má mapa zobrazit na webu"
        }
    })

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    build_index()
