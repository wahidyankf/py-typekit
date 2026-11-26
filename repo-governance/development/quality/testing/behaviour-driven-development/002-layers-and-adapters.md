---
description: >-
  Defines the unit, integration, and end-to-end layers that bind the scenario corpus, how a test is classified, which
  test targets each project role carries, and the layer choices an adopter records.
when_to_use: >-
  Use when deciding which layer a test belongs to, which test targets a project needs, whether integration tests may
  open a loopback listener, or whether a project sets a coverage floor above the minimum.
---

# Layers and Adapters

Each layer binds the same scenarios through its own adapter and proves them against a different boundary. Classifying a
test honestly is what gives its result a meaning.

## Three Layers

| Layer       | Boundary                                                           | Rule                                                       |
| ----------- | ------------------------------------------------------------------ | ---------------------------------------------------------- |
| unit        | in process, with every operating-system-facing dependency injected | mandatory for every scenario, with no exemption            |
| integration | real local resources the test starts and owns, isolated per run    | no external network, and no service the test did not start |
| end-to-end  | the real public boundary, with synthetic data                      | governed by [End-to-End Testing](../end-to-end-testing.md) |

The unit layer is never exempt because it is the only one cheap enough to run on every change. A scenario without a unit
binding has no fast signal at all.

## Classify by the Strongest Boundary

A test belongs to the layer of the strongest real boundary it touches, whether in setup, in the subject, or in an
assertion. A unit test that reads a real file is an integration test. An integration test that calls an outside service
is an end-to-end test, or a defect.

A misclassified test runs in the wrong gate and breaks the speed and isolation promises of the layer it claims.

## Targets Follow the Project Role

| Project role                 | Test targets it carries                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| application or service       | unit, integration, and end-to-end, the last here or in a dedicated project         |
| library                      | unit, integration, and end-to-end through the published artefact a caller installs |
| executable tool              | unit, integration, and end-to-end through the built executable                     |
| dedicated end-to-end project | end-to-end only, implementing the corpus of the owner it tests                     |

Every scenario is bound at all three layers, because each proves a different boundary and a skipped layer leaves that
boundary unproven. A layer is skipped only for one scenario, by an exemption whose reason is that no boundary exists at
that layer, per [Bindings and Exemptions](003-bindings-and-exemptions.md); never for a whole project. Each project's
README names its scenario corpus, adapters, and test targets, and states every exempt layer with its reason, so an
absence reads as a decision rather than a gap.

Never define a target that only prints a message or exits successfully without testing anything: a no-op target reports
coverage that does not exist.

## Adopter Decisions

| Decision                         | Option                                                | Gains                               | Costs                                              |
| -------------------------------- | ----------------------------------------------------- | ----------------------------------- | -------------------------------------------------- |
| loopback listener in integration | allowed when the test starts, owns, and allowlists it | request handling is proven early    | port collisions and slower runs to manage          |
|                                  | forbidden, leaving network use to end-to-end          | integration stays fast and hermetic | request handling is proven only end-to-end         |
| coverage floor above the minimum | a higher fixed floor than the 99% minimum             | more untested code is blocked       | tests get written to the number, not the behaviour |
|                                  | the 99% minimum alone                                 | one number, with no stricter tier   | gaps between 99% and 100% depend on review         |

Record each choice. An unrecorded choice is made differently by every contributor. The adopter enforces the floor, the
minimum from [Meaningful Coverage](../meaningful-coverage.md#the-floor) or a higher recorded one, in its own gate or CI.
