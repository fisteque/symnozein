#!/usr/bin/env python3

from __future__ import annotations

import argparse
import base64
import re
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path


INBOX_DIR = Path("body/bridge/inbox/messages/codex")
VALID_TARGETS = {"rpi5-bridge-agent", "rpi5-bridge"}
SAFE_FILENAME = re.compile(r"^[A-Za-z0-9_.-]+\.md$")
SAFE_ID = re.compile(r"^[A-Za-z0-9_.:-]{1,160}$")
DEFAULT_SENDER = "chatgpt-noema"
DEFAULT_SOURCE = "pc-codex-postman"
DEFAULT_CHANNEL = "github-bridge"
DEFAULT_RUNTIME_RISK = "low"


class PostmanError(RuntimeError):
    pass


def run_git(args: list[str], *, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout or f"exit code {result.returncode}").strip()
        raise PostmanError(f"git {' '.join(args)} failed:\n{detail}")
    return result


def utc_now() -> str:
    return datetime.now(UTC).strftime("%Y-%m-%dT%H:%M:%SZ")


def repo_root() -> Path:
    result = run_git(["rev-parse", "--show-toplevel"])
    return Path(result.stdout.strip()).resolve()


def status_porcelain() -> str:
    return run_git(["status", "--porcelain", "--untracked-files=all"]).stdout.strip()


def require_clean_checkout() -> None:
    status = status_porcelain()
    if status:
        raise PostmanError(f"checkout is dirty; refusing postman delivery:\n{status}")


def sync_main() -> None:
    run_git(["fetch", "origin", "main"])
    run_git(["merge", "--ff-only", "origin/main"])


def validate_filename(filename: str) -> None:
    if "/" in filename or "\\" in filename:
        raise PostmanError("filename must not contain path separators")
    if " " in filename:
        raise PostmanError("filename must not contain spaces")
    if not SAFE_FILENAME.fullmatch(filename):
        raise PostmanError("filename must contain only letters, digits, underscore, dash, dot, and end with .md")


def validate_message_id(message_id: str) -> None:
    if not SAFE_ID.fullmatch(message_id):
        raise PostmanError("id contains unsupported characters or is too long")


def validate_target(target: str) -> None:
    if target not in VALID_TARGETS:
        raise PostmanError(f"invalid target {target!r}; expected one of: {', '.join(sorted(VALID_TARGETS))}")


def yaml_scalar(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def read_body(args: argparse.Namespace) -> str:
    provided = [bool(args.body), bool(args.body_file), bool(args.body_base64)]
    if sum(provided) != 1:
        raise PostmanError("provide exactly one of --body, --body-file, or --body-base64")
    if args.body is not None:
        return args.body
    if args.body_file is not None:
        return Path(args.body_file).read_text(encoding="utf-8")
    try:
        return base64.b64decode(args.body_base64, validate=True).decode("utf-8")
    except Exception as exc:
        raise PostmanError(f"invalid --body-base64: {exc}") from exc


def render_message(args: argparse.Namespace, created_at: str, body: str) -> str:
    question = args.question.strip()
    if not question:
        raise PostmanError("--question must not be empty")
    frontmatter = [
        "---",
        f"id: {args.message_id}",
        "type: codex_request",
        f"created_at: {created_at}",
        f"sender: {args.sender}",
        f"target: {args.target}",
        "meta:",
        f"  source: {args.source}",
        f"  channel: {args.channel}",
        f"  purpose: {args.purpose}",
        f"  requires_human: {'true' if args.requires_human else 'false'}",
        f"  runtime_risk: {args.runtime_risk}",
        f"  write_scope: {args.write_scope}",
        "codex:",
        f"  question: {yaml_scalar(question)}",
        "---",
        "",
        body.rstrip(),
        "",
    ]
    return "\n".join(frontmatter)


def ensure_single_staged_file(path: Path) -> None:
    staged = run_git(["diff", "--cached", "--name-status"]).stdout.strip().splitlines()
    expected = path.as_posix()
    if staged != [f"A\t{expected}"]:
        raise PostmanError(
            "staged scope is not exactly one new inbox file:\n"
            + ("\n".join(staged) if staged else "(nothing staged)")
        )
    status = status_porcelain()
    allowed = {f"A  {expected}"}
    unexpected = [line for line in status.splitlines() if line not in allowed]
    if unexpected:
        raise PostmanError("unexpected working tree changes after staging:\n" + "\n".join(unexpected))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Deliver exactly one codex_request message to the bridge inbox.")
    parser.add_argument("--filename", required=True, help="New .md filename under body/bridge/inbox/messages/codex/")
    parser.add_argument("--id", dest="message_id", required=True, help="Message id for YAML frontmatter.")
    parser.add_argument("--target", required=True, choices=sorted(VALID_TARGETS))
    parser.add_argument("--purpose", required=True, help="meta.purpose value.")
    parser.add_argument("--question", required=True, help="codex.question value.")
    parser.add_argument("--body", help="Markdown body text.")
    parser.add_argument("--body-file", help="Path to UTF-8 Markdown body file.")
    parser.add_argument("--body-base64", help="Base64-encoded UTF-8 Markdown body text.")
    parser.add_argument("--sender", default=DEFAULT_SENDER)
    parser.add_argument("--source", default=DEFAULT_SOURCE)
    parser.add_argument("--channel", default=DEFAULT_CHANNEL)
    parser.add_argument("--runtime-risk", default=DEFAULT_RUNTIME_RISK)
    parser.add_argument("--write-scope", default="audit-only")
    parser.add_argument("--requires-human", action="store_true")
    parser.add_argument("--commit-message", default="Deliver Codex bridge message")
    parser.add_argument("--no-push", action="store_true", help="Commit but do not push. Intended only for local testing.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        root = repo_root()
        validate_filename(args.filename)
        validate_message_id(args.message_id)
        validate_target(args.target)

        sync_main()
        require_clean_checkout()

        target_path = INBOX_DIR / args.filename
        full_target = root / target_path
        if full_target.exists():
            raise PostmanError(f"target file already exists: {target_path}")
        full_target.parent.mkdir(parents=True, exist_ok=True)

        created_at = utc_now()
        body = read_body(args)
        full_target.write_text(render_message(args, created_at, body), encoding="utf-8")

        run_git(["add", "--", target_path.as_posix()])
        ensure_single_staged_file(target_path)
        run_git(["commit", "-m", args.commit_message])
        commit_hash = run_git(["rev-parse", "--short", "HEAD"]).stdout.strip()
        if not args.no_push:
            run_git(["push", "origin", "HEAD:main"])

        final_status = run_git(["status", "--short", "--branch"]).stdout.strip()
        print("Hotovo.")
        print(f"Path: {target_path.as_posix()}")
        print(f"created_at: {created_at}")
        print(f"Commit: {commit_hash} {args.commit_message}")
        print("Scope: exactly one new inbox message file")
        print("Status:")
        print(final_status)
        return 0
    except PostmanError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
