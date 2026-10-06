---
description: >-
  Defines what every review finding carries: anchor, cited rule, consequence, severity, confidence, refutation, and
  declared scope, plus the extra proof critical and high-risk findings need.
when_to_use: >-
  Use when writing, verifying, or publishing a review finding, or when replying to one as the repairer.
---

# Finding Requirements

Every specialist shares these rules. Only the discipline differs.

## What Every Finding Carries

- **An anchor**: file and line, so the finding is located without interpretation.
- **The rule it applies**, paraphrased in the finding and linked for detail. A bare link hands the reader a lookup task.
- **The consequence in plain terms**: what breaks, and for whom, in one sentence. The anchor and the rule say where and
  which; neither says why it matters.
- **A severity** of `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`. A `LOW` finding keeps its evidence and never blocks.
- **A confidence** from 0 to 100. A finding below the posting floor of 80 is dropped before publication.
- **A refutation clause** naming the specific evidence that would prove the finding wrong.
- **A place inside the declared scope**: the finding stays within the plan or issue scope the change declares, and
  anything beyond it is not raised on this change.

The refutation clause exists because a self-scored confidence cannot be checked by anyone else, and stated confidence
separates findings that survive repair from findings that are rejected far less well than it appears to. What would
disprove a finding is checkable by the repairer and by a human. The floor stays as a cheap filter; the refutation does
the real work.

## Written to Teach

Review threads are permanent and widely read, so a finding is written for someone new to the codebase: terms of art
defined on first use or replaced with plain words, and enough context to act without having seen earlier discussion. "As
discussed" is never enough.

Critique addresses the change and its consequence, never the author's competence, care, or motive. Being blunt about the
defect and neutral about the person are compatible, and the clearest findings are both.

Teaching is one sentence of consequence, not an essay. A finding that describes a real defect in unusable wording is
rewritten by the coordinator where it stands rather than dropped; the defect did not stop being real.

## Critical Findings Require Reproduction

Agreement between reviewers is not evidence. A `CRITICAL` finding carries a reproduction: concrete inputs or state that
produce the wrong output or the crash, not a description of what a reviewer expects would happen. Lacking one, it is
held at a lower severity, or, when the finding also falls in high-risk scope, held for the adversarial verification
below, until a reproduction is attached.

## Adversarial Verification for High-Risk Scope

When a finding touches authentication or authorization, payments, schema migrations, security-sensitive code, or a
public interface contract, a second independent reviewer re-derives it from the change before it is published. The
posture is adversarial: re-deriving the conclusion, not endorsing it. The second reviewer comes from a different model
family where one is available, because two passes from the same family share blind spots.

This scope is distinct from the security-sensitive paths that force a full review. A change can need every specialist
without needing this pass, and the two controls answer different questions: how many reviewers see a change, and whether
one finding is checked twice.

## Calibration Spot-Check

Periodically, sample published findings above the floor and compare stated confidence with the repair outcome: fixed,
rejected, or deferred. Systematic over-confidence or under-confidence moves the floor, and the change records its
evidence. This is a maintainer procedure rather than an automated job; it catches a score that drifts across many
findings, where the reproduction rule catches one unproven finding.

## Repair Replies

A repair reply names the reviewed change state it answers. It then states what changed and why that change resolves the
finding, or rejects the finding with the evidence and the boundary that decided it. A reader should learn the outcome,
not merely see that a thread closed.
