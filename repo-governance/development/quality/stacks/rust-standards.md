---
description: >-
  Fixes the Rust baseline: an explicit edition in every manifest, rustfmt and pedantic Clippy as failing gates, no
  unsafe code outside declared low-level crates, one async runtime and serialization framework, and Rust code shapes.
when_to_use: >-
  Use when creating, configuring, or reviewing a Rust crate or workspace, or when choosing its edition floor, lint
  table, unsafe policy, async runtime, error types, security libraries, or the shape of a Rust type.
---

# Rust Standards

This standard is canonical for Rust. It holds the choices Rust and Cargo leave open, and a Rust programming skill defers
here for each rule it applies.

It implements [Automation Over Manual](../../../principles/automation-over-manual.md),
[Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Immutability](../../../principles/immutability.md), and [Pure Functions](../../../principles/pure-functions.md). The
toolchain file, lockfile, and version pins follow [Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Edition

Every `Cargo.toml` declares `edition`. Cargo reads a manifest without one as the oldest edition, so an omission compiles
quietly under rules nobody chose. A new crate declares the current edition.

## Adopter Decision

| Existing crates             | Gains                             | Costs                                            |
| --------------------------- | --------------------------------- | ------------------------------------------------ |
| move to the current edition | one set of idioms and lints       | each older crate migrates before its next change |
| keep an older edition       | migration is scheduled separately | review holds two editions' rules at once         |

Record the choice with the edition it names.

## Gates

- **Formatting:** `cargo fmt --all -- --check` fails on any change, reading a `rustfmt.toml` committed at the workspace
  root.
- **Lints:** `cargo clippy --all-targets -- -D warnings`, with the `pedantic` group enabled and `clippy::unwrap_used`
  denied outside tests.
- **Unsafe code:** every crate sets `unsafe_code = "forbid"` unless its manifest declares it a low-level crate.

Lint levels live in the manifest's `[lints]` table, or in `[workspace.lints]` inherited through
`lints.workspace = true`, never only in command flags, so an editor and the pipeline read one set. `pedantic` sits at a
lower priority so that a single lint's `allow` overrides it, and each `allow` or `#[rustfmt::skip]` carries its reason,
as [Lint Strictness](../checks/lint-strictness.md) requires.

Production code never calls `unwrap()`. `expect()` appears only where its message states the invariant that rules
failure out, and a library returns `Result` from every fallible operation rather than panicking.

## Unsafe Code

The manifest lint covers every target of the package; a `#![forbid(unsafe_code)]` attribute covers only its own crate
root. A low-level crate is one whose manifest overrides the lint with its reason, accepted in review. It keeps each
block minimal, with a `// SAFETY:` comment stating the invariant and `clippy::undocumented_unsafe_blocks` denied.

## Stack

- **Async runtime:** one runtime serves the workspace, because tasks, timers, and input and output types from two
  runtimes do not interoperate, and async tests run on it. Async code never blocks the runtime: no blocking call inside
  a task, CPU-bound work moves to the runtime's blocking pool, and a lock held across `.await` is async-aware.
- **Serialization:** one framework with derived implementations, shared by the crates the workspace depends on.
- **Errors:** a typed error enum per domain boundary; a binary's entry point may wrap errors with context.

Example: Tokio as the runtime with `#[tokio::test]` and `spawn_blocking`, Serde for serialization, thiserror for the
enums, and anyhow at the entry point.

## Tests

Unit tests sit in a `#[cfg(test)]` module beside the code, and integration tests sit in the crate's `tests/` directory.
That split keeps the layers apart as [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md) requires.
Coverage is measured on the unit run, held to the floor in [Meaningful Coverage](../testing/meaningful-coverage.md), and
any higher floor is recorded under
[Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Modules

1. [Code Shape and Security](rust-standards/001-code-shape-and-security.md)

## Enforcement

Cargo, rustfmt, and Clippy enforce the gates in the adopter's own pull-request gate, where the advisory and licence
checks of [Dependency Bump Policy](../../workflow/dependency-bump-policy.md) and
[Dependency Selection](../code/dependency-selection.md) also run. Example: cargo-audit and cargo-deny. Review applies
the stack rules, the `expect()` and no-panic rules, the code shapes, and the security rules.
