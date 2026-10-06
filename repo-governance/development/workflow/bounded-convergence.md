---
description: >-
  Requires every repeated operation to declare a finite bound and a progress measure before it starts, and to end in a
  recorded terminal result.
when_to_use: >-
  Use when designing any step that can repeat, retry, poll, or iterate until something is satisfied.
---

# Bounded Convergence

Any step that can repeat must be bounded before its first cycle, not when it becomes worrying.

The failure this prevents is specific and common: "try until it passes". It sounds like diligence. It is an unbounded
loop whose termination depends on the problem being solvable by the method being retried — and when it is not, the loop
spends everything available and then stops for a reason unrelated to the work.

## Modules

1. [The Loop Register](bounded-convergence/001-loop-register.md)
2. [Resolving at the Ceiling](bounded-convergence/002-ceiling-scorecard.md)

## What Counts as Repetition

A repeated operation is anything that can run more than once: a retry, a poll, a repair cycle, an iteration over a
worklist, a review that can be re-run.

Not everything that looks repetitive is. A fixed sequence of three named steps is three steps. A worklist processed
once, each item exactly once, is an iteration with a known bound. The distinguishing question is whether there is a path
back to something already done, decided by a result.

## Quality Gates Follow Their Own Contract

A quality gate, a workflow that checks, repairs, and checks again, follows the
[Quality Gate Contract](quality-gate-contract.md) instead of the loop register and ceiling scorecard. The register and
scorecard govern every other repeated operation: retries, polls, worklists, and repair loops outside a gate.

## Defaults for Iterative Gates

The catalog decides a gate's defaults once, in the contract, so they cannot drift from gate to gate:

| Input or signal  | Rule                                                                                         |
| ---------------- | -------------------------------------------------------------------------------------------- |
| strictness level | `mode`, default `normal`: the least strict level that still blocks every real defect         |
| cycle ceiling    | `max-cycles`, 1 to 3, default 3; a repository or caller may lower it, never raise it above 3 |
| early warning    | none; a gate declares no warning cycle, and nothing adds a cycle as the ceiling nears        |

A judging workflow whose flow is finite by construction is a review, not a gate. It declares that one flow, exposes no
ceiling input, and never invents a loop in order to bound it.
