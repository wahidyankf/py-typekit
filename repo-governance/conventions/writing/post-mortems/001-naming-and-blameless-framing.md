---
description: >-
  Fixes where post-mortems live and how they are named by incident date, and requires blameless framing that analyses
  systems and conditions rather than people.
when_to_use: >-
  Use when naming a new post-mortem, or when a draft's root cause, tone, or wording points at a person.
---

# Naming and Blameless Framing

## One Flat Directory

Post-mortems live together in one flat directory the repository declares, beside its other explanatory documentation,
with a `README.md` that indexes every post-mortem in it. There are no subdirectories: incidents are found by date and
system, and a hierarchy would force a classification that nobody makes consistently at the time of writing.

## Named by Incident Date

```text
YYYY-MM-DD-<system>-<short-failure>.md
```

- `YYYY-MM-DD` is the date the **incident** occurred — not the date the document was written, which history records.
- `<system>` names the affected system or service.
- `<short-failure>` says briefly what failed.
- Every component is lowercase kebab-case, per [File Naming](../../structure/file-naming.md).

| Name                                                   | Verdict                                                      |
| ------------------------------------------------------ | ------------------------------------------------------------ |
| `2025-03-14-billing-api-connection-pool-exhaustion.md` | correct                                                      |
| `post-mortem-2025-03-14.md`                            | no system and no failure; the listing sorts but says nothing |
| `2025-03-14__billing-api__pool.md`                     | a double underscore is another record's separator            |
| `2025-03-14-Billing-API.md`                            | capitals, and no failure                                     |

The date leads because post-mortems are read chronologically, so the directory listing is itself a timeline, and because
the incident date, unlike the writing date, never changes. The single hyphen after it is deliberate: a double underscore
joins a completed plan's date to its slug — see
[Lifecycle and Folders](../../structure/plans/001-lifecycle-and-folders.md) — and borrowing it makes two kinds of record
look alike.

## Blameless

A post-mortem analyses systems and processes, never individuals.

Ask for the **second story**: how did this sequence of events make sense to the people involved, with what they knew at
the time? The first story is the timeline of what happened. The second is the context — pressures, signals, defaults,
system state — that made each decision reasonable when it was made. Only the second produces a lasting fix, because the
next person will face the same context.

- **"Human error" is never a root cause.** It is a symptom. The question is which condition made the error likely, or
  made it consequential.
- **No individual is named in a context of fault.** Roles are fine: "the on-call engineer", "the deploy job".
- **No hindsight.** Record what was known at each decision point, not what is known now.
- **No blame-shifting.** Moving fault from a person to a team, a vendor, or a tool is still assigning blame.
  Contributing factors name conditions, not culprits.

Blamelessness is not politeness. People who expect a write-up to find a culprit stop saying what they did and why, and a
post-mortem written from guarded accounts fixes the wrong thing.

The framing follows established practice; see
[Postmortem Culture: Learning from Failure](https://sre.google/sre-book/postmortem-culture/).
