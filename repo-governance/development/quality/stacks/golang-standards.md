---
description: >-
  Fixes the Go baseline: gofmt, vet, and recorded linters as failing gates, every error handled or returned,
  consumer-declared interfaces, goroutines with an owner and stop signal, and statement coverage.
when_to_use: >-
  Use when creating, configuring, or reviewing a Go module, or choosing its linters, an error's form, an interface's
  home, or how a goroutine ends.
---

# Go Standards

Canonical for Go, this standard holds the choices Go and its toolchain leave open; a Go programming skill defers here.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). The module's `go` directive and `go.sum` follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Gates

- **Format:** `gofmt -l` lists no file.
- **Type check:** `go build ./...`, with the vet run compiling test files too.
- **Lint:** [`go vet`](https://pkg.go.dev/cmd/vet) over every package, plus a linter set recorded in committed
  configuration, never only in command flags. Example: golangci-lint's `standard` set
  ([configuration](https://golangci-lint.run/docs/configuration/file/)).

Findings fail at the threshold [Lint Strictness](../checks/lint-strictness.md) sets, and each `//nolint` names its
linter and reason.

## Type and Boundary Safety

The compiler is Go's checker under [Type and Boundary Safety](../code/type-and-boundary-safety.md):

- `any` appears in a signature only where every type is accepted; domain code uses concrete types or constrained
  generics.
- A type assertion uses the two-value form unless a panic is the contract.
- Decoding zero-fills a missing field, so decoded input becomes a domain value through a constructor checking what a
  zero value cannot distinguish; no decoded struct passes inward unchecked.
- Package `unsafe` appears only beside a comment stating its safety invariant.

## Errors

Every returned error is handled or returned, never discarded with `_`, and the error case returns first. Error strings
are lowercase without trailing punctuation, since they get wrapped
([Code Review Comments](https://go.dev/wiki/CodeReviewComments)). The form follows the caller's need:

- to test for one condition, an exported sentinel compared with `errors.Is`;
- to read failure details, an exported error type extracted with `errors.As`;
- only to report or pass it on, an identity-free error wrapped with context through `%w`.

Never branch on message text. A `panic` signals a programmer error or failed startup, never a failure a caller could
handle.

## Interfaces and Concurrency

- An interface is declared in its consuming package, sized to the methods it calls; the implementation returns its
  concrete type.
- `context.Context` is the first parameter of every call that may wait, never stored in a struct.
- Every goroutine has an owner waiting for it and a stop signal.
- Security-relevant randomness comes from `crypto/rand`.
- A zero value is useful where possible, and a getter has no `Get` prefix
  ([Effective Go](https://go.dev/doc/effective_go)).

## Tests

Unit tests sit in `_test.go` files beside their package and run with `-race`, measuring coverage there. A test using
`t.TempDir`, `t.Setenv`, a real listener, or a child process is integration under
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md).

Go coverage counts statements, so no branch figure is claimed. One instrumented unit run measures the whole module
([`-coverpkg` and `-coverprofile`](https://go.dev/doc/build-cover)), and only that figure is held to the floor in
[Meaningful Coverage](../testing/meaningful-coverage.md); integration runs stay outside it. Any floor above the minimum
is recorded under [Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Hermetic Unit Tests

golangci-lint bans impure calls in unit-test files: `forbidigo` patterns forbid clock, file, environment, process, and
random identifiers such as `time.Now` and `os.ReadFile`, kept to `_test.go` files by a `linters.exclusions.rules` entry
with `path-except`; a `depguard` rule with `files: ["$test"]` denies `net`, `os/exec`, and `database/sql`. Integration
files carry a build tag the default lint run omits.

## Documentation

Every exported name has a doc comment beginning with that name. An exported sentinel or error type joins the
[Public Contract](../architecture/public-contract.md), so it is exported only when a caller needs it; a behaviour change
updates its documentation per [Specification Maintenance](../evidence/specification-maintenance.md).

## Adopter Decisions

| Decision              | Option                      | Gains                           | Costs                                                                     |
| --------------------- | --------------------------- | ------------------------------- | ------------------------------------------------------------------------- |
| assertions            | `testing` only              | no dependency                   | longer comparisons, hand-written diffs                                    |
|                       | a library; example: testify | shorter assertions, clear diffs | a dependency, per [Dependency Selection](../code/dependency-selection.md) |
| integration selection | a build tag per file        | tests stay beside code          | a forgotten tag moves a test into unit                                    |
|                       | a separate test directory   | layer visible by path           | tests reach only the exported API                                         |

Record each choice in the repository adapter [Stack Packs](../../../conventions/structure/stack-packs.md) defines.

## Enforcement

The toolchain and recorded linters enforce the gates in the adopter's pull-request gate; review applies the rest.
