---
name: rules-grooming
description: >-
  Sweeps the rule corpus on request for volume carrying no obligation, ranks candidates for approval, and hands each
  approved group to Rules Propagation, proving no obligation was lost.
when_to_use: >-
  Use on explicit request after a repository's structural change, or when rules have grown by repetition rather than new
  obligations.
---

# Rules Grooming

## Entry

A grooming run is explicitly directed. One document over its word budget is no trigger; relocation repairs it per
[Document Word Budget](../../conventions/structure/document-word-budget.md).

- `scope` (`string`, optional, default the whole rule corpus): path prefixes to sweep.
- `classes` (`string`, optional, default every admitted class): classes to consider.
- `dry-run` (`boolean`, optional, default `false`): produce inventory and manifest, handing nothing over.

## Sequence

1. **Inventory every obligation in `scope` first,** recording each distinct one with its audience, condition, and
   locations.
2. **Discover candidates in the admitted `classes` only,** each recording class, paths, measured yield, and evidence:
   - **duplication:** one obligation on several surfaces with no recorded reason to keep both. The kept home is chosen
     by level, then the narrowest binding surface, and must already cover every case the removed text covered; otherwise
     the candidate becomes completing that home first.
   - **scaffolding:** whole sentences stating no obligation, such as a preamble restating its heading; deleted, never
     rewritten.
   - **retirement:** a rule whose subject no longer exists, that a later rule supersedes in practice, or that nothing
     reaches. Missing inbound links alone are not evidence. Only this class removes an obligation.
3. **Rank by yield over risk,** retirement riskiest, and group by subject. Drop a candidate whose yield would not repay
   a propagation run.
4. **Seek approval of the manifest.** Under `dry-run`, the run ends `no-change` here. Duplication and scaffolding may be
   batch-approved, scaffolding against its listed sentences; each retirement is approved alone with its evidence; an
   entry-point document needs approval naming it. Silence is not approval. Record each rejection and deferral with its
   reason; keep deferrals for the next run.
5. **Hand each approved group to [Rules Propagation](../quality/rules-propagation.md) once,** in ranked order, with its
   surfaces, home, and evidence. A propagation blocker is recorded against its item and the run continues; an item is
   never restated more loosely to get it accepted.
6. **Prove preservation.** Re-inventory and compare, excluding index entries and routing clauses from both sides. The
   run passes only when every missing obligation was an approved retirement, none changed its audience, condition,
   qualifier, or exception, and each survivor stays reachable from a surface binding its audience.
7. **Request an effective verdict** from the [Rules Quality Gate](../quality/rules-quality-gate.md) where the adopter
   chose one, then log the run with its size change and each item's disposition.

## Exit

Outputs: the manifest and both obligation inventories (`file`, in the scratch location per
[Temporary Files](../../conventions/structure/temporary-files.md)), and `status` (`enum`: `no-change`, `groomed`,
`partial`, `halted`).

Partial outcome: an unanswered approval ends the run with nothing handed over. An unapproved obligation loss halts it;
its revert is itself a rule edit for propagation, and the class causing the loss is recorded for tightening. A pass
authorizes no commit or push.

## Example Usage

```text
Run rules-grooming with scope "repo-governance/development/" and dry-run true.
```

## Related Workflows

- [Rules Propagation](../quality/rules-propagation.md) writes every approved reduction; the
  [Rules Quality Gate](../quality/rules-quality-gate.md) can judge the resulting state.

## Never a Reduction

- Rewording text only to shorten it, or weakening a qualifier, boundary, exception, or pass condition.
- Cutting any safety guardrail the adopter lists, such as data safety or commit authorization.
- Raising a word budget or deleting a rule to make room.

## Adopter Decisions

| Option            | Trade-off                                                                                                                              |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| three classes     | split documents face the same tests as any text; a heavily split corpus keeps its per-module overhead                                  |
| add fragmentation | an undersized companion module may merge back within budget, carrying every link and index line; one more class can lose an obligation |

Record the choice, and whether that class is approved per item or as a batch. Also record whether step 7 runs: a verdict
every run catches reductions keeping each obligation yet leaving rules incoherent, at a gate pass's cost; otherwise the
gate needs its own direction.

## Principles

This workflow implements [Minimal Sufficiency](../../principles/minimal-sufficiency.md) and
[Governance Continuity](../../principles/governance-continuity.md).
