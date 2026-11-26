---
description: >-
  Defines the optional plan-document route: which changes qualify as plan-only, which specialists review them at each
  tier, and the plan documents the brief omits from cycle 2.
when_to_use: >-
  Use when a change may contain only plan documents, or when a review loop reaches a later cycle on a change that
  carries plan documents.
---

# Plan Document Route

A plan is reviewed as the artifact it is, not as implementation that has not been written yet. An adopter may record the
two controls below. Without that record, every change takes the standard route and the brief omits nothing.

## Which Changes Qualify

A change is plan-only when every hand-authored file in it is a plan document, an index those documents require, or a
non-executable asset they reference, such as an exported image or an editable diagram source. Executable source or
scripts, build or tool configuration and manifests, tests or fixtures, runnable prototypes, unreferenced assets, and
unrelated files send the change down the standard route, even inside a plan directory. Only wholly generated files and
generated regions stay outside this test; vendored files count.

The test is recomputed from the current change every cycle, and the verdict is recorded with the route, because a
plan-only change stops being one the moment a script joins it.

## Who Reviews It

The tier from [Cost and Noise Controls](004-cost-and-noise-controls.md) still applies. The route changes which
specialists run, never how the tier is chosen.

| Tier         | Runs                                                                                                                                    |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| trivial      | the coordinator alone, in one generalist pass that checks security first, then architecture, correctness, documentation, and governance |
| lite or full | security, architecture, correctness, documentation, and governance, plus the coordinator                                                |

Each reviews the plan as the shipping artifact: architecture the design decisions the plan makes, correctness its domain
intent and acceptance criteria, documentation its substantive quality and completeness, and governance its mechanical
conformance. Findings that merely note implementation not yet written are suppressed, because that implementation is
reviewed on the change that ships it. The plan's own contradictions, omissions, and rule violations stay in scope.

## Later Cycles Omit Plan Documents

From cycle 2 onward, the brief omits every plan document, so the loop stops reviewing the prose it wrote in the previous
cycle. The change description stays, because a human reads it first, and on a plan-only change the plan stays too,
because it is what ships. Cycle 1 still reviews every plan document in full.

This is not generated-file filtering under another name. The omitted documents leave the brief because the loop itself
authored them, not because a tool emitted them.
