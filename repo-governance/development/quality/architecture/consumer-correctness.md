---
description: >-
  Requires public API choices to favour the consumer being correct: errors that name the cause and the fix, names that
  match across surfaces, and failure surfaced instead of silent behaviour.
when_to_use: >-
  Use when designing, naming, or changing any public name, error, default, or result shape, or when reviewing such a
  change.
---

# Consumer Correctness First

When two designs both work, choose the one that most helps the consumer be correct. A consumer cannot read maintainer
intent, so an ambiguity in the surface becomes misuse, and misuse becomes an incident. A descriptive surface fails
loudly at the point of error; a terse one fails later, somewhere else.

This standard implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md) and
[Fail Closed](../../../principles/fail-closed.md). It does not change [Public Contract](public-contract.md): message
wording stays free to improve, and a rename stays breaking.

## What It Requires

- **errors name the cause and the fix** — A failure says what was wrong and what to do instead. Followed: each error
  path states the offending condition and the correction. Violated: an error that reports only that something failed, or
  a failure with no message where one was possible.
- **names match across surfaces** — One concept keeps one spelling in code, types, documentation, and errors; see the
  one-spelling precedent in [Naming Choices](../../../../docs/explanation/naming-choices.md). Followed: every documented
  or reported name resolves to the same code element. Violated: two spellings for one concept, or a documented name with
  no code counterpart.
- **no silent behaviour** — Refuse or surface an undecidable input; never quietly absorb it. Followed: unknown values
  fail, and handlers convert only what they name, as `attempt` catches only the types it is given. Violated: a default,
  fallback, or swallowed case that lets misuse pass quietly.

## The Cost Is Length

Descriptive errors and exact names are longer than terse ones. That length is part of the job, not decoration: the whole
job includes being usable by someone who was not there when it was written, per
[Minimal Sufficiency](../../../principles/minimal-sufficiency.md).

## Enforcement

Unenforced by tooling, by decision. No check can tell whether an error names its cause or whether two names spell one
concept, so PR review judges each change against the three observations above.
