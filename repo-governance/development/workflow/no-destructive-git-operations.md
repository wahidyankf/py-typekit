---
description: >-
  Requires per-instance approval, and names an additive equivalent, for any git operation that discards uncommitted
  work, rewrites published history, or removes the means of recovery, force pushes included.
when_to_use: >-
  Use before resetting, cleaning, force-removing, deleting a branch, rewriting commits, or force-pushing, or before
  acting on a worktree this task does not use.
---

# No Destructive Git Operations

Git keeps no undo for work that was never committed, and a rewrite of published history reaches every clone that holds
it. Assume other people, agents, and background processes are using the same machine and remote at the same moment. A
command that costs someone their own scratch work in a solo checkout can destroy another person's work on a shared one.

This standard implements [Deliberate Problem-Solving][deliberate-problem-solving],
[Immutability](../../principles/immutability.md), and
[Root Cause Orientation](../../principles/root-cause-orientation.md).

## The Rule Is the Effect

Any git invocation whose effect is to discard uncommitted changes, destroy work this actor did not create, rewrite
history others may hold, or remove the means of recovering any of those needs explicit approval for that one instance.
The spelling is irrelevant: an alias, a script, a pipeline step, or an unlisted flag with the same effect is covered.
Ask what the command destroys and who made it, not whether it appears below.

## Common Cases

- `git push --force` destroys remote commits absent locally. Instead: `--force-with-lease=<ref>:<expected-sha>` plus
  `--force-if-includes`, approved.
- `git push --force-with-lease` without an expected value destroys the same, once a background fetch refreshed the ref.
  Instead: the explicit `<ref>:<expected-sha>` form.
- rebasing or amending pushed commits destroys history others built on. Instead: `git revert`.
- a whole-history rewriting tool destroys every ref, for everyone. Instead: a scoped revert, coordinated out of band.
- `git reset --hard`, `git checkout -f`, `git switch --discard-changes` destroys uncommitted changes. Instead: commit
  first, or `git stash push -- <path>` and keep the entry.
- `git checkout -- <path>` or `git restore <path>` over edits destroys the unstaged edits at those paths. Instead:
  commit or stash first.
- `git clean -fd` or `git clean -fdx` destroys untracked and ignored files. Instead: `git clean -n` to preview, then
  delete named paths.
- `git stash drop`, `git stash clear` destroys stash entries, which then become prunable. Instead: leave the entries.
- `git branch -D`, `git update-ref -d` destroys a branch, skipping the merged check. Instead: `git branch -d` by
  default; [an unused task branch][clean-up] may use `-D`.
- expiring the reflog and pruning at once destroys the recovery path itself. Instead: let automatic maintenance run.
- `git worktree remove --force`, deleting a worktree folder destroys a working tree and everything uncommitted in it.
  Instead: plain `git worktree remove`, or `git worktree repair` after a move.

## Asking for Approval

First look for a route that destroys nothing: a new commit, a revert, a removal without force. When none exists:

1. State the exact command as it will run.
2. State what it affects: the ref, the commits left unreachable where they can be determined, and the paths.
3. Ask a yes-or-no question and wait for the answer.
4. Run exactly what was approved. If a flag, ref, or target changes, ask again.

Approval never carries forward. The repository can change between two operations, and the earlier answer was about a
state that no longer exists.

A secret found in history is no exception. Its rewrite is approved by whoever holds authority over that history and
follows [No Secrets in Tracked Files](../../conventions/security/no-secrets-in-tracked-files.md), which puts rotation
first.

## Shared-Machine Facts

- Worktrees share the object database and every ref, while each keeps its own `HEAD` and index. Checkouts of different
  branches do not collide, yet garbage collection, pruning, and forced removal reach state other worktrees depend on.
- Git refuses to check out a branch active in another worktree. `--ignore-other-worktrees` defeats that guard, so never
  pass it.
- Stage only by explicit path, never the whole tree, and only the paths [File-Touch Discipline][file-touch-discipline]
  accounts for. A destructive operation in a worktree this task does not use needs positive evidence that worktree is
  idle, not merely no sign it is busy.

## Prefer Additive

When a destructive operation and an additive one reach the same end state, take the one that leaves a trail. A revert
can be reverted; an erased commit cannot be recalled from nothing. Before any bulk deletion, run its dry-run form.

[deliberate-problem-solving]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/principles/deliberate-problem-solving.md
[file-touch-discipline]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/file-touch-discipline.md
[clean-up]: ../../workflows/maintenance/dev-artifact-clean-up.md
