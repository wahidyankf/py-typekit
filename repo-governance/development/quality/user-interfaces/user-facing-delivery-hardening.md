---
description: >-
  Hardens user-facing delivery so design-parity and behaviour defects cannot pass green gates, through plan authoring
  rules, a deployment-configuration sweep, an archival sign-off, and a near-end retest of the running system.
when_to_use: >-
  Use when authoring, executing, or archiving a plan that changes an interface users see or an API operation that
  callers use, or when retesting other reachable behaviour a plan changes near its end.
---

# User-Facing Delivery Hardening

A change that users see or call can pass every unit, end-to-end, lint, and pipeline check, reach zero review findings,
be archived, and still reach its users off-design and carrying a calculation defect. Each check proved what it was
written to prove. None compared the running result with the approved design, and none tried the inputs nobody had
written a test for. This standard closes that gap across a plan's life, from authoring through archival.

It implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Root Cause Orientation](../../../principles/root-cause-orientation.md), and
[Deliberate Problem-Solving](../../../principles/deliberate-problem-solving.md). The root cause it targets is not weak
tests. It is declaring work done before anyone has observed the running result against its design.

## Modules

1. [Authoring a User-Facing Plan](user-facing-delivery-hardening/001-authoring-a-user-facing-plan.md)
2. [Closing a User-Facing Plan](user-facing-delivery-hardening/002-closing-a-user-facing-plan.md)

## Scope

| Applies to                                                                                                    | Does not apply to                                    |
| ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| a plan that changes a rendered interface, rendered output, or public command-line text                        | an internal refactor with no observable output       |
| a plan that adds or changes an API operation, since its callers are its users                                 | a change to documentation or governance alone        |
| executing, verifying, and archiving such a plan, including its done and archival criteria                     | an incidental API behaviour outside a feature change |
| a plan changing other reachable behaviour, such as a library, hook, or pipeline, for the near-end retest only |                                                      |

## What Other Artifacts Already Own

These rules add to existing artifacts and repeat none of them:

| Rule                                                                   | Owner                                                                                                                      |
| ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| green automation does not close a user-facing change                   | [Verification Layers](../manual-verification/002-verification-layers.md)                                                   |
| a real-browser check and a direct API request after a behaviour change | [Behaviour Change Verification](../manual-verification/006-behaviour-change-verification.md)                               |
| where a plan's captures live and how a checklist item cites them       | [Evidence Files](../../../conventions/structure/plans/016-evidence-files.md)                                               |
| ticking each checklist item as it resolves                             | [Plan Execution](../../../workflows/plan/plan-execution.md)                                                                |
| what happens when an archived plan turns out to be defective           | [Phase Boundaries and Delivery Choices](../../../conventions/structure/plans/011-phase-boundaries-and-delivery-choices.md) |
| components refer to colours by token role                              | [Design Tokens](design-tokens.md)                                                                                          |

## Enforcement

An adopter enforces these rules in its own plan review and execution checks: plan review flags a user-facing plan that
lacks the visual-parity step, the archival sign-off, or the near-end retest, and the execution check confirms each ran
and every defect item is ticked before archival. Plan review also flags any other in-scope plan that lacks the near-end
retest.
