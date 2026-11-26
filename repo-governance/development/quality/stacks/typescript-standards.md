---
description: >-
  Fixes the TypeScript baseline: a declared compiler floor, strict options, no any or unchecked assertions, expected
  failures returned as Results, and type check, lint, and format gates.
when_to_use: >-
  Use when configuring, writing, or reviewing TypeScript, or when a change relaxes a compiler option, adds an any or an
  assertion, or throws a failure callers should expect.
---

# TypeScript Standards

This standard is canonical for TypeScript and owns strict typing. It holds only choices the language leaves open; a
TypeScript skill defers here per rule. The compiler proves only what its configuration asks: a permissive option, an
`any`, or an assertion instead of a check lets a program type-check yet fail at runtime.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), [Reproducibility](../../../principles/reproducibility.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). React and Next.js code also follow
[React Standards](react-standards.md) and [Next.js Standards](nextjs-standards.md).

## Compiler Version

Each project declares a minimum compiler version; its lockfile pins the exact compiler every contributor and pipeline
runs. New projects start on the current stable line. Raising the floor is deliberate: checking differs between releases.
Declaring and pinning follow [Native-First Toolchain](../../workflow/native-first-toolchain.md).

## Strict Compiler Options

Every project enables:

- `strict`, for null checks, implicit-`any` errors, and the rest of the strict set;
- `noUncheckedIndexedAccess`, so an indexed read's type admits `undefined`;
- `noImplicitReturns` and `noFallthroughCasesInSwitch`, so no path returns or falls through implicitly;
- `noUnusedLocals` and `noUnusedParameters`, so dead code is a finding.

Never relax an option to make a change compile; fix the code.

## Typing Rules

- **No `any`.** A value of unknown shape is `unknown`, narrowed before use. Unsafe use of a library-returned `any` is a
  finding too.
- **Validate, never assert.** Boundary data (request body, parsed text, storage, environment) passes a type guard or
  schema before the program relies on its type. An assertion states an unchecked belief, so neither a double nor a
  non-null assertion silences a type error.
- **Exclusive states are discriminated unions.** Each state carries a literal tag and only its own fields, so an
  impossible combination, unlike with boolean flags, does not compile. Handling a union covers every tag.
- **Readonly by default.** A property or collection callers must not change is `readonly`; a literal lookup table is a
  constant assertion.
- **Distinct primitives get branded types.** An identifier or quantity confusable with another of the same primitive is
  branded and created only by a validating factory.

Code is organised by feature; no technical layer spans features. Business logic is functions over readonly data,
structured as [Functional Core, Imperative Shell](../architecture/functional-core-imperative-shell.md) or, where ports
exist, [Hexagonal Architecture](../architecture/hexagonal-architecture.md).

## Expected Failures Are Returned

A normal-operation failure, such as invalid input, an unmet rule, or a missing record, is returned as a Result: a
discriminated union of a success holding the value and a failure holding a typed error, so the caller must check before
reaching the value. Exceptions are for programmer errors and broken invariants.

No error is swallowed: a caught error is handled, wrapped with context, or propagated. Every promise is awaited,
returned, or given a rejection handler, since a floating promise's rejection escapes every handler.

## Gates

- **Type check:** the compiler over the whole project, emitting nothing.
- **Lint:** a type-aware linter's recommended type-checked rules, the typing and promise rules above, explicit function
  return types, and `PascalCase` names for interfaces and type aliases.
- **Format:** one formatter, with overlapping lint rules disabled so they never conflict.

Findings fail at the [Lint Strictness](../checks/lint-strictness.md) threshold; each gate is a named target per
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Behaviour is built test-first per
[Test-Driven Development](../testing/test-driven-development.md). A test intercepting network requests in process is a
unit test, never integration evidence. Coverage meets the floor in
[Meaningful Coverage](../testing/meaningful-coverage.md), and any higher floor is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Illustrative Example

`typescript-eslint`'s type-checked configuration enforces `no-explicit-any`, the `no-unsafe-*` rules,
`no-non-null-assertion`, and `no-floating-promises`; Prettier formats, with `eslint-config-prettier` disabling
overlapping rules; `tsc --noEmit` type-checks.

## Hermetic Unit Tests

A lint override whose files glob matches only unit-test files bans what reaches outside the process:
`no-restricted-imports` for modules such as `node:fs`, `node:child_process`, `node:net`, and `node:http`, and
`no-restricted-globals` for `fetch` and `process`, with `no-restricted-properties` for `Date.now` and `Math.random`.
Biome's `noRestrictedImports` and `noRestrictedGlobals` serve the same purpose.

## Enforcement

An adopter enforces the compiler options in its committed configuration and the typing rules in its lint gate. Review
applies what no linter sees, such as whether a failure is expected or exceptional.
