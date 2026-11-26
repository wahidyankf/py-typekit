---
description: >-
  Requires a measurement to come from the integrated execution path, a wall-clock remedy to target the critical path,
  and a remedy written before the timeline was seen to be re-derived from it.
when_to_use: >-
  Use before gating work on a benchmark number, prescribing a fix for a wall-clock regression, or applying a remedy a
  plan wrote in advance.
---

# The Path Measured

A number can be exact and still describe the wrong path. These rules tie a measurement, and any remedy based on it, to
what actually runs.

## 3. Measure the Integrated Path

A benchmark of one isolated invocation does not predict its saving inside a batched or child-process execution model.
Measure the path that runs in practice before gating anything on the number.

The tell is a difference in how the process is spawned. A tool timed alone through a package launcher pays the
launcher's startup on every call; the same tool running as a child of a batch runner that invoked the launcher once does
not. Whenever the benchmark and the real path spawn differently, the isolated figure is at best an upper bound, and a
threshold derived from it can overstate the gain several times over.

## 4. Find the Critical Path Before a Wall-Clock Remedy

Wall-clock time in a parallel dependency graph is a maximum, not a sum. It is insensitive to every component off the
critical path, so a wall-clock remedy first proves that the component it changes is on that path.

Read the per-job timeline. A regression attributed to how jobs are grouped cannot be fixed by regrouping when the
longest job sat outside the groups and took as long before the change.

Sum-type and max-type metrics do not move together. Total runner time can fall in the very runs where wall-clock time
rises. A diagnosis that treats both as symptoms of one cause will be wrong about whichever it reads second.

## 5. A Pre-Authored Remedy Is a Hypothesis

Plans often pair a metric with a prescribed fix at the time they are written. That pairing is a guess about which
component will hold the number, and it is recorded as a guess, as
[Grounding and Citation](../plan-anti-hallucination/001-grounding-and-citation.md) requires of a target with no measured
baseline.

When the gate fires, re-derive the component from the observed timeline before applying the prescribed remedy. Where the
two disagree, the timeline wins, and the plan's remedy is corrected in place rather than executed.
