---
description: >-
  Fixes how a workflow pauses for a person, how workflows nest without cycles, who performs a step that names an agent,
  and what is validated before a run starts.
when_to_use: >-
  Use when a workflow needs human approval, runs another workflow, runs on a harness without the agent it names, or is
  about to be executed.
---

# Checkpoints, Composition, and Execution

## Human Checkpoints

A step that waits for a person is a checkpoint, and it states three things:

1. **The prompt** — the question, with what the person needs to answer it: the report path, the finding count, the diff.
2. **The options** — mutually exclusive, each naming the step or outcome that follows it. An open alternative, which
   accepts an answer nobody listed, and a discussion alternative may instead return to the same checkpoint.
3. **What rejection does** — a rejection option ends the run with a named outcome. It never loops back silently to retry
   the same work.

A checkpoint may adopt a linked decision protocol, such as
[Decision Gates](../../../development/agents/planning-capabilities/003-decision-gates.md), in place of stating its own
prompt and options. It still names the outcome with which a rejection ends the run.

A checkpoint waits for an answer; no timeout approves on the person's behalf. A run resumed after a pause re-presents a
checkpoint left unanswered, and an answer already recorded stands.

## Composition

A step may run another workflow by naming it. The nested workflow runs to one of its own exit outcomes, and that outcome
is the step's result, which later steps reference like any other.

The nesting is declared, never implied: a workflow that runs another names it in the step. Nesting forms no cycle — a
workflow never runs itself, directly or through another — because a cycle has no exit a reader can find.

Composition is how a long procedure stays readable. When a sequence outgrows its document, the independent stretches
become workflows of their own, and the parent names them.

## Execution Mode

A step naming an agent is delegated to that agent when the harness running the workflow defines it. Otherwise the
orchestrator performs the step itself, reading the agent's canonical definition and following it as written. Nested
workflows apply the same choice to their own steps.

Steps that must persist changes run where writes land in the working tree, and the working tree is checked after each
such step, so a delegation that wrote nowhere is caught before a later step builds on it.

The workflow document does not choose the mode, and it names no harness. Which agents a harness defines is adapter
detail, per [Harness Adapters](../../../development/agents/harness-adapters.md), and the same workflow runs correctly
whichever mode each step ends up in.

## Validated Before a Run

Before the first step, a workflow is checked for:

- metadata matching the workflow schema, with `name` matching the file stem;
- `Entry`, `Sequence`, and `Exit` sections present;
- every input and output declaring a type from the stated set, and every file or directory output a path pattern;
- every named agent and nested workflow existing in the repository;
- every reference resolving to a declared input or an earlier step's output;
- no cycle among steps or nested workflows; and
- every checkpoint option naming a step or an outcome, or returning to its own checkpoint.

A run that starts on an unchecked workflow discovers its broken reference halfway through, with half its changes made.
An adopter runs these checks in its own workflow validator, in the pull-request gate, rather than at run time.
