---
description: >-
  Allows one authorized push of a task-owned branch to skip a pre-push hook the compute guard stopped before any check
  started, when the hosted gate mirrors the hook and passes on the same head; plus the standing worktree-to-PR
  pre-authorization for task-owned branches with passing manual screens.
when_to_use: >-
  Use when a compute guard reports exit 124 with a never-started receipt for a pre-push hook and waiting for capacity
  would stall an otherwise ready task branch, or when a worktree-to-PR branch skips its hooks given passing manual
  screens.
---

# Capacity-Held Hook

[Back to Hook Verification](../hook-verification.md)

A hook held back by capacity has run nothing, so it holds no finding to fix. Retrying once the condition clears stays
the default. This module states the exceptions for guard-held hooks: the one-push exception and the standing
worktree-to-PR exception below.

## The Exception

One push of a task-owned branch may skip its pre-push hook when every condition holds:

1. The compute guard stopped the hook before any check started: exit `124` with a `never-started` receipt naming a
   capacity or pressure reason. A hook that started, was shed mid-run, or reported any check result never qualifies.
2. A human authorized that one push by name. The authorization is spent by the push; an agent never authorizes its own
   bypass and never carries an earlier approval into this one.
3. The outbound safety screen passed for the range being pushed. The screen has no bypass; run it directly when the hook
   that normally carries it is the one held back.
4. The repository repeats the hook's deterministic checks in a hosted gate that a merge cannot skip, and the push opens
   or updates the pull request that runs it. A repository with no hosted mirror, or one whose delivery reaches its trunk
   without such a gate, never qualifies.

## After the Push

- Record in the task record: the receipt, the authorizing human, the safety-screen result, and the pull request.
- The branch does not merge until the hosted gate passes on the exact pushed head. A later push replaces that head and
  owes a fresh pass; nothing about this exception waives it.
- Suites the hosted pull-request gate does not run, such as integration or end-to-end suites placed after merge, stay
  owed where their own standards place them. This exception moves no suite.

## Worktree-to-PR Exception

When a task-owned branch lands through a pull request whose quality gate mirrors the skipped hook's deterministic
checks, pushing that branch with `--no-verify` and letting the hosted gate run the checks is sound, and preferable under
HIPPO contention (HIPPO deferral/failure, exit `124`/`125` `never-started`, abnormal latency, or a wait). The maintainer
pre-authorizes `--no-verify` on `git commit` and `git push` for such a branch landing through
[the integration path](../integration-path.md) — worktree to pull request to merge — with no per-instance prompt when
every condition below holds, superseding the earlier HIPPO-congestion-only pre-authorization.

- The branch is a task-owned worktree branch whose only route to `main` is its pull request. Direct pushes to `main`
  stay excluded: explicit per-instance authorization still applies.
- A hook that reported a violation is fixed at its cause; no reported finding is skipped. The outbound safety screens
  have no bypass — the tracked-tree screen and the per-commit range screen both exit `0`, with no leak-review finding,
  run manually. The `commit-msg` hook stays enabled.
- Formatting is done by hand; the hosted gate verifies it.
- The bypass cites receipt and screen evidence in the push and PR notes, and never carries into a later operation.
- The branch does not merge until the hosted gate passes on the exact pushed head. A later push owes a fresh pass.

Enforcement: gated — [`pr-quality-gate.yml`](../../../../.github/workflows/pr-quality-gate.yml) runs on every pull
request, blocking the merge on a bypassed-hook failure; review verifies the cited evidence against the gate result.

## What This Never Covers

- A hook that ran and failed, however unrelated the failure looks. Fix the cause or seek direction under the parent
  standard; a capacity receipt from an earlier attempt does not convert a failure into a deferral.
- Skipping a commit hook to land work locally where no hosted gate will ever see it.
- Weakening, muting, or removing any check, locally or hosted, to make room for this exception.

**Enforcement: unenforced by decision**, because task ownership, human authorization, and receipt authenticity are
judgements no mechanical check settles. Review verifies the recorded receipts against the hosted gate's result.
