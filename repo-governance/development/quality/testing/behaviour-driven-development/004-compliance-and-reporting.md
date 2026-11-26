---
description: >-
  Separates static binding compliance from semantic review, fails the behaviour-coverage check on a missing binding or
  justification, places each scenario check in its gate, and requires a generated per-feature status report.
when_to_use: >-
  Use when configuring behaviour-driven development gates, deciding which scenario checks run in hooks, or publishing
  the scenario status of a feature.
---

# Compliance and Reporting

Green bindings prove that steps resolve and pass. They do not prove that a scenario's words match what the code does,
and that takes a different check.

## Static Compliance Is Not Semantic Proof

Static compliance resolves every step to its binding and applies the limits in
[Bindings and Exemptions](003-bindings-and-exemptions.md). It neither executes scenarios nor judges whether a binding
tests what its sentence says.

After a material change to scenarios or to their implementation, run the
[Gherkin Implementation Review](../../../../workflows/quality/gherkin-implementation-review.md). It checks the scenarios
against the real behaviour of the implementation and its tests, across every applicable layer and every part of the
corpus the change reaches, not only the files that changed.

## The Behaviour-Coverage Check

Every scenario is bound at the unit, integration, and end-to-end layers unless it carries an exemption. The static
behaviour-coverage check fails on each of these:

- a scenario with no binding at a layer it is not exempt from;
- an exemption with no written justification;
- a stale exemption, at a layer where a binding exists; and
- a scenario exempt at both the integration and end-to-end layers, which is a detail for a plain test.

The check is proven on a deliberately violating corpus that it fails and on a conforming one that it passes.

## Each Check in Its Gate

Placement uses the surfaces
[Surfaces and Mutation](../../../../conventions/structure/repository-configuration/003-surfaces-and-mutation.md)
declares.

| Check                 | Runs                                                                             |
| --------------------- | -------------------------------------------------------------------------------- |
| unit scenarios        | in `pull-request`, inside the fast gate, for affected projects                   |
| static compliance     | in `pull-request`, globally, as the fast gate's last step                        |
| integration scenarios | in `pull-request` on every pull request, as a required job for affected projects |
| end-to-end scenarios  | in a `main` or `scheduled` workflow, and for affected journeys before completion |
| semantic review       | after a material change to scenarios or implementation, before completion        |

No scenario runs in a hook: a slow hook gets bypassed, and the pull-request gate runs these jobs in parallel on any
runner. End-to-end stays off the per-pull-request path because its journeys are the slowest and may depend on outside
services.

A repository with no pull-request gate runs the same checks in its local landing gate before landing or pushing,
end-to-end included where its dependencies are local, and records the result its status report is produced from.

## Generated Status Report

Each feature has a status report generated from runner results and binding evidence, never written by hand. For every
scenario and layer it shows passed, failed, or exempt, with the recorded reason for an exemption.

A hand-maintained status table reports what someone believed. A generated one reports what ran, so it is produced from
the latest full run.

## Manual Confirmation at the Boundary

Scenarios do not replace a person checking the running system. A behaviour change still receives the direct checks in
[Behaviour Change Verification](../../manual-verification/006-behaviour-change-verification.md), and an API change the
request that [API Testing](../api-testing.md) requires.
