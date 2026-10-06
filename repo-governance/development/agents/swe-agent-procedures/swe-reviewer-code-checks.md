---
description: >-
  Holds the six code checks of the swe-reviewer agent, moved verbatim from its definition so the definition fits its
  word budget.
when_to_use: >-
  Use when swe-reviewer audits code and its definition points here.
---

# SWE Reviewer Code Checks

Moved verbatim from [swe-reviewer](../../../../.agents/agents/swe-reviewer.md), which links each section here, per
[Document Word Budget](../../../conventions/structure/document-word-budget.md).

## Code

1. **Placement and failure handling.** [Hexagonal Architecture][hexagonal-architecture] and [Functional Core, Imperative
   Shell][functional-core-imperative-shell], with error fates, logging, and input validation judged as
   [Developing Applications](../../../../.agents/skills/developing-applications/SKILL.md) teaches, and types per
   [Type and Boundary Safety](../../quality/code/type-and-boundary-safety.md).
2. **Clarity and cost.** [Code Clarity][code-clarity], [Code as Liability][code-as-liability],
   [Dependency Selection](../../quality/code/dependency-selection.md), and [Shell Scripts][shell-scripts] for any script
   in scope.
3. **Stack rules** from the stacks the project lists, read from the repository's local copies as
   [Stack Packs](../../../conventions/structure/stack-packs.md) resolves them. A stack with no recorded standard gets no
   stack rule, and the missing decision is reported.
4. **Test design.** Each test sits at its layer, per the test-boundary standard below; doubles follow
   [Test Doubles](../../quality/testing/test-doubles.md), data follows [Test Data Isolation][test-data-isolation], any
   git fixture follows [Git Fixture Isolation][git-fixture-isolation], and a coverage number measures only what
   [Meaningful Coverage](../../quality/testing/meaningful-coverage.md) allows.
5. **Test-first evidence.** New or changed behaviour has a test, and the records
   [Cycle and Evidence](../../quality/testing/test-driven-development/001-cycle-and-evidence.md) requires exist wherever
   the work kept them. Behaviour shipped with no test is a finding.
6. **Regression tests.** Each bug fix carries the test
   [Regression Tests](../../quality/testing/test-driven-development/003-regression-tests.md) requires.

[hexagonal-architecture]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/architecture/hexagonal-architecture.md
[functional-core-imperative-shell]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/architecture/functional-core-imperative-shell.md
[code-clarity]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/code/code-clarity.md
[code-as-liability]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/code/code-as-liability.md
[shell-scripts]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/code/shell-scripts.md
[test-data-isolation]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/test-data-isolation.md
[git-fixture-isolation]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/git-fixture-isolation.md
