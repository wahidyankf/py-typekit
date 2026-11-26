---
name: tutorial-primer-quality-gate
description: >-
  Judges one primer, a tutorial scoped to just enough of a subject for its dependent topics, against its scope,
  capstone, and example rules, with adapter-supplied product thresholds, in at most three bounded cycles.
when_to_use: >-
  Use when someone explicitly asks to review a primer, after writing or restructuring one, or before publishing it.
---

# Tutorial Primer Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md): a read-only checker,
a frozen ledger, one separate writer, at most three cycles, and an advisory verdict. This file adds only what is
primer-specific. A primer teaches just enough of a subject for the topics that depend on it, and promises that stated
scope, not whole-subject coverage.

## Entry

The gate starts only on an explicit request naming it; no workflow calls it. No cycle waits for a person: editorial
review sits before cycle 1 or after the verdict, per
[Human Review](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#human-review).

## Inputs

| Input        | Type    | Values                                          | Default  |
| ------------ | ------- | ----------------------------------------------- | -------- |
| `subject`    | string  | One primer's folder, capstone and code included | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all`                | `normal` |
| `max-cycles` | integer | 1, 2, or 3                                      | 3        |

Any other `max-cycles` value, or a missing subject, refuses to start.

Product thresholds come from the adopter's adapter at `repo-governance/development/quality/gate-adapters/<product>.md`.
Here it holds the example count floor, annotation density band, example part lengths, file layout, and front matter. A
count is a floor, never a cap. Each threshold lives only there. Without an adapter, only the generic rules apply.

## Deterministic Boundary

The checker reports none of these; the entry and exit checks run their owners.

| Property                                     | Owned by                 | This catalog runs |
| -------------------------------------------- | ------------------------ | ----------------- |
| Markdown formatting and lint                 | the formatter and linter | none              |
| File names                                   | the file-name validator  | none              |
| Diagram rendering, label length, and palette | the diagram validator    | none              |
| Example code compiles and runs               | the example test suite   | none              |

The catalog publishes no tutorial, so an adopter fills the last column with its declared gate's tools. A property none
of its tools owns leaves the table and becomes judgeable.

## Cycle

Each cycle is one full audit by `tutorial-primer-checker`, loading the `creating-by-example-tutorials` skill, and one
repair by [Tutorial Primer Propagation](tutorial-primer-propagation.md), run by `tutorial-primer-fixer`, per
[Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md). The audit
asks whether:

- the primer's overview states its "just enough" scope and its dependent topics; a missing scope statement is
  `CRITICAL`, since nothing else can be judged without it;
- every example serves that stated scope; drift toward comprehensive coverage is scope creep, while an example a stated
  dependent topic needs is not;
- the capstone is a light exercise consolidating the scoped features, not a full project;
- each example meets the per-example rules of the
  [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md#cycle): its parts, self-containment, on-line
  annotations, and density within the adapter's band, measured per example;
- examples are grouped by theme, with a sound rise in complexity; and
- the example count meets the adapter's floor.

The primer declares one type from [Tutorial Types](../../conventions/writing/tutorial-types.md). Prose, facts, and links
belong to the [Content Quality Gate](content-quality-gate.md). Scope-creep calls, capstone scale, grouping, and
progression are judgement rows.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged, with no added row.

## Verdict

| Verdict              | The caller                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                   |
| `PASS_WITH_FINDINGS` | records the verdict and open non-blocking rows, continues                           |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, or issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, or unavailable), then acts as for `FAIL` |

No verdict stops the caller or authorizes publishing.

## Ledger

`local-tmp/quality/tutorial-primer/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, with the columns and closing verdict block in
[the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger). It is
never committed.

## Example Usage

```text
Run tutorial-primer-quality-gate on the primer folder learn/just-enough-sql.
```

## Related Workflows

- [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md) owns the per-example rules a primer reuses.
