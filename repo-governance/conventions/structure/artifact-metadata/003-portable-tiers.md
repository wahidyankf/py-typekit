---
description: >-
  Requires every canonical agent to declare exactly one of four workload tiers, describing normal use rather than naming
  a vendor model.
when_to_use: >-
  Use when assigning a tier to an agent, or when a vendor model name is proposed as metadata.
---

# Portable Tiers

Every canonical agent declares exactly one `tier`:

| Tier        | Normal workload                                                         |
| ----------- | ----------------------------------------------------------------------- |
| `ultra`     | rare, highest-complexity synthesis where cost and latency are secondary |
| `plan`      | architecture, planning, or high-context judgement                       |
| `execution` | normal implementation, repair, and repository mutation                  |
| `fast`      | narrow lookup, classification, or inexpensive deterministic support     |

## The Tier Is Not a Quality Ranking

`fast` is not a worse agent but a narrow one, and a heavier tier makes every invocation slower and costlier without
improving any answer.

## Select From Normal Use, Not the Hardest Case

Every agent has an occasional hard invocation. Choosing a tier from that case moves the whole roster upward, and after a
few rounds the tiers stop distinguishing anything.

Ask what this agent does on a typical day.

## No Vendor Model Names

A tier names a workload. It never names a model, a provider, a context size, or a price band.

Model names change independently in each harness, so metadata naming one goes stale, in every copy, with nothing to
signal the drift.

Where a repository maps tiers to concrete models, that mapping lives in its own configuration — keyed by harness and
then by tier — and never in the agent. A profile may declare a tier with an empty mapping. An empty mapping pins
nothing, so the harness applies its own default model and effort. Declaring a tier empty is a deliberate choice; in a
profile that maps tiers, leaving a tier undeclared is an error.

## Match the Tier to the Workload's Complexity

Choose the lightest tier that does the normal workload reliably. Output someone has to correct costs more than the tier
saved, and reasoning the work never uses is paid for on every run.

Start from the lightest tier. Each heavier tier has to be argued for, never assumed:

| The normal workload                                                                | Tier        |
| ---------------------------------------------------------------------------------- | ----------- |
| follows a fixed procedure with no branching judgement                              | `fast`      |
| applies stated rules, validates against fixed criteria, or follows a template      | `execution` |
| invents an approach, synthesizes across domains, or makes cascading judgement      | `plan`      |
| audits a plan or its execution against a specification with high-context judgement | `plan`      |
| has demonstrably failed at `plan` on work expensive to detect and to undo          | `ultra`     |

This table governs selection; the table at the top of this module only characterizes each tier.

When the answer is unclear, `execution` is safer than `fast`: a narrow tier meeting an unexpected state fails quietly.

Two tests settle most borderline cases. Judge the core loop — what the agent does repeatedly — rather than its setup: an
agent that orients once and then applies rules is an `execution` agent. And weigh what a wrong answer costs: a flawed
plan steering a long piece of work justifies more than a missed entry the next check will catch.

## `ultra` Needs Evidence

Anticipated difficulty is not evidence. An agent moves to `ultra` only with a record of the observed `plan`-tier
failure, why a cheaper remedy — a narrower scope, a better instruction, a skill — does not apply, and what would return
it to `plan`.

## The Tier Is Justified in the Body

A reviewer has to be able to test a tier. The agent's body states its normal workload in terms the table above applies
to, and a tier heavier than that workload implies states its reason there too. Where the table places the stated
workload at the declared tier, that statement is itself the justification.

## Declared, Never Inherited

An omitted tier fails. It never means `plan`, and it never means whatever the calling session uses.

Treating an omitted tier as a deliberate choice of the top working tier is rejected: an omission cannot be told apart
from an oversight, so review approves both. Inheritance belongs one step later — the tier is always declared, and only
the model a harness runs for it is inherited, through an empty mapping or a profile that maps no tier.
