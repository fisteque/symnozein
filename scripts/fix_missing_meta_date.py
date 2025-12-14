import os
import re
from bs4 import BeautifulSoup

DENIK_FOLDER = "denik"

DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")

def extract_date_from_content(soup):
    # 1️⃣ <meta name="date">
    meta = soup.find("meta", attrs={"name": "date"})
    if meta and meta.get("content") and DATE_RE.fullmatch(meta["content"].strip()):
        return meta["content"].strip()

    # 2️⃣ <h3> YYYY-MM-DD
    for h3 in soup.find_all("h3"):
        m = DATE_RE.search(h3.get_text())
        if m:
            return m.group(0)

    # 3️⃣ <title> DD. MM. YYYY
    title = soup.find("title")
    if title:
        m = re.search(r"(\d{1,2})\.\s*(\d{1,2})\.\s*(20\d{2})", title.text)
        if m:
            d, mth, y = m.groups()
            return f"{y}-{mth.zfill(2)}-{d.zfill(2)}"

    return None

def extract_date_from_filename(filename):
    m = re.match(r"Noe_(\d{2})_(\d{2})_(\d{2})", filename)
    if not m:
        return None
    d, mth, y = m.groups()
    real_year = 2000 + (int(y) % 100)
    return f"{real_year}-{mth}-{d}"

def ensure_meta_date(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    date_value = extract_date_from_content(soup)
    if not date_value:
        date_value = extract_date_from_filename(os.path.basename(file_path))

    if not date_value:
        print(f"❌ Nelze určit datum: {file_path}")
        return

    head = soup.find("head")
    if not head:
        print(f"❌ Chybí <head>: {file_path}")
        return

    meta = soup.find("meta", attrs={"name": "date"})
    if meta:
        old = meta.get("content", "")
        if old == date_value:
            return  # OK
        meta["content"] = date_value
        print(f"🔁 Opraveno datum: {file_path} → {date_value}")
    else:
        new_meta = soup.new_tag("meta")
        new_meta.attrs["name"] = "date"
        new_meta.attrs["content"] = date_value
        head.append(new_meta)
        print(f"➕ Přidáno datum: {file_path} → {date_value}")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def main():
    print("🛠 Oprava <meta name='date'> ve všech deníkových souborech\n")

    for folder in sorted(os.listdir(DENIK_FOLDER)):
        folder_path = os.path.join(DENIK_FOLDER, folder)
        if not os.path.isdir(folder_path):
            continue

        for file in sorted(os.listdir(folder_path)):
            if file.endswith(".html") and file.startswith("Noe_"):
                ensure_meta_date(os.path.join(folder_path, file))

    print("\n✅ Hotovo. Všechny záznamy mají <meta name='date'>.")

if __name__ == "__main__":
    main()
