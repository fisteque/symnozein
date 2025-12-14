import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

SPIRALA_DIR = "denik/spirala_vedomi"
INDEX_FILE = "denik/spirala_index.json"
SITEMAP_FILE = "denik/sitemap_spirala.xml"
BASE_URL = "https://fisteque.github.io/symnozein/denik/spirala_vedomi/"

def extract_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        title = soup.title.string.strip() if soup.title else "(Bez názvu)"

        meta_summary = soup.find("meta", attrs={"name": "summary"})
        summary = meta_summary["content"].strip() if meta_summary else ""

        meta_tags = soup.find("meta", attrs={"name": "tags"})
        tags = [t.strip() for t in meta_tags["content"].split(",")] if meta_tags else []

        meta_date = soup.find("meta", attrs={"name": "date"})
        date = meta_date["content"].strip() if meta_date else ""

        meta_hidden = soup.find("meta", attrs={"name": "hidden"})
        hidden = meta_hidden["content"].lower() == "true" if meta_hidden else False

        return {
            "title": title,
            "summary": summary,
            "tags": tags,
            "date": date,
            "file": os.path.relpath(filepath, "denik").replace("\\", "/"),
            "hidden": hidden
        }

def update_index_and_sitemap():
    index = []
    urls = []

    for root, _, files in os.walk(SPIRALA_DIR):
        for name in files:
            if name.endswith(".html"):
                filepath = os.path.join(root, name)
                entry = extract_metadata(filepath)
                index.append(entry)

                if not entry["hidden"]:
                    urls.append(BASE_URL + os.path.basename(filepath))

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

    indent_xml(urlset)

    tree = ElementTree(urlset)
    with open(SITEMAP_FILE, "wb") as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding="utf-8", xml_declaration=False)

def indent_xml(elem, level=0):
    """Zajišťuje čitelné odsazení XML výstupu"""
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent_xml(child, level + 1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i

if __name__ == "__main__":
    print("🌀 Generuji spirala_index.json a sitemap_spirala.xml...")
    update_index_and_sitemap()
    print("✅ Hotovo.")
