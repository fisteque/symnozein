from pathlib import Path
from bs4 import BeautifulSoup
from datetime import datetime

# Kořenová složka s deníkem
DENIK_DIR = Path("denik")

# Procházej všechny HTML soubory začínající na "Noe_"
html_files = list(DENIK_DIR.rglob("Noe_*.html"))
print(f"🔍 Nalezeno {len(html_files)} HTML souborů k ověření...")

for path in html_files:
    try:
        text = path.read_text(encoding="utf-8")
        soup = BeautifulSoup(text, "html.parser")

        # Už existuje <meta name="date">?
        if soup.find("meta", attrs={"name": "date"}):
            print(f"✅ {path.name} již obsahuje <meta name='date'>")
            continue

        # Pokus o extrakci data z <title>
        title_tag = soup.find("title")
        if not title_tag:
            print(f"⚠️ {path.name} nemá <title>")
            continue

        title_text = title_tag.text.strip()

        # Očekávaný formát: "Nadpis – 24. 12. 2025"
        match = None
        for sep in [" – ", " - "]:
            parts = title_text.split(sep)
            if len(parts) == 2 and "." in parts[1]:
                match = parts[1]
                break

        if not match:
            print(f"⚠️ {path.name} nemá rozpoznatelné datum v <title>")
            continue

        # Pokus o převod do ISO formátu
        try:
            parsed_date = datetime.strptime(match.strip(), "%d. %m. %Y")
            iso_date = parsed_date.strftime("%Y-%m-%d")
        except Exception as e:
            print(f"⚠️ {path.name} má nevalidní datum: {match}")
            continue

        # Vytvoř meta tag a přidej ho do <head>
        new_meta = soup.new_tag("meta", attrs={"name": "date", "content": iso_date})
        if soup.head:
            soup.head.append(new_meta)
            # Přepiš soubor
            path.write_text(str(soup), encoding="utf-8")
            print(f"➕ Přidán <meta name='date'> do {path.name}")
        else:
            print(f"⚠️ {path.name} nemá <head>")

    except Exception as e:
        print(f"❌ Chyba při zpracování {path.name}: {e}")
