---
name: dev-artifact-clean-up
description: >-
  Removes the scratch files, reports, branches, and worktrees a task created, proves them gone, and reconciles the
  default branch, retaining with reasons what it cannot safely remove.
when_to_use: >-
  Use after finishing any task, plan, or investigation that produced artifacts the repository should not keep.
---

# Dev Artifact Clean-Up

## Entry

A task, plan, or investigation has finished and produced artifacts useful during the work but not part of its result.

Finished means [landed](../../conventions/structure/plans/009-portability.md#what-landed-means) or deliberately
abandoned: never between units sharing a worktree, and never as a periodic sweep.

- `integration` (`enum`: `pull-request`, `local-main`; required): the adopter's integration path. `pull-request`
  isolates each task, reviews its head, and leaves worktrees and branches step 3 guards; `local-main` leaves only files
  and build output, without isolation or a reviewed head.
- `outcome` (`enum`: `pass`, `partial`, `fail`; required): how the producing run ended.

## Sequence

1. **Enumerate what the task created.** Scratch directories, generated reports, temporary scripts, downloaded fixtures,
   task branches and worktrees, and any tooling installed only for this work. Include regenerable build output and
   [leaked test containers](dev-artifact-clean-up/002-leaked-test-containers.md). Never list a real environment file,
   per [Agent Environment-File Access](../../conventions/security/agent-env-file-access.md), or other local secret:
   nothing rebuilds one.

   Never delete a secret-bearing file or directory from the primary `main` checkout. An exact ignored, nonshared cache
   such as `.fvm-cache/` is scratch after recorded regeneration, non-use, and secret-free evidence, regardless of
   origin.

2. **Classify each one:**

   | Class    | Disposition                                                                                                                                                                                                                         |
   | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
   | result   | keep; it is part of what the work delivered                                                                                                                                                                                         |
   | evidence | keep where the plan declared evidence, which for a plan is its `evidence/` folder, per [Evidence Files](../../conventions/structure/plans/016-evidence-files.md); a task outside a plan keeps evidence where its own rules place it |
   | scratch  | remove                                                                                                                                                                                                                              |
   | unknown  | investigate before removing; never delete something you cannot classify                                                                                                                                                             |

   After a `partial` or `fail` outcome, the worktree and build output are evidence until diagnosis; logs and traces a
   diagnosis needs always are.

3. **Remove the scratch class.** Delete files, remove worktrees, delete task branches that served their purpose. Under
   `pull-request`, a worktree or branch goes only when the tool's own listing shows this task created it, nothing in it
   is uncommitted, unpushed, or running, and its pull request merged at the local tip or was deliberately abandoned;
   otherwise retain it with the reason. Remove from outside the directory, and never force a worktree removal or stash
   to empty one, since a clone's worktrees share one stash stack. A plain branch delete refuses after a rebase or squash
   merge. After a pruning fetch, force it only for a task branch no worktree holds that **landed**, its pull request
   merged with its head equal to the tip or `git cherry origin/main <branch>` printing only `-` lines, or is **stale**,
   its tip over 72 hours old with no open pull request. When that cherry prints a `+` line, preserve a stale tip first:
   keep its remote branch if that holds the tip, else `git bundle create <path> origin/main..<branch>` under ignored
   scratch, recording the path. Delete a remote branch by exact ref only if merging did not, and a stale one only after
   that. A branch the Git host protects against deletion is protected on purpose: retain it; never lift that protection.
4. **Preserve unrelated work.** A dirty file this task did not create is not cleanup's business: cleanup removes what
   the task made, never restoring a working copy to some imagined clean state.
5. **Prove absence.** Re-list the paths to confirm they are gone and the working tree holds only what it should. An
   unverified cleanup is a claim.
6. **Reconcile the default branch.** With a remote, fetch with pruning, fast-forward, and prove zero divergence both
   ways. A refused fast-forward is a local commit to inspect, never to force, and ends the run `retained`, naming that
   commit.

## Exit

A `clean` result means every task-created artifact is classified, the scratch class is removed with absence verified,
unrelated changes are untouched, and any remote default branch shows zero divergence.

Outputs: `result` (`enum`: `clean`, `retained`) and `retained-items` (`string`, each kept artifact and why). `retained`
is the partial outcome; it is terminal and never authorizes a forced removal.

## Example Usage

```text
Run dev-artifact-clean-up with integration pull-request and outcome pass.
```

## Related Workflows

- [Execution](../plan/plan-execution.md) produces most of what this removes.
- [Release Cut](release-cut.md) leaves build scratch for it.
- [Irreversible Deletion](dev-artifact-clean-up/001-irreversible-deletion.md) says why `unknown` is never removed.
