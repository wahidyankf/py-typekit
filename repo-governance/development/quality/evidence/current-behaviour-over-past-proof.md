---
description: >-
  Replaces past proof that can no longer be produced, or that only adds complexity, with a recorded observation of
  current behaviour, without waiving any check that can still run today.
when_to_use: >-
  Use when a plan-execution check, quality gate, audit, or delivery checklist asks for a past run, baseline, record, or
  verdict that no longer exists or would have to be rebuilt.
---

# Current Behaviour Over Past Proof

A check sometimes asks for proof from the past that nobody kept: a red run that was never captured, a baseline taken in
a worktree that is gone, a notice that was never recorded, a propagation step that should have run before the edits, or
a reviewed head that was never written down. That history cannot be recovered honestly.

This standard implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md) and
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md).

## The Rule

When a plan-execution check, quality gate, audit, or delivery checklist asks for past proof that can no longer be
produced, or that would only add complexity to rebuild, do not reconstruct it. Observe the current behaviour directly
instead: run the current suites on the current head, read the live state, or read the current files. Record that
observation as an ordinary evidence record, and add one line naming the past proof it replaces and why that proof is
unavailable.

Reason: a rebuilt record documents the rebuilding, not the event it claims to show, and it costs effort without adding
certainty. The criterion is about how the work behaves now, and that can always be observed.

## Boundaries

- This substitutes evidence; it never waives it. The current observation must establish the criterion on its own.
- A check that can still run today runs today. Only proof tied to a past moment is substituted.
- A check whose purpose is a current property still runs, even when it repeats a past step. A harness or gate still
  proves it can fail, per [Cycle and Evidence](../testing/test-driven-development/001-cycle-and-evidence.md).
- Do not re-stage a past state, back-date a record, or present a new run as an old one to fill the gap.
- When the behaviour itself can no longer be observed, this rule does not apply. Use the **accepted as permanently
  unmet** disposition of
  [Knowledge Capture and Archival](../../../conventions/structure/plans/008-knowledge-capture-and-archival.md#resolution-is-not-a-tick).

## Observations

- **Followed:** the evidence record holds a current command, revision, time, and result that establish the criterion,
  plus one substitution line naming the missing past proof.
- **Violated:** a past artefact is rebuilt or back-dated; a verdict blocks only because unrecoverable history is missing
  while current behaviour establishes the criterion; or a check that can still run is skipped under this rule.

## Enforcement

**Unenforced by decision.** Whether a past proof is truly unrecoverable, and whether a current observation establishes
the criterion, are judgements no mechanical check settles. The execution checker and the reviewer judge them from the
evidence record and its substitution line.
