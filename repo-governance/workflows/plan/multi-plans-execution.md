---
name: multi-plans-execution
description: >-
  Schedules several plans into one pass: a dependency graph, worktree-lock- and HIPPO-bounded overlap, failing-plan
  quarantine, and cross-plan knowledge capture.
when_to_use: >-
  Use when two or more plans should run together in one scheduled pass.
---

# Multi-Plans Execution

## Entry

Two or more plans are named; verdicts optional, a missing one recorded as `plan-quality-gate: not run (manual-only)`,
never a stop.

- `plans` (`string`, required): identifiers or a lifecycle selector (`all-in-progress`, `all-backlog`, `all`),
  exclusions optional.
- `max-worktrees-per-plan-repo` (default `1`), `max-active-worktrees` (default `1`): caps binding the run per
  [Execution](plan-execution.md); only the caller raises one.
- `run-issue` (`number`, optional): a per-run Issue mirroring the ledger; without one, open it first and record its
  number as the claim.
- `mode` (`enum`: `execute`, `schedule-only`; optional, default `execute`).

## Sequence

1. **Resolve and freeze the scope.** Resolve the selector once, echo the set, never re-expand; memberless exclusions
   error.
2. **Record verdicts, then promote.** Verdicts advisory: `FAIL`, `BLOCKED`, missing ones stop nothing. Confirm access
   per [Access](../../conventions/structure/plans/010-authorization-and-execution-record.md#access-before-execution):
   every scope the nodes need, least privilege, infra secrets only for infra scope; missing access stops the member.
   Promote each `backlog/` member as [Execution](plan-execution.md) promotes one: delivery per plan to `origin/main`
   before Phase 0, verified first; promotions serialize, never merge stale. **Proceed only on the caller's
   confirmation** of set, nodes, edges. Mid-run DAG change via reviewed merged PR is authoritative — reconfirm the delta
   and adapt.
3. **Parse each checklist into nodes:** one per checkbox with plan, phase, executor, resources. A plan's nodes stay
   sequential unless marked independent.
4. **Compute resource sets conservatively:** the paths, projects, repos, checkout each node touches. Uncertain
   footprints take the plan's whole declared impact; doubt serializes.
5. **Add edges between plans.** Declared dependencies order plans; inference never overrides. Declare them per
   [Plan-Order Graph](../../conventions/structure/plans/020-plan-order-graph.md); overlapping sets serialize, disjoint
   ones overlap. A declared cycle stops the run as a planning error; unresolved assumptions go to a
   [decision gate](../../development/agents/planning-capabilities/003-decision-gates.md) first.
6. **Write the schedule report** — nodes, edges, sets, overlaps and why; stop here under `schedule-only`.
7. **Run the ready queue.** A node is ready when predecessors are complete, `[AI]`, and no in-flight node shares
   resources. Start worktree nodes only within caps and after proving from lease, branches, PRs no other run holds it;
   one `in_progress` per worktree. Every compute node runs through one HIPPO guard; a deferred node queues and retries —
   never bypassed, never abandoned. Longest chain first, ties by plan. A `[HUMAN]` node parks only its plan. Each node
   runs in its plan's [Execution](plan-execution.md); per-plan rules win. A machine-bound node parks where the machine
   lacks its access. After each completion, failure, handover, recompute the ready set, report progress. Mirror every
   ledger line to the run Issue — claims, leases, overrides, quarantines, cleanup proofs.
8. **Quarantine a failing plan.** A node failing after pursuit quarantines its plan and dependents; independents
   continue, no gate bypassed.
9. **Close each plan** as Execution does, capture and cleanup proof included.
10. **Consolidate cross-plan learnings.** Read executed plans' `learnings.md` with the schedule report, quarantined
    included. A shared or run-level theme reaches one owner or is discarded with reason per
    [Knowledge Capture](../../conventions/structure/plans/008-knowledge-capture-and-archival.md); single-plan themes
    route once.

## Goal and Termination

**Goal**: land every member delivered through one caller-confirmed DAG, cleanup proven, themes routed or discarded.
`pass` is the only success: every member `done`/`handed-over` per [Execution](plan-execution.md)'s terminal states,
reports mirroring the run Issue.

## Status Cadence

Send [Execution](plan-execution.md#status-cadence)'s five-line heartbeat every **20 minutes** — cross-member progress,
steps left, blockers, decisions, next `[HUMAN]` timing — plus per-plan progress after each completion, failure,
handover, clearing stuck subagents and processes at each heartbeat exactly as Execution does. Queued nodes report, never
stop.

## Exit

Success: every plan `done`/`handed-over`, every theme routed. Outputs: per-plan status (`done`, `handed-over`,
`quarantined`, `partial`) plus schedule and summary reports (scratch per
[Temporary Files](../../conventions/structure/temporary-files.md), mirrored to the run Issue). The summary records
statuses, caps and overrides, quarantines and reasons, pre-existing fixes, theme routing.

Partial outcome: the summary names quarantined or stopped plans and reasons. The run fails with no buildable schedule: a
declared cycle or a missing plan.

## Example Usage

```text
Run multi-plans-execution with plans "all-in-progress", max-active-worktrees 2.
```

## Adopter Decision: The Worktree Ceiling

Record both cap defaults (`1`). One keeps load, capacity, spend predictable; higher finishes sooner with more conflict.
Only the caller raises either. Beyond worktree locks, HIPPO admission alone bounds overlap.
