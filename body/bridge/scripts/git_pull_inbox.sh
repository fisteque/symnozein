#!/bin/bash
set -e

source ~/.config/noema/github.env

REPO_DIR="/home/fiste/Noema/symnozein"
SOURCE_INBOX="$REPO_DIR/body/bridge/inbox/inbox.json"
TARGET_INBOX="/home/fiste/Noema/bridge/inbox/inbox.json"

cd "$REPO_DIR"

git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

cp "$SOURCE_INBOX" "$TARGET_INBOX"

echo "Inbox stažen z GitHubu do bridge."