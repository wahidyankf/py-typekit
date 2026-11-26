---
name: plan-execution-check
description: >-
  Evaluates substantive execution and pre-archive cleanup, records archive readiness, and names post-delivery cleanup
  that remains pending.
when_to_use: >-
  Use once every substantive delivery item is terminal and before the archival move.
---

# Execution Check

## Entry

Every substantive item in `delivery.md` is terminal. Post-delivery cleanup may remain explicitly `pending` under
[Dependency Graph and Recovery](../../conventions/structure/plans/014-dependency-graph-and-recovery.md). Archival has
not started.

## Sequence

The evaluation runs in this fixed order. The order matters: each step assumes the previous one held, and reordering
produces findings that contradict each other.

1. **Scope.** Did the executed work match the plan's stated scope — nothing quietly added, nothing quietly dropped?
2. **Requirements.** Is every acceptance criterion terminal, and does its evidence actually establish it?
3. **Checklist evidence.** Does every completed item carry a result, and does the result match what the repository now
   contains?
4. **Gates.** Did every declared gate run and return a terminal result, including the ones that returned findings?
5. **Cleanup.** Is all cleanup required before archival complete and proven? Are the worktree, local and remote task
   branches, and other post-delivery removals explicitly recorded as `pending` in `delivery.md` for cleanup after the
   final delivery lands?
6. **Knowledge capture.** Is every `learnings.md` entry resolved to a durable owner or discarded with a reason?

Where a step asks for past proof that can no longer be produced, judge the recorded observation of current behaviour
that replaces it, per
[Current Behaviour Over Past Proof](../../development/quality/evidence/current-behaviour-over-past-proof.md). A missing
past record alone is not a finding.

## Exit

One terminal archive-readiness verdict is recorded. Archival proceeds only on a verdict that permits it. The verdict
does not claim post-delivery cleanup is complete; the task remains open until actual cleanup is verified and recorded in
the final delivery record outside `plans/done/` (the archival PR body for a pull-request route).

## Archival Is Blocked, Not Warned

An unresolved acceptance criterion, an unproven pre-archive cleanup, or an unrouted learning blocks archival outright.
Required post-delivery cleanup must be marked `pending`, never `met`, and does not block archive readiness. It remains a
task obligation: final task completion is blocked until cleanup is verified and its proof is recorded in the final
delivery record. This check judges substantive execution and is not a quality gate, so the advisory verdicts of the
[Quality Gate Contract](../../development/workflow/quality-gate-contract.md) do not cover it.

This is strict by design. A plan in `plans/done/` records completed substantive execution and archive readiness. An
explicitly pending post-delivery cleanup remains visible in the archived checklist, and the external final delivery
record must prove it before the task is called complete.

Resolve any blocking item and re-run the check. There is no partial archival and no archival with an unresolved
acceptance criterion, pre-archive cleanup, or unrouted learning.
