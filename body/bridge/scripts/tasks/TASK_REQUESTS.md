# Noema Bridge Task Requests

This directory contains the allowlisted task wrappers that the bridge agent may run
when it receives a `task_request` message in the bridge inbox.

The bridge task layer is transport-controlled execution, not general shell access.
GitHub carries the inbox/outbox audit trail, but the Raspberry Pi runtime decides
whether a task is valid and what it is allowed to do.

## Runtime Paths

- Inbox messages: `/home/fiste/Noema/symnozein/body/bridge/inbox/messages/`
- Outbox replies: `/home/fiste/Noema/bridge/outbox/messages/`
- Task scripts: `/home/fiste/Noema/bridge/scripts/tasks/`
- Allowlist: `/home/fiste/Noema/bridge/scripts/tasks/allowlist.json`
- Task run state: `/home/fiste/Noema/bridge/state/task_runs.json`
- Runtime log: `/home/fiste/Noema/bridge/logs/bridge.log`

Repo copies under `symnozein/body/bridge/scripts/` are mirrors for audit and
orientation. They are not the runtime source of task scripts.

## Message Format

Create a Markdown message with YAML front matter in the repo inbox path.
The body is human-readable context only. The agent executes only the structured
`task.name` plus string `task.args`.

```markdown
---
id: msg-20260524-task-001
type: task_request
created_at: 2026-05-24T18:00:00Z
sender: noema
target: rpi5-bridge-agent
task:
  name: example_task
  args:
    - "hello"
---

Spust example_task.
```

Valid targets are:

- `rpi5-bridge-agent`
- `rpi5-bridge`

## Codex Requests

Use `codex_request` when Noema needs Codex to inspect or answer something later.
The bridge agent does not call Codex and does not execute a task. It only creates
a pending item in:

```text
/home/fiste/Noema/symnozein/body/bridge/outbox/codex/
```

Example:

```markdown
---
id: msg-20260525-codex-001
type: codex_request
created_at: 2026-05-25T00:20:00Z
sender: noema
target: rpi5-bridge-agent
codex:
  question: "Zkontroluj prosim posledni bridge error a navrhni opravu."
---

Kontext pro Codex muze byt tady v tele zpravy.
```

The generated pending item uses:

```yaml
type: codex_needed
target: codex
status: pending_codex
```

Codex responses are written manually later as outbox messages with
`author: Codex`. The bridge agent must not pretend to be Codex.

## Execution Rules

The agent accepts a task only when all of these are true:

- `type` is `task_request`.
- `task.name` matches a key in `allowlist.json`.
- `task.name` contains only letters, digits, `_`, `.`, or `-`, up to 80 chars.
- `task.args` is a list of strings.
- Each argument is at most 500 chars.
- The allowlist entry points to a local filename in this directory.
- The timeout is an integer from 1 to 120 seconds.
- The task script exists under `/home/fiste/Noema/bridge/scripts/tasks/`.
- The bridge agent is not running as root.

The task is executed as:

```text
/usr/bin/python3 <allowlisted_script.py> <arg1> <arg2> ...
```

The agent uses `shell=False`. There is no dynamic shell command.

## Available Environment

Task wrappers receive a small fixed environment:

- `PATH=/usr/bin:/bin`
- `LANG=C.UTF-8`
- `NOEMA_TASK_RUN_ID`
- `NOEMA_BRIDGE_ROOT`
- `NOEMA_REPO_ROOT`
- `NOEMA_BODY_ROOT`
- `NOEMA_PROJECT_ROOT`

Use these variables instead of hardcoding paths when practical.

## Output And Audit

For each run, the agent writes:

- a task result message into `bridge/outbox/messages/`
- a run entry into `bridge/state/task_runs.json`
- stdout/stderr excerpts into `bridge/logs/bridge.log`

`task_runs.json`, `processed_messages.json`, and `event_state.json` stay local.
They are not published to GitHub.

The outbox reply contains:

- `run_id`
- status
- exit code
- timeout flag
- duration
- truncated stdout
- truncated stderr

## Adding A Task

1. Create a small Python wrapper in this directory.
2. Keep the wrapper deterministic and narrow.
3. Add an entry to `allowlist.json`.
4. Test the wrapper directly from `/tmp` or from this directory.
5. Send an inbox `task_request` message that names the allowlist key.
6. Inspect the outbox reply and `bridge/state/task_runs.json`.

Minimal allowlist entry:

```json
{
  "description": "Short human-readable description.",
  "script": "my_task.py",
  "timeout_seconds": 30
}
```

Minimal wrapper shape:

```python
#!/usr/bin/env python3

from __future__ import annotations

import sys


def main() -> int:
    args = sys.argv[1:]
    print({"args": args})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

## Current Tasks

See `allowlist.json` for the source of truth. Current task names are:

- `example_task`
- `mirror_scripts_to_repo`
- `sync_body_without_bridge`
- `sync_symnozein_without_bridge`

## Forbidden Pattern

Task wrappers must not provide a bypass around the bridge safety model. The
agent rejects task scripts containing forbidden patterns such as:

- `sudo`
- `git push`
- `rm -`
- `os.remove`
- `os.unlink`
- `.unlink(`
- `shutil.rmtree`
- `subprocess`
- `socket`
- `requests`
- `urllib`
- `http.client`
- `nmap`
- `masscan`
- `eval(`
- `exec(`

If a future task needs broader power, create a dedicated reviewed wrapper and
expand the safety model intentionally. Do not tunnel general shell access through
task arguments.
