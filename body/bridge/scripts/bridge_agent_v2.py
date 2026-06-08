#!/usr/bin/env python3

import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

import yaml


AGENT_ID = "rpi5-bridge-agent"

BRIDGE_ROOT = Path(os.environ.get("NOEMA_BRIDGE_ROOT", Path(__file__).resolve().parents[1])).resolve()
PROJECT_ROOT = Path(os.environ.get("NOEMA_PROJECT_ROOT", BRIDGE_ROOT.parent)).resolve()
BODY_ROOT = Path(os.environ.get("NOEMA_BODY_ROOT", PROJECT_ROOT / "symnozein" / "body")).resolve()
if not BODY_ROOT.exists():
    BODY_ROOT = PROJECT_ROOT / "body"

INBOX_DIR = BODY_ROOT / "bridge" / "inbox" / "messages"
OUTBOX_DIR = BODY_ROOT / "bridge" / "outbox" / "messages"
CODEX_RUNTIME_INBOX_DIR = Path(os.environ.get("NOEMA_CODEX_INBOX", PROJECT_ROOT / "codex" / "inbox")).resolve()
STATE_DIR = BRIDGE_ROOT / "state"
LOG_FILE = BRIDGE_ROOT / "logs" / "bridge.log"
PROCESSED_FILE = STATE_DIR / "processed_messages.json"
EVENT_STATE_FILE = STATE_DIR / "event_state.json"
TASK_RUNS_FILE = STATE_DIR / "task_runs.json"
BODY_STATE_FILE = PROJECT_ROOT / "state" / "body_state.json"
TASKS_DIR = BRIDGE_ROOT / "scripts" / "tasks"
TASK_ALLOWLIST_FILE = TASKS_DIR / "allowlist.json"

REQUIRED_FIELDS = {"id", "type", "created_at", "sender", "target"}
VALID_TARGETS = {AGENT_ID, "rpi5-bridge"}
SAFE_TASK_NAME = re.compile(r"^[A-Za-z0-9_.-]{1,80}$")
MAX_TASK_ARG_LENGTH = 500
MAX_TASK_OUTPUT_CHARS = 6000
FORBIDDEN_TASK_SCRIPT_PATTERNS = (
    "sudo",
    "git push",
    "rm -",
    "os.remove",
    "os.unlink",
    ".unlink(",
    "shutil.rmtree",
    "subprocess",
    "socket",
    "requests",
    "urllib",
    "http.client",
    "nmap",
    "masscan",
    "eval(",
    "exec(",
)


