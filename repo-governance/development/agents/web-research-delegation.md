---
description: >-
  Routes public-web research above a fixed per-claim threshold to one designated research agent, fixes who may hand it
  over, and allows three closed exceptions each exempt agent names.
when_to_use: >-
  Use when an agent, skill, or workflow needs facts only the public web holds, or when auditing one that can search or
  fetch.
---

# Web Research Delegation

Agents need facts the repository does not hold: current interface signatures, released versions, specification wording.
Without a rule, each agent grows its own search loop, floods its caller's context with raw pages, and sources findings
however its author chose.

## The Rule

Public-web research belongs to one designated research agent. Research that reaches the threshold below goes to that
agent, unless one of the three exceptions applies.

Only a top-level session, or an agent declaring `subagent` while running top-level, hands research over. A delegated
agent that reaches the threshold returns the need to its caller, and a skill never delegates, leaving the threshold to
whatever loads it; see the Skills Never Delegate section of [Capability Forms](capability-forms.md).

The adopter records the designated agent's name once, where agent definitions can cite it. The name differs between
repositories; the rule does not.

## The Threshold

For a single claim, **two or more searches, or three or more page fetches, means delegate**. Below that, an in-context
call is permitted.

| Situation                                                         | Action                  |
| ----------------------------------------------------------------- | ----------------------- |
| one fetch of an authoritative URL already in hand                 | in context, exception 1 |
| two or more searches to find the right source for one claim       | delegate                |
| three or more pages to cross-reference before deciding            | delegate                |
| research spanning several claims, or a survey of current practice | delegate                |
| checking whether a URL responds                                   | in context, exception 2 |
| a repair agent re-validating the one finding it is fixing         | in context, exception 3 |

The threshold is a number because judgement varies by author and a reviewer cannot check it. Counting calls is crude,
but the same for everyone.

## Why One Agent

- **Lean callers.** Multi-page research runs in isolation; the caller receives conclusions, not pages.
- **Uniform sourcing.** The research agent cites every claim and labels its confidence.
- **One improvement point.** A better search strategy lands in one definition, not in many copies.

## Exceptions

There are exactly three, and the list is closed. A fourth is a change to this standard, not a judgement made inside an
agent file.

1. **Single-shot verification of a known URL.** When the authoritative URL is already known, from an audit record, a
   user instruction, or an official registry page, one fetch of it stays in context and does not count toward the
   threshold. An agent launch for one call costs more than the call.
2. **Reachability checking.** An agent whose job is whether a URL responds and where it redirects fetches that URL
   directly. Its question is liveness, not content, so delegating only adds latency.
3. **Same-context re-validation by a repair agent.** An agent fixing one recorded finding re-checks that finding in the
   context it was reported in, because the check and the fix must agree. When the check grows into research beyond that
   one finding, the repair agent escalates the finding back to the reporting side rather than researching itself.

## Applying It

- **Agent definitions** that can search or fetch carry a short delegation section that cites this standard, states the
  threshold, and says whether reaching it means delegating or returning the need to the caller. An agent relying on an
  exception names which one, and why, in its own file.
- **Skills** that verify facts cite this standard instead of restating the threshold, and keep only how they consume
  research results.
- **Workflows** cite this standard at the step that verifies facts, where the performing agent applies it.

## Out of Scope

Lookups inside the local repository. How verification results are classified, which the adopter's factual-validation
guidance owns: this standard decides who researches, not how outcomes are labelled. How the research agent itself
searches, which its own definition governs.

## Compliance

An agent complies when it cannot search or fetch at all, or when it carries a delegation section citing the threshold
and names any exception it relies on as one of the three. An adopter enforces these checks in its own agent-definition
checker.
