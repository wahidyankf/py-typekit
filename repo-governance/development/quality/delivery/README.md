---
description: >-
  Indexes the delivery standards: keeping a user-reachable service available through changes, observing long-running
  automation, and keeping hosted pipeline storage inside a budget.
when_to_use: >-
  Use when changing or restarting a live service, running a long-lived automation loop, or managing what a hosted
  pipeline stores.
---

# Delivery Standards

Delivery standards. They answer how running services, automation loops, and pipelines stay available, observable, and
within budget.

## Directory Map

- [Automation Loop Observability](automation-loop-observability.md) — startup preflights and raw error output for
  long-running loops
- [CI Storage Budget](ci-storage-budget.md) — artifact retention, bounded caches, and a spend limit that stops runs
- [Live-Service Continuity](live-service-continuity.md) — keeping a user-reachable service available through changes,
  releases, and restarts
- [Live-Service Continuity Modules](live-service-continuity/README.md) — the modules on invariants, release cutover, and
  restart discipline
