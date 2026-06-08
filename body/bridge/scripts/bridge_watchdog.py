#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import Any


DEFAULT_PROJECT_ROOT = Path("/home/fiste/Noema")
DEFAULT_RUNTIME_ROOT = DEFAULT_PROJECT_ROOT / "bridge"
DEFAULT_REPO_ROOT = DEFAULT_PROJECT_ROOT / "symnozein"

WATCHDOG_ID = "rpi5-bridge-watchdog"
SYSTEMD_SAFE_PROPERTIES = ("ActiveState", "SubState", "Result", "NRestarts", "ExecMainStatus")
STEP_STALL_LIMITS_SECONDS = {
    "inbound sync": 120,
    "bridge agent": 90,
    "write bridge summary": 60,
    "outbound sync": 180,
}


class WatchdogError(RuntimeError):
    pass


def utc_now() -> datetime:
    return datetime.now(UTC)


def utc_iso(value: datetime | None = None) -> str:
    return (value or utc_now()).isoformat().replace("+00:00", "Z")


def utc_stamp(value: datetime | None = None) -> str:
    return (value or utc_now()).strftime("%Y-%m-%dT%H%M%SZ")


def utc_month(value: datetime | None = None) -> str:
    return (value or utc_now()).strftime("%Y-%m")


def parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.strip():
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def age_seconds(value: object, now: datetime) -> float | None:
    parsed = parse_utc(value)
    if parsed is None:
        return None
    return max(0.0, (now - parsed).total_seconds())


def ensure_inside(path: Path, root: Path) -> Path:
    resolved_path = path.resolve()
    resolved_root = root.resolve()
    if resolved_path != resolved_root and resolved_root not in resolved_path.parents:
        raise WatchdogError(f"Unsafe path outside allowed root: {path}")
    return resolved_path


def atomic_write_json(path: Path, data: dict[str, Any], root: Path) -> None:
    ensure_inside(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, root)
    tmp_path.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp_path.replace(path)


def atomic_write_text(path: Path, text: str, root: Path) -> None:
    ensure_inside(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp-{os.getpid()}")
    ensure_inside(tmp_path, root)
    tmp_path.write_text(text, encoding="utf-8")
    tmp_path.replace(path)


def load_json(path: Path, root: Path) -> dict[str, Any]:
    ensure_inside(path, root)
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"_parse_error": f"Invalid JSON: {path.name}"}
    if not isinstance(data, dict):
        return {"_parse_error": f"JSON root is not an object: {path.name}"}
    return data