@dataclass(frozen=True)
class Message:
    path: Path
    frontmatter: dict[str, Any]
    body: str
    sha256: str

    @property
    def message_id(self) -> str:
        return str(self.frontmatter["id"])


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_iso(dt: datetime | None = None) -> str:
    return (dt or utc_now()).isoformat().replace("+00:00", "Z")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def assert_inside(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise ValueError(f"Unsafe path outside allowed root: {path}")
    return resolved_path


def atomic_write_text(path: Path, text: str, allowed_root: Path) -> None:
    ensure_dir(path.parent)
    assert_inside(path, allowed_root)
    tmp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    assert_inside(tmp_path, allowed_root)
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def log(message: str, level: str = "INFO") -> None:
    ensure_dir(LOG_FILE.parent)
    assert_inside(LOG_FILE, BRIDGE_ROOT)
    line = f"[{utc_iso()}] [{level}] {message}"
    with LOG_FILE.open("a", encoding="utf-8") as handle:
        handle.write(line + "\n")
    print(line)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def parse_frontmatter_block(block: str) -> dict[str, Any]:
    data = yaml.safe_load(block) or {}
    if not isinstance(data, dict):
        raise ValueError("YAML front matter must contain an object")
    return data


def parse_markdown_message(path: Path) -> Message:
    assert_inside(path, INBOX_DIR)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("Missing YAML front matter")

    try:
        frontmatter_block, body = text[4:].split("\n---\n", 1)
    except ValueError as exc:
        raise ValueError("Unclosed YAML front matter") from exc

    frontmatter = parse_frontmatter_block(frontmatter_block)
    missing = sorted(REQUIRED_FIELDS - frontmatter.keys())
    if missing:
        raise ValueError(f"Missing required front matter fields: {', '.join(missing)}")

    return Message(
        path=path,
        frontmatter=frontmatter,
        body=body,
        sha256=sha256_file(path),
    )


def load_processed() -> dict[str, Any]:
    ensure_dir(STATE_DIR)
    assert_inside(PROCESSED_FILE, STATE_DIR)
    if not PROCESSED_FILE.exists():
        return {"version": 1, "messages": {}, "pending": {}, "errors": []}

    with PROCESSED_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("processed_messages.json must contain an object")
    if data.get("version") != 1:
        raise ValueError("Unsupported processed_messages.json version")
    if not isinstance(data.get("messages"), dict):
        raise ValueError("processed_messages.json must contain messages object")
    if "pending" in data and not isinstance(data["pending"], dict):
        raise ValueError("processed_messages.json pending must contain object")
    if "errors" in data and not isinstance(data["errors"], list):
        raise ValueError("processed_messages.json errors must contain list")
    data.setdefault("pending", {})
    data.setdefault("errors", [])
    return data


def save_processed(data: dict[str, Any]) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(PROCESSED_FILE, text, STATE_DIR)


def load_event_state() -> dict[str, Any]:
    ensure_dir(STATE_DIR)
    assert_inside(EVENT_STATE_FILE, STATE_DIR)
    if not EVENT_STATE_FILE.exists():
        return {"version": 1, "body_state": {}, "reported_events": {}}

    with EVENT_STATE_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise ValueError("event_state.json must contain an object")
    if data.get("version") != 1:
        raise ValueError("Unsupported event_state.json version")
    if "body_state" in data and not isinstance(data["body_state"], dict):
        raise ValueError("event_state.json body_state must contain object")
    if "reported_events" in data and not isinstance(data["reported_events"], dict):
        raise ValueError("event_state.json reported_events must contain object")
    data.setdefault("body_state", {})
    data.setdefault("reported_events", {})
    return data


def save_event_state(data: dict[str, Any]) -> None:
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(EVENT_STATE_FILE, text, STATE_DIR)


def load_task_runs() -> dict[str, Any]:
    ensure_dir(STATE_DIR)
    assert_inside(TASK_RUNS_FILE, STATE_DIR)
    if not TASK_RUNS_FILE.exists():
        return {"version": 1, "runs": []}

    with TASK_RUNS_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("task_runs.json must contain an object")
    if data.get("version") != 1:
        raise ValueError("Unsupported task_runs.json version")
    if "runs" in data and not isinstance(data["runs"], list):
        raise ValueError("task_runs.json runs must contain a list")
    data.setdefault("runs", [])
    return data


def save_task_runs(data: dict[str, Any]) -> None:
    data["runs"] = data.get("runs", [])[-200:]
    text = json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    atomic_write_text(TASK_RUNS_FILE, text, STATE_DIR)


def relative_to_body(path: Path) -> str:
    return path.resolve().relative_to(BODY_ROOT.resolve()).as_posix()


def audit_path(path: Path) -> str:
    resolved = path.resolve()
    body_root = BODY_ROOT.resolve()
    project_root = PROJECT_ROOT.resolve()
    if resolved == body_root or body_root in resolved.parents:
        return resolved.relative_to(body_root).as_posix()
    if resolved == project_root or project_root in resolved.parents:
        return resolved.relative_to(project_root).as_posix()
    return str(resolved)


def message_sort_key(path: Path) -> tuple[str, str]:
    try:
        message = parse_markdown_message(path)
        created_at = str(message.frontmatter.get("created_at") or "")
    except Exception:
        created_at = ""
    return created_at, path.name


def list_inbox_messages() -> list[Path]:
    if not INBOX_DIR.exists():
        log(f"Inbox messages directory does not exist: {INBOX_DIR}", level="WARN")
        return []

    assert_inside(INBOX_DIR, BODY_ROOT)
    return sorted(
        (
            path
            for path in INBOX_DIR.glob("*.md")
            if path.is_file() and not path.name.startswith(".")
        ),
        key=message_sort_key,
    )


def list_observed_files(path: Path) -> list[Path]:
    if not path.exists():
        return []
    assert_inside(path, BODY_ROOT)
    return sorted(
        (
            item
            for item in path.iterdir()
            if item.is_file() and not item.name.startswith(".")
        ),
        key=lambda item: (item.stat().st_mtime, item.name),
    )


def latest_file_name(paths: list[Path]) -> str:
    if not paths:
        return "(none)"
    return paths[-1].name


def sanitize_filename_part(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "-", value.strip())
    cleaned = cleaned.strip(".-")
    return cleaned[:80] or "message"


def event_key(payload: dict[str, Any]) -> str:
    data = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def render_markdown_message(frontmatter: dict[str, Any], body: str) -> str:
    yaml_text = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body.rstrip()}\n"


