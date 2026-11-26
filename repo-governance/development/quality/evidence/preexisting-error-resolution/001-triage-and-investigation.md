---
description: >-
  Separates a missing regenerable artifact from a real defect, then takes a real failure from its full output to a
  verified cause, including auditing a mitigation that did not hold.
when_to_use: >-
  Use when a gate fails on a checkout and it is not yet known whether the failure is environmental or a defect.
---

# Triage and Investigation

## Triage First

Some failures are not defects. An ignored, regenerable artifact, such as build output, a dependency directory, or a tool
cache, can be absent because something cleaned it, and the right response is to regenerate it and retry.

- Regenerate with the repository's documented command, then re-run the step that failed. A first run from a cold cache
  is slow, not broken.
- Only a failure that **reproduces after a clean regeneration** is a defect, and the rule applies to it.
- A gate that fails on one checkout while the same commit passes elsewhere is first reproduced in a clean checkout.
  Local contamination, such as stale output, a nested copy of tracked files, or a stray artifact a tool discovers, adds
  findings that belong to no commit.

Regeneration is never avoided by damaging the repository:

- build output is never committed, and an ignored path is never un-ignored to keep an artifact around; and
- destructive recovery, such as a hard reset, a forced clean, or force-removing a worktree, is never used in place of
  regenerating. Nothing tracked was lost, so there is nothing to recover.

## Investigate a Real Failure

1. **Read the full output.** The whole trace or report, not its summary line.
2. **Establish that it predates the change.** Reproduce it on the base without the change, or show that it fails in a
   component the change did not touch.
3. **Trace it to its cause.** Diagnose before changing anything, as
   [Root Cause Orientation](../../../../principles/root-cause-orientation.md) requires.
4. **Fix and verify** under the rule in [Preexisting Error Resolution](../preexisting-error-resolution.md).

## When a Mitigation Already Exists

A failure that an earlier fix was meant to prevent is not evidence that it cannot be fixed. It is first evidence that
the mitigation does not do what it claims.

- **Observe the consumer, not the mitigation's intent.** A step that prepares a resource helps only if it names that
  resource the way the consumer requests it. Confirm by watching the consumer's actual invocation, through its own debug
  output or a stand-in that records its arguments, never by re-reading the mitigation's comment.
- **Make the mitigation able to fail.** A step that iterates an empty list does nothing and still exits cleanly. Assert
  that it produced a non-empty result, and prefer constructs that behave the same on every platform it runs on.

A mitigation that cannot fail cannot be verified, and it can sit in place, passing review, while protecting nothing.
