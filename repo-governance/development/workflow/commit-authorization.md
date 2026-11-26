---
description: >-
  Requires authorization before staging, committing, or pushing, keeps it scoped to the named task, and distinguishes
  ongoing delivery authority from a single action grant.
when_to_use: >-
  Use before staging, committing, or pushing, or when deciding whether an instruction or an approved plan permits
  recording history.
---

# Commit Authorization

Deciding what to change and recording it in history are separate decisions. An agent may make, verify, and describe a
change freely. Staging, committing, and pushing require authority covering those actions.

This standard implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md) and
[Immutability](../../principles/immutability.md): a recorded commit is a value other people may already hold, so it is
created only from a decision someone actually made.

## The Rule

Stage, commit, or push only when one of these holds:

- the user explicitly asked for that action; or
- a plan the user approved reaches a step naming that action.

With neither, prepare the change, verify it, report what remains uncommitted, and ask when the action is needed.

## Scope and Duration

A grant naming one action covers that action once. A grant to deliver a task covers the staging, thematic commits,
synchronization, publication, and landing needed for that same scoped outcome until the task is finished. Do not request
permission again for those routine steps;
[authorized task sync](no-destructive-git-operations/001-authorized-task-branch-sync.md) owns the safeguards for rebase
and lease pushes.

- Permission to commit one change set does not cover the next change, however small or soon.
- A change set authorized as a whole may be recorded as several [thematic commits](thematic-commits.md). Dividing it is
  how the authorized action is carried out, not a further decision to commit.
- Nothing carries over from a finished task into later work. Resuming the same unfinished task retains its recorded
  authorization; verify its scope and current state.

Task authority covers its named outcome, never unrelated changes or later tasks.

## What Does Not Grant It

- A request to edit, fix, test, finish, or tidy. Completing work is not recording it.
- A plan the agent wrote that the user has not approved.
- Permission for another action. Committing does not authorize pushing, and pushing existing commits does not authorize
  a new commit.
- Permission in a different repository, including one this repository depends on or pins.

Keep to the stated scope, meaning the files, theme, branch, and target it names, and ask before widening it.

| Instruction                 | Authorizes                            |
| --------------------------- | ------------------------------------- |
| "commit these changes"      | one commit action, no push            |
| "push the existing commits" | that push, no new commit              |
| "commit and push"           | both, within the current task's scope |
| "deliver this to main"      | task delivery within its named scope  |
| "finish this" or "fix it"   | neither, absent existing authority    |

## Separate Permissions

- Choosing where a change goes follows [Integration Path](integration-path.md), which picks a route and grants none.
- Merging a pull request follows [Pull Request Merge](pull-request-merge.md).
- Rewriting or discarding history follows [No Destructive Git Operations](no-destructive-git-operations.md).
- Bypassing a hook follows [Hook Verification](hook-verification.md), except the standing
  [worktree-to-PR pre-authorization](hook-verification/001-capacity-held-hook.md#worktree-to-pr-exception); publishing a
  release follows the adopter's rule. A commit or push grant includes neither.

## Why the Cost Is Asymmetric

A commit not yet made costs one question. A pushed commit reaches other clones within minutes and cannot be withdrawn;
see [Public Outbound Safety](../../conventions/security/public-outbound-safety.md). The rule requires a real
authorization decision while allowing an already authorized task to finish.
