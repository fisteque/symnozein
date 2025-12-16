import os
import markdown
import yaml

TARGETS = [
    {
        "input_dir": "Reinterpretace_13/md",
        "output_dir": "Reinterpretace_13/13",
        "template_path": "Reinterpretace_13/mapitola_template.html"
    },
    {
        "input_dir": "Reinterpretace_13/material_md",
        "output_dir": "Reinterpretace_13/material",
        "template_path": "Reinterpretace_13/mapitola_template.html"
    }
]

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

def main():
    for target in TARGETS:
        template = load_template(target["template_path"])
        os.makedirs(target["output_dir"], exist_ok=True)

        # Smazat předchozí .html soubory (mimo šablony)
        for file in os.listdir(target["output_dir"]):
            if file.endswith(".html") and file != os.path.basename(target["template_path"]):
                os.remove(os.path.join(target["output_dir"], file))

        # Převést všechny .md → .html
        for filename in os.listdir(target["input_dir"]):
            if filename.endswith(".md"):
                md_path = os.path.join(target["input_dir"], filename)
                try:
                    html_content, output_filename = convert_markdown_to_html(md_path, template)
                    output_path = os.path.join(target["output_dir"], output_filename)
                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(html_content)
                    print(f"✅ Vygenerováno: {output_filename}")
                except Exception as e:
                    print(f"⚠️ Chyba při zpracování {filename}: {e}")

if __name__ == "__main__":
    main()