def write_outbox_message(
    frontmatter: dict[str, Any],
    body: str,
    filename_prefix: str,
    now: datetime | None = None,
) -> Path:
    ensure_dir(OUTBOX_DIR)
    assert_inside(OUTBOX_DIR, BODY_ROOT)

    timestamp = now or utc_now()
    stamp = timestamp.strftime("%Y-%m-%dT%H%M%SZ")
    safe_prefix = sanitize_filename_part(filename_prefix)
    reply_path = OUTBOX_DIR / f"{stamp}_{safe_prefix}.md"
    counter = 1
    while reply_path.exists():
        reply_path = OUTBOX_DIR / f"{reply_path.stem}-{counter}{reply_path.suffix}"
        counter += 1

    assert_inside(reply_path, OUTBOX_DIR)
    atomic_write_text(reply_path, render_markdown_message(frontmatter, body), OUTBOX_DIR)
    return reply_path


def write_codex_needed(message: Message) -> Path:
    ensure_dir(CODEX_RUNTIME_INBOX_DIR)
    assert_inside(CODEX_RUNTIME_INBOX_DIR, PROJECT_ROOT)

    now = utc_now()
    message_id = message.message_id
    codex_payload = message.frontmatter.get("codex")
    question = None
    if isinstance(codex_payload, dict) and isinstance(codex_payload.get("question"), str):
        question = codex_payload["question"].strip()
    if not question:
        question = message.body.strip()
    if not question:
        raise ValueError("codex_request requires codex.question or non-empty message body")

    frontmatter = {
        "id": f"codex-request-{now.strftime('%Y%m%d-%H%M%S')}-{sanitize_filename_part(message_id)}",
        "type": "codex_request",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": "codex",
        "reply_to": message_id,
        "status": "pending_codex",
        "requested_by": str(message.frontmatter.get("sender") or "noema"),
        "source_message": relative_to_body(message.path),
    }
    body_lines = [
        "# Codex Needed",
        "",
        f"- source_message_id: `{message_id}`",
        f"- source_sender: `{message.frontmatter.get('sender')}`",
        f"- source_created_at: `{message.frontmatter.get('created_at')}`",
        "",
        "## Question",
        "",
        question,
        "",
        "## Source Body",
        "",
        message.body.strip() or "(empty)",
    ]

    stamp = now.strftime("%Y-%m-%dT%H%M%SZ")
    path = CODEX_RUNTIME_INBOX_DIR / f"{stamp}_codex-request-{sanitize_filename_part(message_id)}.md"
    counter = 1
    while path.exists():
        path = CODEX_RUNTIME_INBOX_DIR / f"{path.stem}-{counter}{path.suffix}"
        counter += 1
    assert_inside(path, CODEX_RUNTIME_INBOX_DIR)
    atomic_write_text(path, render_markdown_message(frontmatter, "\n".join(body_lines)), CODEX_RUNTIME_INBOX_DIR)
    return path


def ack_frontmatter(message: Message, now: datetime) -> dict[str, Any]:
    message_id = message.message_id
    return {
        "id": f"reply-{now.strftime('%Y%m%d-%H%M%S')}-{sanitize_filename_part(message_id)}",
        "type": "ack",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": str(message.frontmatter.get("sender") or "noema"),
        "reply_to": message_id,
        "status": "ok",
        "processed_by": AGENT_ID,
    }


def write_ack(message: Message) -> Path:
    now = utc_now()
    return write_outbox_message(
        ack_frontmatter(message, now),
        f"Zprava `{message.message_id}` byla prijata a zpracovana.",
        f"rpi5_reply-{message.message_id}",
        now=now,
    )


