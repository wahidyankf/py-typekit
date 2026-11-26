---
description: >-
  Requires local checks before each commit, catching up with the trunk by rebasing, with named merge exceptions that
  yield where the integration route forbids merging, and fixing or reverting a red trunk at once.
when_to_use: >-
  Use before committing or pushing, when choosing between rebase and merge to catch up with the trunk, or when the
  trunk's pipeline turns red.
---

# Integration Hygiene

Three habits keep a shared trunk usable. Each costs the person following it very little, and skipping any of them costs
everyone else.

This standard implements [Root Cause Orientation](../../principles/root-cause-orientation.md) and
[Immutability](../../principles/immutability.md).

## Check Before Committing

Before each commit, run locally the checks the change can affect: tests, lint, type checks, and the build. The pipeline
is the second line of defence, not the first. Leaving it to find the problem turns a failure caught in seconds into one
caught in minutes, after other people may already have pulled it.

## Catch Up by Rebase While Unshared

Before pushing, bring the branch current with the latest trunk: fetch, then rebase the local commits onto it. Replaying
unshared commits keeps history linear, keeps a bisect meaningful, and lets conflicts be resolved one commit at a time.

For an authorized task-owned branch, follow the bounded
[task sync contract](no-destructive-git-operations/001-authorized-task-branch-sync.md). Outside that contract, rebase
only commits nobody else holds; merge instead in these cases:

| Situation                                          | Why merge is the safer choice                        |
| -------------------------------------------------- | ---------------------------------------------------- |
| the commits were already pushed and may be fetched | rebasing them rewrites history other people hold     |
| conflicts are heavy or recur across many commits   | one resolution is safer than many                    |
| both sides have diverged a long way                | replaying each local commit multiplies the conflicts |
| the parallel timing is itself worth keeping        | a merge commit records it                            |
| the outcome is uncertain                           | a merge rewrites nothing and can be revisited        |

Where [Integration Path](integration-path.md) forbids merging the trunk into a task branch, that rule wins: rebase, and
apply [No Destructive Git Operations](no-destructive-git-operations.md) to a rewrite outside the task sync contract.

A rebase that goes wrong is abandoned with `git rebase --abort`, a merge with `git merge --abort`; each returns to the
state before it started. When commits arrived, complete [Integration Diff Review](integration-diff-review.md) before
pushing.

## A Red Trunk Is Fixed or Reverted Now

When the trunk's pipeline fails, fix it at once or revert the breaking change with `git revert`, which adds an inverse
commit instead of rewriting history. Deferring is not an option: everyone who pulls a broken trunk inherits the failure,
and nothing can be released from it.

A revert is not a defeat. It restores a green trunk in one commit and leaves the real fix to be made at its cause,
without the whole team waiting on it.

## Owned Elsewhere

- Branch lifespan, worktrees, and the route to the trunk: [Integration Path](integration-path.md).
- How commits are divided and described: [Thematic Commits](thematic-commits.md) and
  [Commit Messages](commit-messages.md).
- Following the pipeline after a push: [CI Post-Push Verification](ci-post-push-verification.md).
- The order a change is built in, and keeping its edits surgical: [Implementation Stages](implementation-stages.md).
