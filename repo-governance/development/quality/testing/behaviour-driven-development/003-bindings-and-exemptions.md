---
description: >-
  Requires strict resolution of every scenario step, forbids bindings that pass without exercising the subject, and
  limits an exemption to one scenario at one layer with a boundary reason and alternative proof.
when_to_use: >-
  Use when writing or reviewing step bindings, when a step is undefined, ambiguous, or unused, or when proposing that a
  scenario skip a layer.
---

# Bindings and Exemptions

A binding connects a sentence to a check. When it can pass without the check running, the scenario becomes documentation
that claims to be a test.

## Strict Resolution

Every step resolves to exactly one binding in each applicable layer. The adopter configures its test run so that each of
these fails it:

- an undefined step;
- an ambiguous step that matches more than one binding;
- a duplicate binding for the same expression; and
- an unused binding that no step matches.

Each expanded row of a scenario outline counts as a scenario of its own. Bindings stay thin, translating the step and
calling the subject, with shared setup and helpers kept in support modules.

## A Binding Must Exercise the Subject

A binding never:

- asserts a value it was handed instead of one the subject produced;
- returns early or does nothing;
- remains a stub or pending placeholder; or
- passes without invoking the subject under test.

Each of these is a defect even when the run is green, and review treats it as a failure.

## Exemptions

An exemption excuses one scenario from one layer, and only for a boundary reason: that layer cannot reach the behaviour
at all, as with a hardware sensor or a page hosted by a third party. Every exemption, whether tag or inventory entry,
carries a written justification stating that reason and its alternative proof: the scenario's unit binding, which no
exemption can remove, or a binding at the other layer when that layer also covers the behaviour.

Difficulty, runtime, speed, flakiness, cost, and unfinished work such as a TODO are never valid reasons. Each describes
a problem to fix, not a boundary. Nor is "not user-visible": such a scenario leaves the corpus instead.

An exemption never applies to a `Feature`, a `Rule`, or a `Background`, never to the unit layer, and never removes all
proof of a behaviour. The unit binding is mandatory for every scenario precisely because it is the alternative proof.

A scenario exempt at both the integration layer and the end-to-end layer is a detail, not contract behaviour: only the
unit layer proves it. It moves out of the corpus into a plain test beside the code, per
[Behaviour-Driven Development](../behaviour-driven-development.md#scenario-or-plain-test).

How exemptions are recorded is an adopter decision:

| Option                            | Gains                                          | Costs                                               |
| --------------------------------- | ---------------------------------------------- | --------------------------------------------------- |
| a comment and tag on the scenario | the reason sits beside the scenario it excuses | the corpus carries test-layer vocabulary            |
| a reviewed inventory file         | the corpus stays a pure statement of behaviour | the inventory can drift from the scenarios it names |

In the tag form, which an adopter of the
[Test and Gate Contract](../../checks/test-and-gate-contract/005-behaviour-corpus.md) takes, a comment directly above
the tag carries the reason and names the target whose run is the alternative proof:

```gherkin
# Exemption(e2e): <reason>; alternative-proof: <target>
@e2e-exempt
Scenario: <scenario name>
```

The integration layer uses `@integration-exempt` in the same way. No `@unit-exempt` tag exists. A tag without a valid
comment fails, and so does a stale exemption: a binding at the exempted layer means the tag is no longer true, and the
check fails with "stale exemption — remove the tag". The adopter enforces the format and these limits in its static
behaviour-coverage check, in the pull-request gate.
