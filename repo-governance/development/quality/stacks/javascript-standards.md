---
description: >-
  Fixes the JavaScript baseline: files type-checked through JSDoc under strict compiler options, runtime validation at
  external input, modern language defaults, handled promises, and separate type check, lint, and format gates.
when_to_use: >-
  Use when creating, configuring, or reviewing authored JavaScript, or when a change adds untyped input, turns off
  checking for a file, or chooses its test runner or coverage instrument.
---

# JavaScript Standards

This standard is canonical for authored JavaScript: scripts, tools, and modules written as `.js`, `.mjs`, or `.cjs`,
including inside a TypeScript project. It holds the choices the language leaves open; a JavaScript skill defers here per
rule. TypeScript code follows [TypeScript Standards](typescript-standards.md) instead.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Fail Closed](../../../principles/fail-closed.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). The runtime version, lockfile, and every tool
below follow [Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Type check:** the TypeScript compiler checks JavaScript, emitting nothing: project-wide through `allowJs` and
  `checkJs`, or per file through `// @ts-check`
  ([JS projects](https://www.typescriptlang.org/docs/handbook/intro-to-js-ts.html)). The configuration enables `strict`
  and `noUncheckedIndexedAccess`.
- **Lint:** a linter over a committed flat configuration. Where it runs type-aware rules, the lockfile pins a compiler
  in the linter's supported range. Example: ESLint with typescript-eslint.
- **Format:** one formatter; a shared configuration disables overlapping lint rules instead of running the formatter as
  a lint rule. Example: Prettier with `eslint-config-prettier`
  ([integrating with linters](https://prettier.io/docs/integrating-with-linters)).

Findings fail at the [Lint Strictness](../checks/lint-strictness.md) threshold.

## Type and Boundary Safety

JSDoc annotations are JavaScript's static types under [Type and Boundary Safety](../code/type-and-boundary-safety.md):

- Every exported function declares parameter and return types in JSDoc; a shared shape is a `@typedef`.
- A file excluded from checking is a waiver with its reason, never a default.
- An error the checker must accept is silenced with `// @ts-expect-error` and its reason, which fails once the error is
  gone; never `// @ts-ignore`.
- Never write `any` in JSDoc; unknown data is typed `unknown` and narrowed.
- A JSDoc annotation on parsed data is a claim, not a check: nothing checks JavaScript types at runtime. Input from a
  request, a file, `JSON.parse`, the command line, or the environment passes a runtime guard or schema before the
  program relies on its shape.

## Language Defaults

- Code is written as ES modules, which run in strict mode.
- Bindings are `const`, or `let` when reassigned, never `var`. Equality is `===`. Value-built strings are template
  literals; value iteration uses `for...of`
  ([MDN code style](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Code_style_guide/JavaScript)).
- Asynchronous code uses `async` and `await`. Every promise is awaited, returned, or given a rejection handler, since a
  floating promise's rejection escapes every handler.
- A caught error is handled, wrapped with context through `cause`, or rethrown, never swallowed. Only `Error` objects
  are thrown.

## Tests

Tests follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md): a test intercepting network requests
in process is a unit test, never integration evidence. A gate relies only on a coverage instrument its runtime or runner
marks stable, measuring branches where it can, per [Meaningful Coverage](../testing/meaningful-coverage.md). Example:
Vitest with V8 coverage ([coverage](https://vitest.dev/guide/coverage)). Any floor above the minimum is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Hermetic Unit Tests

Plain JavaScript unit-test files take the restricted-import mechanism of
[TypeScript Standards](typescript-standards.md#hermetic-unit-tests): a lint override scoped to unit-test globs, with
`no-restricted-imports` for file, process, and network modules and `no-restricted-globals` for `fetch` and `process`.

## Documentation

An exported function's JSDoc is both its type and its reference documentation, so it states behaviour and thrown errors
as well as types. An observable behaviour change updates it per
[Specification Maintenance](../evidence/specification-maintenance.md) and
[Public Contract](../architecture/public-contract.md).

## Adopter Decisions

| Decision    | Option                        | Gains                                 | Costs                                    |
| ----------- | ----------------------------- | ------------------------------------- | ---------------------------------------- |
| check scope | project-wide `checkJs`        | no file escapes by omission           | existing backlog cleaned before the gate |
|             | per-file `// @ts-check`       | file-by-file adoption                 | an unmarked file is silently unchecked   |
| test runner | the runtime's built-in runner | no dependency                         | coverage may still be experimental       |
|             | a runner package, like Vitest | stable branch coverage and watch mode | a dependency to pin and upgrade          |

Record each choice in the [Stack Packs](../../../conventions/structure/stack-packs.md) repository adapter; a per-file
choice records how an unmarked file is found.

## Enforcement

The compiler, linter, and formatter enforce the gates in the adopter's pull-request gate. Review applies boundary
validation and the promise and error rules no linter fully sees.
