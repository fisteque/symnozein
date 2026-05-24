#!/bin/bash
set -e

source ~/.config/noema/github.env

REPO_DIR="/home/fiste/Noema/symnozein"
SOURCE_DIR="/home/fiste/Noema/bridge/scripts/"
TARGET_DIR="$REPO_DIR/body/bridge/scripts/"

cd "$REPO_DIR"

git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

rsync -av \
  --exclude "__pycache__/" \
  --exclude "*.pyc" \
  "$SOURCE_DIR" "$TARGET_DIR"

git add body/bridge/scripts/

if git diff --cached --quiet; then
  echo "Scripts beze změny, není co commitovat."
  exit 0
fi

git commit -m "Sync RPi5 bridge scripts"

git push https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main

echo "Scripts synchronizovány na GitHub."