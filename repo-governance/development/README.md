---
description: >-
  Indexes the development layer, which holds engineering standards and practices that apply while work is being done,
  and maps each stage of delivering a change to the artifacts that govern it.
when_to_use: >-
  Use when locating an engineering standard, when deciding whether new guidance is a standard rather than a procedure,
  or when finding which artifact governs a stage of delivering a change.
---

# Development

Engineering standards. A convention decides how the repository is arranged; a standard here decides how work inside it
is done well.

| Area        | Holds                                                                                                       |
| ----------- | ----------------------------------------------------------------------------------------------------------- |
| `agents/`   | standards for the coding-agent capabilities a repository publishes                                          |
| `quality/`  | what proves a change works, what a proof has to look like, and how code is designed, tested, and contracted |
| `workflow/` | the shape of work itself, rather than its subject, from setup through commit and integration                |

## Lifecycle Map

Where each stage of delivering a change is governed. The map adds no rule; each linked artifact owns its own.

| Stage          | Governed by                                                                                                                                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| idea and plan  | [Plans](../conventions/structure/plans.md), [Ideas Grooming](../workflows/plan/plan-ideas-grooming.md), [Planning](../workflows/plan/plan-planning.md), [Plan Quality Gate](../workflows/quality/plan-quality-gate.md)                                                                         |
| specification  | [Specification Tree](../conventions/structure/specification-tree.md), [Behaviour-Driven Development](quality/testing/behaviour-driven-development.md), [Specification Maintenance](quality/evidence/specification-maintenance.md)                                                              |
| design         | [Architecture Specifications](quality/architecture/architecture-specifications.md), [Hexagonal Architecture](quality/architecture/hexagonal-architecture.md), [Public Contract](quality/architecture/public-contract.md)                                                                       |
| setup          | [Checkout Bootstrap](workflow/checkout-bootstrap.md), [Native-First Toolchain](workflow/native-first-toolchain.md), [Resource-Aware Development](workflow/resource-aware-development.md)                                                                                                       |
| implementation | [Execution](../workflows/plan/plan-execution.md), [Implementation Stages](workflow/implementation-stages.md), [Test-Driven Development](quality/testing/test-driven-development.md), [Code Clarity](quality/code/code-clarity.md), [Stack Standards](quality/stacks/README.md)                 |
| verification   | [Test Boundaries and Gates](quality/testing/test-boundaries-and-gates.md), [Automated Quality Gates](quality/checks/automated-quality-gates.md), [Manual Verification](quality/manual-verification.md), [Gherkin Implementation Review](../workflows/quality/gherkin-implementation-review.md) |
| review         | [Review Disciplines](agents/review-disciplines.md), [Integration Diff Review](workflow/integration-diff-review.md)                                                                                                                                                                             |
| integration    | [Integration Path](workflow/integration-path.md), [Commit Messages](workflow/commit-messages.md), [Pull Request Merge](workflow/pull-request-merge.md), [CI Post-Push Verification](workflow/ci-post-push-verification.md)                                                                     |
| deployment     | [Deployment Build Parity](workflow/deployment-build-parity.md), [Deployment Promotion](workflow/deployment-promotion.md), [Live-Service Continuity](quality/delivery/live-service-continuity.md)                                                                                               |
| upkeep         | [Automation Loop Observability](quality/delivery/automation-loop-observability.md), [Dependency Bump Policy](workflow/dependency-bump-policy.md), [Dev Artifact Clean-Up](../workflows/maintenance/dev-artifact-clean-up.md)                                                                   |
| learning       | [Post-Mortems](../conventions/writing/post-mortems.md), [Knowledge Capture and Archival](../conventions/structure/plans/008-knowledge-capture-and-archival.md)                                                                                                                                 |

## Directory Map

- [Agents](agents/README.md)
- [Quality](quality/README.md)
- [Workflow](workflow/README.md)