def task_result_frontmatter(
    message: Message,
    now: datetime,
    run: dict[str, Any],
) -> dict[str, Any]:
    status = "ok" if run.get("exit_code") == 0 and not run.get("timed_out") else "error"
    return {
        "id": f"task-result-{now.strftime('%Y%m%d-%H%M%S')}-{sanitize_filename_part(message.message_id)}",
        "type": "task_result",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": str(message.frontmatter.get("sender") or "noema"),
        "reply_to": message.message_id,
        "status": status,
        "processed_by": AGENT_ID,
        "task_name": run.get("task_name"),
        "exit_code": run.get("exit_code"),
        "timed_out": run.get("timed_out", False),
    }


def truncate_output(text: str, limit: int = MAX_TASK_OUTPUT_CHARS) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated]\n"


def write_task_result(message: Message, run: dict[str, Any]) -> Path:
    now = utc_now()
    body_lines = [
        f"Task `{run.get('task_name')}` dokoncen.",
        "",
        f"- run_id: `{run.get('run_id')}`",
        f"- status: `{run.get('status')}`",
        f"- exit_code: `{run.get('exit_code')}`",
        f"- timed_out: `{run.get('timed_out', False)}`",
        f"- duration_seconds: `{run.get('duration_seconds')}`",
        "",
        "## stdout",
        "",
        "```text",
        truncate_output(str(run.get("stdout", ""))).rstrip() or "(empty)",
        "```",
        "",
        "## stderr",
        "",
        "```text",
        truncate_output(str(run.get("stderr", ""))).rstrip() or "(empty)",
        "```",
    ]
    return write_outbox_message(
        task_result_frontmatter(message, now, run),
        "\n".join(body_lines),
        f"rpi5_task-result-{message.message_id}",
        now=now,
    )


def is_already_processed(processed: dict[str, Any], message: Message) -> bool:
    entry = processed["messages"].get(message.message_id)
    return isinstance(entry, dict) and entry.get("sha256") == message.sha256


def has_conflicting_processed_id(processed: dict[str, Any], message: Message) -> bool:
    entry = processed["messages"].get(message.message_id)
    return isinstance(entry, dict) and entry.get("sha256") != message.sha256


def record_processed(
    processed: dict[str, Any],
    message: Message,
    status: str,
    reply_path: Path | None = None,
    error: str | None = None,
) -> None:
    entry: dict[str, Any] = {
        "path": relative_to_body(message.path),
        "sha256": message.sha256,
        "processed_at": utc_iso(),
        "status": status,
    }
    if reply_path is not None:
        entry["reply_path"] = audit_path(reply_path)
    if error is not None:
        entry["error"] = error
    processed["messages"][message.message_id] = entry


def record_task_run(run: dict[str, Any]) -> None:
    task_runs = load_task_runs()
    task_runs.setdefault("runs", []).append(run)
    save_task_runs(task_runs)


def record_pending(processed: dict[str, Any], message: Message) -> None:
    processed.setdefault("pending", {})[message.message_id] = {
        "path": relative_to_body(message.path),
        "sha256": message.sha256,
        "detected_at": utc_iso(),
        "status": "pending",
    }
    processed["messages"][message.message_id] = {
        "path": relative_to_body(message.path),
        "sha256": message.sha256,
        "processed_at": None,
        "status": "pending",
    }


def clear_pending(processed: dict[str, Any], message_id: str) -> None:
    processed.setdefault("pending", {}).pop(message_id, None)


def record_error(
    processed: dict[str, Any],
    message_path: Path,
    error: Exception | str,
    message: Message | None = None,
    message_id: str | None = None,
) -> dict[str, Any]:
    error_text = str(error)
    error_entry: dict[str, Any] = {
        "path": relative_to_body(message_path),
        "error": error_text,
        "error_at": utc_iso(),
    }

    if message_path.exists():
        error_entry["sha256"] = sha256_file(message_path)

    if message is not None:
        message_id = message.message_id
        error_entry["message_id"] = message.message_id
        record_processed(processed, message, "error", error=error_text)
        clear_pending(processed, message.message_id)
    elif message_id is not None:
        error_entry["message_id"] = message_id

    processed.setdefault("errors", []).append(error_entry)
    processed["errors"] = processed["errors"][-100:]
    return error_entry


