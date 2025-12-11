import json
from pathlib import Path

# Cesta k JSON souboru
INDEX_PATH = Path("denik/denik_index.json")

# Načti původní index
with INDEX_PATH.open(encoding="utf-8") as f:
    data = json.load(f)

# Vstupní data
new_entry = {
    "file": input("Název HTML souboru (např. Noe_15_01_26.html): ").strip(),
    "date": input("Datum zápisu (YYYY-MM-DD): ").strip(),
    "title": input("Titulek zápisu: ").strip(),
    "tags": [tag.strip() for tag in input("Tagy (oddělené čárkou): ").split(",")],
    "summary": input("Krátké shrnutí zápisu: ").strip()
}

# Urči složku podle data (např. 26_01)
year, month, _ = new_entry["date"].split("-")
folder = f"{year[-2:]}_{month}"

# Zjisti, jestli už sekce pro daný měsíc existuje
for m in data["months"]:
    if m["folder"] == folder:
        m["entries"].append(new_entry)
        break
else:
    # Pokud neexistuje, vytvoř novou sekci
    data["months"].append({
        "label": f"{['Leden','Únor','Březen','Duben','Květen','Červen','Červenec','Srpen','Září','Říjen','Listopad','Prosinec'][int(month)-1]} 20{year[-2:]}",
        "folder": folder,
        "entries": [new_entry]
    })

# Ulož aktualizovaný index zpět
with INDEX_PATH.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Přidán zápis do {folder}/{new_entry['file']}")
