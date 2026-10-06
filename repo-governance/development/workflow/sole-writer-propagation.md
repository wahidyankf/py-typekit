---
description: >-
  Gives each quality-gate family exactly one writer, `<family>-propagation`, run by its repairer agent, and sets the
  eight rules that keep its repairs confined to a frozen ledger, idempotent, and non-recursive.
when_to_use: >-
  Use when writing or adopting a `<family>-propagation` workflow, when a gate hands over a frozen ledger, or when
  deciding whether a repair may touch something its finding did not name.
---

# Sole-Writer Propagation

Each quality-gate family has exactly one writer: the workflow `<family>-propagation`, executed by the family's repairer
agent, `<family>-fixer` unless the repository's gate entry declares another. The gate and its checker judge and never
write, per the [Quality Gate Contract](quality-gate-contract.md). This document holds the rules every writer shares;
each family file states only what differs.

This standard implements [One Source Per Fact](../../principles/one-source-per-fact.md) and
[Minimal Sufficiency](../../principles/minimal-sufficiency.md).

## Why One Writer

A single writer bound to a frozen ledger lets three cycles suffice:

- **The input is fixed.** The writer receives a frozen ledger and may touch only what its rows require, so a repair
  cannot grow into a "while I'm here" edit the next audit reports as a new finding; nitpicks do not cascade.
- **It is idempotent.** The same ledger on the same state produces the same change; rerunning on a repaired state
  changes nothing, so the open count can only fall.
- **Judging and writing stay separate.** The checker never writes, so each audit after a repair is independent of it.

## Shared Rules

1. **Entry.** A propagation runs with a frozen ledger, handed over by its gate or an explicit request naming the rows.
   It keeps any automatic trigger its repository already gives it, such as before a rule change or a
   documentation-changing commit.
2. **Re-validate first.** Before editing, the fixer re-reads each row against the current state and rates confidence per
   [Finding Criticality and Confidence](../quality/evidence/finding-criticality-and-confidence.md). A row that no longer
   holds is `not-applicable`, with evidence. A row whose correct repair is a judgement the ledger does not settle is
   `needs-decision`; the writer does not guess.
3. **Edit only for the row.** Each change traces to one row ID; no formatting sweep, rename, or refactor exceeds what
   the row requires.
4. **Verify each row.** After its edit, the writer proves the row closed with the narrowest sufficient check and records
   the evidence.
5. **Idempotency.** Before editing, the writer checks whether the row's target state already holds; if so, the row is
   `resolved` with no edit.
6. **No recursion.** A propagation never starts its own gate or another propagation; the caller decides whether to audit
   again, keeping the call graph acyclic.
7. **No delivery.** A propagation never commits, pushes, or opens a pull request; its caller owns delivery. One named
   exception: `pr-review-propagation` commits each repair to the reviewed change's own branch and pushes only that
   branch.
8. **Revert on red exit.** When the gate's exit tooling run turns red, the writer reverts the causing repairs and marks
   those rows `not-resolved`.

Each row ends `resolved`, `not-resolved`, `not-applicable`, or `needs-decision`, with evidence. An unreached row stays
`open`, and the gate counts it.

## Family File Shape

A `<family>-propagation.md` workflow carries these headings in this order; a repository's declared structural check for
propagations enforces their presence.

| Heading               | Holds                                                                |
| --------------------- | -------------------------------------------------------------------- |
| `## Contract`         | One line linking this shared propagation contract                    |
| `## Scope`            | The paths this writer may edit for the family                        |
| `## Executor`         | The repairer agent, plus any family skill it loads                   |
| `## Row Verification` | How a row is proven closed for this family                           |
| `## Family Rules`     | Rules only this family needs, such as a rule-change idempotency gate |

The family file never restates a shared rule; it may narrow one, such as shrinking its scope, but never loosens it.

## Executor Naming

In every family the writer is `<family>-propagation`, and its executor is the repairer agent: `<family>-fixer`, or the
agent the repository's gate entry declares. A maker authors; a fixer repairs only ledger rows. One agent never holds
both roles in the same gate run.

## Existing Writers Keep Their Rules

Where a family's propagation already holds stricter writer rules, such as an idempotency gate separating a real rule
change from a non-normative edit, its family file keeps them under `## Family Rules`. Adopting this contract removes
nothing such a writer does today.
