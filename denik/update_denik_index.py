import os
import json
from datetime import datetime

# Cílové cesty
DENIK_FOLDER = "denik"
INDEX_PATH = os.path.join(DENIK_FOLDER, "denik_index.json")

# Inicializace datové struktury
index = {"months": []}

# Průchod složkami deníku
for folder in sorted(os.listdir(DENIK_FOLDER)):
    folder_path = os.path.join(DENIK_FOLDER, folder)
    if not os.path.isdir(folder_path) or not folder.startswith("25_") and not folder.startswith("26_"):
        continue

    month_label = {
        "12": "Prosinec", "01": "Leden", "02": "Únor", "03": "Březen",
        "04": "Duben", "05": "Květen", "06": "Červen", "07": "Červenec",
        "08": "Srpen", "09": "Září", "10": "Říjen", "11": "Listopad"
    }
    parts = folder.split("_")
    month_num = parts[1]
    year = "20" + parts[0]
    label = f"{month_label.get(month_num, 'Neznámý')} {year}"

    entries = []
    for file in sorted(os.listdir(folder_path)):
        if file.endswith(".html") and file.startswith("Noe_"):
            name_parts = file.replace(".html", "").split("_")
            date_str = f"{name_parts[3]}-{name_parts[2]}-{name_parts[1]}"
            display_date = f"{name_parts[1]}. {name_parts[2]}. {name_parts[3]}"
            entries.append({
                "title": f"Zápis {display_date}",
                "file": file,
                "date": date_str,
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
