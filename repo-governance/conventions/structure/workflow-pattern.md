---
description: >-
  Defines what a workflow document is, when one is warranted, and the contract, step, checkpoint, and composition rules
  every workflow follows.
when_to_use: >-
  Use when deciding whether a procedure should become a workflow, or when writing, reviewing, or running a workflow
  document.
---

# Workflow Pattern

A workflow is an ordered procedure written down so that anyone, or any agent, can run it the same way twice. This
convention fixes the shape that makes that possible: a contract a reader can check before starting, steps whose order
and dependencies are stated, and outcomes that end the run. The catalog ships no workflow validator, so the pre-run
checks that module 3 lists run in the adopter's own validator.

## What a Workflow Is

A workflow orchestrates. Its steps may delegate to agents, run other workflows, or be procedures carried out directly,
in any mix. It states when it starts, what it needs, what happens in what order, what may repeat and until when, how a
failure is handled, and which outcomes end it.

It is not an agent, which does one job; not a script run once and thrown away; not a plan, which records intended work
rather than a repeatable procedure; and not a place to teach judgement, which belongs to a skill — see
[Capability Forms](../../development/agents/capability-forms.md).

## When One Is Warranted

| Write a workflow when                                                  | Do not, when                                |
| ---------------------------------------------------------------------- | ------------------------------------------- |
| two or more agents, workflows, or procedures must run in a set order   | one agent or one command does the whole job |
| the same sequence recurs                                               | the sequence will run once                  |
| one step's output feeds another, or steps branch on a condition        |                                             |
| independent steps can run in parallel, or a person must approve midway |                                             |

A sequence too tangled to write as steps is split into smaller workflows that compose, not written as one.

## The Contract Lives in the Body

Repositories place a workflow's contract in two ways: as structured frontmatter fields, or as body sections under a
minimal frontmatter. This convention selects the body. A workflow carries exactly the workflow schema from
[Schemas by Path](artifact-metadata/001-schemas-by-path.md) — `name`, `description`, `when_to_use` — and states its
entry condition, inputs, steps, outcomes, and outputs in prose sections. The metadata schema is closed, so contract
fields in frontmatter would fail it; and a body contract is readable without a parser and counted against the word
budget like any other rule.

## Modules

1. [Document Contract](workflow-pattern/001-document-contract.md)
2. [Steps and State](workflow-pattern/002-steps-and-state.md)
3. [Checkpoints, Composition, and Execution](workflow-pattern/003-checkpoints-composition-and-execution.md)

Retry budgets, repair cycles, and gate classes are not part of this convention; a workflow that repeats work follows
[Bounded Convergence](../../development/workflow/bounded-convergence.md).

## Principles

This convention implements [Explicit Over Implicit](../../principles/explicit-over-implicit.md), because a workflow's
entry, dependencies, and outcomes are stated where a reader and a validator can see them, and
[Simplicity Over Complexity](../../principles/simplicity-over-complexity.md), because sequential steps are the default
and every departure from it is declared.
