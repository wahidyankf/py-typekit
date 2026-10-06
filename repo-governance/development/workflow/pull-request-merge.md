---
description: >-
  Sets every pull-request merge's preconditions (exact-head gates, a current branch, closed conversations, surface
  gates, no unapproved bypass) and records the landing method and merge authority as adopter decisions.
when_to_use: >-
  Use before merging a pull request, when a gate fails close to merge, or when deciding whether readiness or an earlier
  approval permits a merge.
---

# Pull Request Merge

A merge changes the trunk for everyone. Its safety is mechanically checkable, so it rests on preconditions evaluated at
the moment of merge, not on how finished the work feels.

This standard implements [Evidence Over Assertion](../../principles/evidence-over-assertion.md),
[Fail Closed](../../principles/fail-closed.md), and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## Preconditions

Each holds at merge time:

1. **Exact-head gates.** Each required check is green for the pull request's current head commit against its current
   base. A run for an earlier head or another base, or superseded by a later push, is stale and authorizes nothing; see
   [Quality Gate Results][001-quality-gate-results].
2. **A current branch.** The branch contains the latest target, brought forward per [Integration
   Hygiene][integration-hygiene], and the hosting service reports no conflict. A conflict in a generated file is
   resolved in the generator's source, then regenerated and checked for drift, never hand-edited.
3. **Closed conversations.** Every review conversation is resolved or dismissed by the user. Review may be optional; the
   conversations it opens still bind.
4. **Surface gates.** Each deterministic check the changed reachable behaviour requires, whether a running interface,
   endpoint, or other boundary, must have a passing terminal result. A surface quality gate's verdict is advisory, per
   the [Quality Gate Contract](quality-gate-contract.md), so it need not be a pass: it is recorded for the exact head,
   and each open blocking row of a `FAIL` or `BLOCKED` verdict has an owner. Where no reachable behaviour changed, the
   merge record says so.
5. **Outbound safety.** The exact head passed an outbound leak screen, which in a public repository is
   [Public Outbound Safety](../../conventions/security/public-outbound-safety.md). A suspected secret halts merge
   handling and follows [No Secrets in Tracked Files](../../conventions/security/no-secrets-in-tracked-files.md); no
   green check, closed conversation, or earlier clean screen permits merging it.

Preconditions are evaluated per merge; meeting them once says nothing about the next pull request. Before merging,
present each precondition's status and its evidence.

The repository records its landing method. A rebase keeps the branch's [thematic commits][thematic-commits], a squash
collapses them, and a merge commit is unavailable where [Integration Path](integration-path.md) keeps history linear.

**Recorded here: rebase.** Each pull request lands by a rebase merge, keeping its commits on the linear trunk.

## Landing Identity

A rebase or squash landing must prove that the landed tree equals the reviewed pull-request head tree. Reconciliation
records both tree identifiers and refuses cleanup when either is absent or they differ; commit identifiers cannot prove
this for rewritten history. The post-merge integration record fails on a missing or unequal tree.

## No Bypass Without Named Permission

Never merge over a failing or pending required check, an unresolved conversation, or branch protection, and never use an
administrative override. A user may waive one named gate for one named merge; that waiver covers nothing else, reaches
no later merge, and never covers the outbound-safety screen.

When a gate fails, report which and why, fix the cause, rerun it, then re-evaluate every precondition.

## Draft Until Done

Open each pull request as a draft and iterate while it stays one; mark it ready once the work meets its done definition.
Readiness says the work is finished; it satisfies no precondition and authorizes no merge. Where marking it ready
retriggers the checks, the following run counts.

## Adopter Decision: Merge Authority

- **preconditions** — The merge happens: an agent merges once all preconditions hold, unless a plan step names a human
  gate; Trade-off: fast and consistent, but any gate gap becomes a merge gap, so test depth carries weight
- **explicit approval** — The merge happens: a person approves each merge after the preconditions hold, for that one
  pull request; Trade-off: a human backstop for gate misses, but merges wait, and approval can become a signature
  without evidence

The repository records its choice. Either way the preconditions are the same and only the actor differs; the commits and
pushes that built the branch remain under [Commit Authorization][commit-authorization].

[001-quality-gate-results]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/manual-verification/001-quality-gate-results.md
[integration-hygiene]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/integration-hygiene.md
[thematic-commits]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/thematic-commits.md
[commit-authorization]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/commit-authorization.md
