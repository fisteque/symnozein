import os
import json
from datetime import datetime

BODY_DIR = "body"
OUTPUT_FILE = os.path.join(BODY_DIR, "body_index.json")


def scan_directory(base_path):
    result = []

    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == "body_index.json":
                continue

            full_path = os.path.join(root, file)
            rel_path = os.path.relpath(full_path, base_path)

            stat = os.stat(full_path)

            result.append({
                "path": rel_path.replace("\\", "/"),
                "size": stat.st_size,
                "modified": datetime.fromtimestamp(stat.st_mtime).isoformat()
            })

    return sorted(result, key=lambda x: x["path"])


def main():
    files = scan_directory(BODY_DIR)

    index = {
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "count": len(files),
        "files": files
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"Updated {OUTPUT_FILE} with {len(files)} files.")


if __name__ == "__main__":
    main()
