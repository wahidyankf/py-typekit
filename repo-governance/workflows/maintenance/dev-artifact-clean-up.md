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

- `integration` (`enum`: `pull-request`, `local-main`; required): the adopter's integration path, here `pull-request`,
  which leaves the worktrees and branches step 3 guards.
- `outcome` (`enum`: `pass`, `partial`, `fail`; required): how the producing run ended.

## Sequence

1. **Enumerate what the task created.** Scratch directories, generated reports, temporary scripts, downloaded fixtures,
   task branches and worktrees, and any tooling installed only for this work. Include regenerable build output. Never
   list a real environment file, per [Agent Environment-File Access][agent-env-file-access], or other local secret:
   nothing rebuilds one.

   Never delete a secret-bearing file or directory from the primary `main` checkout. An exact ignored, nonshared cache
   is scratch after recorded regeneration, non-use, and secret-free evidence, regardless of origin.

   A task here can create, all ignored, with rebuild commands: `worktrees/<task>` and its branch; `.venv/`
   (`uv sync --locked`); `node_modules/` (`npm ci`); `__pycache__/` and `.pytest_cache/` (`uv run pytest`);
   `.ruff_cache/` (`uv run ruff check`); `.coverage` (`uv run --locked coverage run -m pytest`); `dist/` (`uv build`);
   scratch under `local-tmp/`.

2. **Classify each one:**

   - **result:** keep; it is part of what the work delivered.
   - **evidence:** keep where the plan declared evidence, which for a plan is its `evidence/` folder, per
     [Evidence Files](../../conventions/structure/plans/015-evidence-files.md); a task outside a plan keeps evidence
     where its own rules place it.
   - **scratch:** remove.
   - **unknown:** investigate before removing; never delete something you cannot classify.

   After a `partial` or `fail` outcome, the worktree and build output are evidence until diagnosis; logs and traces a
   diagnosis needs always are.

3. **Remove the scratch class.** Delete files and remove worktrees. Under `pull-request`, a worktree goes only when
   `git worktree list` shows this task created it, nothing in it is uncommitted, unpushed, or running, and its pull
   request merged or was deliberately abandoned; otherwise retain it with the reason. Remove from outside the directory;
   never force a worktree removal or stash to empty one, since worktrees share one stash stack.

   A rebase merge makes `git branch -d` refuse. After `git fetch origin --prune`, `git branch -D <branch>` may delete a
   task branch no worktree holds (`git worktree list --porcelain` names no `branch refs/heads/<branch>`) that either
   **landed**, its pull request `MERGED` with `headRefOid` equal to the tip or `git cherry origin/main <branch>`
   printing only `-` lines, or is **stale**, its tip's committer date over 72 hours old with no open pull request from
   it. When that cherry prints a `+` line, a stale tip is preserved first: keep `origin/<branch>` if it holds the tip,
   else `git bundle create <path> origin/main..<branch>` under `local-tmp/`, recording the path. The remote branch goes
   by exact ref, `git push origin --delete <branch>`. Otherwise retain the branch with the reason. Never use wildcard
   refs, delete `main` or a protected branch, or lift a host's branch protection.

4. **Preserve unrelated work.** A dirty file this task did not create is left alone: cleanup removes only what the task
   made.
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

## Deletion Is Permanent

Version control restores only committed work, so deleting an uncommitted artifact is permanent; hence `unknown` routes
to investigation, never removal.

[agent-env-file-access]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/security/agent-env-file-access.md
