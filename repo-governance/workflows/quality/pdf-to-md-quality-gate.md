---
name: pdf-to-md-quality-gate
description: >-
  Judges a Markdown conversion, or one section of a large one, for fidelity to its source PDF in at most three bounded
  cycles, and returns one advisory verdict.
when_to_use: >-
  Use when someone explicitly asks for a fidelity review of a converted PDF, after a conversion is written or edited, or
  before the Markdown is relied on in place of its source.
---

# PDF to Markdown Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md) (read-only checker,
frozen ledger, one separate writer, at most three cycles, advisory verdict) and states only what is specific to PDF
conversions, where the PDF is the truth and the Markdown its copy.

## Entry

The gate starts only on an explicit request naming it; no workflow calls it. The conversion already exists, made
beforehand by `pdf-to-md-maker`; the gate never converts.

## Inputs

| Input        | Type    | Values                                                             | Default  |
| ------------ | ------- | ------------------------------------------------------------------ | -------- |
| `subject`    | string  | A source PDF and its Markdown, optionally narrowed to a page range | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all`                                   | `normal` |
| `max-cycles` | integer | 1, 2, or 3                                                         | 3        |

A page range covers that range and its Markdown span, so a large conversion is judged by section. Another `max-cycles`
value or a missing subject refuses to start.

Tool commands come from the adopter's adapter at `repo-governance/development/quality/gate-adapters/pdf-to-md.md`:
commands for extraction, character recognition, per-dimension comparison, and diagram parsing; the recognized-page
marker; any numeric recognition error-rate thresholds; the repair count above which a repair is uncertain; and the
fallback for a source too large to compare exhaustively. Without an adapter, the `converting-pdf-to-markdown` skill's
judgement applies.

## Deterministic Boundary

The checker reports none of these; entry and exit checks run their owners instead.

| Property                                     | Owned by                 | This catalog runs               |
| -------------------------------------------- | ------------------------ | ------------------------------- |
| Markdown formatting and lint                 | the formatter and linter | `prettier`, `markdownlint-cli2` |
| File names                                   | the file-name validator  | none                            |
| Diagram accessibility, palette, label length | the diagram validator    | none                            |

An adopter replaces the last column with its declared gate's tools. Fidelity is never delegated: no generic check reads
the PDF. Whether a diagram parses is judged unless the declared gate parses diagrams.

## Cycle

Each cycle is one full audit by `pdf-to-md-checker`, loading the `converting-pdf-to-markdown` skill, and one repair by
[PDF to Markdown Propagation](pdf-to-md-propagation.md), run by `pdf-to-md-fixer`, per
[Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md).

The checker extracts the source afresh, never reusing the conversion's intermediate output, and judges the skill's seven
dimensions separately: text completeness, text accuracy, heading levels, nesting depth, structure (reading order and
tables), figure coverage, and technical validity (diagrams and recognized pages). It rates each gap with the skill's
conversion table, where a missing section, page, or table is `CRITICAL`.

Verbatim permits only whitespace normalization. Heading depth follows section numbering before font size. An ambiguous
figure stays a placeholder, never a guessed diagram. Every recognized page is marked. An unextractable page is reported
as not checked, never as matching.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged. This gate adds no row.

## Verdict

| Verdict              | The caller                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                   |
| `PASS_WITH_FINDINGS` | records the verdict and the open non-blocking rows, and continues                   |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, or issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, or unavailable), then acts as for `FAIL` |

No verdict stops the caller, and a verdict covers only what was compared.

## Ledger

`local-tmp/quality/pdf-to-md/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, with the columns and closing verdict block in
[the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger). Each row
names its source page, Markdown location, and dimension. The verdict block also records page coverage; table, figure,
and diagram counts; and each dimension sampled rather than checked exhaustively, with its pages. The ledger is never
committed.

## Example Usage

```text
Run pdf-to-md-quality-gate on standards/framework.pdf and its Markdown, pages 120-180, mode strict.
```

## Related Workflows

- [Docs Quality Gate](docs-quality-gate.md) judges reader-facing documents, not copies of a source.
