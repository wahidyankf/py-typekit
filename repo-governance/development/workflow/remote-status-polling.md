---
description: >-
  Spaces repeated status reads against a rate-limited hosting service at least three minutes apart, forbids streaming
  watches, forbids retriggering a workflow with an active or recent run for the same commit, and recovers from a rate
  limit by waiting.
when_to_use: >-
  Use when waiting on a pipeline run, pull request checks, a deployment, or other remote state behind a request budget,
  or when a status read has just been rate-limited.
---

# Remote Status Polling

Every remote state read spends from a request budget the whole account shares. Asking more often finishes no run sooner,
and a spent budget stops other work too.

This standard sets the mechanics behind the polling step of [CI Post-Push Verification](ci-post-push-verification.md)
and the spacing inside the ceiling every remote wait declares under [Bounded Convergence](bounded-convergence.md). It
implements [Minimal Sufficiency](../../principles/minimal-sufficiency.md) and
[Deliberate Problem-Solving](../../principles/deliberate-problem-solving.md).

## Scope

Any repeated read of state a remote, rate-limited service holds, such as a pipeline run, a pull request's checks, or a
deployment, through any client, a browser refresh included. A single lookup is not polling; a second read awaiting the
same change is.

## The Interval

| Rule           | Requirement                                                                                  |
| -------------- | -------------------------------------------------------------------------------------------- |
| spacing        | three to five minutes between reads of the same state; slower is always allowed              |
| one read       | each poll is one bounded status request, read in full before deciding to ask again           |
| known duration | when a run's usual duration is known, the first read waits that long instead of the interval |
| event first    | where the service offers a completion event or notification, prefer waiting on it to polling |

A gate usually taking eight minutes gets its first read at eight minutes. Time between reads belongs to independent
work, not watching.

## Never Stream

A watch command, a follow of a running log, an automatic refresh, and any long-lived connection that reports as state
changes are forbidden. Their request rate belongs to the tool, not the caller: a watch refreshing every three seconds
makes about six hundred reads over a thirty-minute run; spaced polling needs about ten.

## Trigger Discipline

1. Before triggering a workflow for a commit, read whether a run for that commit is already queued or in progress. If
   one is, follow that run instead of starting another.
2. Never trigger the same workflow for the same commit again within ten minutes of its last trigger.
3. When a newer run cancelled an older one, trigger nothing until the newer run reaches a terminal result.

A fix pushed as a new commit starts its own runs, followed at once. An extra run for one commit spends requests on its
setup and reads; where a concurrency rule cancels the older run, a hasty retrigger leaves both non-green, proving
nothing.

## When a Run Looks Stuck

First confirm a run exists for the pushed commit. Where none does, waiting never helps: find why the change started
none, such as a conflict with its base.

A run not yet reported is no evidence of a fault. Say it is still pending, and read again after the interval, within the
wait's declared ceiling. Past the run's known duration plus a recorded margin, report it as stuck rather than pending.
Retriggering a slow run adds a second run to await and resets the first's evidence.

## Recovering From a Rate Limit

1. Stop every call to the service at the first response the service identifies as a rate limit; the same status can mean
   an authorization failure. Never retry in a loop: each retry spends from the budget the reset is refilling.
2. Wait until the reported reset time plus a small margin. Where none is reported, wait at least thirty-five minutes.
3. Make one light read to confirm the limit has cleared, then resume at the normal interval.
4. If the limit still holds, wait again the same way, within the wait's declared ceiling, and make no other call.

## Enforcement

An adopter enforces this where its automation issues status reads, such as a shared polling helper with the interval
built in, or a review rule rejecting watch commands and unspaced loops in scripts and pipeline definitions.
