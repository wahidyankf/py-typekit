---
description: >-
  Fixes the post-mortem's required sections and their order, from the metadata table through references, and where the
  optional background and supporting data go.
when_to_use: >-
  Use when drafting a post-mortem, or when checking a draft for a missing, merged, or misplaced section.
---

# Required Sections

Every post-mortem contains these sections, in this order, after its title. A fixed order means a reader looking for the
root cause of any incident finds it in the same place, and a missing section is visible by its absence.

| #   | Section                    | Holds                                                                                               |
| --- | -------------------------- | --------------------------------------------------------------------------------------------------- |
| 1   | Metadata table             | incident date, investigation date, severity, incident status, and author by role — before any prose |
| 2   | Summary                    | two to four sentences: what failed, for how long, and the outcome; written last, placed first       |
| 3   | Impact                     | who and what was affected, for how long, time to detect, and time to resolve                        |
| 4   | Detection                  | how the incident was discovered, labelled with one category below                                   |
| 5   | Timeline                   | absolute timestamps with an explicit offset                                                         |
| 6   | Root Cause                 | the deepest systemic condition that let the trigger cause harm                                      |
| 7   | Trigger                    | the proximate event that started the chain                                                          |
| 8   | Contributing Factors       | the conditions that made it worse or made recovery harder                                           |
| 9   | Resolution and Mitigations | the fix applied, kept separate from the root-cause fix still open                                   |
| 10  | Action Items               | the tracked table defined in [Severity and Action Items](003-severity-and-action-items.md)          |
| 11  | What Went Well             | what limited the impact, including where luck did                                                   |
| 12  | Lessons Learned            | two to five insights that generalize beyond this fix                                                |
| 13  | References                 | logs, dashboards, related plans and post-mortems, and sources consulted                             |

The metadata table records incident status as `Investigating` or `Resolved`, and severity as `Sev-N — Label`. Where time
to detect cannot be measured because nothing alerted, Impact says `unknown` and why.

## Detection Categories

Detection ends with one label in parentheses: `(Manual)`, `(Monitoring Alert)`, `(Automated Health Check)`, or
`(User Report)`.

The label is what turns a set of post-mortems into evidence. A run of `(User Report)` says the monitoring is missing,
which no single document shows.

## Timeline

Timeline entries use absolute timestamps in the repository's declared zone, formatted per
[Timestamps](../timestamps.md). Relative offsets such as `T+5min` are never the primary form: they need an anchor to
mean anything, and the anchor is the first thing lost when an excerpt is quoted.

## Root Cause and Trigger Stay Separate

The trigger is what pulled the thread; the root cause is why pulling it did damage. A certificate expiring is a trigger.
Having no expiry monitoring and no automatic renewal is the root cause. Merge the two, and the action items renew this
certificate and leave the next one to expire the same way.

Name every contributing factor that existed. Fixating on a single cause produces one action item for an incident that
had four conditions.

## Resolution Separates Two Fixes

- **Applied fix** — what restored service.
- **Open root-cause fix** — what still has to change to prevent recurrence, carried into Action Items.

A post-mortem that records only the applied fix reads as finished while the condition that caused the incident remains.

## Luck Is Recorded

Luck that limited the damage belongs in What Went Well — recorded, not celebrated. It is a latent risk: the next
incident may not get it.

## Optional Sections

- **Background** — context a reader outside the incident needs. It may precede the Summary when the incident cannot be
  understood without it.
- **Supporting Data** — graphs, log excerpts, and metric snapshots, redacted. It follows References.
