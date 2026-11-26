---
description: >-
  Governs how an orchestrating agent runs work in parallel: a declared concurrency cap, dependency-first dispatch,
  output-polled stuck detection, and verified results.
when_to_use: >-
  Use when spawning background agents, batching independent tool calls, or diagnosing a delegated agent that has gone
  quiet.
---

# Subagent Orchestration

An orchestrator that delegates to background agents works with incomplete information. It sees their eventual results,
not their progress, and three failures follow: too many agents at once collide on rate limits and budget, a stalled
agent never reports, and a result reported as complete turns out not to be.

Each failure has a pre-decided answer here. The cap, the polling interval, the stall threshold, and the adopter's
maximum wait are stated as numbers, so every orchestrator applies them the same way and a reviewer can check them. A
limit inferred from how responsive things feel gets set mid-batch, by the party with the most reason to raise it.

## Modules

1. [Concurrency](subagent-orchestration/001-concurrency.md)
2. [Stuck Detection and Recovery](subagent-orchestration/002-stuck-detection-and-recovery.md)
3. [Results and Reporting](subagent-orchestration/003-results-and-reporting.md)

## Scope

In scope: how many units of work run at once and in what order, how a stalled delegated agent is detected and recovered,
and what an orchestrator does with what comes back. Independent tool calls batched in one turn fall under the
concurrency rules; delegated agents fall under all of them.

Out of scope: a delegated agent's internal behaviour, the shape of agent definitions, and shell-level parallelism inside
a script.

Where the repository runs an admission control for compute-bearing work, that control allocates processor and memory
capacity. The cap here bounds token spend and rate-limit pressure. Each applies on its own terms, and neither
substitutes for the other.
