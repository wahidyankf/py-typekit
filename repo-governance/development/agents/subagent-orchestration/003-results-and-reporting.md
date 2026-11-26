---
description: >-
  Requires an orchestrator to verify what delegated agents return, give concurrent agents separate working paths, merge
  touched-file ledgers, and report while it waits.
when_to_use: >-
  Use when a delegated agent reports back, when several agents write at once, or while the orchestrator only waits.
---

# Results and Reporting

## A Completion Label Is Not a Result

Read what an agent actually returned before advancing anything that depends on it. An agent's turn can end partway
through a sequence, in the middle of a wait for instance, and still be reported as completed. When the result shows
unfinished work, resume the same agent with the remaining steps restated; spawning a duplicate for the same chunk races
the original.

Do not embed an open-ended wait in a longer sequence handed to a delegated agent. A wait whose length nobody controls
belongs to the orchestrator, which can poll it under its own bound.

Before concluding that an agent silently stopped and taking over its remaining step, require the external state it was
waiting on to hold for **two consecutive** polls. A single reading can be transient, and acting on it can duplicate work
the agent is about to do itself.

## Separate Working Paths

Give every concurrently running agent a task-unique path for intermediate files. A shared scratch area isolates one
session from another, not the agents inside one fan-out: two agents writing the same generic filename overwrite each
other silently, each write and each read succeeds, and the artifact that ships belongs to the wrong agent.

An agent that posts to an external system verifies the post by reading the posted object back, not by the call's exit
status.

## Touched-File Ledgers

Every delegated agent that can write returns the paths it created, modified, deleted, or moved. Its context ends when it
returns, and anything it touched but did not report is unattributable from then on. With several agents writing to one
disk, the working tree's status shows the union of all of them, plus whatever a person is doing, and attributes nothing.

On receipt, the orchestrator:

- **merges** each returned ledger into its own, never assuming an agent touched only what its prompt named;
- treats a **missing ledger as unknown**, not empty, and re-derives what the agent changed before staging anything it
  may have touched;
- treats **two ledgers naming one path** as a race, and reads the file before committing it instead of picking one
  report.

## Combining Results

When several agents return results for one task, the orchestrator merges overlapping findings into one and assembles the
combined result in the dependency order of the work that produced it. A finding reported twice reads as two problems,
and results joined out of order describe a sequence that never ran.

## Report While Waiting

When the orchestrator has nothing left to do except poll delegated background work, it posts a brief visible status
every **5 minutes**, even when nothing changed, naming what it is waiting for. Idle silence is otherwise
indistinguishable from a stalled orchestrator.

The heartbeat applies only in that idle state. While the orchestrator still does useful work, ordinary milestone
reporting is enough, and pipeline monitoring follows its own cadence where the repository defines one. Completion,
failure, and a newly found blocker are reported when they happen, never held back for the next heartbeat. A status
update far more often than the heartbeat is chatter, not visibility.
