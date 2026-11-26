---
description: >-
  Requires a shared tool to declare its public surface, fixes which changes to commands, flags, exit codes,
  configuration, and machine-readable output are breaking, and names what stays private.
when_to_use: >-
  Use when changing a command, flag, exit code, configuration key, or machine-readable output of a tool others pin, or
  when deciding whether a change needs a major version.
---

# Public Contract

A consumer pins a tool by version and calls it from a hook or a gate it does not want to think about again. That pin has
to mean the same thing tomorrow.

[Consumer Independence](../../../principles/consumer-independence.md) establishes that the surface is a contract and
that breaking it ships only as a major version. This standard fixes how the contract is declared and where the line
between compatible and breaking falls. It also implements
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md) and
[Immutability](../../../principles/immutability.md).

## Declare the Contract

The tool's documentation lists its public surface. Anything not listed is not offered.

| Surface                 | What is public                                                                    |
| ----------------------- | --------------------------------------------------------------------------------- |
| commands                | every command path                                                                |
| flags                   | every flag name, and the meaning of its value                                     |
| exit codes              | every code and the condition it maps to, which is what a caller branches on       |
| configuration keys      | every key, whether it is required, and the meaning of its value                   |
| machine-readable output | every documented record shape: its fields, their types, and what each field means |

The particular codes, keys, and shapes belong to each tool. This standard fixes only that they are declared, and how
they may change.

## Compatible and Breaking

| Change                                                         | Class      |
| -------------------------------------------------------------- | ---------- |
| adding a command, flag, configuration key, or output field     | compatible |
| making a required configuration key optional                   | compatible |
| removing or renaming any public element                        | breaking   |
| changing what an element means, or the type of an output field | breaking   |
| making an optional configuration key required                  | breaking   |
| tightening validation of a value consumers already declare     | breaking   |
| giving an existing exit code an additional meaning             | breaking   |

The test is whether a consumer that worked yesterday still works today on the same pin. A configuration that validated
on a version validates on it tomorrow.

## Exit Codes Stay Few and Distinct

A caller must be able to act on the exit code alone, without knowing which subcommand ran. Each code therefore names one
class of outcome, and a new condition either belongs to an existing class or is a major version.

Overloading a code is the quiet break. The old code still appears, so nothing fails loudly, and every consumer has lost
the ability to tell two conditions apart. An outcome where the tool could not check at all never shares a code with a
clean result, as [Fail Closed](../../../principles/fail-closed.md) requires.

## A Rename Is a Contract Change

A rename is not a spelling correction. It removes one public element and adds another, and it is classified as a
removal, however much better the new name reads.

A breaking change lands with its specification and documentation updated in the same change, so the version that
introduces it also describes it.

## What Is Not Public

Unless the documentation lists them, these carry no promise:

- the wording of human-readable messages;
- output ordering beyond what a documented format guarantees;
- log lines written to standard error; and
- every internal module and function.

A consumer that parses a human-readable message has taken a dependency the tool never offered. Keeping these free to
improve is what lets the declared surface stay still.

## Enforcement

An adopter keeps its declared surface classified and versioned as above, and enforces it at an enforcement point it
names, such as its own test suite or gate.
