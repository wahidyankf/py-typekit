---
description: >-
  Keeps an application users can reach available while work on it continues: invariants that hold throughout, a blocking
  preflight before material changes, verified release cutover, and disciplined restarts.
when_to_use: >-
  Use before changing, releasing, or restarting an application that users can reach while the work is under way.
---

# Live-Service Continuity

This standard applies whenever an application the repository owns is reachable by a user while work on it continues. An
explicit no-downtime requirement is blocking, not aspirational.

Treat the service as in use even when no traffic is visible. Never infer an idle or maintenance window from the time of
day, from process activity, or from the fact that the work is development.

It implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md),
[Immutability](../../../principles/immutability.md), and
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md).

## Modules

1. [Invariants](live-service-continuity/001-invariants.md)
2. [Release Cutover](live-service-continuity/002-release-cutover.md)
3. [Restart Discipline](live-service-continuity/003-restart-discipline.md)

## The Blocking Gate

Before a material change:

1. Identify the active server and any proxy in front of it.
2. Record baseline health and responsiveness at the exact route users reach, with enough samples to compare against, and
   name the responsiveness budget in numbers before the work starts.
3. Decide whether the change can affect compilation, startup, routing, authentication, storage, or a journey a user is
   part-way through.
4. If it can, and no independent healthy backend exists, establish one before editing anything.

Stopping the only process and starting it again is not a zero-downtime change, however quickly it comes back.

## When the Live Surface Degrades

If any active check fails or the responsiveness budget is exceeded, stop unrelated work at once, and then:

1. restore the last healthy backend, or route traffic back to it;
2. verify the user journey and the budget;
3. capture what happened as a learning, with nothing private in it; and
4. only then resume.

Never continue a plan while the live surface is degraded. A plan whose work involves a cutover makes continuity and
rollback explicit in its delivery checkpoints.
