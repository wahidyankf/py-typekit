---
description: >-
  Governs a repository that dispatches work to the repositories owning it: the inventory it keeps current, set names
  that only select members, per-target handling of fan-out requests, and halting on uncertainty.
when_to_use: >-
  Use when a request received in one repository must change others, or names a set of repositories to act on together.
---

# Coordination Repository

A coordination repository is a checkout that receives requests about other repositories and knows how to reach them. It
directs each request to where the work belongs, and never becomes the place that work is owned.

## The Inventory

The coordination repository keeps one list of the repositories it can reach:

| Field      | Records                                                 |
| ---------- | ------------------------------------------------------- |
| identity   | the repository's name and its local checkout path       |
| membership | every named set it belongs to                           |
| owns       | the source, rules, and operations it is responsible for |
| delivery   | how a change to it normally lands on its main line      |

Routing reads this list, so an entry that no longer describes its repository sends later work to the wrong place. When
authorized work alters a recorded field, the entry is corrected as its own explicit change to the coordination
repository. When the task does not permit that correction, the discrepancy is raised with the requester instead of being
left in place.

## Directing Work Is Not Owning It

Receiving a request grants the coordination repository nothing over the repository that owns the work. The owner's
instructions govern every change made there, and its code, rules, operations, and releases stay with it. The
coordination repository itself changes only for work it owns, such as its inventory.

What each target keeps to itself — its instructions, mutations, proof, and cleanup — is fixed by
[Delivery Seams and Ownership](../../development/agents/planning-capabilities/005-delivery-seams-and-ownership.md).

## Set Names

A set name expands, through the inventory, to its recorded members and no others. It picks which repositories a request
applies to. It adds no permission beyond the request, and a repository that resembles a member without being recorded as
one is left alone.

## Fan-Out Requests

A request to repeat a change elsewhere — to "propagate" it, to "do the same", or words to that effect — authorizes that
change, at the requested scope, in each repository or set member the request names. Each target receives the requested
change, adjusted only where its own rules demand, and never enlarged.

Every target is a separate task:

1. **Look first.** Read its instructions and its current state — uncommitted changes, branches, worktrees, pending
   reviews, and remote state — before changing anything.
2. **Land it the target's way**, as
   [Delivery Seams and Ownership](../../development/agents/planning-capabilities/005-delivery-seams-and-ownership.md)
   fixes.
3. **Leave unrelated work alone.** Changes already present in the target that the request did not produce are never
   reverted, reformatted, or folded into the delivered change.
4. **Close it on its own.** The target is done once the change sits on its main line — remote, or local where there is
   no remote — and its [development-artifact clean-up](../../workflows/maintenance/dev-artifact-clean-up.md) has ended.
   Its worktrees and branches go then, without waiting for the other targets.

The request as a whole finishes when no target remains open.

## Halt on Uncertainty

Work on a target halts, and the problem is reported, when its checkout cannot be found, when more than one repository
could be the one meant, or when its own instructions disagree with its inventory entry. The coordination repository
creates no checkout, adds no remote, and settles no rule conflict on the owner's behalf. Targets the problem does not
touch proceed.

Guessing places a change in a repository nobody asked to change, or takes a decision that belonged to its owner. Undoing
either costs far more than reading the report.

## Beyond Routing

Obligations between repositories that go further than dispatching work — parity, consumption, shared learning — are set
by [Related Repositories](related-repositories.md).

## Principles

This convention implements [Fail Closed](../../principles/fail-closed.md), because an uncertain target halts instead of
proceeding, and [Deliberate Problem-Solving](../../principles/deliberate-problem-solving.md), because each target is
inspected before it is changed.