def report_error_outbox(
    event_state: dict[str, Any],
    error_entry: dict[str, Any],
) -> Path | None:
    key = event_key(
        {
            "kind": "error",
            "path": error_entry.get("path"),
            "sha256": error_entry.get("sha256"),
            "error": error_entry.get("error"),
            "message_id": error_entry.get("message_id"),
        }
    )
    reported = event_state.setdefault("reported_events", {})
    if key in reported:
        return None

    now = utc_now()
    frontmatter = {
        "id": f"error-{now.strftime('%Y%m%d-%H%M%S')}-{key[:12]}",
        "type": "error",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": "noema",
        "status": "error",
        "severity": "error",
        "event_key": key,
        "source_path": error_entry.get("path"),
    }
    if error_entry.get("message_id") is not None:
        frontmatter["reply_to"] = error_entry["message_id"]

    body_lines = [
        "Bridge agent zaznamenal chybu.",
        "",
        f"- path: `{error_entry.get('path')}`",
        f"- error: `{error_entry.get('error')}`",
    ]
    if error_entry.get("message_id") is not None:
        body_lines.append(f"- message_id: `{error_entry['message_id']}`")

    outbox_path = write_outbox_message(
        frontmatter,
        "\n".join(body_lines),
        f"rpi5_error-{key[:12]}",
        now=now,
    )
    reported[key] = {
        "type": "error",
        "reported_at": utc_iso(),
        "outbox_path": relative_to_body(outbox_path),
    }
    return outbox_path


def load_task_allowlist() -> dict[str, Any]:
    assert_inside(TASK_ALLOWLIST_FILE, TASKS_DIR)
    if not TASK_ALLOWLIST_FILE.exists():
        raise ValueError(f"Task allowlist does not exist: {TASK_ALLOWLIST_FILE}")
    with TASK_ALLOWLIST_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or data.get("version") != 1:
        raise ValueError("Task allowlist must contain version 1 object")
    tasks = data.get("tasks")
    if not isinstance(tasks, dict):
        raise ValueError("Task allowlist must contain tasks object")
    return data


def parse_task_request(message: Message) -> tuple[str, list[str]]:
    task = message.frontmatter.get("task")
    if not isinstance(task, dict):
        raise ValueError("task_request requires task object in front matter")
    name = task.get("name")
    args = task.get("args", [])
    if not isinstance(name, str) or not SAFE_TASK_NAME.fullmatch(name):
        raise ValueError("task.name must be a safe allowlist task name")
    if not isinstance(args, list) or not all(isinstance(arg, str) for arg in args):
        raise ValueError("task.args must be a list of strings")
    if any(len(arg) > MAX_TASK_ARG_LENGTH for arg in args):
        raise ValueError(f"task.args entries must be <= {MAX_TASK_ARG_LENGTH} chars")
    return name, args


def validate_task_definition(task_name: str, definition: Any) -> tuple[Path, int]:
    if not isinstance(definition, dict):
        raise ValueError(f"Allowlist entry for {task_name} must be an object")
    script_name = definition.get("script")
    timeout_seconds = definition.get("timeout_seconds", 30)
    if not isinstance(script_name, str) or "/" in script_name or "\\" in script_name:
        raise ValueError(f"Allowlist entry for {task_name} must use a local script filename")
    if not isinstance(timeout_seconds, int) or timeout_seconds < 1 or timeout_seconds > 120:
        raise ValueError(f"Allowlist timeout for {task_name} must be 1..120 seconds")
    script_path = assert_inside(TASKS_DIR / script_name, TASKS_DIR)
    if not script_path.exists() or not script_path.is_file():
        raise ValueError(f"Allowlisted task script does not exist: {script_name}")
    script_text = script_path.read_text(encoding="utf-8", errors="replace")
    lowered = script_text.lower()
    for pattern in FORBIDDEN_TASK_SCRIPT_PATTERNS:
        if pattern in lowered:
            raise ValueError(f"Allowlisted task script contains forbidden pattern: {pattern}")
    return script_path, timeout_seconds


