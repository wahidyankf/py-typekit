---
description: >-
  Indexes the repository check standards: how every rule is enforced, which gate runs each check, the test and gate
  contract, how strict lint and Markdown checks are, how validators are built, and what a new check needs.
when_to_use: >-
  Use when adding, placing, or tightening an automated check, or deciding whether a validation belongs to a
  deterministic check or a judgement review.
---

# Checks and Gates Standards

Check and gate standards. They answer which automated check runs where, how strict it is, and how it earns its place.

## Directory Map

- [Automated Quality Gates](automated-quality-gates.md) — which checks run at commit, message, push, and pipeline time
- [Deterministic and Judgement Validation](deterministic-and-judgement-validation.md) — one owning layer per category,
  and the handoff between layers
- [Lint Strictness](lint-strictness.md) — failing at warning severity, cleaning a backlog before a gate goes live,
  documented waivers, and reviewed autofixes
- [Markdown Quality](markdown-quality.md) — Markdown formatting and linting, archive exclusion, and rule-set decisions
- [Repository Check Policy](repository-check-policy.md) — what a new check needs, how it runs, and when it goes
- [Repository Validation Methodology](repository-validation-methodology.md) — scoping a match to the region its rule
  governs, anchored and escaped patterns, file-relative paths, recorded edge cases, and documented checks
- [Software Quality Enforcement](software-quality-enforcement.md) — an enforcement class and route for every rule, no
  superficial satisfaction, and nothing inspected is no pass
- [Test and Gate Contract](test-and-gate-contract.md) — rules C1 to C24 that every repository's tests and gates meet,
  each with its module and enforcement disposition
- [Test and Gate Contract Modules](test-and-gate-contract/README.md) — registry, surfaces, scope, test levels, behaviour
  corpus, coverage floor, and conformance record
