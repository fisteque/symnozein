import os
import sys
import markdown
import yaml
from datetime import datetime, date as date_type

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

# ---------- helpers ----------

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
    """
    Vždy vrací STRING ve formátu YYYY-MM-DD nebo prázdný string.
    """
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

# ---------- conversion ----------

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
    html = html.replace("{{™

date}}", date)
    html = html.replace("{{summary}}", summary)
    html = html.replace("{{tags}}", tags_str)
    html = html.replace("{{hidden}}", hidden)
    html = html.replace("{{body}}", html_body)

    out_name = os.path.splitext(os.path.basename(md_path))[0] + ".html"
    return html, out_name

# ---------- processing ----------

def process_target(key):
    target = TARGETS[key]
    print(f"\n🔄 Zpracovávám složku: {key}")

    template = load_template(target["template_path"])

    inputs = [f for f in os.listdir(target["input_dir"]) if f.endswith(".md")]
    if not inputs:
        print("⚠️ Žádné .md soubory – nic nemažu.")
        return

    os.makedirs(target["output_dir"], exist_ok=True)

    for f in os.listdir(target["output_dir"]):
        if f.endswith(".html"):
            os.remove(os.path.join(target["output_dir"], f))

    for filename in inputs:
        md_path = os.path.join(target["input_dir"], filename)
        try:
            html, out_name = convert_markdown_to_html(md_path, template)
            out_path = os.path.join(target["output_dir"], out_name)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"✅ {out_name}")
        except Exception as e:
            print(f"❌ {filename}: {e}")

# ---------- entry ----------

def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--only":
        key = sys.argv[2]
        if key in TARGETS:
            process_target(key)
            return
    print("Použití: python convert_all.py --only [13|material]")
    sys.exit(1)

if __name__ == "__main__":
    main()
