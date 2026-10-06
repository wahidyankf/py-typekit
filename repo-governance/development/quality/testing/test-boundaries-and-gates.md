---
description: >-
  States what each test boundary excludes, keeps the layers in separate suites, builds gates from named targets, and
  fixes what the fast gate holds, how gating coverage is measured, and which choices an adopter records.
when_to_use: >-
  Use when classifying a test, defining a project's test targets, composing the fast gate, or deciding where coverage is
  measured and where a slow suite runs.
---

# Test Boundaries and Gates

A test result means something only when the test sits where it claims to. A unit test reading a real file is slow,
order-sensitive, and running in a gate that promised neither.

This standard implements [Reproducibility](../../../principles/reproducibility.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). The three layers, classification by the
strongest boundary a test touches, the loopback choice, and whether a coverage floor exists are owned by [Layers and
Adapters][002-layers-and-adapters].

## What Each Boundary Excludes

- **unit**: touches a real filesystem, database, environment, clock, random source, child process, or network; each is
  injected
- **integration**: reaches an external network, drives a browser, or observes the served origin; it uses only local
  resources it owns
- **end-to-end**: calls an external service nobody controls without explicit authorization

The unit exclusion covers setup and assertions as well as the subject. End-to-end means observing the public boundary,
not permission to use more resources.

## Keep the Suites Apart

Unit, integration, and end-to-end tests live in separate trees or targets, so a gate selects one layer without filtering
by name. Support that never executes on its own, such as contracts, bindings, and fixtures, may be shared.

## Gates Compose Named Targets

Each layer and each static check is its own named target. Aggregate gates compose those names instead of repeating their
commands, because a copied command drifts from the original.

- **lint**: formatting, style, suspicious-code, and dependency findings, per
  [Lint Strictness](../checks/lint-strictness.md)
- **type check**: compiler and static-type findings, leaving no build output behind
- **unit, integration, end-to-end**: one layer's suite each; the unit run also measures coverage
- **static behaviour coverage**: scenario and binding resolution, executing nothing, where scenarios exist

## The Fast Gate

The fast gate runs type check, lint, unit with coverage, and static behaviour coverage, in that order, so the cheapest
failure to read comes first. It runs before a push over what the change affects, and after the last cycle of
[Test-Driven Development](test-driven-development.md). A dedicated end-to-end project's fast gate holds only its type
check, lint, and static behaviour coverage.

It never runs an integration or end-to-end suite. Those run where [Compliance and
Reporting][004-compliance-and-reporting] places them, with integration ahead of the complete end-to-end run, so a local
failure surfaces before the slower journeys that depend on it.

## Coverage Is Measured Where It Gates

Gating coverage comes from the run that executed the tests, because two runs can disagree. What coverage may measure is
owned by [Meaningful Coverage](meaningful-coverage.md). Each module excluded from measurement is named in the project's
README, with the reason a test at that layer may not reach it.

Lowering a floor or widening an exclusion changes what the repository is willing to ship. It is a change to a gate, made
as [Software Quality Enforcement][software-quality-enforcement] requires.

## Adopter Decisions

- **layers a floor covers** — Option: unit only; Gains: the floor stays inside the fast gate; Costs: code that only real
  resources reach is unmeasured
- **layers a floor covers** — Option: unit and integration; Gains: real-boundary code is measured as well; Costs: a
  second floor, run outside the fast gate
- **task runner** — Option: a task-graph tool; Gains: affected selection and ordering come built in; Costs: one more
  tool to pin and maintain
- **task runner** — Option: plain scripts; Gains: nothing beyond the language toolchain; Costs: affected selection is
  maintained by hand

Record each applicable choice. Each project's README names the commands its targets resolve to, and every omitted target
with its reason.

## Enforcement

A failing gate is fixed at its cause, never weakened or bypassed. Review applies the classification as tests change, and
a validator for it is added only when [Repository Check Policy][repository-check-policy] admits one. The adopter
enforces the gate contracts in its own task configuration and `ci`.

[002-layers-and-adapters]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/behaviour-driven-development/002-layers-and-adapters.md
[004-compliance-and-reporting]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/testing/behaviour-driven-development/004-compliance-and-reporting.md
[software-quality-enforcement]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/checks/software-quality-enforcement.md
[repository-check-policy]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/checks/repository-check-policy.md
