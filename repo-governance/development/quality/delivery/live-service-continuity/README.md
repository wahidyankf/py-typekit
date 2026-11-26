---
description: >-
  Indexes the ordered modules holding the invariants, release cutover rules, and restart discipline for keeping a
  user-reachable service available during work.
when_to_use: >-
  Use to locate the module that governs one part of changing, releasing, or restarting a live service.
---

# Live-Service Continuity Modules

The [Live-Service Continuity](../live-service-continuity.md) entrypoint indexes the rule these modules hold; read them
in sequence.

## Directory Map

- [001 Invariants](001-invariants.md) — what stays true throughout a change: availability, responsiveness, served
  revision, the last good version, shared state, and cleanup
- [002 Release Cutover](002-release-cutover.md) — immutable artifacts, revision-checked candidates, explicit migrations,
  connection-safe traffic cutovers, and rollback before diagnosis
- [003 Restart Discipline](003-restart-discipline.md) — reusing the identified server, keeping it where its owner
  watches it, and restarting when its inputs change
