---
description: >-
  Requires a new external dependency to meet a need the standard library and existing mechanisms cannot, with rejected
  alternatives, maintenance evidence, and owned consequences recorded and the version locked.
when_to_use: >-
  Use before adding, replacing, or removing a runtime, development, build, or test dependency, or when reviewing a
  changed manifest or lockfile.
---

# Dependency Selection

A dependency is a lasting obligation. It enters the lockfile, the supply-chain checks, the release, and the trust
boundary of everyone who runs the result, and someone has to update it, audit it, and answer for it when it breaks.
Adding one is a decision that gets stated.

This standard implements [Minimal Sufficiency](../../../principles/minimal-sufficiency.md),
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md), and
[Reproducibility](../../../principles/reproducibility.md). It applies [Code as Liability](code-as-liability.md) to code
someone else wrote.

## Prefer What Is Already Here

Reach for what already exists first, in the order
[Scope of a Change](../../../principles/minimal-sufficiency/001-scope-of-a-change.md) fixes: an existing mechanism, the
standard library, the platform, a dependency already present. Among new dependencies, prefer a small, well-maintained
one over a large one.

## When a New One Is Justified

Add an external dependency only when all of these hold:

- **A concrete need** exists that the standard library or an existing mechanism cannot meet without a disproportionate
  cost in correctness, security, interoperability, or maintenance. Convenience is not a need.
- **It is established practice** for that problem, not a novel or repository-specific shortcut.
- **Current evidence from the project itself** shows active maintenance, compatibility with the supported toolchain, and
  a credible response to defects and security reports.

Never add one to replace a small amount of clear code the repository would own, to serve a need that is only predicted,
or to avoid learning a capable standard-library facility.

## Record the Decision

The plan or change description that adds a dependency records:

| Record                    | Holds                                                                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------- |
| the need                  | what the repository must do that it cannot reasonably do itself                                       |
| the rejected alternatives | including the standard library and writing it directly, each with why it lost                         |
| the evidence              | release cadence, defect response, and whether anyone still owns the project                           |
| the owned consequence     | what happens if it is abandoned, relicensed, or ships an advisory; if the answer is to vendor it, now |
| what it brings along      | its transitive dependencies, and whether it reaches the network, the filesystem, or other processes   |

What a dependency pulls in is part of what is adopted. A dependency that crosses a boundary the repository guards
crosses it on the repository's behalf.

## Lock It and Check It

Lock the version through the ecosystem's normal mechanism, and land the lockfile in the same change as the manifest. A
lockfile updated on its own is a diff nobody can review.

The dependency then passes the repository's existing advisory, licence, and duplicate-source checks. One that cannot
pass them is not a candidate.

A version copied from another repository carries that repository's advisories, and a successful install does not reveal
them. Audit after adding or copying a pin, and resolve a finding by moving the pin, not by lowering the audit threshold
or overriding the resolved version.

## Removal

Removing a dependency needs no justification beyond the change passing, and it is preferred. It lands with the code that
stopped needing it, and the lockfile moves in the same change.

When the conditions above stop holding, reassess replacement the next time the dependency is materially changed or
causes a concrete problem. A dependency that is merely old is not a reason for churn.

## Verification

Review every changed manifest and lockfile against the recorded decision. It passes when the need is explicit, the
rejected built-in alternative is named, maintenance claims cite current primary sources, the owned consequence is
stated, and the repository's gates pass with the dependency in place.

An adopter enforces the lock and the audit in its own supply-chain gate, so neither depends on a reviewer remembering.
