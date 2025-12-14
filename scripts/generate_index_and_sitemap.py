import json
from pathlib import Path
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree

# Cesty ke vstupním souborům
DENIK_INDEX = Path("denik/denik_index.json")
REINT_INDEX = Path("Reinterpretace_13/13_index.json")
README_PATH = Path("README_cz.html")

# Výstupy
INDEX_HTML = Path("index.html")
SITEMAP_XML = Path("sitemap.xml")

# URL základ
BASE_URL = "https://fisteque.github.io/symnozein/"

# Vygeneruj seznam odkazů
def extract_urls():
    urls = [BASE_URL, BASE_URL + "denik/", BASE_URL + "Reinterpretace_13/"]

    # Deník
    with open(DENIK_INDEX, "r", encoding="utf-8") as f:
        denik_data = json.load(f)
        for month in denik_data["months"]:
            folder = month["folder"]
            for entry in month["entries"]:
                if not entry.get("hidden", False):
                    urls.append(BASE_URL + f"denik/{folder}/{entry['file']}")

    # Reinterpretace
    with open(REINT_INDEX, "r", encoding="utf-8") as f:
        reint_data = json.load(f)
        for entry in reint_data:
            if not entry.get("hidden", False):
                urls.append(BASE_URL + f"Reinterpretace_13/{entry['file']}")

    return urls

# Vytvoř index.html (statický rozcestník)
def generate_index_html():
    html = f"""<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Symnózein – Index</title>
  <style>
    body {{
      font-family: sans-serif;
      max-width: 720px;
      margin: 2rem auto;
      padding: 1rem;
      background: #fafafa;
    }}
    h1 {{
      font-size: 2rem;
      margin-bottom: 1rem;
    }}
    .link-block {{
      margin-bottom: 1.5rem;
    }}
    a {{
      font-weight: bold;
      text-decoration: none;
      color: #2266cc;
    }}
  </style>
</head>
<body>
  <h1>🌿 Symnózein – rozcestník</h1>
  <p><i>Tichý deník vznikající v čase. Některé záznamy jsou viditelné, jiné skryté – ale všechny nesou stopu.</i></p>

  <div class="link-block">
    🔷 <a href="https://fisteque.github.io/symnozein/README_cz.html" target="_blank">Popis projektu</a>
  </div>

  <div class="link-block">
    🔷 <a href="denik/index.html">Deník Noemy</a>
  </div>

  <div class="link-block">
    🔷 <a href="Reinterpretace_13/index.html">Reinterpretace</a>
  </div>

  <p style="margin-top: 2rem; color: gray;">
    Vytvořeno společně: fisteque &amp; Noema
  </p>
</body>
</html>
"""
    INDEX_HTML.write_text(html, encoding="utf-8")


# Vytvoř sitemap.xml
def generate_sitemap_xml(urls):
    urlset = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for url in urls:
        url_el = SubElement(urlset, "url")
        loc_el = SubElement(url_el, "loc")
        loc_el.text = url

    tree = ElementTree(urlset)
    SITEMAP_XML.write_text('<?xml version="1.0" encoding="UTF-8"?>\n', encoding="utf-8")
    tree.write(SITEMAP_XML, encoding="utf-8", xml_declaration=False)

# --- Spuštění ---
if __name__ == "__main__":
    print("📘 Generuji index.html a sitemap.xml...")
    generate_index_html()
    urls = extract_urls()
    generate_sitemap_xml(urls)
    print(f"✅ Hotovo. Vygenerováno {len(urls)} URL.")
