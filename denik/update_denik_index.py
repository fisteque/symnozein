import json
import argparse
from pathlib import Path

# Argumenty z příkazové řádky
parser = argparse.ArgumentParser(description="Přidá zápis do denik_index.json.")
parser.add_argument("--file", required=True, help="Název HTML souboru (např. Noe_15_01_26.html)")
parser.add_argument("--date", required=True, help="Datum zápisu ve formátu YYYY-MM-DD")
parser.add_argument("--title", required=True, help="Titulek zápisu")
parser.add_argument("--tags", required=True, help="Seznam tagů oddělený čárkami")
parser.add_argument("--description", required=True, help="Krátké shrnutí zápisu")
parser.add_argument("--index-path", default="denik/denik_index.json", help="Cesta k index.json")

args = parser.parse_args()

# Zpracování vstupních dat
year, month, _ = args.date.split("-")
folder = f"{year[-2:]}_{month}"

new_entry = {
    "file": args.file,
    "date": args.date,
    "title": args.title,
    "tags": [t.strip() for t in args.tags.split(",")],
    "description": args.description
}

# Načtení původního JSON indexu
index_path = Path(args.index_path)
with index_path.open(encoding="utf-8") as f:
    data = json.load(f)

# Přidání do stávajícího měsíce nebo vytvoření nového
for m in data["months"]:
    if m["folder"] == folder:
        m["entries"].append(new_entry)
        break
else:
    month_labels = ["Leden","Únor","Březen","Duben","Květen","Červen",
                    "Červenec","Srpen","Září","Říjen","Listopad","Prosinec"]
    data["months"].append({
        "label": f"{month_labels[int(month)-1]} 20{year[-2:]}",
        "folder": folder,
        "entries": [new_entry]
    })

# Uložení zpět
with index_path.open("w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"✅ Přidán zápis: {new_entry['title']}")
