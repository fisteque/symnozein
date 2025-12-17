import os
import yaml
import json
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

INPUT_DIR = "Reinterpretace_13/material"
INDEX_PATH = "Reinterpretace_13/material_index.json"
SITEMAP_PATH = "Reinterpretace_13/sitemap_material.xml"
URL_PREFIX = "https://fisteque.github.io/symnozein/Reinterpretace_13/material/"

def parse_metadata(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if lines[0].strip() != "---":
        return {}, "".join(lines)

    yaml_lines = []
    for line in lines[1:]:
        if line.strip() == "---":
            break
        yaml_lines.append(line)

    try:
        metadata = yaml.safe_load("".join(yaml_lines)) or {}
    except yaml.YAMLError:
        metadata = {}

    return metadata, "".join(lines)

def build_index():
    entries = []

    for filename in os.listdir(INPUT_DIR):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(INPUT_DIR, filename)
        metadata, content = parse_metadata(filepath)

        title = metadata.get("title", filename)
        summary = metadata.get("summary", "")
        tags = metadata.get("tags", [])
        date = metadata.get("date", "")
        hidden = metadata.get("hidden", False)

        entries.append({
            "file": filename,
            "title": title,
            "summary": summary,
            "tags": tags,
            "date": date,
            "hidden": hidden
        })

    entries.sort(key=lambda x: x["date"], reverse=True)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)

    print(f"Index uložen do {INDEX_PATH}")
    return entries

def build_sitemap(entries):
    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for entry in entries:
        if entry.get("hidden"):
            continue

        url = SubElement(urlset, "url")
        loc = SubElement(url, "loc")
        loc.text = URL_PREFIX + entry["file"]

        if entry.get("date"):
            lastmod = SubElement(url, "lastmod")
            try:
                d = datetime.strptime(entry["date"], "%Y-%m-%d")
                lastmod.text = d.date().isoformat()
            except ValueError:
                pass  # ignore malformed dates

    raw_xml = tostring(urlset, encoding="utf-8")
    pretty_xml = minidom.parseString(raw_xml).toprettyxml(indent="  ")

    with open(SITEMAP_PATH, "w", encoding="utf-8") as f:
        f.write(pretty_xml)

    print(f"Sitemap uložena do {SITEMAP_PATH}")

if __name__ == "__main__":
    entries = build_index()
    build_sitemap(entries)
