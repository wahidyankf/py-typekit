---
description: >-
  Indexes the workflow standards that govern how work is bounded, ordered, committed, integrated, deployed, and brought
  to a terminal state, and how a working environment and its toolchain are prepared.
when_to_use: >-
  Use when designing a repeated operation, when committing, integrating, or deploying a change, when preparing an
  environment or toolchain, or when a process has no obvious stopping point.
---

# Workflow Standards

Standards about the shape of work rather than its subject. Version-control, integration, environment, and toolchain
standards sit alongside them.

## Directory Map

- [Bare Repository Landing](bare-repository-landing.md) — landing through the task's linked worktree, topology checks,
  and the fast-forward reconcile of local main
- [Bounded Convergence](bounded-convergence.md) — how a repeated operation is bounded and how it ends, with quality
  gates deferred to their own contract
- [Bounded Convergence Modules](bounded-convergence/README.md) — the modules on loop register and ceiling scorecard
- [Checkout Bootstrap](checkout-bootstrap.md) — the declared per-checkout bootstrap before any commit, push, or
  task-runner command, and when it reruns
- [CI Post-Push Verification](ci-post-push-verification.md) — following every covering pipeline workflow to green after
  a push, and the gate for a repository with no remote
- [Commit Authorization](commit-authorization.md) — when staging, committing, and pushing are permitted, distinguishing
  single-action grants from ongoing scoped task delivery
- [Commit Messages](commit-messages.md) — the Conventional Commits format and type list, and why types never decide
  commit boundaries
- [Dependency Bump Policy](dependency-bump-policy.md) — exact pins, the long-term-support, soak, and waiver paths,
  vulnerability clearance, and the written cutoff
- [Deployment Build Parity](deployment-build-parity.md) — a hosting build that runs every declared build prerequisite,
  traced output includes, and prerequisite and build command changing together
- [Deployment Promotion](deployment-promotion.md) — per-project pointer branches, who may move them, build gating,
  confirming the build, and domain cutover
- [File-Touch Discipline](file-touch-discipline.md) — the touched-path ledger, carrying it through context loss,
  reconciling before staging, and foreign paths
- [Git Author Identity](git-author-identity.md) — identity from user-level configuration only, no local overrides, and
  no agent-set identity
- [Hook Verification](hook-verification.md) — hook bypass as a separate per-operation permission, fixing a failing hook
  at its cause, and bypass disclosure
- [Implementation Stages](implementation-stages.md) — work, then right, then fast only on measured need, with surgical
  edits and verifiable success criteria
- [Integration Diff Review](integration-diff-review.md) — reading and reconciling every incoming commit's diff before
  the next action
- [Integration Hygiene](integration-hygiene.md) — checks before committing, rebase-or-merge catch-up, and fixing or
  reverting a red trunk
- [Integration Path](integration-path.md) — the branch or direct route to the trunk, branch lifespan, one worktree per
  task, reconcile, and cleanup
- [Native-First Toolchain](native-first-toolchain.md) — pinned native toolchain managers, the idempotent health command,
  what repair may change, and when to revisit
- [No Destructive Git Operations](no-destructive-git-operations.md) — bounded authorized task sync, per-instance
  approval, and additive equivalents for operations that destroy work or rewrite history
- [Pull Request Body](pull-request-body.md) — what a body states, the trunk-state claim, and rewriting the body whenever
  the head moves
- [Pull Request Merge](pull-request-merge.md) — the merge preconditions, the recorded landing method, the no-bypass
  rule, draft readiness, and who holds merge authority
- [Quality Gate Contract](quality-gate-contract.md) — the bounded, advisory cycle every quality gate runs: roles,
  inputs, scoring, termination, verdicts, ledger
- [Quality Gate Contract Modules](quality-gate-contract/README.md) — the modules on inputs, sequence, verdicts, and
  ledger
- [Remote Status Polling](remote-status-polling.md) — the spacing of status reads, no streaming watches, trigger
  discipline, and recovery from a rate limit
- [Repository Rename Propagation](repository-rename-propagation.md) — the sweep that retires an old repository name
  everywhere, and verifying each path with a write
- [Resource-Aware Development](resource-aware-development.md) — one outer pinned admission guard per compute-bearing
  command, its outcomes, workload classes, and parallelism
- [Sole-Writer Propagation](sole-writer-propagation.md) — the one writer per gate family, its eight shared rules, and
  the family file shape
- [Task Runner Target Standards](task-runner-target-standards.md) — target prerequisites, caching only deterministic
  targets, inputs and outputs, names, aggregates, no placeholders
- [Thematic Commits](thematic-commits.md) — one complete purpose per commit, the boundary test, and splitting and
  ordering a change set
- [Upstream Tool Defects](upstream-tool-defects.md) — handling pinned upstream tool defects
- [Workspace Container Builds](workspace-container-builds.md) — the root build context, per-application build files,
  hoisted dependencies, and internal-package resolution
- [Resource modules](resource-aware-development/README.md) — external Nx cache awareness, unadmitted tool runs, and
  resource tiers.
