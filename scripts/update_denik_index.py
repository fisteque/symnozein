import os
import json
import re

# Cílové cesty
DENIK_FOLDER = "denik"
INDEX_PATH = os.path.join(DENIK_FOLDER, "denik_index.json")

# Inicializace datové struktury
index = {"months": []}

# Mapa měsíců
MONTH_LABELS = {
    "12": "Prosinec", "01": "Leden", "02": "Únor", "03": "Březen",
    "04": "Duben", "05": "Květen", "06": "Červen", "07": "Červenec",
    "08": "Srpen", "09": "Září", "10": "Říjen", "11": "Listopad"
}

# Průchod složkami deníku
for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)

    # Složky musí být typu 25_12 nebo 26_01…
    if not os.path.isdir(folder_path):
        continue
    if not (folder.startswith("25_") or folder.startswith("26_")):
        continue

    parts = folder.split("_")
    year = "20" + parts[0]   # např. 25 -> 2025
    month_num = parts[1]
    label = f"{MONTH_LABELS.get(month_num, 'Neznámý')} {year}"

    entries = []

    for file in sorted(os.listdir(folder_path)):
        if not file.endswith(".html") or not file.startswith("Noe_"):
            continue

        name = file.replace(".html", "")

        # Podpora jmen jako:
        # Noe_11_12_25
        # Noe_12_25b
        # Noe_03_07c
        match = re.match(r"Noe_(\d{2})_(\d{2})([a-z]*)", name)

        if not match:
            print(f"⚠️ Varování: Nepodařilo se načíst datum ze souboru: {file}")
            continue

        month = match.group(1)   # 11, 12, 03…
        day = match.group(2)     # 12, 25, 07…
        suffix = match.group(3)  # "", "b", "c"…

        # Datum pro JSON
        full_date = f"{year}-{month}-{day}"
        # Datum pro zobrazení
        display_date = f"{day}. {month}. {year}"

        # Název pro uživatele
        title = f"Zápis {display_date}"
        if suffix:
            title += f" ({suffix})"   # např. Zápis 12. 12. 2025 (b)

        entries.append({
            "title": title,
            "file": file,
            "date": full_date,
            "tags": [],
            "description": ""
        })

    if entries:
        index["months"].append({
            "label": label,
            "folder": folder,
            "entries": entries
        })

# Zápis do JSON
with open(INDEX_PATH, "w", encoding="utf-8") as f:
    json.dump(index, f, ensure_ascii=False, indent=2)
