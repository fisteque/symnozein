#!/bin/bash
set -e

source ~/.config/noema/github.env

cd /home/fiste/Noema/symnozein

git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPO}.git main
