---
name: harness-parity-verification
description: >-
  Verifies, without changing anything, that every supported harness still reaches the one canonical instruction body and
  adapters generated from canonical artifacts, and reports a bounded parity verdict.
when_to_use: >-
  Use after changing root instructions, a canonical agent or skill, an adapter generator, or harness configuration, and
  before delivering that change.
---

# Harness Parity Verification

## Entry

The repository declares at least one supported harness and a deterministic parity check, and the working tree holds a
change that could alter what a harness reads.

- `harness` (`string`, optional): one declared harness to verify. Default: every declared harness. A name the repository
  does not declare ends the run as `blocked`, because narrowing asks a smaller question, never a quieter one.

## Sequence

1. **Record the baseline:** the revision, working-tree status, and declared harness roster. Uncommitted changes belong
   to whoever made them; this run reads them and edits none. Any later tree change invalidates results from this
   baseline.
2. **Inventory what each harness reads.** List the canonical instruction body, every canonical agent and skill, each
   harness's adapters, and each harness configuration file. Search the whole tree for instruction files too, so a
   competing source is inventoried, not assumed absent.
3. **Confirm each route reaches the one body.** Every harness reads the canonical instruction body directly or through a
   single generated adapter, with no overlay, nested override, or copied body, as
   [Harness Adapters](../../development/agents/harness-adapters.md) requires. Every command and path the instructions
   quote exists. Equal names or counts prove nothing; content, routes, permissions, and restrictions decide.
4. **Run the deterministic check.** Run the repository's parity check with caching disabled. Record the exit status and
   what the check says it reconciled: harness, agent, and skill counts, plus any digest. A check that reconciled zero
   harnesses verified nothing. On failure, read every finding by harness, field, and path, not only the summary line.
5. **Bound the runtime claims.** An installed harness that starts is an availability observation; it does not show that
   a vendor's discovery, model, plugins, or user-global settings honour the repository contract. Record runtime
   discovery on its own as verified, not assessed, unavailable, or failed.
6. **Report one verdict** with the commands run, the baseline, the reconciled counts, the runtime scope, and any
   unresolved risk:

   | Verdict        | Means                                                                                     |
   | -------------- | ----------------------------------------------------------------------------------------- |
   | `pass`         | the uncached check succeeded at the baseline, and steps 2 and 3 found no competing source |
   | `fail`         | at least one finding exists                                                               |
   | `blocked`      | the check could not run, reconciled nothing, or needed evidence was unreadable            |
   | `not assessed` | verification did not run                                                                  |

## Exit

A successful run ends with `verdict` (`enum`: `pass`, `fail`, `blocked`, `not assessed`) set to `pass`, and a `report`
(`string`) naming the commands, baseline revision, reconciled counts, and runtime-discovery scope. The working tree is
exactly as the baseline recorded it.

`fail` and `blocked` also end the run, preserving the findings and changing no file.

## Example Usage

```text
Run harness-parity-verification for every declared harness at the current revision.
```

## Related Workflows

- [Harness Quality Gate](harness-quality-gate.md) judges what no repository check can see: a harness changing its own
  conventions.

## Verification and Repair Are Separate Runs

A run that edits while verifying cannot say which state its verdict describes. After `fail`, repair the canonical
artifact or the generator, never an adapter by hand, and rerun from a fresh baseline. Never weaken the check, drop a
restriction, or exclude a path to reach `pass`.

An adopter runs the deterministic check in its own pull-request gate; this workflow adds the reading a gate does not do.

## What the Check Cannot Prove

The check covers canonical content and the adapters generated from it. It cannot show that a vendor model follows an
instruction, that a user-global plugin leaves it intact, or that a harness enforces a restriction it cannot express.
Step 5 keeps those out of `pass`, so a parity verdict never claims anything about vendor or local state.

## Principles

This workflow implements [Evidence Over Assertion](../../principles/evidence-over-assertion.md), because parity rests on
content and a reconciled check, not matching names; [Fail Closed](../../principles/fail-closed.md), because a check that
could not run or reconciled nothing is `blocked`; and [One Source Per Fact](../../principles/one-source-per-fact.md),
because every harness must read one instruction body.
