---
description: >-
  Chooses a Gherkin scenario for contract behaviour and a plain test for a developer detail, makes one canonical corpus
  per owner of runtime code the statement of caller-visible behaviour, and binds it strictly at every applicable test
  layer.
when_to_use: >-
  Use when adding or changing behaviour, choosing between a scenario and a plain test, organizing feature files, binding
  scenarios to tests at a layer, or deciding whether a scenario may be exempt from a layer.
---

# Behaviour-Driven Development

Behaviour is agreed as examples before it is built, and the same examples then drive every test layer able to prove
them. One written scenario, bound strictly, replaces several descriptions of intent that drift apart.

This standard implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Documentation First](../../../principles/documentation-first.md),
[Automation Over Manual](../../../principles/automation-over-manual.md), and
[Evidence Over Assertion](../../../principles/evidence-over-assertion.md).

## Scenario or Plain Test

Who notices a break decides how a behaviour is proved:

- **Contract behaviour** changes what a user, operator, or harness sees when it breaks: command-line output, exit codes,
  machine-readable bodies, protocol results, and access and safety rules. It must be a Gherkin scenario in the specs
  tree.
- **A developer detail** is noticed only by a developer: a branch, an internal helper, a configuration mapping, a
  structure rule. It must be a plain test beside the code, never a scenario.

A scenario is a promise to people outside the code, and a plain test is a promise to its maintainers. A detail written
as a scenario buries the contract in noise; a contract left as a plain test can change unseen.

A scenario that needs both an integration exemption and an end-to-end exemption is a detail: only the unit layer proves
it, so it becomes a plain test, per
[Bindings and Exemptions](behaviour-driven-development/003-bindings-and-exemptions.md).

Enforcement: gated for the exemption pair, by the static check in
[Compliance and Reporting](behaviour-driven-development/004-compliance-and-reporting.md). Unenforced by decision for the
choice itself, because whether anyone outside the code sees a break is a review judgement.

## Every Owner of Runtime Code Owns a Corpus

An owner is anything with runtime code that a user, operator, harness, or caller reaches: a service, a command-line
tool, an interface, or a library. Each keeps one canonical Gherkin corpus in one directory tree, discovered recursively.
An application's scenarios describe what its user sees. A library's scenarios describe behaviour visible to the caller
of its public API, so a library's contract is stated once and does not rely on a consuming application's scenarios. A
script's behaviour is contract behaviour too, when a caller reaches it. Nothing registers feature files in a list; a
list is a second source that falls out of date the first time someone forgets it.

A dedicated end-to-end project implements the corpus of the application it tests. It keeps no scenarios of its own, so a
behaviour never has two competing statements.

## Scenario First, Then Code

For every change to contract behaviour:

1. Read the scenarios that already describe the behaviour.
2. Add or update the scenario so it states the new behaviour.
3. Bind its steps in every applicable layer.
4. Run them and confirm they fail for the expected reason.
5. Implement until they pass.
6. Cover the branches the scenario does not name with plain tests.

A step that passes before the code exists proves only that its binding checks nothing.

A refactor that changes no behaviour leaves every scenario unchanged and starts from a passing run. Where no scenario
covers the code, a characterization test first records its current behaviour, so the refactor has something to preserve.

## Modules

1. [Discovery and Scenarios](behaviour-driven-development/001-discovery-and-scenarios.md)
2. [Layers and Adapters](behaviour-driven-development/002-layers-and-adapters.md)
3. [Bindings and Exemptions](behaviour-driven-development/003-bindings-and-exemptions.md)
4. [Compliance and Reporting](behaviour-driven-development/004-compliance-and-reporting.md)
