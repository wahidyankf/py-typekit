---
name: applying-ci-standards
description: >-
  Guides judging hooks, pipelines, and project test targets against the catalog's gate standards: whether a target is
  real, a coverage exclusion is a true boundary, an exemption reason holds, and a check belongs to another owner.
when_to_use: >-
  Use when auditing or repairing gate wiring or project test targets, or when a gate passes and nobody can say what it
  inspected.
compatibility: Requires read access to the hook, pipeline, and project target definitions under review.
---

# Applying CI Standards

The standards own the rules. [Automated Quality Gates][automated-quality-gates] places each check on its surface;
[Test Boundaries and Gates](../../../repo-governance/development/quality/testing/test-boundaries-and-gates.md) fixes the
layers, the named targets, and the fast gate; [Task Runner Target Standards][task-runner-target-standards] governs
target declarations where a task runner is adopted; [Bindings and Exemptions][003-bindings-and-exemptions] limits
exemptions; and [Software Quality Enforcement][software-quality-enforcement] forbids passing a check by weakening it.
[CI Quality Gate][ci-quality-gate] runs the check-fix loop. This skill covers the judgement a reviewer or repairer of
that wiring needs.

## A Target Name Is a Claim

Open what each target resolves to and ask what it would do on a broken change. A target is real when a defect inside its
boundary makes it fail.

- **the command prints, exits zero, or runs nothing for this project**: a placeholder, and a finding however green it is
- **an aggregate repeats another target's command instead of naming it**: two owners for one command, which will drift
- **a static coverage target starts the test runner or depends on a test run**: a runtime check wearing a static name,
  slow and order-bound
- **a fast gate or hook starts an integration or end-to-end suite**: misplaced, and a slow hook is the one that gets
  bypassed
- **a step's exit status is discarded**: not a gate
- **a check reports zero files, cases, or scenarios inspected**: nothing inspected, which is never a pass

## An Omission Needs a Reason; a Stub Never Passes

A missing target with its reason recorded in the project's README is compliant. A present target that tests nothing is
not. When repairing, never add a stub because a checker expects the slot: build the real target, or remove the stub and
record the omission. A dedicated end-to-end project owns no unit layer of its own, and its existence never lowers the
floor of the project it tests.

## Judge an Exclusion by Its Contents

Where the adopter records a coverage floor, accept an exclusion from it only when all three hold:

- it names a specific file or a narrow function, never a path pattern;
- the named code is wholly a boundary, such as a resource, process, generated code, or static data, with no decision in
  it; and
- a named integration or end-to-end target and scenario exercises that code.

Code that mixes a boundary with a decision is split, so the decision stays under the floor. A broad pattern, or boundary
code with no higher-layer proof, is coverage gaming. Lowering a floor is a gate change made as its own change.

## Weigh an Exemption Reason

Ask whether the layer could reach the behaviour with more effort. If it could, the reason is difficulty in disguise,
however it is worded. "Slow to load" and "flaky in the pipeline" describe problems to fix; "no emulator exists for this
sensor" describes a boundary.

Resolve the named alternative proof: the target and scenario must exist and must cover the behaviour. Words such as "for
now", "until", or a pointer to pending work mark unfinished work, which is never a valid reason. A tag that marks a
scenario as in progress, or selects the layers it runs in, is an exemption without a reason, and is judged as one.

## Delegated Checks Stay Delegated

When a hook or hosted pipeline already owns a check and holds current evidence for this revision, audit how the check is
declared and wired; never re-run or imitate it. A local imitation proves only the imitation. Missing or stale evidence
leaves the check pending, never passed.

## Cite the Rule, Not the Tool

A finding cites the rule a configuration breaks, so it survives a change of tool. As an illustration only: an Nx
`test:coverage:behaviour` target whose `dependsOn` lists `test:unit` breaks the static-coverage rule, and the finding
cites that rule.

[automated-quality-gates]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/checks/automated-quality-gates.md
[task-runner-target-standards]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/task-runner-target-standards.md
[003-bindings-and-exemptions]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/behaviour-driven-development/003-bindings-and-exemptions.md
[software-quality-enforcement]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/checks/software-quality-enforcement.md
[ci-quality-gate]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/workflows/quality/ci-quality-gate.md