def run_allowlisted_task(message: Message) -> dict[str, Any]:
    if os.geteuid() == 0:
        raise ValueError("Refusing to execute bridge tasks as root")

    task_name, task_args = parse_task_request(message)
    allowlist = load_task_allowlist()
    tasks = allowlist["tasks"]
    if task_name not in tasks:
        raise ValueError(f"Task is not allowlisted: {task_name}")

    script_path, timeout_seconds = validate_task_definition(task_name, tasks[task_name])
    run_id = f"{utc_now().strftime('%Y%m%d-%H%M%S')}-{sanitize_filename_part(message.message_id)}"
    started_at = utc_now()
    command = [sys.executable, str(script_path), *task_args]
    log(f"Task run start: name={task_name} run_id={run_id}")

    env = {
        "PATH": "/usr/bin:/bin",
        "LANG": "C.UTF-8",
        "NOEMA_TASK_RUN_ID": run_id,
        "NOEMA_BRIDGE_ROOT": str(BRIDGE_ROOT),
        "NOEMA_REPO_ROOT": str(BODY_ROOT.parent),
        "NOEMA_BODY_ROOT": str(BODY_ROOT),
        "NOEMA_PROJECT_ROOT": str(PROJECT_ROOT),
    }

    timed_out = False
    try:
        completed = subprocess.run(
            command,
            cwd=str(TASKS_DIR),
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout_seconds,
            shell=False,
        )
        exit_code = completed.returncode
        stdout = completed.stdout or ""
        stderr = completed.stderr or ""
    except subprocess.TimeoutExpired as exc:
        timed_out = True
        exit_code = 124
        stdout = exc.stdout or ""
        stderr = (exc.stderr or "") + f"\nTask timed out after {timeout_seconds} seconds."

    finished_at = utc_now()
    run = {
        "run_id": run_id,
        "message_id": message.message_id,
        "task_name": task_name,
        "args": task_args,
        "script": script_path.name,
        "started_at": utc_iso(started_at),
        "finished_at": utc_iso(finished_at),
        "duration_seconds": round((finished_at - started_at).total_seconds(), 3),
        "timeout_seconds": timeout_seconds,
        "exit_code": exit_code,
        "timed_out": timed_out,
        "status": "ok" if exit_code == 0 and not timed_out else "error",
        "stdout": truncate_output(stdout),
        "stderr": truncate_output(stderr),
    }
    record_task_run(run)
    log(
        "Task run finished: "
        f"name={task_name} run_id={run_id} exit_code={exit_code} timed_out={timed_out}"
    )
    if stdout:
        log(f"Task stdout {run_id}: {truncate_output(stdout, 1200).rstrip()}")
    if stderr:
        log(f"Task stderr {run_id}: {truncate_output(stderr, 1200).rstrip()}", level="WARN")
    return run


def load_body_state() -> dict[str, Any] | None:
    if not BODY_STATE_FILE.exists():
        log(f"Body state file does not exist: {BODY_STATE_FILE}", level="WARN")
        return None

    assert_inside(BODY_STATE_FILE, PROJECT_ROOT)
    with BODY_STATE_FILE.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("body_state.json must contain an object")
    return data


def observe_body_state(event_state: dict[str, Any]) -> Path | None:
    body_state = load_body_state()
    if body_state is None:
        return None

    current = {
        "path": "state/body_state.json",
        "sha256": sha256_file(BODY_STATE_FILE),
        "observed_at": utc_iso(),
        "awake": body_state.get("awake"),
        "status": body_state.get("status"),
        "last_hb": body_state.get("last_hb"),
        "last_awake_change": body_state.get("last_awake_change"),
    }
    previous = event_state.get("body_state", {})
    changed_fields = [
        field
        for field in ("awake", "status")
        if previous.get(field) is not None and previous.get(field) != current.get(field)
    ]

    event_state["body_state"] = current
    if not previous:
        log(
            "Body state baseline recorded: "
            f"awake={current.get('awake')} status={current.get('status')}"
        )
        return None
    if not changed_fields:
        log(
            "Body state unchanged: "
            f"awake={current.get('awake')} status={current.get('status')}"
        )
        return None

    key = event_key(
        {
            "kind": "body_state_change",
            "changed_fields": changed_fields,
            "previous": {field: previous.get(field) for field in changed_fields},
            "current": {field: current.get(field) for field in changed_fields},
            "last_awake_change": current.get("last_awake_change"),
        }
    )
    reported = event_state.setdefault("reported_events", {})
    if key in reported:
        return None

    now = utc_now()
    frontmatter = {
        "id": f"state-{now.strftime('%Y%m%d-%H%M%S')}-{key[:12]}",
        "type": "state_event",
        "created_at": utc_iso(now),
        "sender": AGENT_ID,
        "target": "noema",
        "status": "observed",
        "severity": "significant",
        "event_key": key,
        "source_path": current["path"],
        "changed_fields": changed_fields,
    }
    body_lines = [
        "Bridge agent zaznamenal vyznamnou zmenu stavu tela.",
        "",
    ]
    for field in changed_fields:
        body_lines.append(
            f"- {field}: `{previous.get(field)}` -> `{current.get(field)}`"
        )
    body_lines.extend(
        [
            f"- last_hb: `{current.get('last_hb')}`",
            f"- last_awake_change: `{current.get('last_awake_change')}`",
        ]
    )

    outbox_path = write_outbox_message(
        frontmatter,
        "\n".join(body_lines),
        f"rpi5_state-{key[:12]}",
        now=now,
    )
    reported[key] = {
        "type": "body_state_change",
        "reported_at": utc_iso(),
        "outbox_path": relative_to_body(outbox_path),
    }
    log(f"Body state change reported: {relative_to_body(outbox_path)}")
    return outbox_path


