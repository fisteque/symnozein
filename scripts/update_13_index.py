import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

MAPITOLA_DIR = "Reinterpretace_13/13"
INDEX_FILE = "Reinterpretace_13/13_index.json"
SITEMAP_FILE = "Reinterpretace_13/sitemap.xml"
BASE_URL = "https://fisteque.github.io/symnozein/Reinterpretace_13/"


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


def update_index_and_sitemap():
    index = []
    urls = []

    for root, _, files in os.walk(MAPITOLA_DIR):
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                entry = extract_metadata(filepath)
                index.append(entry)

                if not entry["hidden"]:
                    urls.append(BASE_URL + entry["file"])

    index.sort(key=lambda x: x.get("date", ""), reverse=True)

    with open(INDEX_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False, indent=2)

    generate_sitemap(urls)


def generate_sitemap(urls):
    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_el = SubElement(urlset, "url")
        loc_el = SubElement(url_el, "loc")
        loc_el.text = url

    tree = ElementTree(urlset)
    with open(SITEMAP_FILE, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding="utf-8", xml_declaration=False)


if __name__ == "__main__":
    print("📘 Generuji 13_index.json a sitemap.xml...")
    update_index_and_sitemap()
    print("✅ Hotovo.")
