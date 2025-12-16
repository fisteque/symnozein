import os
import json
import re
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, ElementTree

MAPITOL_DIR = 'Reinterpretace_13/13'
OUTPUT_INDEX = 'Reinterpretace_13/13_index.json'
OUTPUT_SITEMAP = 'Reinterpretace_13/sitemap_13.xml'
BASE_URL = 'https://fisteque.github.io/symnozein/Reinterpretace_13/13/'

def extract_meta(content, name):
    match = re.search(rf'<meta\s+name="{re.escape(name)}"\s+content="(.*?)"', content, re.IGNORECASE)
    return match.group(1).strip() if match else None

def parse_tags(tag_string):
    return [tag.strip() for tag in tag_string.split(',')] if tag_string else []

def main():
    index_data = []
    urlset = Element('urlset', xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    for filename in sorted(os.listdir(MAPITOL_DIR)):
        if not filename.endswith('.html'):
            continue

        filepath = os.path.join(MAPITOL_DIR, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        title = extract_meta(content, 'title') or ''
        summary = extract_meta(content, 'summary') or ''
        tags = parse_tags(extract_meta(content, 'tags'))
        date = extract_meta(content, 'date') or ''
        hidden = extract_meta(content, 'hidden') == 'true'
        url = BASE_URL + filename

        index_data.append({
            'file': filename,
            'title': title,
            'summary': summary,
            'tags': tags,
            'date': date,
            'hidden': hidden,
            'url': url
        })

        if not hidden:
            url_el = SubElement(urlset, 'url')
            loc_el = SubElement(url_el, 'loc')
            loc_el.text = url
            lastmod_el = SubElement(url_el, 'lastmod')
            lastmod_el.text = datetime.today().strftime('%Y-%m-%d')

    # Uložit JSON index
    with open(OUTPUT_INDEX, 'w', encoding='utf-8') as f:
        json.dump(index_data, f, indent=2, ensure_ascii=False)

    # Uložit XML sitemap
    tree = ElementTree(urlset)
    tree.write(OUTPUT_SITEMAP, encoding='utf-8', xml_declaration=True)

    print(f'✅ Vygenerováno: {OUTPUT_INDEX} a {OUTPUT_SITEMAP}')

if __name__ == '__main__':
    main()
