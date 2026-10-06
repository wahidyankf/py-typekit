---
description: >-
  Defines the canonical plan system: lifecycle folders, required documents, delivery, validation, evidence, knowledge
  capture, and archival.
when_to_use: >-
  Use when creating, executing, validating, or archiving a formal plan, or when adopting the plan system into a
  repository.
---

# Plans Convention

A formal plan is a durable, checkable record of intended work. It exists so that someone who was not present when the
work was designed — including a cold executor picking it up months later — can carry it out, verify it, and know when it
is finished.

This entrypoint is deliberately short. The modules below hold the complete rule; each is independently readable and each
is what an adopter's plan validator checks against; the catalog ships none.

## Modules

1. [Lifecycle and Folders](plans/001-lifecycle-and-folders.md)
2. [Required Documents](plans/002-required-documents.md)
3. [Technical Shape and Ordered Companions](plans/003-technical-shape-and-companions.md)
4. [Delivery Contract](plans/004-delivery-contract.md)
5. [Workflows and Skills](plans/005-workflows-and-skills.md)
6. [Structural Validation](plans/006-structural-validation.md)
7. [Evidence and Quality](plans/007-evidence-and-quality.md)
8. [Knowledge Capture and Archival](plans/008-knowledge-capture-and-archival.md)
9. [Portability](plans/009-portability.md)
10. [Authorization and Execution Record](plans/010-authorization-and-execution-record.md)
11. [Phase Boundaries and Delivery Choices](plans/011-phase-boundaries-and-delivery-choices.md)
12. [Decision Records](plans/012-decision-records.md)
13. [File Impact](plans/013-file-impact.md)
14. [Dependency Graph and Recovery](plans/014-dependency-graph-and-recovery.md)
15. [Evidence Files](plans/015-evidence-files.md)
16. [Learning Triage](plans/016-learning-triage.md)
17. [Learning Routing](plans/017-learning-routing.md)
18. [Bug-Fix Plan](plans/018-bug-fix-plan.md)

## Conditional Conventions

Some plans carry more than every plan does. Each of these applies only when its trigger holds, and each adds to this
convention without restating it.

- **[Plan Specification Changes][plan-specification-changes]**: changes observable behaviour, an interface,
  architecture, or an executable specification
- **[Plan Migrations][plan-migrations]**: moves, copies, normalizes, replaces, or retires data, configuration, or
  structure
- **[Plan UI Design][plan-ui-design]**: creates or materially changes a user interface
- **[Plan Content Corpora][plan-content-corpora]**: authors or restructures a content corpus inside its own folder

## What This Convention Does Not Decide

It does not decide what a repository should plan, how large a plan should be, or which delivery mode — pull request,
direct [landing](plans/009-portability.md#what-landed-means), local-only landing — a repository uses. Those are the
adopting repository's to choose, and the plan system is designed to survive any of them.

[plan-specification-changes]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/plan-specification-changes.md
[plan-migrations]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/plan-migrations.md
[plan-ui-design]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/plan-ui-design.md
[plan-content-corpora]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/plan-content-corpora.md
