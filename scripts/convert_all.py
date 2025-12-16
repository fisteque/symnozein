import os
import markdown
import yaml

# Cesty ke složkám
TARGETS = [
    {
        "input_dir": "Reinterpretace_13/13_md",
        "output_dir": "Reinterpretace_13/13",
        "template_path": "Reinterpretace_13/13/template.html",
    },
    {
        "input_dir": "Reinterpretace_13/material_md",
        "output_dir": "Reinterpretace_13/material",
        "template_path": "Reinterpretace_13/material/template.html",
    }
]


def load_template(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def convert_markdown_to_html(md_path, template):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            metadata = yaml.safe_load(parts[1])
            markdown_content = parts[2]
        else:
            metadata = {}
            markdown_content = content
    else:
        metadata = {}
        markdown_content = content

    html_body = markdown.markdown(markdown_content, extensions=["extra", "codehilite"])
    html = template.replace("{{ content }}", html_body)

    output_filename = os.path.basename(md_path).replace(".md", ".html")
    return html, output_filename


def main():
    for target in TARGETS:
        template = load_template(target["template_path"])
        os.makedirs(target["output_dir"], exist_ok=True)

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
