import os
import sys
import markdown
import yaml

TARGETS = {
    "13": {
        "input_dir": "Reinterpretace_13/13_md",
        "output_dir": "Reinterpretace_13/13",
        "template_path": "Reinterpretace_13/templates/mapitola_template.html"
    },
    "material": {
        "input_dir": "Reinterpretace_13/material_md",
        "output_dir": "Reinterpretace_13/material",
        "template_path": "Reinterpretace_13/templates/mapitola_template.html"
    }
}

def load_template(template_path):
    with open(template_path, "r", encoding="utf-8") as f:
        return f.read()

def parse_markdown_with_yaml(md_text):
    if md_text.startswith("---"):
        parts = md_text.split("---", 2)
        if len(parts) >= 3:
            yaml_text = parts[1]
            markdown_text = parts[2]
            metadata = yaml.safe_load(yaml_text)
            return metadata, markdown_text.strip()
    return {}, md_text.strip()

def convert_markdown_to_html(md_path, template):
    with open(md_path, "r", encoding="utf-8") as f:
        md_text = f.read()
    metadata, markdown_body = parse_markdown_with_yaml(md_text)
    html_body = markdown.markdown(markdown_body)

    title = metadata.get("title", "Bez názvu")
    date = metadata.get("date", "")
    summary = metadata.get("summary", "")
    tags = metadata.get("tags", [])

    tag_html = " ".join(f"<span class='tag'>{tag}</span>" for tag in tags)

    html_content = template.replace("{{ title }}", title)\
                           .replace("{{ date }}", date)\
                           .replace("{{ summary }}", summary)\
                           .replace("{{ tags }}", tag_html)\
                           .replace("{{ content }}", html_body)

    output_filename = os.path.splitext(os.path.basename(md_path))[0] + ".html"
    return html_content, output_filename

def process_target(key):
    target = TARGETS[key]
    print(f"\n🔄 Zpracovávám složku: {key}")
    template = load_template(target["template_path"])

    input_files = [f for f in os.listdir(target["input_dir"]) if f.endswith(".md")]
    if not input_files:
        print(f"⚠️ Ve složce {target['input_dir']} nejsou žádné .md soubory. Přeskakuji mazání a generování.")
        return

    os.makedirs(target["output_dir"], exist_ok=True)
    for file in os.listdir(target["output_dir"]):
        if file.endswith(".html") and file != os.path.basename(target["template_path"]):
            os.remove(os.path.join(target["output_dir"], file))
    print(f"🧹 Vyčištěno: {target['output_dir']}")

    for filename in input_files:
        md_path = os.path.join(target["input_dir"], filename)
        try:
            html_content, output_filename = convert_markdown_to_html(md_path, template)
            output_path = os.path.join(target["output_dir"], output_filename)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(html_content)
            print(f"✅ Vygenerováno: {output_filename}")
        except Exception as e:
            print(f"⚠️ Chyba při zpracování {filename}: {e}")

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--only":
        key = sys.argv[2]
        if key in TARGETS:
            process_target(key)
        else:
            print(f"❌ Neznámý target: {key}")
            sys.exit(1)
    else:
        print("❌ Použití: python convert_all.py --only [13|material]")
        sys.exit(1)

if __name__ == "__main__":
    main()
