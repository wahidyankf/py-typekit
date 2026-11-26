---
name: content-quality-gate
description: >-
  Judges published content for clear writing, accessible structure, true facts, working links, and its adapter's product
  rules in at most three cycles, returning one advisory verdict.
when_to_use: >-
  Use when someone explicitly asks to review published content, such as a site's articles or learning pages, before
  publishing a batch or to sweep a content tree.
---

# Content Quality Gate

This gate follows the [Quality Gate Contract](../../development/workflow/quality-gate-contract.md) and states only what
is specific to published content.

## Entry

The gate starts only on an explicit request that names it. No workflow calls it.

## Inputs

| Input        | Type    | Values                           | Default  |
| ------------ | ------- | -------------------------------- | -------- |
| `subject`    | string  | Published content paths, by name | required |
| `mode`       | enum    | `lax`, `normal`, `strict`, `all` | `normal` |
| `max-cycles` | integer | 1, 2, or 3                       | 3        |

Any other `max-cycles` value, or a missing subject, refuses to start.

Product rules come from the adopter's adapter at `repo-governance/development/quality/gate-adapters/<product>.md`, which
names the content paths it covers and holds what only that product decides: front matter, tree layout, language policy,
link form, and each generic rule below it overrides, by name. An uncovered path gets the generic rules alone; the
checker never infers a product rule.

## Deterministic Boundary

The checker reports none of these; the entry and exit checks run their owners.

| Property                                                | Owned by                 | This catalog runs |
| ------------------------------------------------------- | ------------------------ | ----------------- |
| Markdown formatting, list markers, indents, empty links | the formatter and linter | none              |
| File names                                              | the file-name validator  | none              |
| Diagram rendering, label length, and palette            | the diagram validator    | none              |
| Internal links and anchors                              | the link validator       | none              |
| Front matter fields                                     | the metadata validator   | none              |

The catalog publishes no content, so an adopter fills the last column with its declared gate's tools. A property they
miss on the content paths, such as links in a tree the link validator excludes, becomes judgeable, per
[Deterministic and Judgement Validation](../../development/quality/checks/deterministic-and-judgement-validation.md).

## Cycle

Each cycle is one full audit by `content-checker` and one repair by `content-fixer` through
[Content Propagation](content-propagation.md), per
[Sequence and Termination](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md). The audit
asks of each page whether:

1. its prose is active, plain, and concise, explaining every unfamiliar term, per
   [Voice and Clarity](../../conventions/writing/content-quality/001-voice-and-clarity.md);
2. its headings nest without skipping a level and name their sections, per
   [Headings and Structure](../../conventions/writing/content-quality/002-headings-and-structure.md);
3. every informative image has alt text, link text names its destination, and colour is never the only cue, per
   [Accessible Content](../../conventions/writing/content-quality/003-accessible-content.md);
4. every code block names its language, per [Formatting](../../conventions/writing/content-quality/004-formatting.md),
   and any time estimate is labelled as one;
5. every factual claim (commands, versions, code, external references) holds against an authoritative source, and steps
   work in their stated order, per [Factual Validation](../../conventions/writing/factual-validation.md) and the
   `validating-factual-accuracy` skill;
6. internal links, image links, and anchors resolve, and external links are reachable, ignoring links in code,
   quotations, and comments, per [Internal Links](../../conventions/writing/internal-links.md) and the
   `validating-links` skill; and
7. it meets every product rule its adapter states.

Wording preference is not a finding. A claim no authoritative source settles is reported as unverified, never as wrong.

## Termination

The contract's
[termination table](../../development/workflow/quality-gate-contract/002-sequence-and-termination.md#termination)
applies unchanged.

## Verdict

| Verdict              | The caller                                                                          |
| -------------------- | ----------------------------------------------------------------------------------- |
| `PASS`               | records the verdict and continues                                                   |
| `PASS_WITH_FINDINGS` | records the verdict and open non-blocking rows, then continues                      |
| `FAIL`               | gives each open blocking row an owner (idea brief, plan item, or issue), continues  |
| `BLOCKED`            | records the cause (tooling, input-changed, or unavailable), then acts as for `FAIL` |

No verdict stops the caller or authorizes publishing.

## Ledger

`local-tmp/quality/content/<subject-slug>__<YYYYMMDDTHHMMZ>.md`, with the columns and closing verdict block in
[the contract](../../development/workflow/quality-gate-contract/003-verdicts-ledger-and-relations.md#ledger). Fact rows
keep their source and retrieval date; the ledger is never committed.

## Example Usage

```text
Run content-quality-gate on content/en/learn/databases with mode normal.
```

## Related Workflows

- [Docs Quality Gate](docs-quality-gate.md) judges repository documents, not published content.
- [Tutorial By Example Quality Gate](tutorial-by-example-quality-gate.md) and sibling tutorial gates judge tutorials by
  kind.
