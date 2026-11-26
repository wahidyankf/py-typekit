---
description: >-
  Orders every change as make it work, then make it right, then make it fast only when measurement proves the need, and
  adds surgical editing and verifiable success criteria to each change.
when_to_use: >-
  Use when planning, implementing, refactoring, or optimizing a change, or when reviewing whether a change skipped a
  stage, optimized without a measurement, or drifted beyond its request.
---

# Implementation Stages

A change moves through three stages in order: make it work, make it right, then make it fast only when a measurement
shows the need. Each stage is complete before the next begins, and no two are combined.

This standard implements [Simplicity Over Complexity](../../principles/simplicity-over-complexity.md),
[Evidence Over Assertion](../../principles/evidence-over-assertion.md), and
[Minimal Sufficiency](../../principles/minimal-sufficiency.md).

## The Stages

| Stage | Aim                                                                                                      | Complete when                                                              | Not during this stage                                                                    |
| ----- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| work  | the most direct solution that meets the requirement                                                      | the behaviour works and its tests pass                                     | abstractions, performance tuning, or restructuring while implementing                    |
| right | readable, maintainable code: clear names, small single-purpose units, error handling, and thorough tests | the code is clean and every test still passes                              | performance tuning, features the requirement does not ask for, or any behaviour change   |
| fast  | a performance need that a measurement demonstrated                                                       | the measured need is met, the tests still pass, and the reason is recorded | tuning without profiling data, tuning beyond the bottleneck, or needless loss of clarity |

Duplication is tolerated while making it work. Removing it belongs to making it right, and an abstraction is extracted
only once it has earned its place, as Simplicity Over Complexity describes.

## Making It Fast

1. Profile to find where the time actually goes.
2. Record a baseline.
3. Change only the bottleneck, and leave the rest of the code clean.
4. Measure again and confirm the change helped.
5. Keep every test passing.
6. Record beside the optimized code why it was needed: the measurement, the bottleneck, and the result.

Tuning on a guess tends to land where little time is spent, costs clarity, and leaves the real bottleneck in place.

## Exceptions

| Situation                                                 | How the order changes                                                          |
| --------------------------------------------------------- | ------------------------------------------------------------------------------ |
| a security fix                                            | correctness leads: the fix is made right before it counts as working           |
| a production hotfix                                       | a working fix ships first and is made right afterwards                         |
| performance is itself a requirement, as in real-time work | performance constrains even the first stage, and the stages still run in order |
| restructuring code that already works                     | begin at the second stage                                                      |

## Surgical Changes

[Minimal Sufficiency](../../principles/minimal-sufficiency.md) owns the scope of a change, including reporting adjacent
improvements rather than folding them in. Within that scope, an edit to existing code also:

- traces every changed line to the request;
- matches the surrounding style and naming, even where a different style would be preferred;
- removes the imports, variables, and functions that this change left unused, and nothing else;
- mentions unrelated dead code instead of deleting it;
- resolves a pre-existing error the change exposes per
  [Preexisting Error Resolution](../quality/evidence/preexisting-error-resolution.md).

## Verifiable Success Criteria

- Before starting, restate the task as criteria a check can confirm or refute. "Tests for empty, missing, and malformed
  input fail, then pass" can be verified; "add validation" cannot.
- In a multi-step plan, pair every step with the check that shows it is done, and begin the next step only after that
  check passes.
- Where a test can express a criterion, write it first and see it fail for the expected reason before implementing. A
  bug fix starts with a test that reproduces the bug.
- A failed check sends the work back to be fixed and checked again. That cycle is a repeated operation, so it carries a
  bound and ends in a recorded result, as [Bounded Convergence](bounded-convergence.md) requires.
