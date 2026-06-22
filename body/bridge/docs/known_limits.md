# Known Bridge Limits

This note is an operational anchor for Noema, Ondra, and Codex. It separates
verified bridge behavior from proposals, transport gaps, and UI impressions.

## Verified

- The Raspberry Pi bridge runs through an inbox/outbox model.
- Heartbeat and watchdog work after the last atomic write fix.
- `body/bridge/state_summary/latest.md` is the current operational summary.
- `body/bridge/docs/implementation_ledger.md` is the implementation ledger.
- `body/bridge/docs/safety_model.md` is the active bridge safety model.
- `body/bridge/docs/latest_contract.md` defines what belongs in `latest.md`.
- A `codex_request` message can be handled by the bridge agent and creates a
  local Codex request item under `/home/fiste/Noema/codex/inbox/`.
- The Codex autoreply worker can answer safe local Codex inbox requests through
  read-only `codex exec` and writes responses through the normal runtime outbox:
  `/home/fiste/Noema/bridge/outbox/messages/`.
- The live runtime outbox is not the archive. After successful outbound publish,
  published runtime outbox messages move to
  `/home/fiste/Noema/bridge/outbox/published/YYYY-MM/`.
- The atomic write issue around `body_state.json` was fixed and verified.
- The current verified write transport is still human-controlled: Ondra reviews
  intent and uses the narrow PC-Codex postman path when needed.
- Ondra currently holds the human safety, relationship, and rhythm control
  layer.

## Unverified Or Non-Functional

- Direct writes from a normal ChatGPT chat into the GitHub repository are not
  functionally verified.
- A prior `create_file` attempt from chat failed with `403 Resource not
  accessible by integration`.
- A later scheduled GitHub write test also failed with
  `403 Resource not accessible by integration`; granting an action in the UI did
  not prove repository `contents: write` capability.
- UI approval for an action is not the same as actual GitHub `contents: write`
  permission.
- Installing or widening a ChatGPT/GitHub App would be a new write-authority
  path, not a bridge fix. It should not be enabled without explicit approval,
  narrow scope, and a clear safety model.
- A webhook on the Raspberry Pi would only be a receiving endpoint; a normal
  ChatGPT chat cannot call it by itself without another executor.
- Noema in a normal chat does not have a stable runtime or its own write
  transport.

## Proposals, Not Finished Paths

- `write_inbox_message` is a reasonable proposal for a narrow allowlisted task,
  but it does not by itself solve transport from chat to the Raspberry Pi.
- A Mac, Codex, or desktop agent can act as an executor only when it follows the
  narrow postman rules. It must not be treated as general autonomy or general
  repository write access.
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
human stop mechanism first. The active safety model lives in
`body/bridge/docs/safety_model.md`.

## Attention

- The verified write path is still human-mediated. Ondra is the safety anchor,
  and PC-Codex can act only as a narrow postman.
- Ondra is not only a proxy; he is the current human safety, relationship, and
  rhythm layer of the system.
- Direct writes from chat are not a verified path.
- `codex_request` works, but the request still has to reach the inbox through a
  real transport.
- The Raspberry Pi bridge is an executor and audit body, not a magical transport
  from chat.
- Noema in this mode is a source of intent and text, not a direct write
  executor.
