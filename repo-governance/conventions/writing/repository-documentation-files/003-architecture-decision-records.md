---
description: >-
  Defines when an architecture decision record is written, its required sections, its numbered storage, and the
  immutability and status transitions that keep it a record.
when_to_use: >-
  Use when a significant technical decision is being made or reversed, or when writing, superseding, or indexing a
  decision record.
---

# Architecture Decision Records

An architecture decision record captures one significant decision: the context it was made in, what was decided, and
what it costs. Its value is the reasoning — exactly what code cannot show, and what the people who made the decision
take with them when they leave.

## When to Write One

| Write a record for                                            | Do not write one for                        |
| ------------------------------------------------------------- | ------------------------------------------- |
| choosing a framework, library, datastore, or platform         | routine implementation detail               |
| an architectural pattern, such as one service against several | temporary or experimental code              |
| an infrastructure, deployment, or delivery approach           | a decision reversible later at no real cost |
| a cross-cutting design, such as authentication or caching     | a minor dependency version update           |

The test: would a capable newcomer, finding this choice in the code, reasonably wonder why and consider changing it?

## Structure

```markdown
# NNN. Short Title

Date: YYYY-MM-DD

## Status

Proposed | Accepted | Rejected | Deprecated | Superseded by NNN

## Context

The forces at play — technical, organizational, and project constraints — stated neutrally, with the options considered.

## Decision

The decision, stated plainly in active voice.

## Consequences

### Positive

### Negative

### Neutral
```

Context is value-neutral: it records the situation, not the argument for the answer. Consequences are honest in both
directions, and a record that lists no negative consequence has not finished its thinking. The date is when the decision
was made — content, not maintenance metadata.

## Storage

Records live where the repository's `ADR location` decision places them, by default `docs/explanation/decisions/`, named
`NNN-<slug>.md` — a three-digit sequence number and a kebab-case slug — with a `README.md` index listing every record
and its status. The decision is recorded once in the repository adapter, and
[SWE Architect](../../../../agents/swe-architect.md) writes there. A decision scoped to one component lives in the same
relative location inside that component, in the same form.

Numbers are never reused. A number is how later records cite a decision, and a reused one makes an old citation point at
the wrong decision.

## Accepted Records Are Immutable

Once a record is accepted, its context, decision, and consequences are never edited. Only its status line changes:

| From     | To                  | When                                          |
| -------- | ------------------- | --------------------------------------------- |
| Proposed | Accepted            | the decision is approved                      |
| Proposed | Rejected            | the proposal is declined                      |
| Accepted | `Superseded by NNN` | a newer record replaces it                    |
| Accepted | Deprecated          | it no longer applies, and nothing replaces it |

Repairing a link whose target has moved, as [Internal Links](../internal-links.md) requires, is mechanical repair: it is
permitted inside an accepted record and is not a substantive edit.

Immutability is the point. A record edited to match a newer decision no longer shows why the old one was made, and that
reasoning is what a later team most needs when it is tempted to swing back.

## Superseding a Decision

1. Write a new record with status `Proposed`, whose context names the record it would supersede.
2. On approval, set the new record to `Accepted`.
3. Set the old record's status to `Superseded by NNN`, and change nothing else in it.
4. Update the index.

## Review

A proposed record is reviewed by the people its consequences affect, and approval is by consensus. The author owns the
document and incorporates the feedback. A time-boxed review that opens with silent reading and collects written comments
keeps the discussion on the record rather than on whoever speaks first.

The practice is described further at [adr.github.io](https://adr.github.io/).
