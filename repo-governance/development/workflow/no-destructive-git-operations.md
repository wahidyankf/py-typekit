---
description: >-
  Requires per-instance approval for destructive Git effects outside an authorized task-owned branch sync, preserving
  other work, published trunk history, and recovery paths.
when_to_use: >-
  Use before resetting, cleaning, force-removing, deleting a branch, rewriting commits, or force-pushing, or before
  acting on a worktree this task does not use.
---

# No Destructive Git Operations

Git keeps no undo for work that was never committed, and a rewrite of published history reaches every clone that holds
it. Assume other people, agents, and background processes are using the same machine and remote at the same moment. A
command that costs someone their own scratch work in a solo checkout can destroy another person's work on a shared one.

This standard implements [Deliberate Problem-Solving][catalog-deliberate-problem-solving],
[Immutability](../../principles/immutability.md), and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## The Rule Is the Effect

Require explicit approval for each Git operation that discards uncommitted changes, destroys another actor's work,
rewrites history others may hold, or removes recovery, except the bounded
[authorized task-owned branch sync](no-destructive-git-operations/001-authorized-task-branch-sync.md). The spelling is
irrelevant: an alias, a script, a pipeline step, or an unlisted flag with the same effect is covered. Ask what the
command destroys and who made it, not whether it appears below.

## Common Cases

- `git push --force` can erase remote commits absent locally. Use an explicit expected-value lease and
  `--force-if-includes` only under the authorized sync contract or per-instance approval.
- `git push --force-with-lease` without an expected value can miss work after a background fetch. Use
  `--force-with-lease=<ref>:<expected-sha>`.
- Rebasing or amending pushed commits rewrites history others built on. Use `git revert` outside the authorized sync
  contract, or obtain per-instance approval.
- Whole-history rewriting affects every ref for everyone. Prefer a scoped revert, coordinated out of band.
- `git reset --hard`, `git checkout -f`, and `git switch --discard-changes` discard uncommitted changes. Commit first,
  or use `git stash push -- <path>` and keep the entry where stashing is authorized.
- `git checkout -- <path>` and `git restore <path>` erase unstaged edits. Commit or stash first where authorized.
- `git clean -fd` and `git clean -fdx` remove untracked and ignored files. Preview with `git clean -n`, then delete
  named paths.
- `git stash drop` and `git stash clear` remove recovery entries. Leave them.
- `git branch -D` and `git update-ref -d` skip the merged check. Use `git branch -d`, or task-branch
  [clean-up](../../workflows/maintenance/dev-artifact-clean-up.md) with its proofs.
- Expiring the reflog and pruning together removes recovery. Let automatic maintenance run.
- `git worktree remove --force` or deleting its folder erases uncommitted work. Use plain `git worktree remove`, or
  `git worktree repair` after a move.

## Asking for Approval

For an operation outside the authorized sync contract, first look for a route that destroys nothing: a new commit, a
revert, a removal without force. When none exists:

1. State the exact command as it will run.
2. State what it affects: the ref, the commits left unreachable where they can be determined, and the paths.
3. Ask a yes-or-no question and wait for the answer.
4. Run exactly what was approved. If a flag, ref, or target changes, ask again.

Such per-instance approval never carries forward. The repository can change between two operations, and the earlier
answer was about a state that no longer exists. Task authorization follows [Commit
Authorization][catalog-commit-authorization].

A secret found in history is no exception. Its rewrite is approved by whoever holds authority over that history and
follows [No Secrets in Tracked Files](../../conventions/security/no-secrets-in-tracked-files.md), which puts rotation
first.

## Shared-Machine Facts

- Worktrees share the object database and every ref, while each keeps its own `HEAD` and index. Checkouts of different
  branches do not collide, yet garbage collection, pruning, and forced removal reach state other worktrees depend on.
- Git refuses to check out a branch active in another worktree. Never defeat that guard with `--ignore-other-worktrees`.
- Stage only explicit paths that [File-Touch Discipline][catalog-file-touch-discipline] accounts for. A destructive
  operation in another task's worktree needs positive evidence it is idle, not merely no sign it is busy.

## Prefer Additive

When destructive and additive operations reach the same end state, take the one that leaves a trail. A revert can be
reverted; an erased commit cannot be recalled from nothing. Before any bulk deletion, run its dry-run form.

[catalog-deliberate-problem-solving]:
  https://github.com/wahidyankf/ose-rules/blob/9e15c702ef01187f5a3fafca975d2891854c0495/repo-governance/principles/deliberate-problem-solving.md
[catalog-commit-authorization]:
  https://github.com/wahidyankf/ose-rules/blob/9e15c702ef01187f5a3fafca975d2891854c0495/repo-governance/development/workflow/commit-authorization.md
[catalog-file-touch-discipline]:
  https://github.com/wahidyankf/ose-rules/blob/9e15c702ef01187f5a3fafca975d2891854c0495/repo-governance/development/workflow/file-touch-discipline.md
