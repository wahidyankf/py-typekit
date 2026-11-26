---
description: >-
  Defines the bug-fix plan: one document carrying a defect's report, duplicate check, root cause, referenced solution,
  delivery, and learnings, what makes each section useful, and which plan rules it is exempt from.
when_to_use: >-
  Use when fixing a defect through a plan in the repository that owns the defective code, or when reviewing, executing,
  or archiving such a plan.
---

# Bug-Fix Plan

A bug-fix plan is the compressed formal plan for one defect. The defect already answers why the work is worth doing and
what the result must do — the behaviour should not happen — so separate business and product documents would restate the
report; a cold executor still needs the evidence, the cause, and the change.

It is reserved for a defect that blocks the work in hand with no workaround. Any other defect is filed as an
[idea brief](015-idea-brief-template.md) and waits for grooming, per
[Upstream Tool Defects](../../../development/workflow/upstream-tool-defects.md) where that standard is adopted.

## Shape

One document, `plans/in-progress/fix-<slug>/README.md`, with these sections in this order:

| Section         | Contains                                                                                                  |
| --------------- | --------------------------------------------------------------------------------------------------------- |
| Bug Report      | every field [Bug Reports](../../writing/bug-reports.md) requires, the version and commit included         |
| Duplicate Check | each search of open issues, pull requests, plans, and idea briefs, with its query and result              |
| Root Cause      | the mechanism that produces the symptom, with evidence a reviewer can check                               |
| Solution        | the change, why it removes the cause, and every reference consulted, cited by URL                         |
| Delivery        | `## Execution Record`, then labelled checklist items: failing regression test, fix, verification, release |
| Learnings       | what executing it taught, routed before archival                                                          |

The slug starts with `fix-` and names the symptom, not the suspected cause: `fix-gate-skips-renamed-files`.

## What Makes Each Section Useful

**Root Cause** separates symptom from mechanism, naming where the behaviour comes from — a file and line, a commit, a
condition — and shows why: a minimal reproduction, a trace, or the failing assertion. "The parser is buggy" is a symptom
restated; "an empty path reaches the matcher at this line and matches nothing" is a cause. A cause that is still a
hypothesis says so and states the test that would confirm it.

**Solution** says why the change removes the cause rather than the symptom, and which conditions it covers beyond the
reported one. Research before choosing: the tool's own documentation, the specification or upstream behaviour it
implements, and prior reports of the same failure, searching the web as well as the repository. Cite each with its URL,
primary sources first. An approach copied from a source names it.

**Delivery** starts with a regression test that fails for the reported reason, so the fix is proven rather than
asserted. Each item carries its executor label, per the [Delivery Contract](004-delivery-contract.md).

## What It Is Exempt From

- **[Required Documents](002-required-documents.md):** it is the one plan with one document; its sections take the six
  documents' roles.
- **[Lifecycle and Folders](001-lifecycle-and-folders.md):** it starts in `in-progress/`, with no idea or backlog stage,
  and moves to `done/` like any plan.
- **The decision gates in [Workflows and Skills](005-workflows-and-skills.md):** a defect has one correct behaviour,
  leaving nothing to interview about.
- **[Authorization](010-authorization-and-execution-record.md):** it needs no separate request when written under an
  adopter's recorded [Upstream Tool Defects](../../../development/workflow/upstream-tool-defects.md) standard, or when
  the owner asks. That standing request also directs its plan quality gate, its execution, and its release: once the
  plan lands, run the gate on it, execute once its verdict is recorded and every open blocking row has an owner, and
  release the fix once its tests pass, without a further prompt.

Every other plan rule holds: slug rules, one root, executor labels, no time estimates, the execution record, knowledge
capture, and archival.

## When It Stops Being One

A fix that needs a design decision, changes an interface its consumers rely on, or needs more than one delivery unit is
not a bug-fix plan. Expand it to the six documents in place, keeping the slug, and run the decision gates before
continuing.

## Landing the Plan First

The plan lands on the owning repository's trunk alone, through its route, before any fix lands. A parallel finder's
duplicate check then sees it, and the fix follows in its own change.
