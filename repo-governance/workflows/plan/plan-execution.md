---
name: plan-execution
description: >-
  Works through a plan's delivery checklist, recording the result of each item as it resolves.
when_to_use: >-
  Use when a plan's quality gate verdict is recorded and its checklist is ready to be executed.
---

# Execution

## Entry

A plan in `plans/in-progress/` whose quality gate verdict is recorded in its `delivery.md`. The verdict is advisory: any
of the four lets execution start, and a `FAIL` or `BLOCKED` verdict's open blocking rows keep the owners the gate gave
them.

The verdict is current and comes from an explicitly directed gate run; without one, execution stops and says so. For a
bug-fix plan, an adopted Upstream Tool Defects standard is that direction. A queued plan is moved into
`plans/in-progress/` first, never copied. Input: `plan` (`directory`, required).

## Sequence

1. **Read the plan before the checklist.** `delivery.md` is executable, not self-explanatory; the other five documents
   hold why each item exists.
2. **Confirm the execution checkout:** which working copy, branch or worktree, and delivery mode. A wrong checkout
   noticed late is expensive. Enter it, synced per [Integration Path](../../development/workflow/integration-path.md),
   before any change; every delivery unit reuses the plan's one worktree when its route uses one.
3. **Mirror the checklist, disk first.** On every start and resume, rebuild the task list from `delivery.md`: one task
   per unchecked action checkbox, in order, and none without one. A tick whose change is absent is removed and its item
   re-run. Dormant recovery items wait for their trigger. See
   [Task Tracking](../../development/agents/task-tracking.md).
4. **Work items in order.** An item blocked by something outside the plan is recorded as blocked, with what would
   unblock it, never skipped silently. A `[HUMAN]` item is prepared as far as possible, then handed over, never
   performed or ticked on that person's behalf.
5. **Resolve each item atomically.** Tick the checkbox, record the result, and move on, in that order, as one step; a
   batch of ticks at session end cannot say which item produced which result. Tick only once the item's outcome and its
   proof both hold.
6. **Record results, not only ticks:** what was produced, what changed, what surprised. A tick says an action happened,
   not what it found. See
   [Verification Routing](../../development/agents/planning-capabilities/006-verification-routing.md).
7. **Pass each phase gate before the next phase.** Per [Phase Boundaries and Delivery
   Choices][011-phase-boundaries-and-delivery-choices], run each gate check as written against the phase's combined
   state, and repair a failure inside the phase before its delivery or the next phase starts.
8. **Land each delivery unit** by the route Integration Path records; a unit is complete once it has
   [landed](../../conventions/structure/plans/009-portability.md#what-landed-means).
9. **Fix what fails, including what was already failing.** A check red before the plan started is, by shipping time, red
   because of this plan's work. Pre-existing explains; it never exempts.
10. **Route discoveries to `learnings.md`**, or a bug-fix plan's Learnings section, as they happen, not from memory.
    Discovered work becomes a new checkbox only when it serves an outcome the plan already has.
11. **Run [Execution Check](plan-execution-check.md)** once every substantive item is terminal.
12. **Close out on a permitting verdict.** Give each dormant recovery item a dated `Not triggered` disposition with its
    evidence, run [Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md) once every delivery unit has landed,
    and archive per
    [Knowledge Capture and Archival](../../conventions/structure/plans/008-knowledge-capture-and-archival.md).

## Exit

Every substantive checklist item is terminal, `learnings.md` holds what execution discovered, and the execution check
has recorded a verdict.

Only the execution check closes a plan. The quality gate judges a plan before execution and after a material change,
never the delivered work, so it is not re-run at the end or before interrupted work resumes.

Partial outcome: only blocked items remain, each recording what would unblock it; the plan stays in `plans/in-progress/`
and the execution check waits. A failed run keeps any worktree and records why.

## Pause Safety

Execution can stop anytime, so the plan itself must always carry enough state to resume: the current checkout, the last
terminal gate, the next unresolved item, and any bounded budget partly consumed. A resumed session continues a budget,
never resets it.

[011-phase-boundaries-and-delivery-choices]:
  ../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md
