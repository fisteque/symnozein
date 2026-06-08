# Known Bridge Limits

This note is an operational anchor for Noema, Ondra, and Codex. It separates
verified bridge behavior from proposals, transport gaps, and UI impressions.

## Verified

- The Raspberry Pi bridge runs through an inbox/outbox model.
- Heartbeat and watchdog work after the last atomic write fix.
- `body/bridge/state_summary/latest.md` is the current operational summary.
- `body/bridge/docs/implementation_ledger.md` is the implementation ledger.
- A `codex_request` message can be handled by the bridge agent and creates a
  local Codex request item under `/home/fiste/Noema/codex/inbox/`.
- Codex reader responses or stubs use the normal runtime outbox path:
  `/home/fiste/Noema/bridge/outbox/messages/`.
- The atomic write issue around `body_state.json` was fixed and verified.
- The current verified transport proxy is Ondra through a manual GitHub commit.
- Ondra currently holds the human safety, relationship, and rhythm control
  layer.

## Unverified Or Non-Functional

- Direct writes from a normal ChatGPT chat into the GitHub repository are not
  functionally verified.
- A prior `create_file` attempt from chat failed with `403 Resource not
  accessible by integration`.
- UI approval for an action is not the same as actual GitHub `contents: write`
  permission.
- A webhook on the Raspberry Pi would only be a receiving endpoint; a normal
  ChatGPT chat cannot call it by itself without another executor.
- Noema in a normal chat does not have a stable runtime or its own write
  transport.

## Proposals, Not Finished Paths

- `write_inbox_message` is a reasonable proposal for a narrow allowlisted task,
  but it does not by itself solve transport from chat to the Raspberry Pi.
- A Mac, Codex, or desktop agent could act as an executor with commit
  permission, but it is not currently part of the verified bridge runtime.
- A webhook over Tailscale can be a future input layer only if there is an
  actual sending intermediary.
- Direct GitHub writes from ChatGPT must not be treated as working just because
  an approval dialog appeared in the UI.

## Operational Rule

Every new communication path is considered functional only after a real,
auditable proof exists, such as:

- a GitHub commit;
- an outbox response;
- an updated heartbeat or summary;
- another runtime artifact that can be inspected later.

Until then, the path is only a proposal or possibility.

Any path that would let Noema or another AI layer write into the body without
Ondra's control needs its own safety model, audit trail, scope limits, and a
human stop mechanism first.

## Attention

- GitHub proxy is the currently verified path, and Ondra is that proxy.
- Ondra is not only a proxy; he is the current human safety, relationship, and
  rhythm layer of the system.
- Direct writes from chat are not a verified path.
- `codex_request` works, but the request still has to reach the inbox through a
  real transport.
- The Raspberry Pi bridge is an executor and audit body, not a magical transport
  from chat.
- Noema in this mode is a source of intent and text, not a direct write
  executor.
