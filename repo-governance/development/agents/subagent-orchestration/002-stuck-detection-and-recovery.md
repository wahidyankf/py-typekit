---
description: >-
  Fixes chunk sizing, the output-polling cadence and stall threshold for delegated agents, and the stop, relaunch,
  split, and report recovery procedure.
when_to_use: >-
  Use when sizing work for a background agent, or when an agent has run long enough that it may have stalled.
---

# Stuck Detection and Recovery

A delegated agent occasionally stalls, most often because it spent its output budget planning structure before producing
content. It may never send a completion signal, and an orchestrator that waits only for that signal waits indefinitely.

## Size Chunks for Observability

Size each delegated chunk so its expected runtime is **3 to 10 minutes**. Small chunks keep a batch observable, limit
what is lost when one stalls, and fit within a healthy output budget. Tune per kind of agent from observed runtimes:
smaller when that kind stalls repeatedly, larger only cautiously when its runs consistently finish in under 2 minutes.

## Two Signals

Completion notifications are the primary signal. Output polling is the secondary signal, used to detect stalls; it never
substitutes for completion.

At spawn, record each agent's identifier beside the output path it was told to write, if it has one. The identifier is
what stops or messages the agent, and a harness may not list it anywhere afterwards.

## Polling

While delegated agents run in the background, poll every **3 minutes**. Inspect the metadata of the output file each
agent was instructed to write, meaning its modification time and size, not its content.

Never read an agent's transcript to check progress. It grows with every tool call, and reading it floods the
orchestrator's context and degrades every decision that follows. Polling much more often than every 3 minutes spends
tool calls without detecting a stall any sooner.

## Stall Threshold

An agent is stuck when either condition holds:

- its output file has not changed for **30 minutes** since the last observed change, or since launch if it never
  changed; or
- no completion has arrived after roughly **three times** the runtime of peers that finished in the same batch.

An agent with no output file, such as one that returns its findings to its caller, is judged by the second condition.
While no peer has finished, or when it runs alone, it is stuck once no completion arrives within the maximum wait the
adopter records as a number before any such agent is spawned; the orchestrator records that value at spawn, beside the
agent's identifier.

| Signal                       | Healthy                | Stuck                                        |
| ---------------------------- | ---------------------- | -------------------------------------------- |
| first output change          | within 3 to 10 minutes | never, or after 30 minutes                   |
| output size across polls     | grows                  | flat                                         |
| completion relative to peers | shortly after them     | long after them                              |
| final content, once complete | a finished section     | stops mid-sentence or on a planning sentence |

## Recovery

1. Stop the agent by its recorded identifier.
2. Relaunch it with the same instructions and the same output path.
3. Record the relaunch in the batch's tracking state, so a second stall on the same chunk is recognized.
4. On a second stall, split the chunk in half and run the halves one after the other, not in parallel.
5. If a half stalls again, stop it and report the chunk to the caller as unrecovered, naming each stall.

Relaunch comes before any diagnosis because the usual cause, an output budget spent on planning, clears on a fresh
start: a new agent has its full budget. Splitting shrinks the task that exhausted the budget. A stall that survives both
points to something in the chunk itself, which the caller has to decide about. Reporting is the bound on recovery: the
same chunk is never relaunched indefinitely, as [Bounded Convergence](../../workflow/bounded-convergence.md) requires of
any repeated operation.
