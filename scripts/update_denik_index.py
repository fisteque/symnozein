import os
import json
import re

# =========================
# KONFIGURACE
# =========================

DENIK_FOLDER = "denik"
INDEX_PATH = os.path.join(DENIK_FOLDER, "denik_index.json")

MONTH_LABELS = {
    "01": "Leden",
    "02": "Únor",
    "03": "Březen",
    "04": "Duben",
    "05": "Květen",
    "06": "Červen",
    "07": "Červenec",
    "08": "Srpen",
    "09": "Září",
    "10": "Říjen",
    "11": "Listopad",
    "12": "Prosinec",
}

# =========================
# POMOCNÉ FUNKCE
# =========================

def extract_summary_from_html(path):
    """
    Zatím vrací prázdný string.
    Později zde můžeme:
    - vzít první <p>
    - nebo <meta name="summary">
    """
    return ""

# =========================
# HLAVNÍ LOGIKA
# =========================

index = {
    "months": []
}

if not os.path.isdir(DENIK_FOLDER):
    raise RuntimeError(f"Složka {DENIK_FOLDER} neexistuje.")

for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)

    # očekáváme formát YY_MM (např. 25_12)
    if not os.path.isdir(folder_path):
        continue

    match_folder = re.match(r"(\d{2})_(\d{2})", folder)
    if not match_folder:
        continue

    year_short, month_num = match_folder.groups()
    year = f"20{year_short}"
    month_label = MONTH_LABELS.get(month_num, "Neznámý")
    label = f"{month_label} {year}"

    entries = []

    for file in sorted(os.listdir(folder_path)):
        if not file.endswith(".html"):
            continue
        if not file.startswith("Noe_"):
            continue

        name = file.replace(".html", "")

        # Podpora:
        # Noe_11_12_25
        # Noe_11_12_25b
        match = re.match(r"Noe_(\d{2})_(\d{2})_(\d{2})([a-z]*)", name)
        if not match:
            print(f"⚠️ Nelze rozpoznat datum: {file}")
            continue

        day, month, year_file, suffix = match.groups()

        full_date = f"20{year_file}-{month}-{day}"
        display_date = f"{day}. {month}. 20{year_file}"

        title = f"Zápis {display_date}"
        if suffix:
            title += f" ({suffix})"

        file_path = os.path.join(folder_path, file)

        entry = {
            "title": title,
            "date": full_date,
            "file": file,
            "tags": [],
            "summary": extract_summary_from_html(file_path),
            "hidden": False
        }

        entries.append(entry)

    if entries:
        index["months"].append({
            "label": label,
            "folder": folder,
            "entries": entries
        })

# =========================
# ZÁPIS JSON
# =========================

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)

print("✅ denik_index.json byl úspěšně aktualizován.")
