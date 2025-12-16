import os
import markdown
import yaml

TEMPLATE_PATH = "Reinterpretace_13/mapitola_template.html"
INPUT_DIR = "Reinterpretace_13/md"
OUTPUT_DIR = "Reinterpretace_13/13"

def load_template():
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        return f.read()

def convert_markdown_to_html(md_path, template):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            _, yaml_block, markdown_text = parts
        else:
            raise ValueError(f"Neplatná YAML hlavička v souboru {md_path}")
    else:
        raise ValueError(f"Chybějící YAML hlavička v souboru {md_path}")

    metadata = yaml.safe_load(yaml_block)
    html_body = markdown.markdown(markdown_text)

    tags = metadata.get("tags", [])
    if isinstance(tags, list):
        tags = ", ".join(tags)

    context = {
        "title": metadata.get("title", ""),
        "summary": metadata.get("summary", ""),
        "tags": tags,
        "date": str(metadata.get("date", "")),
        "hidden": str(metadata.get("hidden", False)).lower(),
        "body": html_body
    }

    html_output = template
    for key, value in context.items():
        html_output = html_output.replace(f"{{{{{key}}}}}", value)

    return html_output, os.path.splitext(os.path.basename(md_path))[0] + ".html"

def main():
    template = load_template()
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # 🧹 Smazat všechny .html kromě šablony
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith(".html") and file != "mapitola_template.html":
            os.remove(os.path.join(OUTPUT_DIR, file))

    # 🔁 Vygenerovat .html pro každý .md
    for filename in os.listdir(INPUT_DIR):
        if filename.endswith(".md"):
            md_path = os.path.join(INPUT_DIR, filename)
            try:
                html_content, output_filename = convert_markdown_to_html(md_path, template)
                output_path = os.path.join(OUTPUT_DIR, output_filename)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(html_content)
                print(f"✅ Vygenerováno: {output_filename}")
            except Exception as e:
                print(f"⚠️ Chyba při zpracování {filename}: {e}")

if __name__ == "__main__":
    main()
