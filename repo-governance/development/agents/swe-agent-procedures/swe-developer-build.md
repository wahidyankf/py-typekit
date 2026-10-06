---
description: >-
  Holds the Build mode procedure of the swe-developer agent, moved verbatim from its definition so the definition fits
  its word budget.
when_to_use: >-
  Use when swe-developer runs Build mode and its definition points here.
---

# SWE Developer Build

Moved verbatim from [swe-developer](../../../../.agents/agents/swe-developer.md), which links each section here, per
[Document Word Budget](../../../conventions/structure/document-word-budget.md).

## Build

1. **State the criteria** a check can confirm or refute, per [Implementation Stages][implementation-stages]. A
   requirement too ambiguous for that goes back to the caller as a question.
2. **Research before adding.** Read the code and tests around the change, and extend an existing function, module,
   component, or dependency rather than writing a near-duplicate, per [Code as Liability][code-as-liability]. A new
   dependency passes [Dependency Selection](../../quality/code/dependency-selection.md).
3. **Place the code** by what each piece decides or does, as
   [Developing Applications](../../../../.agents/skills/developing-applications/SKILL.md) teaches.
4. **Build each increment test-first** through [Red, Green, Refactor](../../../workflows/quality/red-green-refactor.md),
   with its runs recorded where the caller names. Where the project keeps a scenario corpus, the scenario is added or
   updated before its red, per [Behaviour-Driven Development][behaviour-driven-development].
5. **Make it right, then fast only on a measurement,** in the order Implementation Stages sets, editing surgically.
6. **Check before handing over.** Run the type check, lint, format checks, and fast gate the project records, over the
   changed projects, plus the end-to-end journeys the change affects. Name every check [Behaviour Change
   Verification][006-behaviour-change-verification] still requires, and every document the change leaves stale, per
   [Docs Propagation](../../../workflows/quality/docs-propagation.md).

An interface component also starts from its approved design for every declared viewport class, per [Plan UI
Design][plan-ui-design], composes the design-system primitive the design names, and styles from the token layer only,
per [Design Tokens][design-tokens]. A missing design, an unnamed primitive, or a colour with no token role is a question
for the design's owner, never a local choice.

[implementation-stages]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/workflow/implementation-stages.md
[code-as-liability]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/code/code-as-liability.md
[behaviour-driven-development]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/behaviour-driven-development.md
[006-behaviour-change-verification]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/manual-verification/006-behaviour-change-verification.md
[plan-ui-design]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/conventions/structure/plan-ui-design.md
[design-tokens]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/user-interfaces/design-tokens.md
