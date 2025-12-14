import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

# Cesty
spirala_folder = "denik/.spirala_vedomi"
index_file = "denik/spirala_index.json"
sitemap_file = "denik/sitemap_spirala.xml"
base_url = "https://fisteque.github.io/symnozein/denik/.spirala_vedomi/"

# Sběr dat
index = []
for filename in sorted(os.listdir(spirala_folder)):
    if filename.endswith(".html"):
        path = os.path.join(spirala_folder, filename)
        with open(path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        def get(name):
            tag = soup.find("meta", attrs={"name": name})
            return tag["content"].strip() if tag else ""

        meta = {
            "filename": filename,
            "date": get("date"),
            "summary": get("summary"),
            "tags": [t.strip() for t in get("tags").split(",")] if get("tags") else [],
            "hidden": get("hidden").lower() == "true"
        }
        index.append(meta)

# Uložení spirala_index.json
with open(index_file, "w", encoding="utf-8") as f:
    json.dump(index, f, indent=2, ensure_ascii=False)

# Generování sitemap_spirala.xml
urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

for entry in index:
    if not entry["hidden"]:
        url = SubElement(urlset, "url")
        SubElement(url, "loc").text = base_url + entry["filename"]
        if entry["date"]:
            SubElement(url, "lastmod").text = entry["date"]

# Uložení XML
ElementTree(urlset).write(sitemap_file, encoding="utf-8", xml_declaration=True)
