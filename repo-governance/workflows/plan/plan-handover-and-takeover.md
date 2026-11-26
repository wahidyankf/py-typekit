---
name: plan-handover-and-takeover
description: >-
  Writes a resumable handover record before unfinished plan work changes hands, and on resumption discovers, adopts, and
  cleans up every trace of the plan.
when_to_use: >-
  Use when unfinished plan work passes to another session, agent, or person, or a possibly partly worked plan resumes.
---

# Plan Handover and Takeover

## Entry

Handover: unfinished plan work is leaving its session, agent, or person; a finished plan is archived instead. Takeover:
a plan resumes unconfirmed whether already worked; one executing in the right worktree this session continues.

- `mode` (`enum`: `handover`, `takeover`; required).
- `plan` (`string`, required): a plan folder or its bare identifier.
- `repositories` (`string`, optional): extra candidate repositories.

## Sequence

Handover runs steps 1–4, takeover 5–12. Both key on the plan identifier (folder name without date prefix) and track each
probe, anomaly, and cleanup candidate as its own task per [Task Tracking](../../development/agents/task-tracking.md).

1. **Gather verified state per repository:** checkout, branch, head, uncommitted changes, pull request and pipeline
   status, and checkbox counts, re-checking anything possibly stale.
2. **Write the record in fixed section order:** one-line status; verified per-repository state; next steps naming the
   checklist item and first command; active user rule decisions with statement, scope, source, and status, or `None`
   after checking; learned constraints and why they bite; files touched, or where listed; and settled decisions not to
   reopen. Status and next steps are never empty; every section is present.
3. **Save it dated and named by plan identifier** in the scratch location, keeping earlier records.
4. **Report the path** of the non-empty record.
5. **Re-read the instructions and reconcile active rule decisions** before resuming; stop on an unresolved conflict.
6. **Read the newest handover record as a lead** narrowing probes but proving nothing; reconcile its rule decisions too.
7. **Fix the candidates:** this repository, any the plan or a handover names, and `repositories`.
8. **Probe each candidate, persisting every hit to the takeover report:** linked worktrees, local and remote branches,
   pull requests in any state, the plan folder's trunk location, and each found copy's ticks and uncommitted state.
   Judge nothing stale.
9. **Classify each repository into one bucket:** nothing found; delivered (archived and
   [landed](../../conventions/structure/plans/009-portability.md#what-landed-means), every found pull request merged;
   report the invocation as possibly stale); live (partial ticks, nothing contradicting); or anomaly. Evidence fitting
   no bucket or two, or self-contradicting (a worktree without its branch, a pushed branch with neither worktree nor
   pull request, two worktrees for one plan), is an anomaly: stop and escalate with it.
10. **Adopt live work.** Enter its worktree or create one from its branch, never trunk; sync as Execution does.
    Uncommitted changes await the user's direction, never stashed or discarded; rebase conflicts follow the [owned task
    sync contract][task-sync]. Every changed path is unattributed until branch history rebuilds the touched-file record.
    Reuse an existing pull request; tick a checkbox only from cited discovery evidence.
11. **Clean up only after classification.** A found, unadopted worktree or branch passes the pre-removal checks of
    [Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md). Anomalies are never cleaned; anything unproven
    idle stays and is reported; each removal or skip is logged.
12. **Hand each live or plan-owning nothing-found repository to [Execution](plan-execution.md).**

## Exit

Handover: a non-empty record (`file`, `handovers/<date>__<plan>.md` in the scratch location per
[Temporary Files](../../conventions/structure/temporary-files.md)), its path reported.

Takeover: every candidate classified, each stale leftover removed or kept with a stated reason, and step 12's
repositories handed to Execution. Outputs: the takeover report (`file`, scratch location) and reconciled targets (`map`:
repository to bucket, worktree, branch, and pull request).

Partial outcome: an anomaly awaits the user, evidence in the report; its repository is neither cleaned nor handed off
until resolved.

## Example Usage

```text
Run plan-handover-and-takeover with mode handover and plan "plans/in-progress/add-export/".
Run plan-handover-and-takeover with mode takeover and plan "rename-billing".
```

## Related Workflows

- [Multi-Plans Execution](multi-plans-execution.md) schedules several resumed plans.

## Why a Handover Is Only a Lead

A checklist records what is done, not what is safely half-done or which lessons cost; the record carries both. Any later
touch stales it, so takeover verifies everything, bounded by its fixed candidate set. This workflow implements
[Evidence Over Assertion](../../principles/evidence-over-assertion.md) and
[Explicit Over Implicit](../../principles/explicit-over-implicit.md).

[task-sync]: ../../development/workflow/no-destructive-git-operations/001-authorized-task-branch-sync.md
