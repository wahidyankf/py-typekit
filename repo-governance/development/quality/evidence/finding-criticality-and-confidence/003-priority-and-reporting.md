---
description: >-
  Combines criticality and confidence into priorities P0 to P4, fixes the order in which findings are applied, and sets
  what a findings report contains.
when_to_use: >-
  Use when ordering findings for repair, deciding what happens when a fix fails, or writing or reading a findings
  report.
---

# Priority and Reporting

Criticality says what matters and confidence says what is safe. Priority joins them so that the most important safe work
happens first and nothing uncertain is applied quietly.

## The Priority Matrix

- **`CRITICAL`** — `HIGH` confidence: P0: apply at once; blocks until fixed; `MEDIUM` confidence: P1: urgent human
  review; `FALSE_POSITIVE`: report; improve the checker urgently
- **`HIGH`** — `HIGH` confidence: P1: apply after P0, before publication; `MEDIUM` confidence: P2: standard review;
  `FALSE_POSITIVE`: report; improve the checker soon
- **`MEDIUM`** — `HIGH` confidence: P2: apply after P1, only with approval; `MEDIUM` confidence: P3: optional review;
  `FALSE_POSITIVE`: report; note a checker improvement
- **`LOW`** — `HIGH` confidence: P3: batch with other fixes when the owner chooses; `MEDIUM` confidence: P4: suggestion
  only; `FALSE_POSITIVE`: report for information

## Execution Order

Apply P0 first, then P1, then the lower priorities. A failed P0 fix stops the run: the blocking problem is still
present, and later fixes would build on a broken state. A failed fix at a lower priority is recorded, and the run
continues.

## Report Structure

A findings report opens with a count per criticality level and the gate result, then groups findings by criticality,
most critical first. Each finding states:

- its location, down to file and line where one exists;
- its criticality, with the reason for that level;
- its category;
- what is wrong;
- its impact;
- a recommendation; and
- once re-validated, its confidence.

A finding is written so that someone else can act on it without asking a question. The
[`plan-validating-quality`](../../../../../.agents/skills/plan-validating-quality/SKILL.md) skill applies this to plan
review.
