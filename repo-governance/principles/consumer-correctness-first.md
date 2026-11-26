---
description: >-
  States that when options differ, the one that most helps the consumer be correct wins: descriptive errors, exact
  names, and no silent behaviour.
when_to_use: >-
  Use when choosing between a terse surface and a descriptive one, when naming anything a consumer reads or types, or
  when deciding what a failure reports.
---

# Consumer Correctness First

When options differ, choose the one that most helps the consumer be correct. A consumer cannot read maintainer intent;
ambiguity becomes misuse, and misuse becomes incidents. A descriptive surface fails loudly at the point of error, where
it can still be fixed.

## What It Requires

- **Descriptive errors.** A failure names its cause and the fix, so the consumer acts instead of guessing. Where the
  convention fixes the shape, the diagnosis states what is wrong and the advice follows where it is clearly advice — see
  [Errors and Diagnostics](../conventions/structure/command-line-interface-details/006-errors-and-diagnostics.md).
- **Exact names across surfaces.** A thing a consumer reads, types, or branches on carries one exact name everywhere it
  appears: flags, keys, outputs, and documents match, so nothing depends on recognizing a paraphrase.
- **No silent behaviour.** Nothing fails in a way that looks like success, and nothing succeeds in a way that hides what
  happened. An absence the contract leaves undefined is a missing input, and the tool refuses — see
  [Fail Closed](fail-closed.md) and [Consumer Independence](consumer-independence.md).

## The Tie It Breaks

A terse or ambiguous surface that lets misuse pass quietly is the wrong choice even when it is shorter. Brevity that
removes the cause, the fix, or the exact name does not save the consumer time; it moves the cost to diagnosis, where it
is paid with interest.

This does not overrule its siblings. What is written down is governed by
[Explicit Over Implicit](explicit-over-implicit.md); what a control does when it cannot decide is governed by
[Fail Closed](fail-closed.md); whose answer a value is, by [Consumer Independence](consumer-independence.md). This
principle decides only the tie: among options that satisfy those, the most consumer-correct one wins.

## The Cost Is Verbosity

Longer messages, fuller names, and explicit refusals are more text. The text is the cheapest place for the meaning to
live, because every later place — a log search, a support thread, an incident review — is more expensive.

## Where It Is Already Load-Bearing

| Applied in                                                                                                      | As                                                               |
| --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| [Errors and Diagnostics](../conventions/structure/command-line-interface-details/006-errors-and-diagnostics.md) | a diagnostic locates the problem and never carries a secret      |
| [Command-Line Interface](../conventions/structure/command-line-interface.md)                                    | the machine-readable body says exactly what happened             |
| [File Naming](../conventions/structure/file-naming.md)                                                          | one lowercase kebab-case name, never two names one case apart    |
| [Fail Closed](fail-closed.md)                                                                                   | a control that cannot decide refuses rather than passing quietly |

## Enforcement

Judged at review, by decision. No mechanical check can tell whether an error names its cause or whether a name matches
across surfaces; reviewers confirm it, as with any judgement this catalog leaves to review.
