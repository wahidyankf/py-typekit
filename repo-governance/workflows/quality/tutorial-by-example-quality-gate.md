---
name: tutorial-by-example-quality-gate
description: >-
  Judges one By Example tutorial's examples, annotations, and progression, with product thresholds from an adapter, in
  at most three bounded cycles, and returns one advisory verdict.
when_to_use: >-
  Use when someone explicitly asks to review a By Example tutorial, after writing or restructuring one, or before
  publishing it.
---

# Tutorial By Example Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md): a read-only checker,
a frozen ledger, one separate writer, at most three cycles, an advisory verdict. Only what is specific to By Example
tutorials, per [Tutorial Types](../../conventions/writing/tutorial-types.md), is stated here.

## Entry

It starts only on an explicit request naming it; no workflow calls it. No cycle waits for a person: editorial review
sits before cycle 1 or after the verdict, per
[Human Review](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#human-review).

## Inputs

| Input        | Type    | Values                                       | Default  |
| ------------ | ------- | -------------------------------------------- | -------- |
| `subject`    | string  | One tutorial's folder, with its example code | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all`             | `normal` |
| `max-cycles` | integer | 1, 2, or 3                                   | 3        |

Another `max-cycles` value or a missing subject refuses to start.

Product thresholds come from the adopter's adapter at `repo-governance/development/quality/gate-adapters/<product>.md`:
here the example count, annotation density, and diagram count bands, each example part's length, any added part, the
annotation notation, the file layout, and the front matter. Each threshold lives only there; without an adapter, only
the generic rules apply.

## Deterministic Boundary

The checker reports none of these; the entry and exit checks run their owners.

| Property                                     | Owned by                 | This catalog runs |
| -------------------------------------------- | ------------------------ | ----------------- |
| Markdown formatting and lint                 | the formatter and linter | none              |
| File names                                   | the file-name validator  | none              |
| Diagram rendering, label length, and palette | the diagram validator    | none              |
| Example code compiles and runs               | the example test suite   | none              |

The catalog publishes no tutorial, so an adopter fills the last column with its declared gate's tools; a property with
no tool of its own leaves the table, becoming judgeable.

## Cycle

Each cycle is one full audit by `tutorial-by-example-checker`, loading the `creating-by-example-tutorials` skill, and
one repair by [Tutorial By Example Propagation](tutorial-by-example-propagation.md), run by `tutorial-by-example-fixer`,
per [Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md). The
audit asks of each example whether:

- it carries the parts
  [Cookbook and By Example](../../conventions/writing/tutorial-structure/002-cookbook-and-by-example.md) fixes, plus any
  the adapter adds; a missing part is a finding;
- it teaches one concept and is self-contained, running as printed with every other example removed and every import and
  helper present;
- its annotations sit on code lines, show values, intermediate states, and output, and say what a reader needs;
- its annotation density (comment lines over code lines), measured per example, never across the tutorial, is within the
  adapter's band;
- built-in features precede any dependency, and a dependency states what built-ins could not do; and
- its key takeaway states the lesson, not a code summary, and a comparison gives each approach its own block.

Across the tutorial: are examples numbered in sequence, grouped coherently with core features first per level, rising
soundly in complexity, and within the adapter's count bands?

Prose, facts, and links belong to [Content Quality Gate](content-quality-gate.md). Grouping, progression, and annotation
quality are judgement rows.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged, with no added row.

## Verdict

| Verdict              | The caller                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                   |
| `PASS_WITH_FINDINGS` | records the verdict and the open non-blocking rows, and continues                   |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, or issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, or unavailable), then acts as for `FAIL` |

No verdict stops the caller or authorizes publishing.

## Ledger

`local-tmp/quality/tutorial-by-example/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, with the columns and closing verdict block
in [the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger); each
row names its example. It is never committed.

## Example Usage

```text
Run tutorial-by-example-quality-gate on learn/golang/by-example.
```

## Related Workflows

- [Tutorial Primer Quality Gate](tutorial-primer-quality-gate.md) reuses these per-example rules.
