---
description: >-
  Defines case selection and execution proof for local test-first cycles while preserving full regression at phase and
  pre-pull-request boundaries, with full end-to-end scheduling and batching.
when_to_use: >-
  Use when choosing a cycle command, recording filtered-run evidence, planning full regression gates, or scheduling
  end-to-end runs.
---

# Focused Runs and Regression Gates

Reason: keep local feedback short without weakening test-first proof or delivery verification, following
[Evidence Over Assertion](../../../../../principles/evidence-over-assertion.md) and
[Deliberate Problem-Solving](../../../../../principles/deliberate-problem-solving.md).

- During a TDD cycle, run only the check covering the current item to demonstrate Red and Green. Do not run the block to
  prove a single item. An item is one mini test-driven cycle or one delivery checklist item. A block is the whole
  automated suite except end-to-end.
- After each refactor, run the named regression selection covering the changed behaviour and its affected shared
  boundary, rather than a full-suite run for every item.
- At the end of each plan phase, and before PR ready-for-review or session end as a safety net, run the whole automated
  suite except full E2E, including the mandatory fast gate with coverage, plus only the affected E2E flow. No hook runs
  a test, so the phase boundary is where the whole-check pays off. The same passing proof may cover both boundaries
  while its tested scope remains unchanged.
- Run the full E2E suite on its scheduled CI workflow (CRON) by default in every repository that has E2E; keep local E2E
  selective to the touched flow. Repositories without E2E carry no such schedule.
- Never require a full E2E run as a completion condition for plan execution or a plan phase; full E2E is a separately
  batched set.
- Record executed case identities and a positive executed-test count for every filtered cycle run. Zero tests, unmatched
  filters, and cached results that did not execute the intended cases are not proof.

Use runner-level case/file filters. A filtered run must not enforce whole-project coverage on code it intentionally does
not execute: use a separate focused runner invocation without that coverage mode, leaving the full coverage target and
its floor unchanged. Preserve required build/code-generation, resource admission, real-resource ownership, and cleanup
guards.

Existing test-first layers, exceptions, coverage floors, hooks, and continuous-integration contracts remain unchanged.
Full integration/end-to-end runs remain separate from the fast gate.

**Followed observations:** red and green execute only the current item's check, failing and passing on the intended
behaviour assertion; refactor executes affected-boundary cases and passes; phase/pre-PR proof records a passing
whole-suite run except full E2E plus the affected E2E flow; full E2E passes on its schedule; no plan or phase gate names
a full-E2E run as its completion condition; every filtered run records positive execution counts.

**Violated observations:** a per-item unfiltered command executes unrelated cases; refactor omits a named
affected-boundary case; boundary proof substitutes filtered cases for the mandatory whole-suite run or runs the full E2E
suite locally instead of the affected flow; a plan or phase completion waits on a full-E2E run; or runner output
positively reports zero matched tests.

**Enforcement disposition — unenforced by decision:** the smallest meaningful selection, the affected E2E flow, and the
E2E schedule depend on behaviour and boundary context. Plan and execution review inspect commands, executed identities,
counts, and boundary records; no mechanical scanner or gate coverage of local selection, execution order, or schedule
presence is claimed.
