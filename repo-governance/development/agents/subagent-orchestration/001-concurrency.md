---
description: >-
  Makes parallel execution the default for independent work, bounds it with a cap of three that only a plan or user
  declaration changes, and requires dependencies mapped before dispatch.
when_to_use: >-
  Use when deciding whether to run work serially or in parallel, and how many units may run at once.
---

# Concurrency

## Parallel Unless Dependent

Independent units of work run at the same time. Units are independent when neither needs the other's output and every
input needed to launch them is already known: three unrelated file reads are one turn, not three.

The burden of proof sits with serialization. Running independent work one unit at a time requires naming the reason: a
dependency, a shared output, an ordering that must be byte-identical, a transaction, or a documented correctness
constraint. Compute cost alone is not a dependency.

## Map Dependencies Before Dispatch

Before the first dispatch in a session, the orchestrator reads this cap and records N: tool history shows the read
preceding the first spawn, and any spawn preceding the read violates this clause. The orchestrator never changes N on
its own judgement; only a plan or the user declares another value. Disposition: unenforced by decision; review checks
the tool history.

The dependency graph is known before anything is dispatched. Planned work takes it from what the
[Delivery Contract](../../../conventions/structure/plans/004-delivery-contract.md) defines, delivery units and phases in
dependency order; unplanned work maps it before its first dispatch. Two units are independent only when neither reads
what the other writes, so a shared output file, a shared branch, or an ordering constraint makes them dependent however
separable they look. Cleanup is the terminal node and depends on every other node, so it can never remove something
still in use.

The graph's independent width decides how much fans out. The cap limits that width; it never creates it. Splitting a
dependent chain into artificial units to fill idle slots is a defect, and a dependent chain running one unit at a time
is correct.

## The Declared Cap

At most **N** independent units run at once, whether they are delegated agents or tool calls batched in one turn. The
orchestrator is the `+1`: it does not consume a slot, and it stays active while the N run. When a slot frees and
independent work is waiting, the next unit launches immediately, because N limits the instantaneous count rather than
the batch total.

The count covers every delegated agent alive in the session, foreground or background, at any depth: an agent that a
delegated agent spawns takes a slot of its own. It binds in every harness whose session can spawn delegated agents,
whatever that harness calls them. Work beyond N waits until a running unit returns; it is never launched over the cap.

The cap bounds token burn and per-minute rate limits. Each concurrent unit spends independently against the same quota,
and overshooting produces retries that cascade until the batch runs slower than it would have serially. A shared machine
limits it too, since other agents and people draw on the same capacity.

### The Default and Who Changes It

N is **3** unless a plan or the user declares another value, recorded where every orchestrating agent reads it. Three is
set to stay below quota saturation even when agents reach their tool-heavy phases together.

- **Raising** N requires all three of genuinely independent work, machine capacity, and budget headroom, and only a plan
  or the user declares it.
- **Running below** N is required under budget, runner, or disk pressure, and may happen at any point in a batch.

The orchestrator never changes N on its own judgement, least of all upward because early agents finished quickly.
Completion speed varies across a batch; agents that start fast reach their heaviest phases together, and the cap exists
for that phase rather than the opening one.

## Keep the Orchestrator Responsive

Prefer delegated slots for long-running work, and keep the orchestrator free to coordinate. A user who asks a question
mid-batch should not wait behind the orchestrator's own long task. Like everything else here, this preference is bounded
by the dependency graph: only independent work moves to a slot.
