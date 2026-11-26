---
description: >-
  Fixes a workflow document's metadata, its required Entry, Sequence, and Exit sections, what each must state, and where
  rationale goes.
when_to_use: >-
  Use when writing a workflow document, or checking that an existing one states its full contract.
---

# Document Contract

## Location and Name

A workflow lives under `repo-governance/workflows/<group>/`, one file per workflow, and each group directory carries its
index. The file stem is the workflow's identifier and matches its `name` field, as
[Schemas by Path](../artifact-metadata/001-schemas-by-path.md) requires. What the name says follows
[Capability Naming](../capability-naming.md), and its characters follow [File Naming](../file-naming.md).

Only a gate or its propagation ends its file name in `-quality-gate.md` or `-propagation.md`. A module of a workflow
that runs a gate is named after its verdict step, such as `016-step-6-gate-verdict.md`, because a structural check for
gates reads every file with either suffix under the workflows root as a gate or a propagation, wherever it sits.

## Metadata

Exactly `name`, `description`, and `when_to_use`, in that order. Inputs, outputs, steps, and outcomes belong to the
body, never frontmatter.

## Required Sections

```markdown
# <Workflow Title>

## Entry

## Sequence

## Exit
```

| Section    | States                                                                                     |
| ---------- | ------------------------------------------------------------------------------------------ |
| `Entry`    | the condition holding before the first step, and every input taken                         |
| `Sequence` | the numbered steps, in the order they run                                                  |
| `Exit`     | the successful outcome and what it leaves behind, plus any named partial or failed outcome |

A `<family>-quality-gate` carries the sections the
[Quality Gate Contract](../../../development/workflow/quality-gate-contract.md) requires in place of these three. A
`<family>-propagation` carries the headings
[Sole-Writer Propagation](../../../development/workflow/sole-writer-propagation.md) requires, with its entry, sequence,
and exit under `## Family Rules`.

### Entry

The condition is observable: a plan in a named lifecycle root, a verdict recorded, a directory holding at least one
brief. "When ready" is not a condition, since nobody can check it; uncheckable text beside the condition, such as who
needs the result, is context, not condition.

Each input names its type, purpose, whether it is required, and its default when it is not. The type is one of `string`,
`number`, `boolean`, `file`, `file-list`, `directory`, or `enum`, and an `enum` lists its values. A default may instead
be given in the consuming step. A workflow taking no input beyond its entry condition says nothing more.

### Sequence

A numbered list, one step per item, each opening with a short bold phrase naming the step. The rest says what the step
does, and why when not obvious. An item may also state its success criterion: what must hold for the step to be done.
[Steps and State](002-steps-and-state.md) governs what a step declares.

### Exit

Success names the terminal state and every output: a file, a verdict, a moved folder. Each output carries a type from
the same set, and a `file`, `file-list`, or `directory` output also carries the path pattern it is written or moved to.

A workflow need not list failure outcomes it does not handle specially. Unless its item says otherwise, a failing step
ends the run as failed, naming that step. A workflow that can finish partially — some items resolved, others recorded as
blocked — names that partial outcome and what it leaves.

## Sections After Exit

After `Exit`, a workflow should carry `Example Usage`, showing a concrete invocation, and `Related Workflows`, linking
the workflows it composes with, so a reader sees how to start it and where it fits without searching.

It may also carry rationale sections arguing for its shape: why a budget is bounded, why a step comes first, what the
workflow deliberately does not do. Each is a `##` heading stating the argument. Rationale adds no step, but it may state
a constraint that bounds every step, such as a run that writes nothing. A rule that changes what one step does belongs
in that step.

## Why Three Fixed Sections

A reader deciding whether to start needs the entry condition, and one judging whether a run finished needs the exit,
without reading every step. Fixed headings put both in the same place everywhere, so a validator confirms they exist and
a reader never searches.

An adopter enforces the metadata and the three sections with its own workflow check in the pull-request gate.
