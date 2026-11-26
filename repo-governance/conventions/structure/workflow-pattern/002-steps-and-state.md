---
description: >-
  Fixes the three kinds of workflow step, sequential as the default with declared parallel and conditional steps, how
  steps reference inputs and earlier outputs, and what a failing step does.
when_to_use: >-
  Use when writing a workflow step, deciding whether steps may run concurrently, or stating what happens when one fails.
---

# Steps and State

## Three Kinds of Step

| Kind      | The step names                                                                 | Performed by                                                                                                 |
| --------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| delegated | the agent that performs it                                                     | that agent, or the orchestrator in its place — see [Execution](003-checkpoints-composition-and-execution.md) |
| nested    | the workflow it runs, by that workflow's `name` or a relative link to its file | a run of the nested workflow                                                                                 |
| procedure | nothing beyond its own instructions                                            | whoever is running the workflow                                                                              |

A step that names no agent and no workflow is a procedure. Its text is then the whole instruction, so it is written
precisely enough to carry out without guessing, stating whichever of the command, the file, the decision, and what
counts as done apply.

## Sequential by Default

Steps run in their numbered order, one at a time, and a step may use anything an earlier step produced. A step needs no
annotation to run this way.

Two departures are declared in the step itself:

- **Parallel.** A step that groups independent work states that its parts run concurrently. Parts are independent only
  when none reads what another writes and none needs another's result. The dependency graph decides how wide a run fans
  out; a concurrency cap only limits it. Raising the cap above the number of independent parts gains nothing, and
  dependent work is never forced into a parallel slot to fill one.
- **Conditional.** A step that runs only sometimes states its condition as a check on an input or an earlier result.
  When the condition is false, the run continues to the next step unless the step says otherwise: skip to a named step,
  or end the run with a named outcome.

## References and State

A step refers to what it consumes by name: an input declared in `Entry`, or an output of a named earlier step. A
reference to something no earlier step produces, or to a later step, is a defect.

Steps form no cycle. A step that must repeat does so by an explicit instruction in its own item — repeat until a stated
condition holds, within a stated limit — never by pointing back to an earlier step number. A pointer back creates a
cycle among steps, which the pre-run check must reject, so the repetition is stated inside the step that repeats.
Repetition and its limits follow [Bounded Convergence](../../../development/workflow/bounded-convergence.md).

State that must survive an interruption is written somewhere durable as the run proceeds, not held in the runner's
memory, so a resumed run continues from where it stopped.

## When a Step Fails

The default is that a failing step ends the run as failed, naming the step. A step that handles failure differently says
so in its item, choosing one of:

| Handling | Means                                                                    |
| -------- | ------------------------------------------------------------------------ |
| retry    | run the step again, within a stated limit                                |
| continue | record the failure and go on, when later steps do not depend on this one |
| fallback | run a named alternative step                                             |
| escalate | stop at a human checkpoint and let a person choose                       |

A retry without a limit is a loop that ends when someone notices, and a continue that hides a failure from the exit
reports success for a run that did not have it. The exit therefore names every failure a run recorded and continued
past.
