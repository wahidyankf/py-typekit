---
description: >-
  Sets the evidence a new repository check needs, what implements each kind, how a check must behave, where blocking and
  reporting checks run, and what removing one requires.
when_to_use: >-
  Use when proposing, placing, or removing a recurring repository validation such as a gate, a hook step, or a
  validation script.
---

# Repository Check Policy

A repository check is anything that runs on every change to keep the repository itself correct: a gate, a hook step, a
validation script. This policy decides whether one should exist, what implements it, how it behaves, and where it runs.

This standard implements [Minimal Sufficiency](../../../principles/minimal-sufficiency.md),
[Automation Over Manual](../../../principles/automation-over-manual.md), and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Restraint

That a rule can be automated is not a reason to automate it. Reuse first: an existing command, hook, standard tool, or
clear manual review.

A new check needs the repository owner's explicit approval, plus evidence that:

1. the failure it catches recurs;
2. the failure materially affects repository-wide correctness; and
3. central enforcement returns more than the check will cost: its code, tests, documentation, run time, false positives,
   upgrades, and eventual removal.

The last cost is the one usually left out of the estimate, and it is rarely the smallest. Every check written is a check
someone later has to prove obsolete before they can delete it.
[Automation Over Manual](../../../principles/automation-over-manual.md) says when automation pays in general; this is
the bar a specific check clears before it exists.

## What Implements It

| Kind of check                              | Implemented as                                                    |
| ------------------------------------------ | ----------------------------------------------------------------- |
| reads documents: structure, links, budgets | an entry for a declared validator in the repository configuration |
| reads the repository's own shape or wiring | a repository-owned script, beside its own test                    |
| runs an external tool                      | that tool, at a version the repository pins                       |

A check that reads documents is configuration, not new code. A script is warranted only when the rule concerns the
repository's own arrangement and no declared validator expresses it. Entries follow
[Gate Entries](../../../conventions/structure/repository-configuration/002-gate-entries.md).

## How It Behaves

- **Deterministic and offline**, so it can run in a hook without a network and give the same answer twice.
- **Reads tracked state** when it concerns committed content, rather than the working tree, so what it checks is what
  would be published.
- **A reporting check never blocks, and cannot.** A notice able to fail will one day stop an unrelated commit, and the
  fix will be to delete the notice.

## Where It Runs

A **blocking** check is scoped to the paths that can break it, so a change that cannot fail it does not pay for it, and
it runs on the surface [Automated Quality Gates](automated-quality-gates.md) assigns to its kind. A blocking check that
no path narrows runs on every change, and that cost is stated where the check is declared.

A **reporting** check runs before the commit, where the author can still act on it with an edit. A notice that arrives
after the commit asks for an amendment instead.

What each surface runs is written in one place, the repository's declared gate list, and never only inside a hook file
that nobody reads.

Every validator the repository ships is assigned to a named gate surface or explicitly excluded with a reason. A
validator with neither disposition looks authoritative but never runs. The adopter's repository-configuration check
compares its shipped validator inventory with the declared gates and exclusions; the catalog defines the invariant but
does not own that inventory.

## Removing One

A check is removed the way it was added: with evidence. Name what now owns each behaviour it had, or state the ground on
which that behaviour needs no owner, such as its subject being gone or another check already covering it. "It seemed
redundant" is not a ground. The procedure is [Deletion With Proof](../deletion-with-proof.md).

Update every reference in the same change that removes the check. A rule that names a deleted command is worse than no
rule, because it reads as current.
