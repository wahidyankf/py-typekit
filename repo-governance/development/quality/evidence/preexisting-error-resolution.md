---
description: >-
  Requires a gate that was already failing before a change to be triaged, root-caused, fixed as its own change, and
  verified before the blocked work continues, and never skipped, disabled, or bypassed.
when_to_use: >-
  Use when a quality gate or pipeline check fails for a reason the current change did not introduce.
---

# Preexisting Error Resolution

A gate that was red before a change arrived is still red when that change ships. That the failure predates the work is
an explanation, not an exemption, as [Plan Execution](../../../workflows/plan/plan-execution.md) and
[What Minimality Never Removes](../../../principles/minimal-sufficiency/002-what-minimality-never-removes.md) already
state. This standard says how such a failure is resolved.

It implements [Root Cause Orientation](../../../principles/root-cause-orientation.md) and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Modules

1. [Triage and Investigation](preexisting-error-resolution/001-triage-and-investigation.md)
2. [Pipeline Availability](preexisting-error-resolution/002-pipeline-availability.md)

## The Rule

When a preexisting failure blocks a gate:

1. **Triage** whether it is a defect at all, then **investigate** its cause, as the first module describes.
2. **Fix the cause** with the smallest correct change.
3. **Land the fix on its own**, separate from the work it blocked: its own commit where the repository commits, with a
   message saying it resolves a preexisting failure.
4. **Verify** by re-running the affected gates, and resume the original work only once they pass.

A fix too large for one change becomes a plan, and that plan's execution starts before the blocked work resumes. A plan
left waiting is a noted defect with more paperwork.

A defect found along the way that blocks no gate follows the disposition an adopter records under
[Root Cause Orientation](../../../principles/root-cause-orientation.md).

## Never Around It

Each of these turns the gate green and leaves the defect in place:

| Response                                                     | Why it fails                                         |
| ------------------------------------------------------------ | ---------------------------------------------------- |
| skipping the hook, or the pipeline check                     | the broken state reaches everyone downstream         |
| marking a failing test skipped, or commenting out its assert | coverage drops and the regression is hidden          |
| a suppression comment or lint directive over the finding     | the symptom is silenced while the cause remains      |
| deleting a failing test without a replacement                | the behaviour is no longer checked by anything       |
| disabling a cache to hide a stale-cache failure              | the cache configuration stays broken                 |
| "it was broken before my change"                             | the next contributor meets the same failure          |
| a fix-later ticket instead of the fix                        | the defect waits indefinitely and the gate stays red |

The general forms of suppression are listed in [Root Cause Orientation](../../../principles/root-cause-orientation.md).

## Its Own Change, Whatever Its Size

A preexisting fix [lands](../../../conventions/structure/plans/009-portability.md#what-landed-means) in **its own
change, whatever its size**: a separate commit where the repository commits.

A separate change keeps the fix visible instead of buried in unrelated work, lets it be reverted without reverting that
work, keeps its description accurate, and lets a reviewer judge it on its merits. Those benefits hold for a one-line fix
as much as for a large one.

Letting a small fix ride inside the current change would save a landing, at the cost of every benefit above and of a
size threshold someone has to judge each time.

## Scope

Every quality gate, every contributor, people and agents alike, and every branch. It does not cover a test removal that
a documented plan already justifies, or a pipeline that is unavailable rather than failing, which has its own bounded
exception in the second module.
