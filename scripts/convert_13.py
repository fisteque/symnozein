import os
import sys
import markdown
import yaml
from datetime import datetime, date as date_type
import json

TARGETS = {
    "13": {
        "input_dir": "Reinterpretace_13/13_md",
        "output_dir": "Reinterpretace_13/13",
        "template_path": "Reinterpretace_13/templates/mapitola_template.html",
        "index_path": "Reinterpretace_13/13_index.json",
        "sitemap_path": "Reinterpretace_13/sitemap_13.xml",
        "url_prefix": "https://fisteque.github.io/symnozein/Reinterpretace_13/13/"
    },
}

def load_metadata(md_file):
    with open(md_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if lines[0].strip() != '---':
        return {}, ''.join(lines)

    meta_lines = []
    i = 1
    while i < len(lines):
        if lines[i].strip() == '---':
            break
        meta_lines.append(lines[i])
        i += 1

    metadata = yaml.safe_load(''.join(meta_lines))
    content = ''.join(lines[i+1:])
    return metadata, content

def process_target(target_name):
    if target_name not in TARGETS:
        print(f"Unknown target: {target_name}")
        return

    config = TARGETS[target_name]
    input_dir = config['input_dir']
    output_dir = config['output_dir']
    index_path = config['index_path']
    sitemap_path = config['sitemap_path']
    url_prefix = config['url_prefix']
    template = ""

    if config['template_path'] and os.path.exists(config['template_path']):
        with open(config['template_path'], 'r', encoding='utf-8') as f:
            template = f.read()

    index = []
    sitemap_urls = []

    for filename in os.listdir(input_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(input_dir, filename)
            metadata, content = load_metadata(filepath)

            # Skip files with 'hidden: true' in metadata for sitemap
            hidden = metadata.get('hidden', False)

            base_name = os.path.splitext(filename)[0]
            html_filename = base_name + '.html'
            html_url = url_prefix + html_filename

            index_entry = {
                "title": metadata.get("title", base_name),
                "file": html_filename,
                "date": metadata.get("date", ""),
                "summary": metadata.get("summary", ""),
                "tags": metadata.get("tags", []),
                "hidden": hidden
            }
            index.append(index_entry)

            if not hidden:
                sitemap_urls.append(html_url)

            if target_name != "13":
                # Render HTML only for non-material targets
                html_body = markdown.markdown(content, extensions=['extra', 'codehilite', 'toc'])
                final_html = template.replace("{{ content }}", html_body)
                for key, value in metadata.items():
                    final_html = final_html.replace(f"{{{{ {key} }}}}", str(value))

                output_path = os.path.join(output_dir, html_filename)
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(final_html)

    with open(index_path, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    with open(sitemap_path, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for url in sitemap_urls:
            f.write(f"  <url><loc>{url}</loc></url>\n")
        f.write('</urlset>')

def main():
    if len(sys.argv) == 1:
        for target in TARGETS:
            process_target(target)
    elif len(sys.argv) == 3 and sys.argv[1] == "--only":
        process_target(sys.argv[2])
    else:
        print("Použití: python convert_all.py --only [13|material]")
        sys.exit(1)

if __name__ == "__main__":
    main()
