---
description: >-
  Gives every quality rule a declared enforcement class and route, forbids making a check pass by weakening it, and
  never reads a check that inspected nothing, or never ran, as a pass.
when_to_use: >-
  Use before reporting a change complete, when adding or changing a gate, hook, schedule, or review obligation, or when
  a check passes suspiciously easily.
---

# Software Quality Enforcement

A rule is only as strong as what makes it hold; naming that for every rule stops a repository trusting a guarantee
nothing enforces.

This standard implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md),
[Fail Closed](../../../principles/fail-closed.md),
[Root Cause Orientation](../../../principles/root-cause-orientation.md), and
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md). Which surface a check runs on is owned by
[Automated Quality Gates](automated-quality-gates.md), and what a gate returns by
[Quality Gate Results](../manual-verification/001-quality-gate-results.md).

## Every Rule Names Its Class

| Class               | Means                                                                  |
| ------------------- | ---------------------------------------------------------------------- |
| required gate       | an automated command that must pass before applicable work is complete |
| commit gate         | runs automatically and blocks a commit when it fails                   |
| push gate           | runs automatically and blocks a push when it fails                     |
| scheduled detection | finds regressions on a cadence, never blocking an earlier push         |
| required evidence   | a blocking review by a person or agent, without automation             |
| runtime guard       | fails closed before unsafe test, deployment, or other work starts      |

The repository keeps one enforcement map, naming for each maintained outcome its owning rule and every enforcing class
and route.

Each entry names its route truthfully. A rule held only by review is required evidence, never a nonexistent gate, and an
invariant with no route is an intention. Missing automation never weakens a rule; it only changes which class carries
it.

Hooks, pipelines, and schedules implement the map and never replace it. Project READMEs record the commands each route
resolves to.

## Applying the Map

An entry applies when a change can alter its outcome, boundary, artifact, or mechanism. Before completion, run the
narrowest target of every applicable entry and record the evidence. Scheduled detection, reporting after the change
lands, never replaces that local proof.

Automation proves a final state, not the order that produced it, so an ordering rule such as
[Test-Driven Development](../testing/test-driven-development.md) is required evidence even where a gate checks its
result.

Applicable entries, results, and evidence still owed survive compaction and handoff under
[Governance Continuity](../../../principles/governance-continuity.md); a resumed reader reloads the map first.

## No Superficial Satisfaction

Never make a check pass by weakening it. Beyond the suppressions that
[Root Cause Orientation](../../../principles/root-cause-orientation.md) and
[Preexisting Error Resolution](../evidence/preexisting-error-resolution.md) already rule out, each of these is that
move:

- lowering a coverage floor, or widening an exclusion, until the number clears;
- catching an error only to reach a return statement;
- asserting something the code cannot fail; and
- editing a validator so it stops reporting, instead of changing the declaration it reads.

Each leaves the repository reporting a guarantee it no longer has.

When the check itself is wrong, change it deliberately as its own change, a separate commit where the repository
commits, stating why, never inside the change it inconvenienced. Suppressing one finding follows the waiver rule in
[Lint Strictness](lint-strictness.md).

## Nothing Inspected Is Not a Pass

A check that inspected zero files, cases, or scenarios looked at nothing, whatever its exit status. Every check reports
how much it inspected, and an unexplained drop in that count is itself a finding.

A skipped or cancelled required job reports nothing, so an aggregate check merge protection relies on treats a skipped
or cancelled dependency as failed.

Say what a green result proves and no more. A static check that resolves bindings is not a suite that ran them, and a
scanner that matched no pattern has not shown a value safe to publish. Name which check produced the green.

## Reporting Completion

A change is complete when every required gate has passed, its output kept; started or expected to pass does not count.
Report a failed gate with its output and a skipped step with its reason. A claim omitting a skipped step is worse than
an incomplete one, because it stops anyone looking.

An adopter enforces the map in its own hooks, pipeline, and review checklist.
