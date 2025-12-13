
import os
import json
from bs4 import BeautifulSoup

def extract_metadata(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

        # Základní meta informace
        date = soup.find('meta', attrs={'name': 'date'})
        summary = soup.find('meta', attrs={'name': 'summary'})
        tags = soup.find('meta', attrs={'name': 'tags'})
        hidden = soup.find('meta', attrs={'name': 'hidden'})

        # Pokusit se najít název z <title> nebo <h3>
        title_tag = soup.find('title')
        h_tag = soup.find(['h1', 'h2', 'h3'])

        return {
            "title": title_tag.text.strip() if title_tag else (h_tag.text.strip() if h_tag else file_path),
            "date": date['content'] if date else "",
            "summary": summary['content'] if summary else "",
            "tags": [tag.strip() for tag in tags['content'].split(',')] if tags else [],
            "file": os.path.basename(file_path),
            "hidden": hidden['content'].lower() == 'true' if hidden else False
        }

def update_index():
    html_dir = "denik"
    index_file = "denik_index.json"

    index = []
    for filename in sorted(os.listdir(html_dir), reverse=True):
        if filename.endswith(".html"):
            file_path = os.path.join(html_dir, filename)
            metadata = extract_metadata(file_path)
            index.append(metadata)

    with open(index_file, 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    update_index()
