import os
import json
from bs4 import BeautifulSoup
from datetime import datetime

MAPITOLA_DIR = "Reinterpretace_13/13"
INDEX_FILE = "Reinterpretace_13/13_index.json"


def extract_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        title = soup.title.string.strip() if soup.title else "(Bez názvu)"

        meta_description = soup.find("meta", attrs={"name": "description"})
        description = meta_description["content"].strip() if meta_description else ""

        meta_tags = soup.find("meta", attrs={"name": "tags"})
        tags = [t.strip() for t in meta_tags["content"].split(",")] if meta_tags else []

        meta_date = soup.find("meta", attrs={"name": "date"})
        date = meta_date["content"].strip() if meta_date else ""

        meta_hidden = soup.find("meta", attrs={"name": "hidden"})
        hidden = meta_hidden["content"].lower() == "true" if meta_hidden else False

        return {
            "title": title,
            "description": description,
            "tags": tags,
            "date": date,
            "file": os.path.relpath(filepath, "Reinterpretace_13").replace("\\", "/"),
            "hidden": hidden
        }


def load_existing_index():
    if os.path.exists(INDEX_FILE) and os.path.getsize(INDEX_FILE) > 0:
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def update_index():
    index = []
    for root, _, files in os.walk(MAPITOLA_DIR):
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                entry = extract_metadata(filepath)
                index.append(entry)

    index.sort(key=lambda x: x.get("date", ""), reverse=True)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    update_index()
