---
description: >-
  Requires internal references in a plan to be checked against the current revision and external facts to carry a plain
  citation, forbids inline confidence labels, and fixes the order of refusal when a claim cannot be verified.
when_to_use: >-
  Use when a plan cites a path, command, flag, test, agent, skill, number, or external behaviour, or when a claim cannot
  be verified before it is written.
---

# Grounding and Citation

A reference in a plan is a promise that the thing exists. Grounding keeps that promise checkable, a citation shows where
an outside fact came from, and refusal covers the claims that cannot be established at all.

## Ground Every Internal Reference

Before a plan names anything inside the repository, whether a file, directory, command target, flag, function, test,
agent, or skill, verify that it exists at the current revision. When verification fails, take one of three paths:

1. find the correct reference and use it;
2. mark the reference as new, with a delivery item that creates it; or
3. refuse the claim, as described below.

A reference that ought to exist is not a reference.

## Cite External Facts in Plain Text

A fact taken from outside the repository carries a plain citation beside it: the URL, the access date, and a short
excerpt that settles the claim. The citation is ordinary prose or a link, never a bracketed tag.

## No Inline Confidence Labels

A plan carries no inline label stating how a claim was established, such as `[Repo-grounded]`, `[Web-cited]`,
`[Judgment call]`, or `[Unverified]`. A label records what the author says was checked, not what was, and a reader
cannot tell the two apart. Grounding happens while the claim is written; confirming it is the plan checker's job, which
re-verifies every factual claim whatever its author asserted. A decision reads as a decision through its reasoning, not
through a tag.

## What an Unchecked Claim Does

How a plan gate treats a factual claim the checker cannot verify is an adopter decision:

| Option               | Unchecked factual claim                       | Gains                                         | Costs                                                |
| -------------------- | --------------------------------------------- | --------------------------------------------- | ---------------------------------------------------- |
| block the gate       | blocks the gate until verified, cited, or cut | no plan proceeds on an unchecked fact         | slow verification holds up the whole plan            |
| non-blocking finding | a `HIGH` finding that carries a disposition   | work continues while the claim is followed up | an unchecked fact can still surprise execution later |

## Refuse When Uncertain

When a claim cannot be verified, take the first option that works:

1. omit it;
2. move it to the plan's open questions, phrased as a question rather than a fact;
3. restate it as a decision, with its reasoning in the prose; or
4. replace it with a placeholder and a delivery item that establishes the fact.

An unverified claim stated as fact is never an option. A plan that says less and is right is worth more than one that
says more and is partly invented.

## Verify by Claim Category

| Claim                    | Verification                                                         |
| ------------------------ | -------------------------------------------------------------------- |
| file or directory path   | list or read it at the current revision                              |
| command target or script | read the file that defines it, or the tool's own listing of targets  |
| command-line flag        | read the help output of the installed version                        |
| function, method, or API | find its definition in the source                                    |
| test name                | find it in the test files                                            |
| agent or skill           | confirm its definition file exists                                   |
| dependency version       | read the manifest or lock file                                       |
| numeric target           | cite a measured baseline, or state it as a decision with its reasons |
| external behaviour       | cite an authoritative source with URL, access date, and excerpt      |
| cross-link               | resolve it to an existing file                                       |
