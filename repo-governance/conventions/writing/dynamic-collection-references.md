---
description: >-
  Forbids stating the size or the full membership of a growing collection outside its own index, and requires a link to
  that index instead.
when_to_use: >-
  Use when a sentence, summary, table, or directory-tree comment is about to state how many items a collection holds, or
  to list all of them.
---

# Dynamic Collection References

A collection whose membership changes — agents, skills, conventions, principles, workflows, specifications — is
described by name and linked to its index. Its count and its complete member list are stated in that index and nowhere
else.

## Why Counts Go Stale Silently

A count is correct on the day it is written and wrong on the day the next member is added. Nothing signals the change:
the sentence still parses, still reads as authoritative, and still passes every check that does not recount the
directory. The person adding a member updates the index because they are looking at it, and misses the summary three
directories away because they are not.

This is [One Source Per Fact](../../principles/one-source-per-fact.md) applied to a number and to a list. The index owns
the membership; everything else links to it.

## The Rule

- Do not state a collection's size in prose, a heading, a layer or index summary, a table cell, or a directory-tree
  comment. Describe what the collection is for instead.
- Do not embed a list that reads as the complete membership. Link to the index.
- When a reader needs the current size or members, link to the index, where both are maintained in the same change.

```text
Incorrect: The repository ships 14 conventions and 9 workflows.
Correct:   The repository ships conventions and workflows; each index lists them.
Incorrect: agents/    # 23 agent definitions
Correct:   agents/    # agent definitions
```

## When a Count or a List Is Correct

| Context                                                            | Why it is not a stale copy                                             |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| the collection's own index                                         | it is the single source, maintained in the same change as the members  |
| a point-in-time record — a report, commit message, or release note | it describes one moment and is never expected to change                |
| a constraint rather than a description                             | "exactly one `name` field" is a rule, and changing it is a rule change |
| a set that is fixed by definition                                  | it does not grow                                                       |
| an illustrative subset                                             | marked with "for example" or "such as", so it claims no completeness   |
| a subset defined by role                                           | "every checker is read-only" stays true as checkers are added          |

A rule that applies to exactly the members it names, and deliberately to no future member, may name them when the text
says the list is exhaustive by decision.

## Sweeping a Changed Quantity

When a change alters a quantity a document legitimately states — a fixed count of steps, scenarios, or selections —
search for every mention of the old value, not only the places a gate checks. Machine-checked figures defend themselves.
The same number in a narrative sentence or a table row has no checker, and that is where a stale copy survives an
otherwise clean change.

## Enforcement

An adopter enforcing this mechanically does so in its own documentation gate, flagging a number beside a collection noun
anywhere outside that collection's index.
