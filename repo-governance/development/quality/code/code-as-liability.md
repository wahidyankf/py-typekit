---
description: >-
  Treats added code as a lasting maintenance obligation: a change that adds code states what it buys, what it costs to
  keep, and which simpler alternative lost, with tests and specifications exempt.
when_to_use: >-
  Use when adding code, reviewing a change that adds code, or deciding whether a problem should be solved with code at
  all.
---

# Code as Liability

Code is not an asset that gains value by accumulating. Every line is read, understood, kept working, migrated, and in
the end deleted by someone, usually someone who did not write it. Adding code takes on an obligation; deleting code
retires one.

Changing existing code is unremarkable. Growing the total needs a reason good enough to outlast the person who had it,
written where the next reader will find it.

This standard implements [Minimal Sufficiency](../../../principles/minimal-sufficiency.md),
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md),
[Deliberate Problem-Solving](../../../principles/deliberate-problem-solving.md), and
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md).

## The Three Answers

A change that adds code carries a short justification stating:

1. **What it buys.** The concrete capability or defect fix, not the intention. "A caller can resume an interrupted
   upload" is an answer; "improves reliability" is not.
2. **What it costs to keep.** What later readers and changers inherit: a new dependency, a second path that must stay in
   step with the first, a format that now needs migrating.
3. **Which simpler alternative lost, and why.** Including doing nothing, configuring something that already exists,
   extending a caller, and deleting code instead. The options and their default order are in
   [Scope of a Change](../../../principles/minimal-sufficiency/001-scope-of-a-change.md).

Three sentences usually suffice. The trade is made on purpose and left visible, not argued at length. A justification
that restates the change title three ways has answered nothing.

## Where the Answers Live

In the change description, such as the pull request body. That is where the decision is made and reviewed, and version
history keeps it against the merged change, reachable from any line through the history. A source comment drifts from
the code beside it, and a plan is archived when its work ends.

An adopter puts the section in its change template so the prompt appears on every change. The section is removed only
when the change adds no code in scope.

## What Counts as Code

Every non-prose file someone must understand and keep working: source, configuration, scripts, and pipeline definitions
alike. A pipeline job and a module are equally code.

The adopter records the directories that hold such files. That record is a floor, not a boundary: anything executable or
machine-read elsewhere is covered by the same reasoning, and moving a file does not make it free. Prose is outside this
standard; its size is held down by a word budget instead.

Tests, behaviour specifications, and their fixtures are **exempt**. This is stated outright so the standard can never be
cited against writing them: they are what makes changing the other code safe. A change that adds only tests owes no
justification. A redundant or low-value test is still challenged in review, as a question of test quality rather than of
this standard.

## Scrutiny Scales With Reach

| Reach                                                | Depth of answer                           |
| ---------------------------------------------------- | ----------------------------------------- |
| a script run once and then deleted                   | a sentence                                |
| code inside one component, called from one place     | the three answers, briefly                |
| a shared library other components import             | name the callers that will inherit it     |
| tooling that every component's quality gates rely on | justify it against not building it at all |

Reach follows the dependency graph as it stands today, not a fixed list, and the bar moves with it. Scrutiny scales the
depth of the answer, never whether one is owed: a one-line addition to shared tooling still owes all three.

## Enforcement

Review enforces this against the change template. A mechanical check, the section present and non-empty whenever a
change adds non-test lines under the recorded code directories, belongs in the adopter's own gate. Building that check
is itself an addition governed here, so it waits until review has proved insufficient.

A dependency is code someone else wrote; adding one also follows [Dependency Selection](dependency-selection.md).
