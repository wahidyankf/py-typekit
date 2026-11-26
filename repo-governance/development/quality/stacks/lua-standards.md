---
description: >-
  Fixes the Lua baseline: a declared runtime, strict language-server annotation checks, formatter and linter gates, no
  accidental globals, runtime checks at external input, and returned failures.
when_to_use: >-
  Use when creating, configuring, or reviewing Lua, standalone or embedded, or choosing its runtime version,
  diagnostics, linter, or failure style.
---

# Lua Standards

This standard is canonical for Lua, standalone or embedded in a host program, and the Lua programming skill defers to
it. Lua has no official style guide, so these rules rest on the reference manual and the example tools.

It implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Fail Closed](../../../principles/fail-closed.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md). Runtime and tool versions follow
[Native-First Toolchain](../../workflow/native-first-toolchain.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Runtime Version

Every project declares its Lua version in the language server's committed configuration. Embedded Lua runs on the host's
interpreter, so it declares the host's version, and declares the host API to the checker as a library definition, not
undefined globals. Features newer than the declared version are never used.

## Gates

- **Type check:** a language server's diagnostics run as a batch check over the committed configuration, with the type
  and strictness groups raised to error and the weak nil and union checks off. Example: LuaLS with a `.luarc.json` and
  `--check` at warning level ([settings](https://luals.github.io/wiki/settings/)).
- **Format:** one formatter in check mode. Example: `stylua --check`.
- **Lint:** a linter over committed configuration. Example: selene or luacheck.

Findings fail at the [Lint Strictness](../checks/lint-strictness.md) threshold, and each diagnostic disabled in place
carries its reason.

## Type and Boundary Safety

Language-server annotations are Lua's static types under
[Type and Boundary Safety](../code/type-and-boundary-safety.md):

- Every exported function annotates its parameters and returns; a fixed-shape table is a declared class.
- `any` is never written in an annotation; unknown data is checked with `type()` before use.
- A cast annotation is a waiver with its reason.
- Annotations are not checked at runtime, so a value from outside the program (a decoded file, host callback argument,
  or user input) is checked for type and shape where it arrives.

## Language Defaults

- Every variable and function is `local`. A global is created only deliberately, declared where the runtime supports it
  ([manual](https://www.lua.org/manual/5.5/manual.html#2.2)); otherwise the linter flags it.
- A module returns one table and never writes to the global environment.
- The length operator is used only on a sequence; a table that may hold `nil` gaps tracks its own count
  ([length operator](https://www.lua.org/manual/5.5/manual.html#3.4.7)).
- Where the runtime supports them, a binding that must not change is `<const>`, and a resource that must be released is
  `<close>`.

## Failures

An expected failure returns `nil` and an error value, as the standard library does, and every caller checks it. `error`
is raised for programmer errors and broken invariants, with a message or error table naming what failed. A boundary that
must survive a failure catches it with `pcall` or `xpcall` and handles or reports it; a caught error is never discarded
([Programming in Lua](https://www.lua.org/pil/8.4.html)).

## Tests

Tests follow [Test Boundaries and Gates](../testing/test-boundaries-and-gates.md), with the host API injected so domain
logic runs under unit tests outside the host. Host-only code is tested through the host where possible; an omission
states its reason. Example: busted.

Lua coverage counts lines, not branches, so no branch figure is claimed. Code the instrument cannot reach inside a host
moves behind the injected host API until a unit test reaches it, never exempted, per
[Exclusions](../testing/meaningful-coverage/001-exclusions-and-exemptions.md). Example: LuaCov. Any floor above the
minimum is recorded under [Layers and Adapters](../testing/behaviour-driven-development/002-layers-and-adapters.md).

## Hermetic Unit Tests

Two mechanisms ban impure access in unit specs. The linter removes `io` and `os` for unit-spec paths, so each use is an
undefined-global finding; example: a luacheck `files` override with `not_globals`. The unit-spec helper replaces
`require` so loading a network or process module, such as `socket`, fails the spec, and replaces the host's process and
file APIs, such as Neovim's `vim.fn.system` and `vim.uv`, with failing stubs.

## Documentation

An exported function's annotations are its reference documentation, describing its behaviour and each failure it
returns, and are updated with observable behaviour per
[Specification Maintenance](../evidence/specification-maintenance.md).

## Adopter Decisions

Record the declared runtime, host library definitions, and linter in the repository adapter
[Stack Packs](../../../conventions/structure/stack-packs.md) defines.

## Enforcement

The adopter's own pull-request gate runs the language server, formatter, and linter gates. Review applies boundary
checks, the failure convention, and the runtime-version rule.
