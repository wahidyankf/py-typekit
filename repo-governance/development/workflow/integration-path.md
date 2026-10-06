---
description: >-
  Records whether work reaches the trunk through short-lived branches and pull requests or directly, and fixes branch
  lifespan, rebase sync, one reused worktree per task, post-merge reconcile, and cleanup.
when_to_use: >-
  Use before creating a branch or worktree, when syncing a task branch, or when deciding whether a change goes through a
  pull request or straight to the trunk.
---

# Integration Path

The trunk is the only branch that persists. Work reaches it often and in small pieces, and every other branch exists for
one task and is gone within days. This is trunk-based development, and a repository adopts one of its two routes.

This standard implements [Simplicity Over Complexity](../../principles/simplicity-over-complexity.md) and
[Explicit Over Implicit](../../principles/explicit-over-implicit.md). It chooses a route and grants no permission; see
[Commit Authorization][commit-authorization].

## Adopter Decision: The Route

- **short-lived branch via pull request** — Work lands as: a task branch in a worktree, merged under
  [Pull Request Merge](pull-request-merge.md); Fits: a protected trunk, several contributors, gates that must run first;
  Trade-off: a review buffer and hosted gates, at the cost of branch and worktree overhead
- **direct to trunk** — Work lands as: changes on local `main`, pushed to the trunk where a remote exists; Fits: a
  single owner, or no service able to protect the trunk; Trade-off: the least ceremony and no buffer: local gates and
  [CI Post-Push Verification][ci-post-push-verification] carry it all

The repository records its route, and nothing else selects one: not where the work runs, not the size of a change, not a
wish to skip review. What counts as landed follows
[What Landed Means](../../conventions/structure/plans/009-portability.md#what-landed-means). Under the direct route no
task branch, worktree, or pull request serves as a second path; a temporary branch a tool creates for another purpose is
removed when that purpose ends. A repository with no remote follows the direct route locally.

**Recorded here: short-lived branch via pull request.** Every change reaches `main` as a task branch in a worktree,
through a pull request that lands by rebase under [Pull Request Merge](pull-request-merge.md).

Long-lived environment branches tracking what is deployed are not development branches: nothing is developed on them,
and changes flow only from the trunk to them.

## Branch Route Requirements

- **One task, one short-lived branch.** Merge it the day it is created where possible; two days is the ceiling, and past
  it rebase or abandon the branch.
- **Sync by rebase.** Before starting and before resuming, fetch and rebase onto the latest trunk. Never auto-stash,
  discard, or auto-resolve: an unclean tree or a conflict halts the work and goes to its owner. When the sync brings
  commits in, complete [Integration Diff Review][integration-diff-review].
- **Linear history.** Never merge the trunk into a task branch.
- **One worktree per task, reused.** A plan or task provisions at most one worktree and reuses it for every delivery
  unit it yields at `{repository location}/worktrees/<task>`. Units land in turn: land one, sync, branch the next in the
  same directory. A sibling `*-worktrees/` path or a second worktree for the same work is a defect. A new worktree is
  bootstrapped per [Checkout Bootstrap][checkout-bootstrap].
- **One pull request per delivery unit,** cut at a seam meeting
  [Delivery Seams and Ownership](../agents/planning-capabilities/005-delivery-seams-and-ownership.md), opened as a
  draft, described per [Pull Request Body](pull-request-body.md).
- **Reconcile local `main` after every merge.** A merge moves the remote trunk, not the checkout holding local `main`.
  Fast-forward it and prove it as [Bare Repository Landing][bare-repository-landing] describes.
- **Remove all three artifacts,** the worktree, the local branch, and the remote branch, once every unit that used the
  worktree has landed or been abandoned and nothing is unpushed or still running. Keep a worktree whose run failed, and
  say so, rather than deleting the evidence.
  [Dev Artifact Clean-Up](../../workflows/maintenance/dev-artifact-clean-up.md) proves it.

## Worktree Location

Branch-route worktrees live only at `{repository location}/worktrees/<task>`, and the repository ignores `/worktrees/`.
Tools, guards, and bootstrap commands run from that checkout. A sibling `*-worktrees/` location is forbidden because it
escapes the repository's discoverable lifecycle and makes command-center cleanup ambiguous.

## Why the Server Enforces It

A pull request can come from a checkout whose hooks never ran, so hosted gates repeat the local hook contracts.
Branch-route hosting rules enforce trunk protection and linear history for every actor, owners included.

[commit-authorization]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/commit-authorization.md
[ci-post-push-verification]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/ci-post-push-verification.md
[integration-diff-review]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/integration-diff-review.md
[checkout-bootstrap]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/checkout-bootstrap.md
[bare-repository-landing]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/bare-repository-landing.md
