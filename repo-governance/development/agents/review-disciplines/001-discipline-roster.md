---
description: >-
  Lists the review disciplines with the scope each owns and the scope it routes elsewhere, and records the choice
  between nine and eight disciplines.
when_to_use: >-
  Use when chartering a specialist reviewer, or when deciding which discipline a finding belongs to.
---

# Discipline Roster

Every specialist declares two things: what it owns, and what it deliberately does not raise because another discipline
owns it. The second column matters as much as the first. A charter with only an owned scope grows until it overlaps its
neighbours, and overlap is where duplicate and contradictory findings come from.

## The Disciplines

| Discipline           | Owns                                                                                                                               | Routes elsewhere                                                                                                                                         |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| architecture         | new tradeoffs, module boundaries, reversibility, blast radius, quality-attribute effects, new dependencies                         | violation of an existing layering rule → governance; missing domain scenarios → correctness                                                              |
| correctness          | behaviour against domain intent; acceptance criteria across edge and error cases                                                   | error-handling shape rules → governance; whether a boundary should exist → architecture                                                                  |
| governance           | mechanical conformance to documented rules: naming, structure, required files and sections present                                 | whether a new rule should exist → architecture; scenario completeness → correctness; stale instructions → instruction currency; accuracy → documentation |
| security             | secrets in the change, injection, untrusted-input handling, unsafe filesystem or version-control operations                        | security-neutral convention text → governance                                                                                                            |
| test integrity       | coverage gaming; weakened, skipped, or narrowed tests; a fix with no regression test                                               | whether the behaviour is correct → correctness                                                                                                           |
| performance          | concrete or likely regressions, hot-path changes, complexity growth, memory and I/O use                                            | a deliberate quality-attribute tradeoff → architecture; conformance to a documented budget → governance                                                  |
| documentation        | substantive completeness, clarity, drift from code, accessibility, a change description that misstates the change                  | mechanical documentation conformance → governance; whether documented behaviour is correct → correctness                                                 |
| instruction currency | a toolchain, dependency-manager, environment, or pipeline change missing from agent instruction files; empty filler                | whether a new rule should exist → architecture; mechanical conformance → governance                                                                      |
| type soundness       | escape hatches that defeat the type system: unchecked casts, suppressed nullability, ignored type errors, unhandled fallible paths | whether code compiles → the build; unrelated logic → correctness; whether a type boundary should exist → architecture                                    |

## Why Some Lines Fall Where They Do

**Test integrity is not correctness.** A weakened test and a wrong behaviour can show the same symptom. Separating them
lets a finding name the real cause instead of blending both into one vague complaint.

**Instruction currency is not governance.** Governance checks conformance _to_ the instruction files. Nothing in that
charter checks whether those files still describe the toolchain the change just altered, and routing such findings to
governance would make it check something it was never written to check. Instruction filler means text that adds no
enforceable rule; whether an overlong file also counts is part of the adopter decision below.

**Type soundness is not the build.** A clean compile is no evidence against a soundness finding, since the escape hatch
is precisely what let the code compile.

**Documentation is not governance.** Governance asks whether a document follows the mechanical rules; documentation asks
whether it is complete, clear, and still true.

## Adopter Decision: Nine or Eight

| Option | Disciplines               | Fits                                                            | Trade-off                                                                                             |
| ------ | ------------------------- | --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| nine   | all of the above          | pull-request review in a codebase with statically typed source  | widest coverage; type soundness costs a specialist, and may be skipped when no typed source changed   |
| eight  | all except type soundness | local commit-range review, or a repository with no typed source | one fewer specialist per full review; escape-hatch misuse is caught only incidentally, by correctness |

Record the choice once, beside the specialist roster. Ruling (g) in [Boundary Rulings](002-boundary-rulings.md) applies
only under the nine-discipline option.

The same record states how instruction currency treats file length. It leaves length out only where a length gate
already enforces a limit; without such a gate, a file over the adopter's limit is instruction filler this discipline
raises.
