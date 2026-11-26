---
description: >-
  Requires a rule, value, or structure that must hold across several files to live in one declared source, with every
  dependent generated from it, validated against it in the normal gate, and never edited by hand.
when_to_use: >-
  Use when the same rule, value, or structure has to stay identical in two or more files, before writing it as prose
  someone must keep in step by hand.
---

# Mechanize Cross-File Invariants

A rule that must stay true across several files, and is kept true only by contributors remembering every copy, will
eventually be forgotten in at least one. Nothing reports the drift; the copies simply stop agreeing.

This standard implements [One Source Per Fact](../../../principles/one-source-per-fact.md),
[Automation Over Manual](../../../principles/automation-over-manual.md), and
[Root Cause Orientation](../../../principles/root-cause-orientation.md). Hand-synchronized drift is a recurring symptom
of one cause, the missing single source, and repairing each instance leaves that cause in place.

## First, Remove the Copy

The cheapest invariant is one that no longer spans files. Where a dependent can point at the source, by a link or by an
instruction to query the live value, replace the copy with that reference. Generation is for a dependent that must
physically hold the content, because a tool or a harness reads that file.

## The Rule

When the content must exist in more than one file:

1. **Declare one source.** A schema, a registry, or a configuration key holds the content exactly once.
2. **Generate every dependent from it**, mechanically, rather than authoring each copy to match.
3. **Validate the dependents in the normal gate.** A dependent that differs from what the generator would produce now is
   a failure, not a warning. Generation from unchanged input must be byte-identical, so regenerating and comparing is
   the check.
4. **Never edit a generated file by hand.** Its history shows only regenerated diffs. A hand edit that happens to match
   the generator's output is still drift waiting for the next change to the source.

This is the default response wherever a rule would otherwise be stated in prose and trusted to hold identically in
places prose cannot check. It is not a device reserved for one subsystem.

## Working With Generated Files

- A generated dependent changes in the same change as its source. A tree where the two disagree is a published
  inconsistency, even if the next change repairs it.
- A merge conflict in a generated file is resolved in its source, and the dependent is then regenerated. Resolving the
  conflict in the output is editing a generated file by hand.

## Examples

**Pass.** A pipeline's list of checks is copied into its workflow file and into a documentation table, and the two have
already drifted once. The workflow now derives its list from the declared gate registry, and the documentation directs
readers to the command that prints the current set instead of embedding a table.

**Fail.** One cross-cutting rule is written into three governance documents, each in its own words. The next change to
the rule updates two of them, and nothing notices the third.

## Scope

This applies whenever a rule, value, or structure must hold identically in two or more files or surfaces of one
repository. It does not apply to:

- content deliberately allowed to differ, where mechanizing an invariant that is not one produces drift reports for
  divergence that is correct; or
- a rule stated once, with no second location that must agree. There is nothing to mechanize until a second copy exists
  or is planned.

## Where It Is Already Applied

[Harness Adapters](../../agents/harness-adapters.md) generates each harness file from its canonical artifact and
verifies it by regeneration. [Gate Entries](../../../conventions/structure/repository-configuration/002-gate-entries.md)
has hooks dispatch the declared gate list rather than transcribe it.

An adopter enforces the validation step in its own gate.
