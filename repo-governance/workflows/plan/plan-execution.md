---
name: plan-execution
description: >-
  Works through a plan's delivery checklist, recording the result of each item as it resolves.
when_to_use: >-
  Use when a plan's checklist is ready, with or without a quality-gate verdict.
---

# Execution

## Entry

A plan in `plans/in-progress/`, checklist ready. A quality-gate verdict in `delivery.md`, when present, is advisory
history: `FAIL`/`BLOCKED` open rows keep their owners. Execution never runs the gate; a missing verdict records as
`plan-quality-gate: not run (manual-only)`, never a stop. An adopted Upstream Tool Defects standard stays available on
explicit invocation.

A queued plan reaches `plans/in-progress/` only by its own promotion: one pull request moving only it to `origin/main`,
before Phase 0. Worktree from that fresh trunk; the promotion branch dies at merge.

Resolve declared dependencies per
[Dependency Graph and Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md): each satisfied,
or stop at the unmet one; a mid-run graph change in a reviewed merged PR is authoritative — adapt.

Inputs: `plan` (`directory`, required); `max-worktrees-per-plan-repo`, `max-active-worktrees` (defaults `1`,
caller-raised only).

Mirror the run ledger from ignored `local-tmp/` scratch per
[Temporary Files](../../conventions/structure/temporary-files.md) into one per-run Issue, opened first as the claim;
prove sole ownership from lease, branches, open PRs; a stale lease yields only to an explicit caller override.

## Sequence

1. **Read the plan before the checklist.** `delivery.md` is executable, not self-explanatory; the other five hold why.
2. **Confirm the checkout** — copy, branch or worktree, mode — and enter it synced per
   [Integration Path](../../development/workflow/integration-path.md); each unit reuses the plan's one worktree where
   used. Then prove access from the plan's scope alone — least privilege, infra secrets only for infra scope, portable
   versus machine-bound per need; missing access stops the run.
3. **Mirror the checklist, disk first.** Each start or resume rebuilds tasks from `delivery.md`: one per unchecked
   checkbox, in dependency order, none without one. Untick and rerun items missing their change; dormant recoveries stay
   inactive until triggered.
4. **Work ready items under the worktree lock.** Dispatch dependency-terminal items: one `in_progress` per worktree,
   every compute node through one guard — a deferred guard queues, so retry it, never bypass or abandon. Failures block
   only downstream. Record outside blockers and unblockers. Hand `[HUMAN]` items over unperformed, prepared. Revise
   `delivery.md` before reordering; material changes re-pass the quality gate.
5. **Resolve each item atomically.** Tick, record, move on — one step, outcome and proof held; no end-of-session batch
   ticks.
6. **Record results, not only ticks** — product, change, surprise — per
   [Verification Routing](../../development/agents/planning-capabilities/006-verification-routing.md). Ship code in
   RED-GREEN cycles — one RED plus one GREEN per batch, selection frozen — per
   [Red-Green-Refactor](../quality/red-green-refactor.md).
7. **Pass each phase gate before the next** per [Phase Boundaries and Delivery
   Choices][011-phase-boundaries-and-delivery-choices]: run each check as written, repair in phase; fix every failure,
   pre-existing included.
8. **Land each delivery unit** by the route Integration Path records; a unit is complete once it has
   [landed](../../conventions/structure/plans/009-portability.md#what-landed-means). Independent units land in any
   order, gates re-run on refresh, per
   [Delivery Seams and Ownership](../../development/agents/planning-capabilities/005-delivery-seams-and-ownership.md).
9. **Route discoveries to `learnings.md`** (or a bug-fix plan's Learnings) as they arise; add a task only for a planned
   outcome.
10. **Run [Execution Check](plan-execution-check.md)** once substantive items are terminal; only its verdict permits
    archival; cleanup may pend.
11. **Archive and finish delivery** per
    [Knowledge Capture](../../conventions/structure/plans/008-knowledge-capture-and-archival.md): mark dormant
    recoveries dated `Not triggered`; archive and land, retaining worktree and branches. Run
    [Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md), recording proof outside `plans/done/`. The task
    stays open until cleanup verifies per
    [Dependency Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md).

See [Task Tracking](../../development/agents/task-tracking.md).

## Goal and Termination

`pass` is the only success: items terminal, check permits archival, delivery landed, plan in `plans/done/`, worktree and
branches gone, learnings routed. `handed-off`: `[AI]` ready, only a `[HUMAN]` step remains; resume to `pass`. `partial`:
findings remain or work unexecuted; plan stays with blockers and unblockers. `fail`: technical error blocks; both stay.

## Exit

Only the Execution Check permits archival and `pass`. Post-delivery cleanup may pend in `plans/done/`; task completion
awaits proof per [Dependency Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md).

## Status Cadence

Send a five-line heartbeat every **20 minutes** — progress, steps left, blockers, decisions, next `[HUMAN]` timing
(`delivery.md` weights, else `1` each) — plus phase boundaries and terminal states. A queued node is reported, never a
stop. Each heartbeat clears owned subagents and processes of stuck work — `in_progress` with no progress since the last
heartbeat and no guard or error reason: nudge once, escalate if still stuck next.

## Pause Safety

Execution may pause anytime. Record checkout, last gate, next item, consumed budget; resume whole.

[011-phase-boundaries-and-delivery-choices]:
  ../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md
