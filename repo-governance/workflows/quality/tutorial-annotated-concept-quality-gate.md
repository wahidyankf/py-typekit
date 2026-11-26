---
name: tutorial-annotated-concept-quality-gate
description: >-
  Judges one annotated-concept tutorial's mode, worked examples, and diagrams, with adapter thresholds, in at most three
  cycles.
when_to_use: >-
  Use when someone explicitly asks to review an annotated-concept tutorial, after writing or restructuring one, or
  before publishing it.
---

# Tutorial Annotated Concept Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md): a read-only checker,
a frozen ledger, one separate writer, at most three cycles, and an advisory verdict. This file states only what is
specific to annotated-concept tutorials: worked examples clustered by theme, in standard mode (examples may carry code)
or no-code mode (scenarios and decision artifacts).

## Entry

The gate starts only on an explicit request naming it; no workflow calls it. No cycle waits for a person: editorial
review sits before cycle 1 or after the verdict, per
[Human Review](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#human-review).

## Inputs

| Input        | Type    | Values                               | Default  |
| ------------ | ------- | ------------------------------------ | -------- |
| `subject`    | string  | One tutorial's folder, with any code | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all`     | `normal` |
| `max-cycles` | integer | 1, 2, or 3                           | 3        |

Any other `max-cycles` value, or a missing subject, refuses to start. The tutorial's own mode is read from the subject.

Product thresholds live only in the adopter's adapter at
`repo-governance/development/quality/gate-adapters/<product>.md`: how a topic declares its mode, each mode's
worked-example floor, the density band, part lengths, where runnable code lives, the layout, and the front matter. A
count is a floor, never a cap. Without an adapter, only the generic rules apply.

## Deterministic Boundary

The checker reports none of these; entry and exit checks run their owners.

| Property                                     | Owned by             | This catalog runs |
| -------------------------------------------- | -------------------- | ----------------- |
| Markdown formatting and lint                 | formatter and linter | none              |
| File names                                   | file-name validator  | none              |
| Diagram rendering, label length, and palette | diagram validator    | none              |
| Example code compiles and runs               | example test suite   | none              |

The catalog publishes no tutorial; an adopter fills the last column with its declared gate's tools. A property no
adopter tool owns leaves the table and becomes judgeable.

## Cycle

Each cycle is one full audit by `tutorial-annotated-concept-checker` and one repair by
[Tutorial Annotated Concept Propagation](tutorial-annotated-concept-propagation.md), run by
`tutorial-annotated-concept-fixer`, per
[Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md). The audit
reads the declared mode first; every later question branches on it:

- the mode holds: a no-code tutorial contains no code block, a `CRITICAL` finding when broken;
- each worked example carries context on why the concept matters, a fitting medium (code, pseudocode, configuration, or
  diagram), a key takeaway, and any part the adapter adds;
- each code-bearing example is self-contained and runs as printed, with every import present;
- annotation density (comment lines over code lines per code-bearing example) falls within the adapter's band;
- in no-code mode, each decision artifact spells out its reasoning, not just its conclusion;
- worked examples cluster by theme, with sound names and a rise from simple to real-world;
- a diagram appears only where a visual relationship materially aids understanding; and
- the worked-example count meets the adapter's floor for the tutorial's mode.

Prose, facts, and links belong to [Content Quality Gate](content-quality-gate.md). Medium fit, clustering, progression,
and decision-artifact quality are judgement rows.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged; this gate adds no row.

## Verdict

| Verdict              | The caller                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                   |
| `PASS_WITH_FINDINGS` | records the verdict and open non-blocking rows, continues                           |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, or issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, or unavailable), then acts as for `FAIL` |

No verdict stops the caller or authorizes publishing.

## Ledger

`local-tmp/quality/tutorial-annotated-concept/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, with the columns and closing verdict
block in [the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger).
The verdict block records the mode read. It is never committed.

## Example Usage

```text
Run tutorial-annotated-concept-quality-gate on learn/team-leadership.
```

## Related Workflows

- [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md) judges the example-first kind.
