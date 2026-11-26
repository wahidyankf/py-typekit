---
description: >-
  Requires a falsifiability probe to change what its check compares, a scan to assert where it stopped, an exit code to
  come from the check rather than its parser, and a test assertion to stay true after the change lands.
when_to_use: >-
  Use when proving a guard can fail, writing a script that locates a region by walking a file, or writing a test that
  reads the repository or states a before-and-after claim.
---

# Probes and Lasting Assertions

The checks and tests built around a measurement are measurements too. Each can report success while reaching nothing.

## 6. Probes and Scans Assert Their Reach

**A probe changes what the check compares.** Editing a file a guard covers and watching the guard fail proves it can
fail only when the edited file is one the guard actually compares. A guard over generated files ignores the index beside
them; a probe that picks the first file in the directory can land on that index every time, and its pass certifies
nothing. Name the probe target from the guard's own expected set, and record the exit status before and after.
[Absence and Completeness](../plan-anti-hallucination/002-absence-and-completeness.md) holds the matching positive
control for a search.

**A preservation comparison declares its normalization contract.** Name every field the comparison transforms or omits,
the reason for each normalization, and the contract fields that remain unchanged. An unnamed fold can erase the evidence
or the difference under test. This is an evidence-review obligation, unenforced mechanically because the admissible
normalization depends on the contract being proved.

**A scan asserts where it stopped.** A script that walks forward to the last matching line will run past the block it
meant to end at, into another block that happens to match. Stop at the end of the contiguous block and assert its
expected size: for a table, a header, a separator, and the counted rows.

**A parser error is not a verdict.** Argument parsers commonly exit non-zero on an unknown subcommand, which reads
exactly like a validator reporting a failure. Confirm the subcommand exists before treating its exit code as the check's
answer.

**A declaration that matches nothing does nothing.** A build rule that only modifies an item some default already
created silently does nothing where no default created one, and the build stays green. Assert that the artifact appears
where it should land, not that the build succeeded.

## 7. An Assertion Outlives Its Moment

**A baseline read from the current commit expires.** A test that proves a before-state by reading a file at the current
commit is true while the work is uncommitted and false once it lands, because the commit then contains the change. The
before-and-after framing belongs in delivery evidence and in prose. The executable assertion is the invariant that holds
afterwards. Where the transition itself is the subject, build both states in a fixture the test owns, isolated as
[Git Fixture Isolation](../../testing/git-fixture-isolation.md) requires.

**An assertion inside a shared boundary holds everywhere it ships.** Code copied unchanged into other repositories
carries its assertions with it. An assertion naming one repository's documents, counts, or directories passes where it
was written and fails everywhere else, and the failure surfaces during a later port, long after its author's context is
gone. Derive the expectation from a declared source every copy carries, such as a registry, a manifest, or the tree
itself, and state the rule rather than the instance.
[Test Design](../../testing/test-driven-development/002-test-design.md) applies the same rule to completeness sets.
