---
description: >-
  Requires a long-running automation loop to exercise its real dependencies in a startup preflight that exits on
  failure, and to write the raw error output of every failed call into its log.
when_to_use: >-
  Use when writing or reviewing a watcher, poller, queue consumer, runner manager, or any process that repeats work
  unattended.
---

# Automation Loop Observability

A long-running automation loop has a failure mode a one-shot script lacks: it stays up, keeps appending to its log, and
accomplishes nothing. Every outside signal reads as healthy while the one operation that matters fails on each pass.

Two defects together can hide this for days: a health check that exercises something other than the real operation, and
error handling that throws away what the dependency actually answered.

This standard implements [Fail Closed](../../../principles/fail-closed.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Root Cause Orientation](../../../principles/root-cause-orientation.md).

## Scope

It covers any process that repeats work unattended and can keep running while that work fails: watchers, pollers, queue
consumers, runner managers, and agents on a schedule.

It does not cover a one-shot script, which exits and so shows its failure to whoever ran it; a pipeline job, whose host
displays a failed job by design; or an interactive tool, whose output a person is reading.

## Preflight the Real Operation

At startup, before the first iteration, the loop calls each critical dependency exactly as the loop will: the same
operation, the same kind of target, the same credentials. It asserts a specific positive signal in the reply: a field
that must be present, the status code it expects, or the outline of a valid answer.

A stand-in for the dependency does not count:

| Stand-in check                   | Shows                                  | Leaves unshown                                     |
| -------------------------------- | -------------------------------------- | -------------------------------------------------- |
| a credential exists or signs in  | there is a credential                  | whether it may perform the write the loop performs |
| the host answers                 | the network route and name lookup work | whether that particular endpoint takes the request |
| a configuration file loads       | its syntax is acceptable               | whether its values name anything that works        |
| a read against the service works | reading is permitted                   | whether creating, changing, or deleting works      |

When the preflight creates something, such as a probe record or a test object, it gives the probe a unique name, removes
it on success, and leaves nothing harmful if removal fails. A failed removal is logged and does not stop the loop from
starting. A fixed probe name collides with the previous run's leftover and fails the preflight against a healthy
dependency.

When the preflight fails, the process exits unsuccessfully and never enters its loop. The supervisor restarts it with
backoff, and a process that keeps exiting shows up in supervisor status in a way a quietly looping one never does.
Logging a warning and carrying on rebuilds the silent loop the preflight was there to prevent.

## Keep What the Dependency Said

Every external call inside the loop captures its error stream along with its output, and every log line about a failure
includes that raw output unaltered.

- Never discard the error stream. The status, redirect, or permission message it carries is usually the whole diagnosis.
- Never substitute a message of the script's own for the raw output. A line such as "no result returned" records what
  the script believed; while a loop is failing silently, that belief is wrong by definition. Log the interpretation and
  the raw output side by side.

```bash
# Merge the error stream into the captured text; tolerate a failed call so the diagnostic is still written.
raw=$(<external-command> 2>&1) || true
if ! printf '%s' "$raw" | jq -e '.<required-field>' >/dev/null; then
  log "ERROR: <operation> gave no <required-field>; raw output follows: $raw"
fi
```

Tolerating the exit status there is deliberate. Under the strict mode [Shell Scripts](../code/shell-scripts.md)
requires, an unhandled failure would end the script before the diagnostic reached the log, so the failure is handled in
the open, in the loop, instead of by the shell.

## Enforcement

Review applies both requirements. An adopter enforces the mechanical part in its own lint or review checklist for loop
scripts, for example by rejecting a discarded error stream in them.
