---
description: >-
  Requires the plan system to be usable by any repository on its own, with no coordinating repository, shared registry,
  or private detail as a dependency, and defines when a change has landed under the delivery mode the adopter records.
when_to_use: >-
  Use when adopting the plan system into a repository, when checking that a change to it has not introduced an external
  dependency, or when a rule must say that a change has landed.
---

# Portability

This specification is complete on its own. A repository that has read it can run the whole plan lifecycle without access
to any other repository, service, or index.

That is a constraint on how the specification may be written, not just a description of it.

## No External Dependencies

The plan system must not require:

- a coordinating or control-plane repository;
- a shared plan index, registry, or ledger held somewhere else;
- naming any particular repository, organization, group, or team;
- a maintainer's absolute path, machine, or account;
- an internal host, address, network, or topology; or
- a private artifact, convention, or process a reader cannot see.

A rule that cannot be stated without one of those is not portable, and it belongs to the repository that needs it rather
than to this specification.

Examples and placeholders are semantic: `<slug>`, `plans/in-progress/<slug>/delivery.md`, `YYYY-MM-DD`. They stand for a
shape, and a reader substitutes their own. They are never a real path from somewhere else with the identifying parts
lightly changed.

## Delivery Mode Is the Adopter's

The plan system deliberately says nothing about how changes reach a repository's main line. Pull requests, direct
[landings](#what-landed-means), and local-only landings in a repository with no remote at all are equally compatible,
because `delivery.md` declares its execution checkout and delivery units rather than assuming them.

A repository with delivery constraints of its own — a required review, a protected branch, a remote it must not have —
records them as its own artifact and applies them alongside this convention. That artifact is the adopter's; it is not a
variant of the specification and it does not travel back into it.

## What Landed Means

A change has **landed** when it has reached the adopter's integration target in the form the adopter records: merged
through a pull request, committed on the trunk, or present on the trunk's working copy, committed or not.

- The adopter **must** record that definition once, in its own policy or overlay, and every other statement of landing
  refers to it.
- Where changes arrive through pull requests, landed means merged, and nothing else changes.
- Catalog text **must not** assume a commit beyond what landing requires.
- Evidence and a gate's subject name the revision with any uncommitted paths, plus the commit identifier when one
  exists, and terminal and archival steps say land.
- A check accepts work that landed uncommitted wherever the adopter's definition allows it. An ancestry or tip check
  applies only where the adopter integrates through branches or pull requests.

The reason is that a repository landing work without committing it would otherwise diverge from every sentence that
demands a commit. No gate checks this: whether a sentence needs a commit or only a landing is a judgement, so a rules
review owns it.

## Deviation Is Allowed, Silence Is Not

An adopting repository may diverge. What it may not do is diverge invisibly.

For each block of this specification, an adopter records exactly one of:

| Status                      | Means                                                                 |
| --------------------------- | --------------------------------------------------------------------- |
| adopted                     | applied as written                                                    |
| adapted, with reason        | applied in a different form, and here is why                          |
| not applicable, with reason | this repository's characteristics make it irrelevant, and here is why |

A reason is required for the latter two, and "we do it differently" is not one — it restates the status. The point of
the record is that a future reader can tell a considered divergence from an incomplete adoption, and those two look
identical from the outside.

An absent or incomplete row is itself a finding. A repository that has adopted nine blocks and never mentions the tenth
has not adopted nine blocks; it has an unknown state.
