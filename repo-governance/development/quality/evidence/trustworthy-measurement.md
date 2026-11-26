---
description: >-
  Requires a measured number to show that its command ran and finished, that it measured the path that really runs, and
  that its metric can respond to the change, before it justifies a decision.
when_to_use: >-
  Use before a benchmark timing, pipeline metric, coverage figure, or other measured number justifies a decision, a
  remedy, or an acceptance threshold.
---

# Trustworthy Measurement

A measurement is a claim about the system. The damaging ones are rarely slightly wrong. They are claims about something
else that look exactly like a good result: a harness that never ran the command reports a remarkable speedup, a
benchmark of one isolated invocation reports a saving the integrated path never pays, and a metric that cannot respond
to a change reports a regression the change did not cause.

Looking harder at the number catches none of these. Each needs its own check before the number justifies anything.

This standard implements [Evidence Over Assertion](../../../principles/evidence-over-assertion.md),
[Deliberate Problem-Solving](../../../principles/deliberate-problem-solving.md),
[Root Cause Orientation](../../../principles/root-cause-orientation.md), and
[Fail Closed](../../../principles/fail-closed.md).

## The Rules

1. **Prove the command ran.** Assert its exit status and its output, never only its duration.
2. **Prove the run finished.** A terminal exit marker, written last, separates a finished run from a killed one.
3. **Measure the integrated path.** An isolated invocation does not predict what the real execution model pays.
4. **Find the critical path first.** A wall-clock remedy must change a component on that path.
5. **Treat a pre-authored remedy as a hypothesis.** The observed timeline decides which component to change.
6. **Make probes and scans assert their reach.** A probe changes what its check compares; a scan asserts where it
   stopped.
7. **Make an assertion outlive its moment.** Assert the invariant that holds after the change, in every repository the
   assertion ships to.

## Modules

Read in order. The first covers the run itself, the second what the run measured, and the third the checks and tests
built around a measurement.

1. [The Run Itself](trustworthy-measurement/001-the-run-itself.md)
2. [The Path Measured](trustworthy-measurement/002-the-path-measured.md)
3. [Probes and Lasting Assertions](trustworthy-measurement/003-probes-and-lasting-assertions.md)

## Scope

Any number that justifies a decision: benchmark timings, pipeline metrics, disk measurements, coverage figures, and
acceptance thresholds. Diagnostic output no decision depends on is out of scope until someone quotes it in a plan, a
gate, or a review; from then on it is in.

## Related Standards

- [Absence and Completeness](plan-anti-hallucination/002-absence-and-completeness.md) sets what a zero result and a
  completeness claim need; these rules keep a measured result from passing for the wrong reason.
- [Quality Gate Results](../manual-verification/001-quality-gate-results.md) fixes the terminal results a gate returns.
- [Deletion With Proof](../deletion-with-proof.md) applies the same demonstration to removing something.

An adopter enforces the exit-status and terminal-marker checks in its own harness, gate, or CI wherever measured runs
are scripted.
