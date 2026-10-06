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

Three of the four plan workflows this repository runs live here. The fourth, the quality gate, lives in
[`quality/`](../quality/README.md) beside every other gate. Cleanup is a general maintenance concern and lives in
[`maintenance/`](../maintenance/README.md), because work that is not a plan also leaves artifacts behind.

| Workflow                                        | Ends when                                                 |
| ----------------------------------------------- | --------------------------------------------------------- |
| [Planning](plan-planning.md)                    | a complete six-document plan has its quality-gate verdict |
| [Execution](plan-execution.md)                  | every substantive checklist item is terminal              |
| [Quality Gate](../quality/plan-quality-gate.md) | an advisory verdict is recorded against a frozen draft    |
| [Execution Check](plan-execution-check.md)      | a terminal execution verdict permits or blocks archival   |

With [Dev Artifact Clean-Up](../maintenance/dev-artifact-clean-up.md), these cover the stages a plan passes through
here; idea and backlog grooming are not adopted, so a plan starts from Planning.

## Directory Map

- [Planning](plan-planning.md)
- [Execution](plan-execution.md)
- [Execution Check](plan-execution-check.md)
