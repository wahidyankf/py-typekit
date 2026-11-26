---
name: plan-execution
description: >-
  Executes a plan's delivery checklist, recording results.
when_to_use: >-
  Use when a plan's checklist is ready, verdict or not.
---

# Execution

## Entry

A plan in `plans/in-progress/`, checklist ready. Verdicts advisory: `FAIL`/`BLOCKED` open rows keep their owners.
Execution never runs the gate; missing verdicts are recorded as `plan-quality-gate: not run (manual-only)`, never a
stop. For a bug-fix plan, an adopted Upstream Tool Defects standard stays available on request.

A queued plan reaches `plans/in-progress/` only by its own promotion: one pull request (or permitted direct commit)
moving only it to `origin/main`, updating its
[Plan-Order Graph](../../conventions/structure/plans/020-plan-order-graph.md) node, before Phase 0. Worktree from that
fresh trunk; the promotion branch dies at merge.

Inputs: `plan` (directory, required); `max-worktrees-per-plan-repo` (default `1`); `max-active-worktrees` (default `1`).
Only the caller raises a cap.

Mirror the run ledger from the [Temporary Files](../../conventions/structure/temporary-files.md) scratch into one
per-run Issue. Before worktree work, prove from lease, branches, open PRs no other run holds the plan. A stale lease
yields only to an explicit caller override naming it.

Resolve declared dependencies under the [Plan-Order Graph](../../conventions/structure/plans/020-plan-order-graph.md):
each satisfied, else stop and name the unmet; silence is none. On disagreement reconcile the diagram first; mid-run
change via reviewed merged PR is authoritative — adapt it.

## Sequence

1. **Read the plan before the checklist.** `delivery.md` is executable, not self-explanatory; the other five hold why.
2. **Confirm the checkout** — copy, branch or worktree, mode — and enter it synced per
   [Integration Path](../../development/workflow/integration-path.md); each unit reuses the plan's one worktree where
   used. Confirm access per
   [Access](../../conventions/structure/plans/010-authorization-and-execution-record.md#access-before-execution): every
   scope the plan needs, least privilege, infra secrets only for infra scope; missing access stops the run.
3. **Mirror the checklist, disk first.** Each start or resume rebuilds tasks from `delivery.md`: one per unchecked
   checkbox, in dependency order, none without one. Untick and rerun items missing their change; dormant recoveries stay
   inactive until triggered.
4. **Work ready items under the worktree lock.** Dispatch dependency-terminal items: one `in_progress` per worktree,
   every compute node through one guard per
   [Resource-Aware Development](../../development/workflow/resource-aware-development.md). A deferred guard queues —
   retry it, never bypass, never abandon. Failures block only downstream. Record external blockers and unblockers. Hand
   `[HUMAN]` items over unperformed, prepared. Revise `delivery.md` before reordering; material changes re-pass the
   quality gate. Code-shipping items use batched cycles per
   [Phase Boundaries](../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md).
5. **Resolve each item atomically.** Tick, record, move on — one step, in order, only with outcome and proof held; note
   product, change, surprise. No end-of-session batch ticks.
6. **Pass each phase gate before the next** per
   [Phase Boundaries](../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md): run each check as
   written, repair in phase; fix every failure, pre-existing included.
7. **Land each delivery unit** via the Integration Path when
   [landed](../../conventions/structure/plans/009-portability.md#what-landed-means); gates re-run on refresh.
   Independent units land in any order.
8. **Route discoveries** to `learnings.md` (or a bug-fix plan's Learnings) as they arise; add a task only for a planned
   outcome.
9. **Run [Execution Check](plan-execution-check.md)** once substantive items are terminal; only its verdict permits
   archival; cleanup may pend.
10. **Archive and finish delivery** per
    [Knowledge Capture](../../conventions/structure/plans/008-knowledge-capture-and-archival.md): mark dormant
    recoveries dated `Not triggered`; archive and land, retaining worktree and branches. Run
    [Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md), recording proof outside `plans/done/`. The task
    stays open until cleanup verifies per
    [Dependency Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md).

## Goal and Termination

One end state; `pass` is the only success:

- **`pass`**: all items terminal, check permits archival, delivery landed and verified, plan in `plans/done/`,
  worktree/branches gone, learnings routed or discarded.
- **`handed-off`**: `[AI]` work ready, only a `[HUMAN]` merge or decision remains. No archive or cleanup; resume to
  `pass` after confirmation.
- **`partial`**: findings remain or work unexecuted. Plan stays in `plans/in-progress/` with its location; blockers and
  unblockers only.
- **`fail`**: a technical error blocks completion; plan and work location stay for diagnosis.

## Exit

Only the Execution Check permits archival and `pass`. Cleanup may pend in `plans/done/`; task completion awaits proof
per [Dependency Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md).

## Status Cadence

Milestones carry ordinary progress. Independently send a user-visible five-line heartbeat every **20 minutes** —
weighted progress, steps left, blockers, decisions, next `[HUMAN]` timing — plus phase boundaries and terminal states.
Weights from `delivery.md`, else `1` each. A queued node is reported, never a stop. At each heartbeat, clear owned
subagents and processes of stuck work: `in_progress` with no progress since the last heartbeat and no guard or error
reason is stuck — list it under blockers, nudge once, escalate if stuck again next.

## Pause Safety

Execution may pause anytime. Record checkout, last gate, next item, consumed budget; resume whole.
