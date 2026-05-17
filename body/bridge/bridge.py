import json
from datetime import datetime

INBOX = "inbox/inbox.json"
OUTBOX = "outbox/outbox.json"
LOG = "logs/bridge.log"

def log(message):
    timestamp = datetime.now().isoformat()
    with open(LOG, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

try:
    with open(INBOX, "r") as f:
        data = json.load(f)

    response = {
        "status": "ok",
        "received": data,
        "message": "Most funguje."
    }

    with open(OUTBOX, "w") as f:
        json.dump(response, f, indent=2)

    log("Inbox přečten a outbox zapsán.")

except Exception as e:
    log(f"CHYBA: {e}")
    print(e)


