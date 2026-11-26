---
name: tutorial-in-the-field-quality-gate
description: >-
  Judges one in-the-field guide against its scenario, built-in-first, and production-code rules, with product thresholds
  from an adapter, in at most three bounded cycles, and returns one advisory verdict.
when_to_use: >-
  Use on an explicit request to review an in-the-field guide, after writing or restructuring one, or before publishing
  it.
---

# Tutorial In the Field Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md) and states only what
is specific to in-the-field guides, which teach production practice inside one working scenario.

## Entry

The gate starts only on an explicit request naming it; no workflow calls it. No cycle waits for a person: editorial
review sits before cycle 1 or after the verdict, per
[Human Review](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#human-review).

## Inputs

| Input        | Type    | Values                                         | Default  |
| ------------ | ------- | ---------------------------------------------- | -------- |
| `subject`    | string  | One guide set's folder, or listed guides in it | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all`               | `normal` |
| `max-cycles` | integer | 1, 2, or 3                                     | 3        |

Any other `max-cycles` value, or a missing subject, refuses to start.

Product thresholds come from the adopting repository's adapter at
`repo-governance/development/quality/gate-adapters/<product>.md`. For this kind it holds the guide count, annotation
density, and diagram count bands, the file layout, and the front matter. Each threshold lives only there; without an
adapter, only the generic rules apply.

## Deterministic Boundary

The checker reports none of these; the entry and exit checks run their owners.

| Property                                     | Owned by             | This catalog runs |
| -------------------------------------------- | -------------------- | ----------------- |
| Markdown formatting and lint                 | formatter and linter | none              |
| File names                                   | file-name validator  | none              |
| Diagram rendering, label length, and palette | diagram validator    | none              |
| Guide code compiles and runs                 | example test suite   | none              |

The catalog publishes no tutorial, so an adopter fills the last column with its declared gate's tools. A property it has
no tool for leaves the table and becomes judgeable.

## Cycle

Each cycle is one full audit by `tutorial-in-the-field-checker`, loading the `creating-in-the-field-tutorials` skill,
and one repair by [Tutorial In the Field Propagation](tutorial-in-the-field-propagation.md), run by
`tutorial-in-the-field-fixer`, per
[Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md). The audit
asks whether each guide:

- declares one type from [Tutorial Types](../../conventions/writing/tutorial-types.md) and keeps one recognizable
  scenario throughout, each step giving the exact action and its output, with checkpoints and recovery notes where the
  scenario fails in practice;
- puts the built-in approach first: a framework or library shown before the language's or platform's own approach is
  `CRITICAL`;
- justifies every framework by the built-in approach's limits, shown before it arrives, with a trade-off section saying
  when the simpler approach still suffices;
- has production-complete code: errors handled, resources released on every path, configuration from the environment,
  not hardcoded, and no credential anywhere;
- teaches a production pattern fitting the scenario's context;
- has diagrams that each help a reader follow the scenario; and
- keeps annotation density (comment lines over code lines per code block) within the adapter's band.

Of the whole set, it asks whether guide and diagram counts fall within the adapter's bands.

Prose, facts, and links belong to the [Content Quality Gate](content-quality-gate.md). Trade-off depth, justification
quality, pattern fit, and diagram usefulness are judgement rows.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged. This gate adds no row.

## Verdict

| Verdict              | The caller                                                                       |
| -------------------- | -------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                |
| `PASS_WITH_FINDINGS` | records the verdict and the open non-blocking rows, and continues                |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, unavailable), then acts as for `FAIL` |

No verdict stops the caller or authorizes publishing.

## Ledger

`local-tmp/quality/tutorial-in-the-field/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, never committed, with the columns and
closing verdict block in
[the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger).

## Example Usage

```text
Run tutorial-in-the-field-quality-gate on the guide folder learn/golang/in-the-field with mode strict.
```

## Related Workflows

- [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md) judges the example-first kind.
