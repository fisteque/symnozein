import os
import markdown
import yaml
from bs4 import BeautifulSoup

def parse_markdown_with_yaml(md_path):
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    if content.startswith("---"):
        parts = content.split("---", 2)
        metadata = yaml.safe_load(parts[1])
        body = parts[2].strip()
    else:
        metadata = {}
        body = content.strip()
    return metadata, body

def convert_markdown_to_html(md_path, template_path, output_path):
    metadata, md_body = parse_markdown_with_yaml(md_path)

    # Markdown to HTML
    html_body = markdown.markdown(md_body, extensions=["fenced_code", "tables"])

    # Load template
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Prepare metadata variables
    title = metadata.get("title", "")
    summary = metadata.get("summary", "")
    tags = metadata.get("tags", [])
    date = metadata.get("date", "")
    hidden = metadata.get("hidden", "false")

    # Fill in template
    html_output = template
    template_vars = {
        "title": str(title),
        "summary": str(summary),
        "tags": str(", ".join(tags) if isinstance(tags, list) else tags),
        "date": str(date),
        "hidden": str(hidden),
        "body": html_body,
    }

    for key, value in template_vars.items():
        html_output = html_output.replace(f"{{{{{key}}}}}", value)

    # Save output
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html_output)
