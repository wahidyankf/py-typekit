---
name: specs-propagation
description: >-
  Repairs the rows of a frozen specs-quality ledger inside the listed specification folders, applying only repairs a
  rule settles and leaving every change to what a specification requires to its owner; the specs family's sole writer.
when_to_use: >-
  Use when the Specs Quality Gate hands over a frozen ledger, or when someone explicitly names rows of one to repair.
---

# Specs Propagation

## Contract

This is the `specs` family's sole writer, under
[Sole-Writer Propagation](../../development/workflow/sole-writer-propagation.md).

## Scope

Only the specification folders the gate's subject lists, with their subfolders. A row whose repair would reach any other
path is `needs-decision`, however obvious the edit.

## Executor

`specs-fixer`, loading the `validating-specification-structure` skill.

## Row Verification

A row closes when rereading the edited folder shows the row's target state and the repository's specification structure
and link checks exit 0 over it. Each ledger row ends `resolved`, `not-resolved`, `not-applicable`, or `needs-decision`,
with evidence.

## Family Rules

### Entry

The [Specs Quality Gate](specs-quality-gate.md) hands over a frozen ledger, or an explicit request names its rows.

- `findings` (`file`, required): the frozen ledger, with the listed folders it was frozen against.

### Sequence

1. **Sort each row** into one of three groups, which "What a Repair May Touch" in the
   `validating-specification-structure` skill details where the executor loads it:
   - **safe after re-checking**, applied: an index regenerated, a file renamed to the naming rule, a relative path or a
     view listing corrected;
   - **needs a person**, `needs-decision`: a missing user story, shared preconditions reconciled across a folder, a
     cross-folder contradiction, or a renamed actor;
   - **left alone**, `not-applicable` as outside what a repair may change: what a scenario says or requires,
     implementation alignment, or a legitimate difference between perspectives.

   A row that fits no group is `needs-decision`, never guessed.

2. **Apply only what the rule settles.** An index is regenerated from what its folder holds, using the structure check's
   output where one is adopted. A rename goes through version control's move, so history follows the file, and a
   relative path is corrected from the target's real location.
3. **Never change what a specification requires.** A repair that would add, remove, or reword a requirement or a
   scenario's expected behaviour is `needs-decision` for the specification's owner.
4. **Keep the recorded layout.** Where the repository recorded a layout that differs from
   [Specification Tree](../../conventions/structure/specification-tree.md), no file moves toward that convention; a
   migration is planned work.
5. **Mark delegated evidence `pending`** where a check's scope intersects an edited file, then verify each row.

### Exit

Outputs: `status` (`enum`: `no-change`, `landed`, `partial`, `input-changed`) and the ledger, each row with its status
and evidence. The caller [lands](../../conventions/structure/plans/009-portability.md#what-landed-means) the repairs. A
rerun on unchanged inputs changes nothing.

## Example Usage

```text
Run specs-propagation with the ledger the specs quality gate froze for billing/api and billing/web.
```

## Related Workflows

- [Specs Quality Gate](specs-quality-gate.md) judges the listed folders and hands its blocking rows here.
- [Docs Propagation](docs-propagation.md) carries a specification change into the documents that cite it.
