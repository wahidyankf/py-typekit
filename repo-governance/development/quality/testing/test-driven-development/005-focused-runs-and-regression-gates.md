---
description: >-
  Defines focused local test selections and execution evidence while preserving complete regression and coverage
  gates at phase and pull-request boundaries.
when_to_use: >-
  Use when selecting a local red, green, or refactor run, writing its evidence, or scheduling complete regression
  gates for a phase or pull request.
---

# Focused Runs and Regression Gates

For each local RED and GREEN item, run the named case or smallest relevant test selection that demonstrates the
behaviour; do not rerun the whole suite for every item. Run the named affected behaviours and shared boundaries after
each REFACTOR step, expanding the selection when the change affects more code.

Record the exact command, test path, selected case identities, positive executed case count, exit status, and observed
result for each step. An unmatched filter, zero executed cases, or cached output that executes nothing is not proof.

Use the raw runner's selection when an aggregate enforces coverage over code deliberately omitted from a focused run. Do
not lower coverage floors or change their exclusions or full-coverage targets. Keep required build, code generation,
resource admission, fixture isolation, and cleanup around every selected run.

At each phase end, and before pull-request ready-for-review or session end as a safety net, run the whole automated
suite except the full E2E suite, plus only the affected E2E flow. One recorded complete run may satisfy both boundaries
when the tested code, tests, configuration, and affected scope are unchanged; otherwise rerun. Focused runs replace no
hook, CI, or delivery gate. A full E2E run is never a completion condition for a plan phase or plan execution; full E2E
stays a separately batched set on its scheduled workflow.

Followed evidence names relevant executed cases with positive counts and the complete boundary runs. A per-item whole
suite, a selection omitting an affected shared boundary, nonexecuting evidence, a required full E2E as a gate, or a
missing required complete gate violates this rule. Existing TDD scope exceptions remain unchanged.

**Enforcement: unenforced by decision.** Selecting the meaningful affected scope and proving its recorded evidence
require judgement; static text checks do not establish semantic test execution.

The repository remains unit-only with its 100% branch coverage floor and existing exclusions, as recorded in the
[Repository Adapter](../../stacks/repository-adapter.md). Integration and E2E gates apply only where adopted. This
library member has no E2E suite and therefore no full-E2E schedule (no-schedule statement); if E2E is adopted later, its
full suite runs on its scheduled CI workflow by default with local runs selective to the touched flow.
