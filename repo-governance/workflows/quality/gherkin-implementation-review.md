---
name: gherkin-implementation-review
description: >-
  Compares written Gherkin acceptance scenarios against what the implementation and its tests actually do.
when_to_use: >-
  Use when a change adds or modifies Gherkin acceptance criteria, before the work is declared complete.
---

# Gherkin Implementation Review

## Entry

A change has added or modified Gherkin scenarios, and an implementation claims to satisfy them.

A material change to a binding, an exemption, or the compliance check also enters.

- `scope` (`enum`: `changed`, `full`; optional, default `changed`): the scenarios the change reaches, or the whole
  corpus.

## Sequence

1. **Freeze the scenario list.** Every scenario added or changed by this work, enumerated before review starts. Under
   `full` it is the whole corpus; `changed` adds scenarios a changed binding, exemption, or check reaches.
2. **For each scenario, locate the implementation** — the code path that makes it true — and the test that would fail if
   that path broke. Both, separately.
3. **Assign exactly one status:**

   | Status        | Means                                                                         |
   | ------------- | ----------------------------------------------------------------------------- |
   | implemented   | the behaviour exists and a test fails without it                              |
   | untested      | the behaviour exists but nothing fails when it breaks                         |
   | unimplemented | the scenario describes behaviour that does not exist                          |
   | drifted       | the implementation does something the scenario no longer accurately describes |
   | exempt        | exemption holds; alternative proof read, recorded as test path                |

4. **Resolve `drifted` by deciding which is wrong.** Either the scenario was superseded and must be rewritten, or the
   implementation diverged and must be corrected. Editing the scenario to match whatever the code happens to do is not a
   resolution; it converts a specification into a description.
5. **Record every status** with the implementation path and the test path.

## Exit

Every frozen scenario carries a status, and no scenario remains `untested`, `unimplemented`, or `drifted` without an
explicit decision recorded against it.

The review record (`file`, per [Temporary Files](../../conventions/structure/temporary-files.md)) holds the row count,
every row, the exemption inventory, and each command with its result.

## One Row per Scenario and Layer

The frozen list expands every outline example into its own scenario, and each scenario is reviewed once per layer that
[Layers and Adapters](../../development/quality/testing/behaviour-driven-development/002-layers-and-adapters.md) makes
applicable. The row count is expanded scenarios times applicable layers, exempt rows included. A missing row fails the
review.

A non-exempt row follows its scenario end to end:

- **Given** sets up the precondition with a boundary-valid fixture or injected double, on synthetic data kept apart per
  [Test Data Isolation](../../development/quality/testing/test-data-isolation.md).
- **When** calls real production code or the boundary the scenario names.
- **Then** asserts on evidence that call produced, observed from outside.

Besides the defects in
[Bindings and Exemptions](../../development/quality/testing/behaviour-driven-development/003-bindings-and-exemptions.md),
a row is `untested` when an expected-outcome table supplies success, a literal success follows a helper's own action,
the assertion misses the stated behaviour, or any step can reach production data.

Each exemption is checked per layer against that module's limits, its alternative proof read. An exempt layer keeps no
silent success branch, so accidental execution fails. Scenario counts, pattern searches, and green runs never replace
reading each row. Run the affected scenarios in every layer as
[Compliance and Reporting](../../development/quality/testing/behaviour-driven-development/004-compliance-and-reporting.md)
places them; a failing run blocks completion like a failing row. A row that cannot pass stays failed until its seam or
binding is fixed; an exemption never repairs it.

## Assertion Theater Is a Failure, Not a Pass

A test that executes the scenario's steps and asserts nothing that could distinguish success from failure is `untested`,
not `implemented`. So is one whose only assertion is that the code ran without throwing.

The check is mechanical: break the behaviour; a test that still passes established nothing. Such a test is worse than
none: it occupies a real test's place, counts in coverage, and is trusted by everyone who does not read it.

## Why This Is a Distinct Review

A passing suite proves only that its tests pass, not that they match the agreed scenarios, and it cannot notice a
scenario nobody implemented, which has no test to fail. Only walking the scenarios closes that gap. One canonical review
does this; several overlapping versions give a scenario several places to be missed.
