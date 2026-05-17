#!/usr/bin/env python3

import json
import hashlib
import subprocess
from pathlib import Path
from datetime import datetime, UTC

BASE = Path(__file__).resolve().parent.parent

INBOX = BASE / "inbox/inbox.json"
OUTBOX = BASE / "outbox/outbox.json"
LOG = BASE / "logs/bridge.log"

PULL_SCRIPT = BASE / "scripts/git_pull_inbox.sh"
PUSH_SCRIPT = BASE / "scripts/git_push_outbox.sh"

STATE_FILE = BASE / ".last_inbox_hash"


def log(text):
    timestamp = datetime.now(UTC).isoformat()
    line = f"[{timestamp}] {text}"

    print(line)

    with open(LOG, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def file_hash(path):
    data = path.read_bytes()
    return hashlib.sha256(data).hexdigest()


def load_last_hash():
    if not STATE_FILE.exists():
        return None

    return STATE_FILE.read_text().strip()


def save_hash(h):
    STATE_FILE.write_text(h)


def load_inbox():
    with open(INBOX, "r", encoding="utf-8") as f:
        return json.load(f)


def write_outbox(message, received):
    data = {
        "status": "ok",
        "received": received,
        "message": message,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open(OUTBOX, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():

    log("=== Bridge agent start ===")

    subprocess.run([str(PULL_SCRIPT)], check=True)

    current_hash = file_hash(INBOX)
    last_hash = load_last_hash()

    if current_hash == last_hash:
        log("Inbox beze změny.")
        return

    inbox = load_inbox()

    received = inbox.get("message", "")

    log(f"Nová zpráva: {received}")

    response = (
        f"Zpráva přečtena agentem v "
        f"{datetime.now(UTC).isoformat()} UTC"
    )

    write_outbox(response, inbox)

    save_hash(current_hash)

    log("Odpověď zapsána do outboxu.")

    subprocess.run([str(PUSH_SCRIPT)], check=True)

    log("Outbox pushnut na GitHub.")
    log("=== Bridge agent end ===")


if __name__ == "__main__":
    main()