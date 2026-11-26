---
description: >-
  Lists the availability, responsiveness, revision, last-good-version, shared-state, and cleanup invariants that hold
  for a live service through every step of a change.
when_to_use: >-
  Use when planning or reviewing a change to a live service, to check what must stay true at each step.
---

# Invariants

These invariants hold on any hosting platform. Where a rule names a proxy, a port, or a working copy, it describes a
self-hosted service as an example; a managed platform or orchestrator meets the same rule through its own mechanism.

## Availability and Responsiveness

- The active endpoints, local and routed, are never left refusing connections, timing out, returning unexpected server
  errors, or exposing a half-finished authentication or data cutover.
- A successful status code is evidence of availability, not of responsiveness. Sample the exact user-facing route
  continuously through preflight, gates, candidate qualification, promotion, and drain, against a numeric budget: the
  failures allowed, a percentile latency, and a maximum for any single sample. A plan may tighten the budget; loosening
  it is a governance change, never an exception taken during implementation.

## History Is Not Deployment

- A commit or a push changes repository history only. It does not update a running service or prove which revision that
  service runs.
- Before reporting a change to a live service complete, verify that the routed service serves the intended revision or
  its observable behaviour. If it does not, complete a no-downtime cutover first.

## Keep the Last Good Version

- Preserve the last usable reader and writer until the replacement passes its normal read-back and the critical user
  journey.
- Keep a stable serving version independent of the work being edited. Start and verify a replacement beside the active
  version, then switch traffic to it with a cutover that drops no held connection. On a self-hosted service, for
  example, the replacement runs on a separate port outside the working copy, and a proxy's graceful reload performs the
  cutover.
- Retain the previous healthy backend until the replacement passes local, routed, and any real-time connection checks.
- Never edit dependency, configuration, runtime, or supervision inputs underneath the only active server that reloads
  code. Those inputs can break the running process before any planned restart.

## Shared State

- When two versions can reach one mutable store, their schemas and locking are mutually compatible; otherwise only the
  active version writes.
- Long-lived connections drain within a bounded period. Compatible clients reconnect by themselves and never need a
  manual refresh.
- Acknowledged state shared by several clients lives outside any single connection's process. Reconnection uses a stable
  session identity, an ordered catch-up sequence, and idempotent command identifiers. Presence and connection ownership
  are ephemeral, never authoritative state.

## Leave Only What Serves

After final verification and any drain, stop every non-production server, watcher, candidate, and temporary proxy the
work no longer needs. Keep the active route and any capacity deliberately retained for rollback. Cleanup left undone
means the work is not finished.
