---
description: >-
  Requires a pull-request body to state the problem, decisions, scope and non-goals, proof, reading order, residual
  risk, and the resulting trunk-state claim, and to be rewritten whenever the head moves.
when_to_use: >-
  Use when opening a pull request, after pushing new commits to one, or when checking whether a body still matches its
  diff.
---

# Pull Request Body

A body exists to make a diff reviewable. The diff already shows what changed; the body carries what the diff cannot,
namely why, what was decided, and how it was proved. Every merge precondition that depends on a reader assumes the body
is accurate.

This standard implements [Evidence Over Assertion](../../principles/evidence-over-assertion.md) and
[Explicit Over Implicit](../../principles/explicit-over-implicit.md).

## What It Carries

| Part                | Holds                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| outcome             | the problem and the result rather than a list of edits, so a reader can judge whether one answers the other                                                         |
| decisions           | what was chosen and what was rejected; a declined alternative is the thing a diff can never show                                                                    |
| scope and non-goals | what is in and what is deliberately out, each with its reason, so an exclusion reads as a decision                                                                  |
| seam                | why this is one delivery unit under [Delivery Seams and Ownership](../agents/planning-capabilities/005-delivery-seams-and-ownership.md), never a line or file count |
| proof               | the named gate, test, or scenario that failed before and passes now; "tested locally" proves nothing                                                                |
| reading order       | where to start, and which paths to skip, with generated output and mechanical churn named                                                                           |
| risk and rollback   | what could still go wrong, and the step that undoes or contains it                                                                                                  |
| surprises           | a reversal, a departure from the plan, or an exception to a rule                                                                                                    |
| trunk state         | why the merged trunk meets the repository's claim, decided below                                                                                                    |

Where the change comes from a plan, link the plan and name the delivery unit. A change to rules or documentation carries
all of this as well; without the obligation its body decays into a changelog.

## Adopter Decision: The Trunk-State Claim

| Claim      | The body states                                                                                                         | Fits                                               |
| ---------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| releasable | a release could be cut from the merged trunk, and what a consumer pinned to a changed public surface would see          | tools, libraries, and catalogs consumed by version |
| deployable | the merged trunk could reach production at once, covering each flag's enabled and disabled paths and its removal record | services deployed continuously from the trunk      |

The repository records which claim its bodies make.

## Plain Claims

Never report a check as passed without having read its output. Never describe work as complete when part of it was
skipped; name that part and the reason.

## It Never Goes Stale

Every push that moves the head updates the body in the same step, before the new head counts as reviewable. A body that
describes a diff the head no longer has is stale evidence, just as an earlier gate run is. Rewriting it is also how
scope that grew during the work gets stated openly instead of slipping through.

## Enforcement

Unenforced by tooling, by decision. No check can tell whether a stated reason is the real one, or whether a body still
matches its diff. A body contradicted by the diff it ships is a legitimate finding for any review. The body is outbound
text, so it also passes [Public Outbound Safety](../../conventions/security/public-outbound-safety.md) before it is
posted.
