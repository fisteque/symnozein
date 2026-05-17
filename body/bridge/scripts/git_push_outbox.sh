#!/bin/bash
set -e

source ~/.config/noema/github.env

REPO_DIR="/home/fiste/Noema/symnozein"
SOURCE_OUTBOX="/home/fiste/Noema/bridge/outbox/outbox.json"
TARGET_OUTBOX="$REPO_DIR/body/bridge/outbox/outbox.json"

cd "$REPO_DIR"

git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

cp "$SOURCE_OUTBOX" "$TARGET_OUTBOX"

git add body/bridge/outbox/outbox.json

if git diff --cached --quiet; then
  echo "Outbox beze změny, není co commitovat."
  exit 0
fi

git commit -m "Update RPi5 bridge outbox"

git push https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

echo "Outbox odeslán na GitHub."
