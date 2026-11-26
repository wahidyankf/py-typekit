---
description: >-
  Sets the bounded sequence every quality gate runs, from freezing the subject to the exit check, and the termination
  table that maps each ending to exactly one verdict.
when_to_use: >-
  Use when running a quality gate, when deciding whether another cycle may start, or when a run has to end.
---

# Sequence and Termination

## Sequence

One cycle is one full audit followed by one repair. Every arrow back to an earlier step is bounded by the cycle counter
`k`.

```mermaid
flowchart TD
    accTitle: Quality gate sequence
    accDescr: An entry check, a root-cause pre-step when it is red, a bounded audit and repair loop, an exit check, and one verdict.
    classDef default fill:#CA9161,stroke:#000000,color:#000000,stroke-width:2px
    Freeze["Freeze subject<br/>revision plus scope"] --> Entry["Entry tooling run"]
    Entry -- red --> Root["Root-cause pre-step<br/>at most 3 attempts,<br/>outside the cycle budget"]
    Entry -- green --> K1["k = 1"]
    Root -- green --> K1
    Root -- still red --> Blocked["BLOCKED<br/>tooling"]
    K1 --> Audit["Full audit<br/>by the checker"]
    Audit -- no open blocking row --> Early["Verdict per step 5"]
    Audit -- blocking rows --> Ledger["Freeze ledger L_k"]
    Ledger --> Prop["Family propagation<br/>run by the fixer,<br/>repairs only L_k rows<br/>and verifies each row"]
    Prop --> Progress{"Blocking count did not fall<br/>since the previous audit?"}
    Progress -- yes --> NoProgress["FAIL<br/>no progress"]
    Progress -- no --> Ceiling{"k equals max-cycles?"}
    Ceiling -- no --> Next["k = k + 1"]
    Next --> Audit
    Ceiling -- yes --> Exit["Exit tooling run<br/>and per-row verification"]
    Exit --> Final["PASS, PASS_WITH_FINDINGS,<br/>or FAIL"]
```

1. **Freeze the subject.** Record the revision with any uncommitted paths, its commit identifier when one exists, and
   the exact scope. A subject changed during the run by anything other than this run's own writer ends it `BLOCKED`
   (input-changed), and the ledger is kept.
2. **Run the entry check.** Green continues. Red starts the root-cause pre-step in
   [Inputs, Scoring, and the Deterministic Boundary](001-inputs-scoring-and-boundary.md).
3. **Audit.** The checker audits the whole frozen scope in its current state, rates each finding's criticality, and
   reports nothing the Deterministic Boundary table excludes.
4. **Classify.** Each row is blocking or not under the mode threshold.
5. **Terminate early** when no blocking row is open, because the writer has nothing left to repair. The verdict is
   `FAIL` when a blocking row is `not-resolved` or `needs-decision`; otherwise it is `PASS` if the ledger holds no open
   row at all, and `PASS_WITH_FINDINGS` if it does.
6. **Hand off.** Freeze the open blocking rows as ledger `L_k` and run `<family>-propagation`. It re-validates and rates
   each row, repairs only rows of `L_k`, verifies each, and records its status with evidence, per
   [Sole-Writer Propagation](../sole-writer-propagation.md).
7. **Require progress.** From the second audit on, the open blocking count must be strictly lower than at the previous
   audit. Otherwise the run ends `FAIL` (no progress).
8. **Stop at the ceiling.** When `k` equals `max-cycles`, no further audit runs; a fourth audit is never reached. The
   exit check runs once. The writer reverts a repair that turned it red and marks that row `not-resolved`. The run ends
   `PASS` or `PASS_WITH_FINDINGS` when every blocking row is closed, `resolved` with evidence or `not-applicable`, and
   the exit check is green, and `FAIL` otherwise.

A blocking row left `not-resolved`, by a reverted repair or by a family's deferral, stays blocking: it ends the run
`FAIL` whether the run stops early or at the ceiling, and the verdict reports it.

At the ceiling, verified repairs stay. Nothing asks a person mid-run whether to continue, and nothing adds a cycle.

## Termination

| Condition                                                                    | Verdict                        |
| ---------------------------------------------------------------------------- | ------------------------------ |
| An audit has no open row, and no blocking row is `not-resolved`              | `PASS`                         |
| An audit has open rows, none blocking, and no blocking row is `not-resolved` | `PASS_WITH_FINDINGS`           |
| After the final repair: every blocking row closed, exit run green            | `PASS` or `PASS_WITH_FINDINGS` |
| A blocking row is `not-resolved` or `needs-decision`, or open at the ceiling | `FAIL`                         |
| The open blocking count did not fall between two audits                      | `FAIL`                         |
| Entry tooling still red after 3 root-cause attempts                          | `BLOCKED` (tooling)            |
| The subject changed during the run                                           | `BLOCKED` (input-changed)      |
| The checker or the propagation could not run                                 | `BLOCKED` (unavailable)        |
| `max-cycles` is outside 1–3, or `subject` is missing                         | Refuses to start               |

Every run reaches exactly one row of this table. A gate file copies the table unchanged into its `## Termination`
section or links it, and adds no row of its own.
