---
description: >-
  Indexes this repository's canonical agent definitions, each declaring what it needs and what it must not do before any
  harness adapter translates that declaration.
when_to_use: >-
  Use when locating a canonical agent definition or deciding what a new one must declare.
---

# Canonical Agents

Agent definitions in their canonical, harness-neutral form. One Markdown file per agent.

Each declares what it needs and must not do in this repository's vocabulary; a harness adapter translates that. A human
edits the canonical file, and an adapter is generated from it, never edited in place.

## Directory Map

- [docs-checker](docs-checker.md) — auditing documentation claims against their sources
- [docs-fixer](docs-fixer.md) — applying re-validated documentation findings
- [plan-checker](plan-checker.md) — auditing a plan draft against the plan specification
- [plan-execution-checker](plan-execution-checker.md) — auditing finished plan execution before archival
- [plan-fixer](plan-fixer.md) — repairing the rows of a frozen plan ledger through Plan Propagation
- [plan-maker](plan-maker.md) — authoring a formal plan through both decision gates
- [pr-review-checker](pr-review-checker.md) — coordinating one review pass and publishing its single consolidated review
- [pr-review-docs-checker](pr-review-docs-checker.md) — reviewing a change's documentation for completeness and drift
- [pr-review-fixer](pr-review-fixer.md) — answering every finding a published review raised on the change
- [pr-review-governance-checker](pr-review-governance-checker.md) — checking a change against the rules its repository
  documents
- [pr-review-instruction-checker](pr-review-instruction-checker.md) — finding toolchain changes the instruction files no
  longer describe
- [pr-review-integrity-checker](pr-review-integrity-checker.md) — finding weakened tests, gamed coverage, and missing
  regression tests
- [pr-review-logic-checker](pr-review-logic-checker.md) — judging a change's behaviour against domain intent and
  acceptance criteria
- [pr-review-performance-checker](pr-review-performance-checker.md) — finding a change's regressions and cost growth
- [pr-review-scout](pr-review-scout.md) — classifying a review pass and assembling its shared brief
- [pr-review-security-checker](pr-review-security-checker.md) — finding secrets, injection, and unsafe operations in a
  change
- [pr-review-types-checker](pr-review-types-checker.md) — finding type escape hatches a change adds or widens
- [rules-checker](rules-checker.md) — auditing a repository's rules for contradictions and drift
- [rules-fixer](rules-fixer.md) — applying re-validated rule repairs through Rules Propagation
- [swe-architect](swe-architect.md) — designing boundaries before a build, reviewing it after, and the architecture
  review lens
- [swe-debugger](swe-debugger.md) — repairing failing type checks, lint, and tests at the cause
- [swe-developer](swe-developer.md) — building behaviour test-first and applying re-validated findings
- [swe-releaser](swe-releaser.md) — cutting releases, deploying artifacts, and repinning tools through documented
  workflows
- [swe-reviewer](swe-reviewer.md) — auditing code, component source, and scenario bindings against adopted standards
