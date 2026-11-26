---
description: >-
  Governs how an agent carries multi-step work: plan it before acting, delegate broad research, verify the result before
  reporting done, and re-plan when the approach stops working.
when_to_use: >-
  Use when starting a task with several steps, deciding whether to hand part of it to a delegated agent, or about to
  report work as finished.
---

# Agent Workflow Orchestration

These rules govern the working session rather than any document. They apply to every agent carrying a task from request
to report, whatever the task is.

## Plan Non-Trivial Work First

A task is non-trivial when any of these holds:

- it needs three or more distinct steps;
- it changes several files or components;
- it involves a structural or architectural choice; or
- the right approach is not evident from the request.

Non-trivial work gets a written plan of its approach before the first change: the steps, their order, and how each will
be confirmed. Small work, such as a single unambiguous change, is exempt only from that upfront plan. Planning a typo
fix costs attention and clarifies nothing.

The exemption never extends to the live task list. [Task Tracking](task-tracking.md) governs when that list opens and
how it is kept, for every task whatever its size. The written plan is working state for the session, distinct from a
plan under the [Plans Convention](../../conventions/structure/plans.md), which this standard neither requires nor
replaces.

Planning comes first because an agent that acts before stating its steps discovers the dependencies between them by
breaking them.

## Delegate Broad Research, Keep the Decision

Hand work to a delegated agent when it would otherwise flood the working context: reading across many files, answering
independent questions in parallel, or a subtask large enough to need its own plan.

Only a top-level session, or an agent declaring `subagent` while running top-level, hands work over. One exception: an
agent that declares `dispatches` may, as a delegate, hand work to exactly those agents where the harness lets a
delegated agent spawn agents; where it cannot, that agent runs as the main thread. Any other delegated agent that needs
further delegation returns the need to its caller, for the reason [Capability Forms](capability-forms.md) gives.

- **One concern per delegate.** A delegate given two questions answers the easier one well.
- **Findings, not transcripts.** The delegate returns conclusions and the evidence for them, not everything it read
  along the way.
- **Not for small lookups.** A read or search that takes one or two operations is cheaper done directly than described
  to someone else. Public-web research follows the threshold in [Web Research Delegation](web-research-delegation.md)
  instead of this floor.

The reason is the quality of what follows. Detail needed for the research but not for the decision crowds out the
reasoning that comes after it.

## Verify Before Reporting Done

Work is not done because its commands ran. Before reporting completion, reconcile the task list as the completion rule
in [List Lifecycle](task-tracking/001-list-lifecycle.md) requires, and:

1. re-read every changed file and confirm the intended change is present;
2. run the checks that cover the change, and read their output for failures that did not stop the run; and
3. demonstrate the behaviour the request asked for, not only that no existing check failed.

| Change           | Minimum verification                                            |
| ---------------- | --------------------------------------------------------------- |
| behaviour change | covering tests pass, and the new behaviour is shown directly    |
| defect fix       | a check that failed before the fix passes after it              |
| refactor         | the same checks pass before and after, with behaviour unchanged |
| documentation    | every link resolves and the content renders as intended         |
| any change       | nothing that passed before the change fails after it            |

A passing suite is necessary and not sufficient: it proves nothing about behaviour it does not exercise. See
[Evidence Over Assertion](../../principles/evidence-over-assertion.md).

## Re-Plan When the Approach Stops Working

Stop and re-plan when consecutive steps produce unexpected results, when an assumption the plan depends on proves false,
or when the approach still works but grows more complicated with each step.

Re-planning names the assumption that failed and states the revised approach before the next change. Pushing on instead
builds each workaround on the previous one, and a chain of workarounds takes longer to unwind than a restart from a
known state. A repair loop inside the plan carries its own bound — see
[Bounded Convergence](../workflow/bounded-convergence.md).
