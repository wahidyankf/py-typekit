---
description: >-
  Requires a measured run to prove it executed, by asserting exit status and output rather than duration, and to prove
  it finished, by writing a terminal exit marker as its last action.
when_to_use: >-
  Use before trusting a timing from a harness or loop, or when a command runs in the background, under a timeout, or
  long enough that its result is read afterwards.
---

# The Run Itself

A run fails as evidence at either end: the command never started, or it started and died. The two differ in cause and
look identical in the record, a file of plausible output and no error.

## 1. Prove the Command Ran

A timing harness reports elapsed time whether or not the command it times executed. Before recording any duration,
assert that the command exited successfully and produced the output it should. A command that did not run is very fast.

Silent transformations produce exactly this false result:

| Trap                                                                 | What the record shows                                                                     |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| a shell that passes a variable holding several words as one argument | every call fails at once with a usage error, and the loop reports a few milliseconds each |
| a pipeline status variable read in a shell that does not define it   | an empty value where the exit code belongs, with no warning                               |
| a path filter whose wildcard does not cross directory separators     | no match, read as "no file changed"                                                       |
| an alias or wrapper that rewrites a command or its output            | a result from a different tool than the one named                                         |
| a build cache replaying an earlier result                            | a success proving a previous run passed, not that anything ran against this change        |

Do:

- measure under a shell whose splitting rules are explicit, with an array or a `case`, and repeat the command several
  times and divide;
- capture the exit status without a pipe, or with pipe failure enabled and the status read directly;
- prefer a query whose empty result can only mean empty, such as taking the full list and filtering it;
- bypass the cache, or assert that no replay occurred, whenever the run itself is the evidence; and
- keep instrumentation lighter than its subject: an interpreter whose startup outlasts a sub-second command measures
  itself.

## 2. Prove the Run Finished

Timeouts terminate commands, supervisors shed processes under memory pressure, and wrappers are cancelled between steps.
The output written before the kill survives and reads as the whole result.

Record the exit status as the run's final action, in the same artifact as its output:

```bash
<command> > <output-file> 2>&1
echo "TERMINAL_EXIT=$?" >> <output-file>
```

Append the marker after the redirect, so it lands even when the command writes nothing. The file then answers three
questions partial output cannot: did it finish, what did it return, and is this all of it.

| Observation                               | Unsafe reading | Correct reading                  |
| ----------------------------------------- | -------------- | -------------------------------- |
| no marker, and no process                 | still running  | did not finish: investigate      |
| no marker, and output ending mid-way      | nearly done    | did not finish: investigate      |
| success text in the output, and no marker | passed         | unknown: there is no exit status |

A tool's own summary is a sentence, not an outcome. Check for the marker before reading any result as final.

Run one gated command per unit of background work. When a wrapper chaining several commands dies at the second, the
first one's success cannot be attributed and the rest never ran, and the wrapper may have written nothing that says so.

Elapsed time is not evidence either way. A wrapper that died after ninety seconds and one still working after ninety
seconds look the same from outside; only the marker tells them apart. A report written as the work proceeds, under
[Temporary Files](../../../../conventions/structure/temporary-files.md), carries a final status for the same reason.
