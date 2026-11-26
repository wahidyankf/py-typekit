---
name: ux-review-fix-planning
description: >-
  Runs exploratory, usability, and design-fidelity passes in turn on a live surface, attributing findings per pass, and
  turns them into a gated fix plan without editing source.
when_to_use: >-
  Use when a running user-facing surface needs correctness, first-use, and design-fidelity findings in one fix plan, or
  an earlier findings plan needs refreshing.
---

# UX Review Fix Planning

## Entry

The working tree is clean, and the user-facing surface is running and reachable.

- `origin` (`string`, required): the surface's address.
- `routes` (`string`, required): routes or screens every pass reviews.
- `goal` (`string`, required): each pass's charter, read through its own lens.
- `viewports` (`string`, optional, default every supported viewport class).
- `locales` (`string`, optional, default every supported locale, not the default alone).
- `design-source` (`string`, optional, default none): an approved external design for the third pass.
- `plan-mode` (`enum`: `new`, `merge`, optional, default `new`): author a plan or extend one.
- `plan-identifier` (`string`, optional, default derived from `goal`): the new plan's folder name.
- `merge-target` (`directory`, required under `merge`): the findings plan to extend.

## Sequence

1. **Pre-flight.** Confirm the clean tree, a working real-browser integration, every route answering at `origin`, and
   under `merge` an existing `merge-target`; any failure ends the run `fail`.
2. **Checkpoint: settle the scope** only when the answer changes the run (ambiguous addresses, an unstated `plan-mode`),
   per [Decision Gates](../../development/agents/planning-capabilities/003-decision-gates.md); otherwise state the
   default taken. A rejection ends the run `rejected`.
3. **Compile carry-forward lists** of earlier defect classes and changed surfaces for every pass, per
   [Usability Probes](../../development/quality/manual-verification/008-usability-probes-and-completeness.md).
4. **Open the report** shaped by [Findings and the Plan](ux-review-fix-planning/002-findings-and-the-plan.md), so a
   stopped run keeps its findings.
5. **Run the first two passes.** Run [Exploratory and Usability Review](exploratory-usability-review.md) with `origin`,
   `routes`, and `viewports`, folding `goal`, `locales`, and the carry-forward lists into its declared tasks so the
   spec-blind lens receives nothing that workflow withholds. Each lens fills its own section; a pass that cannot run is
   recorded as a missing perspective without stopping the run.
6. **Run the design-fidelity pass** once step 5 is recorded, per
   [Design-Fidelity Pass](ux-review-fix-planning/001-design-fidelity-pass.md), handling a failure as step 5 does.
7. **Cross-reference root causes**, and under `merge` re-verify prior findings, per module 002.
8. **Critique completeness** with step 3's completeness critic. Re-run each owning pass at most once, against its frozen
   gaps and no new task, per
   [its standard](../../development/quality/manual-verification/003-exploratory-and-usability.md) and
   [Bounded Convergence](../../development/workflow/bounded-convergence.md); record each open gap's reason.
9. **Author the plan.** Run [Planning](../plan/plan-planning.md) on `plan-path`, briefed with the report and module
   002's content. Its [Quality Gate](plan-quality-gate.md) verdict is never re-run; residual findings go to the person
   before hand-back.
10. **Hand back.** Record only the plan's paths through the repository's delivery mode, and report `plan-path`, counts
    per pass, and `final-status`. A material surface change before execution calls for a fresh `merge` run.

## Exit

`final-status` (`enum`: `pass`, `partial`, `fail`, `rejected`) is `pass` when all three passes ran and the gate returned
`PASS` or `PASS_WITH_FINDINGS`; `partial` when a pass could not run or the gate returned `FAIL`; `fail` at pre-flight;
and `rejected` at the checkpoint, the last two leaving no plan.

Otherwise the run leaves `plan-path` (`directory`, at `plans/backlog/<plan-identifier>/` or `merge-target`), the report
(`file`, at `<reports-dir>/ux-review-fix-planning-<yyyy-mm-dd-hh-mm>-<uuid>-report.md`), and `exploratory-count`,
`usability-count`, and `design-count` (`number`).

## Example Usage

```text
Run ux-review-fix-planning with origin <preview-address>, routes "/checkout", goal "a first-time buyer pays".
```

## Related Workflows

- [Exploratory and Usability Review](exploratory-usability-review.md) runs the first two passes.
- [Planning](../plan/plan-planning.md) authors the plan; [Execution](../plan/plan-execution.md) applies it after review.

## The Plan Is the Deliverable

The run writes only its report and the plan, never source or the live surface, so a person reviews one attributed
proposal first. A near-end retest under
[User-Facing Delivery Hardening](../../development/quality/user-interfaces/user-facing-delivery-hardening.md) is a
separate round.

## Why One Pass at a Time

Passes run in turn so none writes the report concurrently, and the design pass runs last so its designs never reach the
spec-blind lens. Reconciling three independent readings before a fix implements
[Deliberate Problem-Solving](../../principles/deliberate-problem-solving.md); naming each finding's pass implements
[Explicit Over Implicit](../../principles/explicit-over-implicit.md).
