#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit(
        "Chybí modul PyYAML. Přidej do workflow instalaci balíčku pyyaml."
    ) from exc


ROOT = Path(__file__).resolve().parents[1]
SK_MD_DIR = ROOT / "denik" / "SK_md"
OUTPUT_JSON = SK_MD_DIR / "SK_index.json"


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text

    parts = text.split("\n---\n", 1)
    if len(parts) != 2:
        return {}, text

    raw_meta = parts[0][4:]
    body = parts[1]

    try:
        meta = yaml.safe_load(raw_meta) or {}
    except yaml.YAMLError as exc:
        raise ValueError(f"Neplatný frontmatter: {exc}") from exc

    if not isinstance(meta, dict):
        raise ValueError("Frontmatter musí být YAML objekt.")

    return meta, body


def normalize_tags(tags: object) -> list[str]:
    if tags is None:
        return []

    if isinstance(tags, list):
        return [str(tag).strip() for tag in tags if str(tag).strip()]

    if isinstance(tags, str):
        return [tag.strip() for tag in tags.split(",") if tag.strip()]

    return [str(tags).strip()]


def entry_from_md(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    meta, _body = parse_frontmatter(text)

    title = str(meta.get("title", "")).strip()
    date = str(meta.get("date", "")).strip()
    summary = str(meta.get("summary", "")).strip()
    hidden = bool(meta.get("hidden", False))
    tags = normalize_tags(meta.get("tags"))

    return {
        "title": title,
        "file": md_path.name,
        "date": date,
        "summary": summary,
        "tags": tags,
        "hidden": hidden,
    }


def sort_key(entry: dict) -> tuple[str, str]:
    # Nejnovější nahoře, pak název
    return (entry.get("date", ""), entry.get("title", ""))


def main() -> None:
    if not SK_MD_DIR.exists():
        raise SystemExit(f"Složka neexistuje: {SK_MD_DIR}")

    entries: list[dict] = []

    for md_path in sorted(SK_MD_DIR.glob("*.md")):
        # Případná budoucí README / pomocné soubory lze přeskočit tady
        if md_path.name.startswith("."):
            continue

        entries.append(entry_from_md(md_path))

    entries.sort(key=sort_key, reverse=True)

    OUTPUT_JSON.write_text(
        json.dumps(entries, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(f"Aktualizováno: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
