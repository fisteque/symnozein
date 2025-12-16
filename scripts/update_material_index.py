import os
import json
import datetime
import yaml
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
import xml.dom.minidom as minidom

# Cesty
md_dir = Path("Reinterpretace_13/material/")
index_file = Path("Reinterpretace_13/material_index.json")
sitemap_file = Path("Reinterpretace_13/sitemap_material.xml")

# Výchozí URL
base_url = "https://fisteque.github.io/symnozein/Reinterpretace_13/material/"

entries = []

# Získání metadat ze souborů
for file in md_dir.glob("*.md"):
    with open(file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines and lines[0].strip() == "---":
        try:
            end_idx = lines[1:].index("---\n") + 1
        except ValueError:
            continue  # Přeskoč, pokud není konec YAML
        yaml_text = ''.join(lines[1:end_idx])
        metadata = yaml.safe_load(yaml_text)

        if metadata:
            if "date" in metadata and isinstance(metadata["date"], datetime.date):
                metadata["date"] = metadata["date"].isoformat()

            metadata["file"] = file.name
            entries.append(metadata)

# Řazení dle data
entries.sort(key=lambda x: x.get("date", ""), reverse=True)

# Zápis do JSON
with open(index_file, "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2, ensure_ascii=False)

# Vytvoření XML stromu pro sitemap
urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
for entry in entries:
    if not entry.get("hidden", False):
        url = SubElement(urlset, "url")
        loc = SubElement(url, "loc")
        loc.text = base_url + entry["file"]

# Pretty print
xml_str = tostring(urlset, encoding="utf-8")
parsed = minidom.parseString(xml_str)
pretty_xml_as_string = parsed.toprettyxml(indent="  ", encoding="utf-8")

# Zápis do sitemap_material.xml
with open(sitemap_file, "wb") as f:
    f.write(pretty_xml_as_string)

print(f"Aktualizováno: {index_file} a {sitemap_file}")
