---
description: >-
  Requires reading the full diff of every commit an integration brings onto the current branch, and reconciling the
  task, plan, assumptions, and completed verification, before the next action.
when_to_use: >-
  Use immediately after a rebase, pull, merge, cherry-pick, or fast-forward brings in commits the branch did not have.
---

# Integration Diff Review

An integration that brings in commits moves the ground under the work in progress. A file being edited may have moved, a
function being called may have a new signature, a rule being followed may have been rewritten. Git reports textual
conflicts and nothing else, so a clean integration proves the history's shape and not the work's safety.

This standard implements [Deliberate Problem-Solving](../../principles/deliberate-problem-solving.md) and
[Evidence Over Assertion](../../principles/evidence-over-assertion.md).

## What Counts as Incoming

A commit is incoming when it was absent from the branch before the operation and present after it. Branch membership
decides, not authorship: a commit the same person made in another branch or session is still incoming here. Rebasing,
pulling, merging, cherry-picking, and fast-forwarding local `main` all qualify. An operation that brings nothing in,
such as a pull reporting that the branch is already up to date, needs no review.

## The Checkpoint

Before the next task action:

1. **Identify the range.** Note the tip before the operation (after a rebase, `ORIG_HEAD` or the reflog) and list what
   arrived with `git log --oneline <old>..<new>`.
2. **Read the full diff.** Use `git diff <old>..<new>`, or `git show` per commit for a long range. Commit subjects and a
   list of paths are not the diff.
3. **Reconcile everything active.** The current task, the rest of the plan, every assumption in use, the set of files
   this work owns, and every check already run or still to run. A semantic effect matters even where no path overlaps.
4. **Keep ownership honest.** Paths that arrived do not become this work's files by arriving. A path joins that set only
   when this work goes on to change it.
5. **Adjust and record.** Update the task or plan, replace assumptions that no longer hold, and rerun each completed
   check whose evidence depended on the old tip. Record the reconciliation before continuing.

## What to Look For

- files this work is editing or about to edit that were renamed, restructured, or changed nearby
- functions, types, or configuration keys the work calls or reads
- instruction and rule files that redefine something the work follows
- dependency, lockfile, or toolchain changes that break an assumption about available tools or interfaces
- tests that now cover, or now contradict, the behaviour being changed
- completed checks whose inputs the incoming range touched

## Not a Review

- Continuing because no conflict markers appeared.
- Reading the commit list and skipping the changed lines.
- Treating a fast-forward as safe because it created no merge commit.
- Trusting a check that ran against the old tip.

## Enforcement

Unenforced by tooling, by decision. Git can print the range, but no check can tell whether its consequences were
understood and each affected assumption adjusted. Review and the plan's own checkpoints carry the obligation, and
[Integration Path](integration-path.md) places it after every sync.
