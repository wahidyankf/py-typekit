---
description: >-
  Splits specialist review into disciplines with owned and routed-away scope, a boundary tie-breaker, pre-decided
  grey-zone rulings, anchored findings, and noise controls.
when_to_use: >-
  Use when designing or running a review that fans one change out to several specialist reviewers, or when the owner of
  a finding is unclear.
---

# Review Disciplines

A single generalist reviewer carries every concern in one prompt, and nothing tells it where one concern ends and the
next begins. Splitting review across specialists buys depth and creates a different failure: a finding two specialists
could each claim gets raised twice, argued differently every cycle, or raised by neither.

The split works only when four things are written down once and read by every reviewer: what each discipline owns and
what it routes away, a tie-breaker for findings that fit no discipline cleanly, the recurring borderline cases already
decided, and the controls that keep a many-reviewer fan-out affordable and quiet.

## Modules

1. [Discipline Roster](review-disciplines/001-discipline-roster.md)
2. [Boundary Rulings](review-disciplines/002-boundary-rulings.md)
3. [Finding Requirements](review-disciplines/003-finding-requirements.md)
4. [Cost and Noise Controls](review-disciplines/004-cost-and-noise-controls.md)
5. [Plan Document Route](review-disciplines/005-plan-document-route.md)

## Roles

| Role        | Does                                                                                          |
| ----------- | --------------------------------------------------------------------------------------------- |
| scout       | classifies the change, reads prior thread outcomes, and assembles shared context once         |
| specialist  | discovers findings inside one discipline and hands them to the coordinator                    |
| coordinator | deduplicates, re-categorizes, filters, and verifies raw findings, then publishes one review   |
| repairer    | fixes each published finding, or rejects it with the evidence and the boundary that decide it |

Only the coordinator publishes. Specialists posting separately produce overlapping and contradictory advice, and nobody
is accountable for reconciling it.

## Scope

In scope: any review that sends one change to more than one specialist, whether the change is a pull request or a local
commit range. The roster, the tie-breaker, and the finding rules hold wherever the change lives.

Throughout these modules, a **thread** is the adopter's recorded review record for one finding: a hosted review thread
for a pull request, or an entry in a findings record for a local commit range.

Out of scope: the definitions behind each severity level, which the adopter's severity scale owns, and the ceiling on
the review-and-repair loop, which the [Quality Gate Contract](../workflow/quality-gate-contract.md) fixes at three
cycles with no mid-run wait for a person. Whether the split pays off is measured by the adopter against its own review
history.
