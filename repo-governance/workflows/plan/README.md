---
name: plan
description: >-
  Indexes the plan-lifecycle workflows, from grooming an idea through reviewing finished execution before archival, and
  the companion workflows for scheduling, handover, and parity planning.
when_to_use: >-
  Use when starting any stage of the plan lifecycle, or when checking that a repository can run the lifecycle end to
  end.
---

# Plan Workflows

Five of the six lifecycle workflows live here, with three companion workflows listed after them. The sixth, the quality
gate, lives in [`quality/`](../quality/README.md) beside every other gate. The seventh capability of the plan lifecycle
— cleanup — is a general maintenance concern and lives in [`maintenance/`](../maintenance/README.md), because work that
is not a plan also leaves artifacts behind.

| Workflow                                        | Ends when                                                    |
| ----------------------------------------------- | ------------------------------------------------------------ |
| [Ideas Grooming](plan-ideas-grooming.md)        | every idea brief is promoted, kept with a reason, or retired |
| [Backlog Grooming](plan-backlog-grooming.md)    | every backlog plan is current, ordered, or removed           |
| [Planning](plan-planning.md)                    | a complete six-document plan has its quality-gate verdict    |
| [Execution](plan-execution.md)                  | every substantive checklist item is terminal                 |
| [Quality Gate](../quality/plan-quality-gate.md) | an advisory verdict is recorded against a frozen draft       |
| [Execution Check](plan-execution-check.md)      | a terminal execution verdict permits or blocks archival      |

Together with [Gherkin Implementation Review](../quality/gherkin-implementation-review.md) and
[Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md), these cover the whole lifecycle. A repository missing
one of them has a stage nobody owns.

## Companion Workflows

These serve the lifecycle without being a stage of it.

| Workflow                                                    | Ends when                                                                   |
| ----------------------------------------------------------- | --------------------------------------------------------------------------- |
| [Multi-Plans Execution](multi-plans-execution.md)           | every scheduled plan has a recorded status and cross-plan themes are routed |
| [Plan Handover and Takeover](plan-handover-and-takeover.md) | a resumable record exists, or resumed work is classified and handed on      |
| [Parity Planning](plan-parity-planning.md)                  | each repository in a parity set holds a gated plan, every deviation decided |

## Directory Map

- [Ideas Grooming](plan-ideas-grooming.md)
- [Backlog Grooming](plan-backlog-grooming.md)
- [Planning](plan-planning.md)
- [Execution](plan-execution.md)
- [Execution Check](plan-execution-check.md)
- [Multi-Plans Execution](multi-plans-execution.md)
- [Plan Handover and Takeover](plan-handover-and-takeover.md)
- [Parity Planning](plan-parity-planning.md)
