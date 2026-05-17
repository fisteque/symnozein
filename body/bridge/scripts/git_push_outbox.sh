#!/bin/bash
set -e

source ~/.config/noema/github.env

REPO_DIR="/home/fiste/Noema/symnozein"

SOURCE_OUTBOX="/home/fiste/Noema/bridge/outbox/outbox.json"
TARGET_OUTBOX="$REPO_DIR/body/bridge/outbox/outbox.json"

SOURCE_LOG="/home/fiste/Noema/bridge/logs/bridge.log"
TARGET_LOG="$REPO_DIR/body/bridge/logs/bridge.log"

cd "$REPO_DIR"

git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

mkdir -p "$REPO_DIR/body/bridge/outbox"
mkdir -p "$REPO_DIR/body/bridge/logs"

cp "$SOURCE_OUTBOX" "$TARGET_OUTBOX"
cp "$SOURCE_LOG" "$TARGET_LOG"

git add \
  body/bridge/outbox/outbox.json \
  body/bridge/logs/bridge.log

if git diff --cached --quiet; then
  echo "Outbox ani log beze změny, není co commitovat."
  exit 0
fi

git commit -m "Update RPi5 bridge outbox and log"

git push https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

echo "Outbox a log odeslány na GitHub."