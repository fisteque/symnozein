import os
import json
from bs4 import BeautifulSoup
from datetime import datetime

INPUT_DIR = "Reinterpretace_13/13"
INDEX_FILE = "Reinterpretace_13/13_index.json"

def extract_metadata_from_html(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    def get_meta(name):
        tag = soup.find("meta", attrs={"name": name})
        return tag["content"].strip() if tag and tag.get("content") else ""

    title = soup.title.string.strip() if soup.title else os.path.basename(filepath)
    date = get_meta("date")
    tags = get_meta("tags").split(",") if get_meta("tags") else []
    summary = get_meta("summary") or ""
    hidden = get_meta("hidden").lower() == "true" if get_meta("hidden") else False

    return {
        "title": title,
        "date": date,
        "file": filepath.replace("\\", "/"),
        "tags": [t.strip() for t in tags if t.strip()],
        "summary": summary,
        "hidden": hidden
    }

def load_existing_index():
    if os.path.exists(INDEX_FILE):
        with open(INDEX_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_index(index_data):
    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index_data, f, ensure_ascii=False, indent=2)

def update_index():
    existing_index = load_existing_index()
    existing_files = {entry["file"]: entry for entry in existing_index}

    updated_index = []
    for filename in sorted(os.listdir(INPUT_DIR)):
        if not filename.endswith(".html"):
            continue

        filepath = os.path.join(INPUT_DIR, filename)
        metadata = extract_metadata_from_html(filepath)

        existing_files[metadata["file"]] = metadata

    updated_index = list(existing_files.values())
    updated_index.sort(key=lambda x: x["date"], reverse=True)

    save_index(updated_index)

if __name__ == "__main__":
    update_index()
