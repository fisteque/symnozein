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
    }
}

def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def parse_markdown_with_yaml(md_text):
    lines = md_text.splitlines()
    if lines and lines[0].strip() == "---":
        try:
            end = lines[1:].index("---") + 1
            yaml_text = "\n".join(lines[1:end])
            body = "\n".join(lines[end + 1:])
            metadata = yaml.safe_load(yaml_text) or {}
            return metadata, body.strip()
        except ValueError:
            pass
    return {}, md_text.strip()

def normalize_date(value):
    if value is None:
        return ""
    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")
    if isinstance(value, date_type):
        return value.isoformat()
    if isinstance(value, str):
        try:
            return datetime.fromisoformat(value).strftime("%Y-%m-%d")
        except Exception:
            print(f"⚠️ Neplatné datum: '{value}'")
            return ""
    print(f"⚠️ Neznámý typ data: {type(value)}")
    return ""

def convert_markdown_to_html(md_path, template):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()

    metadata, markdown_body = parse_markdown_with_yaml(md_text)
    html_body = markdown.markdown(markdown_body)

    title   = str(metadata.get("title", "Bez názvu"))
    summary = str(metadata.get("summary", ""))
    tags    = metadata.get("tags", [])
    hidden  = str(metadata.get("hidden", "false")).lower()
    date    = normalize_date(metadata.get("date"))

    tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)

    html = template
    html = html.replace("{{title}}", title)
    html = html.replace("{{date}}", date)
    html = html.replace("{{summary}}", summary)
    html = html.replace("{{tags}}", tags_str)
    html = html.replace("{{hidden}}", hidden)
    html = html.replace("{{body}}", html_body)

    out_name = os.path.splitext(os.path.basename(md_path))[0] + ".html"

    index_record = {
        "title": title,
        "file": out_name,
        "date": date,
        "summary": summary,
        "tags": tags if isinstance(tags, list) else [],
        "hidden": hidden == "true"
    }

    return html, out_name, index_record

def process_target(key):
    target = TARGETS[key]
    print(f"\n🔄 Zpracovávám složku: {key}")

    template = load_template(target["template_path"])
    inputs = [f for f in os.listdir(target["input_dir"]) if f.endswith(".md")]
    if not inputs:
        print("⚠️ Žádné .md soubory – nic nemažu.")
        return

    os.makedirs(target["output_dir"], exist_ok=True)

    # smaž staré .html soubory
    for f in os.listdir(target["output_dir"]):
        if f.endswith(".html"):
            os.remove(os.path.join(target["output_dir"], f))

    index = []
    sitemap_urls = []

    for filename in inputs:
        md_path = os.path.join(target["input_dir"], filename)
        try:
            html, out_name, record = convert_markdown_to_html(md_path, template)
            out_path = os.path.join(target["output_dir"], out_name)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"✅ {out_name}")
            index.append(record)
            if not record["hidden"]:
                sitemap_urls.append(target["url_prefix"] + out_name)
        except Exception as e:
            print(f"❌ {filename}: {e}")

    # Zápis index.json
    with open(target["index_path"], "w", encoding="utf-8") as f:
        json.dump(sorted(index, key=lambda r: r["date"], reverse=True), f, ensure_ascii=False, indent=2)
        print(f"📘 Zapsán index: {target['index_path']}")

    # Zápis sitemap.xml
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for url in sitemap_urls:
        sitemap_content += f'  <url><loc>{url}</loc></url>\n'
    sitemap_content += '</urlset>\n'
    with open(target["sitemap_path"], "w", encoding="utf-8") as f:
        f.write(sitemap_content)
        print(f"🌐 Zapsána sitemap: {target['sitemap_path']}")

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--only":
        key = sys.argv[2]
        if key in TARGETS:
            process_target(key)
            return
    print("Použití: python convert_all.py --only [13]")
    sys.exit(1)

if __name__ == "__main__":
    main()