def pid_is_alive(pid: object) -> bool | None:
    if not isinstance(pid, int) or pid <= 0:
        return None
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def sanitized_systemctl_status(unit: str) -> dict[str, str]:
    result = subprocess.run(
        ["systemctl", "show", unit, "--no-pager", *[f"--property={prop}" for prop in SYSTEMD_SAFE_PROPERTIES]],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    status: dict[str, str] = {}
    if result.returncode != 0:
        status["Unavailable"] = "true"
        return status
    for line in result.stdout.splitlines():
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key in SYSTEMD_SAFE_PROPERTIES:
            status[key] = value
    return status


def load_watchdog_state(runtime_root: Path) -> dict[str, Any]:
    path = runtime_root / "state" / "bridge_watchdog_state.json"
    state = load_json(path, runtime_root)
    if state.get("version") != 1:
        state = {"version": 1, "active": {}, "history": []}
    state.setdefault("active", {})
    state.setdefault("history", [])
    return state


def save_watchdog_state(runtime_root: Path, state: dict[str, Any]) -> None:
    state["history"] = state.get("history", [])[-200:]
    atomic_write_json(runtime_root / "state" / "bridge_watchdog_state.json", state, runtime_root)


def stable_fingerprint(payload: dict[str, Any]) -> str:
    text = json.dumps(payload, ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def safe_snapshot(
    cycle_state: dict[str, Any],
    lock_state: dict[str, Any],
    cycle_error_state: dict[str, Any],
    systemd: dict[str, dict[str, str]],
    now: datetime,
) -> dict[str, Any]:
    return {
        "cycle": {
            "status": cycle_state.get("status"),
            "started_at": cycle_state.get("started_at"),
            "finished_at": cycle_state.get("finished_at"),
            "last_step": cycle_state.get("last_step"),
            "error": cycle_state.get("error"),
        },
        "lock": {
            "status": lock_state.get("status"),
            "current_step": lock_state.get("current_step"),
            "created_at": lock_state.get("created_at"),
            "expires_at": lock_state.get("expires_at"),
            "last_progress_at": lock_state.get("last_progress_at"),
            "owner": lock_state.get("owner"),
            "host": lock_state.get("host"),
            "pid_alive": pid_is_alive(lock_state.get("pid")),
            "progress_age_seconds": age_seconds(lock_state.get("last_progress_at"), now),
        },
        "cycle_error": {
            "status": cycle_error_state.get("status"),
            "active_fingerprint": cycle_error_state.get("active_fingerprint"),
            "step": cycle_error_state.get("step"),
            "repeat_count": cycle_error_state.get("repeat_count"),
            "first_seen_at": cycle_error_state.get("first_seen_at"),
            "last_seen_at": cycle_error_state.get("last_seen_at"),
        },
        "systemd": systemd,
    }


def summary_mtime_age_seconds(repo_root: Path, now: datetime) -> float | None:
    summary = repo_root / "body" / "bridge" / "state_summary" / "latest.md"
    if not summary.exists():
        return None
    mtime = datetime.fromtimestamp(summary.stat().st_mtime, UTC)
    return max(0.0, (now - mtime).total_seconds())


def detect_incidents(
    runtime_root: Path,
    repo_root: Path,
    *,
    include_systemctl: bool,
    cycle_missing_seconds: int,
    running_timeout_seconds: int,
    summary_stale_seconds: int,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    now = utc_now()
    cycle_state = load_json(runtime_root / "state" / "bridge_cycle_state.json", runtime_root)
    lock_state = load_json(runtime_root / "state" / "bridge_cycle.lock.json", runtime_root)
    cycle_error_state = load_json(runtime_root / "state" / "cycle_error_state.json", runtime_root)
    systemd = {
        "bridge-cycle.timer": sanitized_systemctl_status("bridge-cycle.timer") if include_systemctl else {},
        "bridge-cycle.service": sanitized_systemctl_status("bridge-cycle.service") if include_systemctl else {},
    }
    snapshot = safe_snapshot(cycle_state, lock_state, cycle_error_state, systemd, now)
    incidents: list[dict[str, Any]] = []

    timer_status = systemd.get("bridge-cycle.timer", {})
    service_status = systemd.get("bridge-cycle.service", {})
    timer_state = timer_status.get("ActiveState")
    if include_systemctl and timer_state and timer_state != "active":
        incidents.append({"kind": "bridge_timer_inactive", "severity": "error", "step": None})

    service_result = service_status.get("Result")
    service_active = service_status.get("ActiveState")
    if include_systemctl and service_result not in (None, "", "success") and service_active != "active":
        incidents.append({"kind": "bridge_service_failed", "severity": "error", "step": None})

    status = cycle_state.get("status")
    finished_age = age_seconds(cycle_state.get("finished_at"), now)
    if cycle_state.get("_parse_error") or not cycle_state:
        incidents.append({"kind": "cycle_missing", "severity": "error", "step": None})
    elif status == "running":
        started_age = age_seconds(cycle_state.get("started_at"), now)
        if started_age is None or started_age > running_timeout_seconds:
            incidents.append({"kind": "cycle_stuck_running", "severity": "error", "step": cycle_state.get("last_step")})
    elif status == "ok":
        if finished_age is None or finished_age > cycle_missing_seconds:
            incidents.append({"kind": "cycle_missing", "severity": "error", "step": cycle_state.get("last_step")})
    elif status == "error":
        incidents.append({"kind": "cycle_error_status", "severity": "error", "step": cycle_state.get("last_step")})

    summary_age = summary_mtime_age_seconds(repo_root, now)
    if summary_age is None or summary_age > summary_stale_seconds:
        incidents.append({"kind": "summary_stale", "severity": "warn", "step": "write bridge summary", "summary_age_seconds": summary_age})

    lock_status = lock_state.get("status")
    if lock_status == "active":
        current_step = str(lock_state.get("current_step") or "")
        expires_at = parse_utc(lock_state.get("expires_at"))
        expired = expires_at is not None and expires_at <= now
        dead_pid = pid_is_alive(lock_state.get("pid")) is False
        if lock_state.get("owner") == "rpi5-bridge-cycle" and (dead_pid or expired):
            incidents.append({"kind": "stale_lock", "severity": "error", "step": current_step or None})

        progress_age = age_seconds(lock_state.get("last_progress_at"), now)
        limit = STEP_STALL_LIMITS_SECONDS.get(current_step)
        if limit is not None and (progress_age is None or progress_age > limit):
            incidents.append(
                {
                    "kind": "step_stalled",
                    "severity": "error",
                    "step": current_step,
                    "progress_age_seconds": progress_age,
                    "limit_seconds": limit,
                }
            )

    if cycle_error_state.get("status") in {"active", "repeated"}:
        incidents.append(
            {
                "kind": "cycle_error_active",
                "severity": "error",
                "step": cycle_error_state.get("step"),
                "cycle_error_fingerprint": cycle_error_state.get("active_fingerprint"),
            }
        )

    for incident in incidents:
        fingerprint_payload = {
            "kind": incident.get("kind"),
            "step": incident.get("step"),
            "cycle_error_fingerprint": incident.get("cycle_error_fingerprint"),
            "lock_owner": snapshot["lock"].get("owner"),
            "lock_host": snapshot["lock"].get("host"),
            "lock_pid_alive": snapshot["lock"].get("pid_alive"),
            "lock_status": snapshot["lock"].get("status"),
        }
        incident["fingerprint"] = stable_fingerprint(fingerprint_payload)
        incident["detected_at"] = utc_iso(now)
        incident["snapshot"] = snapshot

    return incidents, snapshot


def render_markdown(frontmatter: dict[str, Any], body: str) -> str:
    import yaml

    yaml_text = yaml.safe_dump(
        frontmatter,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).strip()
    return f"---\n{yaml_text}\n---\n\n{body.rstrip()}\n"


def write_outbox_attempt(runtime_root: Path, incident: dict[str, Any], now: datetime) -> Path:
    outbox_dir = runtime_root / "outbox" / "messages"
    ensure_inside(outbox_dir, runtime_root)
    filename = f"{utc_stamp(now)}_rpi5_bridge-watchdog-{incident['kind']}.md"
    path = outbox_dir / filename
    counter = 1
    while path.exists():
        path = outbox_dir / f"{path.stem}-{counter}{path.suffix}"
        counter += 1
    frontmatter = {
        "id": f"bridge-watchdog-{now.strftime('%Y%m%d-%H%M%S')}-{incident['fingerprint'][:12]}",
        "type": "bridge_watchdog_incident",
        "created_at": utc_iso(now),
        "sender": WATCHDOG_ID,
        "target": "noema",
        "status": "incident",
        "severity": incident.get("severity", "error"),
        "kind": incident.get("kind"),
        "step": incident.get("step"),
        "fingerprint": incident.get("fingerprint"),
    }
    body = "\n".join(
        [
            "Bridge watchdog zachytil incident.",
            "",
            f"- kind: `{incident.get('kind')}`",
            f"- severity: `{incident.get('severity')}`",
            f"- step: `{incident.get('step')}`",
            f"- fingerprint: `{incident.get('fingerprint')}`",
            f"- detected_at: `{incident.get('detected_at')}`",
            "",
            "Lokální JSON incident je zdroj pravdy; tato zpráva je jen pokus o pozdější publikaci.",
        ]
    )
    atomic_write_text(path, render_markdown(frontmatter, body), runtime_root)
    return path


def write_incident_json(runtime_root: Path, incident: dict[str, Any], now: datetime) -> Path:
    incident_dir = runtime_root / "incidents" / utc_month(now)
    ensure_inside(incident_dir, runtime_root)
    filename = f"bridge-watchdog-{utc_stamp(now)}-{incident['kind']}-{incident['fingerprint'][:12]}.json"
    path = incident_dir / filename
    atomic_write_json(path, incident, runtime_root)
    return path


def handle_incidents(runtime_root: Path, incidents: list[dict[str, Any]], *, write_outbox: bool) -> int:
    state = load_watchdog_state(runtime_root)
    active = state.setdefault("active", {})
    now = utc_now()
    created = 0
    current_fingerprints = {incident["fingerprint"] for incident in incidents}

    for incident in incidents:
        fingerprint = incident["fingerprint"]
        existing = active.get(fingerprint)
        if isinstance(existing, dict) and existing.get("status") == "active":
            existing["last_seen_at"] = utc_iso(now)
            existing["repeat_count"] = int(existing.get("repeat_count", 1)) + 1
            continue

        incident_record = dict(incident)
        incident_record["status"] = "active"
        incident_record["first_seen_at"] = utc_iso(now)
        incident_record["last_seen_at"] = utc_iso(now)
        incident_record["repeat_count"] = 1
        incident_record["outbox_write_status"] = "skipped"
        incident_path = write_incident_json(runtime_root, incident_record, now)
        incident_record["incident_path"] = str(incident_path)

        if write_outbox:
            try:
                outbox_path = write_outbox_attempt(runtime_root, incident_record, now)
                incident_record["outbox_write_status"] = "ok"
                incident_record["outbox_path"] = str(outbox_path)
            except Exception as exc:
                incident_record["outbox_write_status"] = "failed"
                incident_record["outbox_error"] = exc.__class__.__name__
            write_incident_json(runtime_root, incident_record, now)

        active[fingerprint] = {
            "status": "active",
            "kind": incident_record.get("kind"),
            "step": incident_record.get("step"),
            "first_seen_at": incident_record["first_seen_at"],
            "last_seen_at": incident_record["last_seen_at"],
            "repeat_count": 1,
            "incident_path": incident_record.get("incident_path"),
            "outbox_write_status": incident_record.get("outbox_write_status"),
            "outbox_path": incident_record.get("outbox_path"),
        }
        state.setdefault("history", []).append(
            {
                "event": "incident_created",
                "at": utc_iso(now),
                "fingerprint": fingerprint,
                "kind": incident_record.get("kind"),
                "step": incident_record.get("step"),
            }
        )
        created += 1

    for fingerprint, entry in list(active.items()):
        if fingerprint in current_fingerprints:
            continue
        if isinstance(entry, dict) and entry.get("status") == "active":
            entry["status"] = "cleared"
            entry["cleared_at"] = utc_iso(now)
            state.setdefault("history", []).append(
                {
                    "event": "incident_cleared",
                    "at": utc_iso(now),
                    "fingerprint": fingerprint,
                    "kind": entry.get("kind"),
                    "step": entry.get("step"),
                }
            )

    state["last_check_at"] = utc_iso(now)
    state["last_incident_count"] = len(incidents)
    save_watchdog_state(runtime_root, state)
    return created


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check local bridge cycle health and record local incidents.")
    parser.add_argument("--runtime-root", type=Path, default=DEFAULT_RUNTIME_ROOT)
    parser.add_argument("--repo-root", type=Path, default=DEFAULT_REPO_ROOT)
    parser.add_argument("--cycle-missing-seconds", type=int, default=180)
    parser.add_argument("--running-timeout-seconds", type=int, default=120)
    parser.add_argument("--summary-stale-seconds", type=int, default=300)
    parser.add_argument("--no-systemctl", action="store_true", help="Skip systemctl status collection.")
    parser.add_argument("--no-outbox", action="store_true", help="Do not attempt runtime outbox incident publication.")
    parser.add_argument("--json", action="store_true", help="Print a JSON result summary.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    runtime_root = args.runtime_root.resolve()
    repo_root = args.repo_root.resolve()
    try:
        ensure_inside(runtime_root, runtime_root)
        incidents, snapshot = detect_incidents(
            runtime_root,
            repo_root,
            include_systemctl=not args.no_systemctl,
            cycle_missing_seconds=args.cycle_missing_seconds,
            running_timeout_seconds=args.running_timeout_seconds,
            summary_stale_seconds=args.summary_stale_seconds,
        )
        created = handle_incidents(runtime_root, incidents, write_outbox=not args.no_outbox)
        result = {
            "status": "incident" if incidents else "ok",
            "incident_count": len(incidents),
            "created_count": created,
            "kinds": [incident["kind"] for incident in incidents],
            "snapshot": snapshot,
        }
        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
        else:
            print(f"bridge_watchdog status={result['status']} incidents={len(incidents)} created={created}")
            for incident in incidents:
                print(f"- {incident['kind']} step={incident.get('step')} fingerprint={incident['fingerprint']}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
