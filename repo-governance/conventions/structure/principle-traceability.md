---
description: >-
  Requires every convention and development standard to name, in its own document, the principles it implements, and to
  be checked against every principle before it lands.
when_to_use: >-
  Use when writing a convention or development standard, or when reviewing whether a rule is still grounded in a
  principle.
---

# Principle Traceability

A rule that cannot say which principle it serves is a preference with enforcement attached. Tracing each rule to a
principle makes its reason findable, and makes the rules a changed principle affects findable too.

## The Rule

Every convention and development standard implements at least one principle, and the link is recorded rather than
inferred.

The chain runs from principle, which says why, through the convention or standard, which says what or how, to the
implementation that enforces it: a gate, automation, an agent, a workflow, or review. Every link in that chain is
visible from at least one end.

## Recorded in the Rule

Each convention and development standard names the principles it implements in its own document, with a link to each. A
reader of the rule sees its grounding without leaving it, and a rule with no such record is visibly incomplete. An
existing rule without a record gains one in the next change that touches it, so rules that predate adoption are not read
as already non-compliant.

A principle page may also list where it applies. That list is a complementary index over the rules' own records, useful
for finding a changed principle's dependents, and it never substitutes for the record in the rule.

## When Writing a Rule

1. **State the problem.** A rule with no problem to solve is not needed.
2. **Name the principle.** If no principle applies, the rule is either unnecessary or evidence of a missing principle,
   and a principle is written only once it is already load-bearing.
3. **Check it against every principle**, not only the one it names. A rule that serves one principle by breaking another
   is revised, or the conflict is settled at the higher level as [Governance Layers](governance-layers.md) describes.
4. **Check whether an existing mechanism already suffices.** A new rule that duplicates one is a second authority.
5. **Name its enforcement**: the gate or automation that checks it, or an explicit statement that review judges it.

## When Reviewing a Change

Review confirms that a changed rule still traces to its principles, contradicts none, and is still enforced the way its
record says. A trace to a principle the rule no longer serves is worse than none: it lends the rule authority it has
lost.

When principles appear to pull against each other, some repositories rank them. Any such ranking depends on that
repository's own set of principles and is recorded there; this convention does not fix one.

Because the record has a fixed place, an adopter can check mechanically, in its own governance check, that every
convention and standard added or changed since adoption names at least one principle; whether each trace is still true
stays with review.

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because a rule's
grounding is written down rather than inferred, and [Documentation First](../../principles/documentation-first.md),
because a rule records why as well as what.