def process_inbox() -> int:
    log("=== Bridge agent v2 start ===")
    log(f"Bridge root: {BRIDGE_ROOT}")
    log(f"Body root: {BODY_ROOT}")

    processed = load_processed()
    event_state = load_event_state()
    try:
        observe_body_state(event_state)
    except Exception as exc:
        log(f"Failed to observe body state: {exc}", level="ERROR")
        error_entry = {
            "path": "state/body_state.json",
            "error": str(exc),
            "error_at": utc_iso(),
        }
        report_error_outbox(event_state, error_entry)
    save_event_state(event_state)

    handled = 0
    pending_count = 0
    message_paths = list_inbox_messages()
    log(f"Inbox message files found: {len(message_paths)}")
    codex_inbox_paths = list_observed_files(CODEX_RUNTIME_INBOX_DIR)
    log(
        "Codex runtime inbox files observed: "
        f"{len(codex_inbox_paths)} latest={latest_file_name(codex_inbox_paths)}"
    )

    for message_path in message_paths:
        try:
            message = parse_markdown_message(message_path)
        except Exception as exc:
            log(f"Skipping invalid message {message_path.name}: {exc}", level="ERROR")
            error_entry = record_error(processed, message_path, exc)
            report_error_outbox(event_state, error_entry)
            save_processed(processed)
            save_event_state(event_state)
            continue

        if is_already_processed(processed, message):
            log(f"Already processed: {message.message_id}")
            continue

        if has_conflicting_processed_id(processed, message):
            error = f"Duplicate id with different content: {message.message_id}"
            log(f"Rejected {error}", level="ERROR")
            error_entry = record_error(
                processed,
                message_path,
                error,
                message_id=message.message_id,
            )
            report_error_outbox(event_state, error_entry)
            save_processed(processed)
            save_event_state(event_state)
            continue

        record_pending(processed, message)
        save_processed(processed)
        pending_count += 1
        log(f"Pending message registered: {message.message_id}")

        if str(message.frontmatter.get("target")) not in VALID_TARGETS:
            log(f"Ignoring message for different target: {message.message_id}")
            record_processed(processed, message, "ignored")
            clear_pending(processed, message.message_id)
            handled += 1
            save_processed(processed)
            continue

        try:
            message_type = str(message.frontmatter.get("type"))
            if message_type == "task_request":
                run = run_allowlisted_task(message)
                reply_path = write_task_result(message, run)
                status = "ok" if run.get("status") == "ok" else "error"
            elif message_type == "codex_request":
                reply_path = write_codex_needed(message)
                status = "pending_codex"
            else:
                reply_path = write_ack(message)
                status = "ok"
            record_processed(processed, message, status, reply_path=reply_path)
            clear_pending(processed, message.message_id)
            handled += 1
            log(f"Reply written for {message.message_id}: {audit_path(reply_path)}")
            save_processed(processed)
        except Exception as exc:
            log(f"Failed to process {message.message_id}: {exc}", level="ERROR")
            error_entry = record_error(processed, message_path, exc, message=message)
            report_error_outbox(event_state, error_entry)
            save_processed(processed)
            save_event_state(event_state)

    save_processed(processed)
    save_event_state(event_state)
    log(f"Pending message count this run: {pending_count}")
    log(f"Pending message count remaining: {len(processed.get('pending', {}))}")
    log(f"Processed message count: {handled}")
    log("=== Bridge agent v2 end ===")
    return handled


def main() -> None:
    process_inbox()


if __name__ == "__main__":
    main()
