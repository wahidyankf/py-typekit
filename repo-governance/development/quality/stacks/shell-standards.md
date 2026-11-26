---
description: >-
  Fixes the shell baseline beyond script mechanics: an analysable dialect or a named fallback, analyser and formatter
  gates, strict-mode gaps closed, quoted and validated input, small scripts, and behaviour tests without coverage.
when_to_use: >-
  Use when creating, configuring, reviewing, or testing a shell script, choosing its dialect, or deciding whether logic
  has outgrown shell.
---

# Shell Standards

This standard is canonical for shell as a stack. It inherits [Shell Scripts](../code/shell-scripts.md), which owns the
declared interpreter, strict mode, executable bit, comments, JSON parsing, and output inspection, adding only the
choices a shell stack leaves open. A shell programming skill defers to both.

It implements [Fail Closed](../../../principles/fail-closed.md),
[Simplicity Over Complexity](../../../principles/simplicity-over-complexity.md), and
[Automation Over Manual](../../../principles/automation-over-manual.md).

## Gates

- **Static analysis:** every script is analysed at the [Lint Strictness](../checks/lint-strictness.md) threshold, each
  check-disabling directive carrying its reason. Example: ShellCheck.
- **Format:** one formatter in diff mode over committed settings, failing on any change. Example: `shfmt -d`.
- **Unsupported dialect:** a script the analyser cannot read passes the shell's own syntax check instead, and review
  carries what analysis would have caught. Example: ShellCheck reads sh, Bash, dash, and ksh but not Zsh
  ([SC1071](https://www.shellcheck.net/wiki/SC1071)), so a Zsh script runs `zsh -n`.

A repository script uses an analysable dialect unless the script exists to configure a shell that is not one.

## Strict Mode Has Gaps

Exit-on-error does not apply inside a condition, left of `&&` or `||`, or in a command substitution unless the shell
inherits it, and `local x="$(cmd)"` reports the status of `local`, not `cmd`
([BashFAQ 105](https://mywiki.wooledge.org/BashFAQ/105)). So:

- a function whose failure matters is not called only as a condition;
- a declaration and an assignment from a command substitution are separate statements; and
- a Bash script relying on substitutions failing sets `shopt -s inherit_errexit`.

A Zsh script's strict mode is `ERR_EXIT`, `PIPE_FAIL`, and `NO_UNSET`
([options](https://zsh.sourceforge.io/Doc/Release/Options.html)).

## Type and Boundary Safety

Shell has no types, so [Type and Boundary Safety](../code/type-and-boundary-safety.md) maps to discipline at input:

- Every expansion is quoted, as `"${var}"`, and a list is an array, never a space-separated string.
- Arguments are checked for count and shape before use, and an operand taken from input follows `--`.
- `eval` and unquoted command construction are never used.
- In Bash, tests use `[[ ]]` and substitutions use `$( )`.

## Keep Scripts Small

Shell orchestrates commands; domain logic lives elsewhere. A script needing data structures beyond arrays or arithmetic
beyond counters, or growing past roughly a hundred lines, moves its logic to a language with types and a unit layer
([Shell Style Guide](https://google.github.io/styleguide/shellguide.html)). Within a script:

- variables inside functions are `local`; and
- a script longer than a few commands defines functions and ends in `main "$@"`.

## Tests

An integration shell test runs the script as callers do and asserts exit status, output, and effects. Each is isolated
per [Git Fixture Isolation](../testing/git-fixture-isolation.md) and
[Test Data Isolation](../testing/test-data-isolation.md), and is classified by the boundary it touches under
[Test Boundaries and Gates](../testing/test-boundaries-and-gates.md). Example: bats-core.

Shell coverage is never a gate: available instruments report unreliably for shell
([kcov](https://raw.githubusercontent.com/SimonKagstrom/kcov/master/doc/kcov.1)), so no floor or surrogate figure is
recorded, per [Meaningful Coverage](../testing/meaningful-coverage.md). Behaviour tests over every documented exit path
carry the evidence.

## Hermetic Unit Tests

Shell has no process-free seam, so a unit test sources the script's functions, its `main` call guarded to skip when
sourced, and calls them in the test's shell. Every command a function runs is stubbed, with `PATH` set to a directory of
stubs so an unstubbed command fails with status 127, and every path is injected as text. Logic that cannot be tested
this way moves to a stack with a seam.

## Documentation

A script's header comment states its purpose, as Shell Scripts requires. Its exit statuses and streams follow
[Command-Line Interface](../../../conventions/structure/command-line-interface.md) at the tier the adopter records, and
a script at the full bar documents usage through help.

## Adopter Decisions

| Decision  | Option                           | Gains                                    | Costs                                    |
| --------- | -------------------------------- | ---------------------------------------- | ---------------------------------------- |
| test tool | a shell test framework           | tests read as the shell they exercise    | a dependency to pin                      |
|           | the repository's main test stack | one runner and one report for every test | each test spawns the script as a process |

Record the choice in the repository adapter [Stack Packs](../../../conventions/structure/stack-packs.md) defines.

## Enforcement

The analyser, formatter, and syntax check enforce the gates in the adopter's pull-request gate; review applies quoting,
input checks, strict-mode gaps, and script size.
