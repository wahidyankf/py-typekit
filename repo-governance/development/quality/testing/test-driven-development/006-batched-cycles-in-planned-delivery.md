---
description: >-
  Runs one test-first cycle per delivery batch instead of per scenario, keeping per-scenario failing tests and a single
  batch record, with full regression only at the phase or push boundary.
when_to_use: >-
  Use when a plan already delivers work in batches and the per-scenario red-green ceremony would cost more than it
  proves, or when deciding whether a batch is too large to share one cycle.
---

# Batched Cycles in Planned Delivery

When a plan already delivers work in batches — one pull request or one delivery boundary at a time — the cycle may run
per batch instead of per scenario, so planned work does not pay a full red-green ceremony for every scenario:

1. Write the batch's tests first, from its scenarios, before any production change in the batch.
2. Run one focused RED run for the batch. Every scenario's test must fail for its stated reason; group the reasons in
   one batch record, not one record per scenario. A test that passes is repaired before implementation starts.
3. Implement the batch, then run the identical selection to GREEN. Keep the selection frozen between RED and GREEN.
4. Refactor inside the batch with the selection green; a behaviour change noticed along the way joins the batch's tests
   or becomes its own cycle.
5. Run the full applicable regression and touched end-to-end flows only at the phase or push boundary, per the
   repository's focused-runs and regression-gate rules.
6. Do not repeat an accepted RED whose tests and production code are unchanged.

A batch is one cohesive behaviour slice sharing a boundary and fixtures. Unrelated failures in one RED run mean the
batch is too large; split it. Small single-scenario changes and single bug fixes keep the per-scenario cycle. This
module changes run and evidence granularity only: it never permits writing tests after the code, and the existing scope
exemptions are unchanged. Batching leaves small cycles in place for test authorship: each test still covers one
behaviour, and only the RED, GREEN, and refactor runs and their records are grouped per batch.
