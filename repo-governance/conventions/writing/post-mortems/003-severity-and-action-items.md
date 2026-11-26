---
description: >-
  Fixes the four-level incident severity scale and the action-item table: verb-led, owned, prioritized P0 to P2, and
  tracked to a plan or issue.
when_to_use: >-
  Use when classifying an incident's severity, or when writing or reviewing a post-mortem's action items.
---

# Severity and Action Items

## Severity Scale

Every post-mortem classifies its incident with exactly one tier, written as `Sev-N — Label`, for example
`Sev-3 — Moderate`.

| Tier  | Label    | Definition                                                                                           |
| ----- | -------- | ---------------------------------------------------------------------------------------------------- |
| Sev-1 | Critical | data loss, corrupted production state, or total outage of a production service or critical interface |
| Sev-2 | Major    | significant production degradation, or every change blocked from reaching the main line              |
| Sev-3 | Moderate | intermittent or single-component degradation with a workaround, and no data loss                     |
| Sev-4 | Minor    | cosmetic or low-impact; affects the development workflow rather than production users                |

This scale is the repository's only definition of incident severity. A second scale elsewhere — in a runbook, a tracker,
or a template — is where two incidents of the same kind start receiving different tiers.

## Action Items

Each action item is:

- **Actionable** — it starts with a verb.
- **Specific** — it names the system, file, or process that changes.
- **Bounded** — it has a clear definition of done.
- **Owned** — by a role.
- **Prioritized** — P0, P1, or P2.
- **Tracked** — by a plan or issue reference.

| Priority | Means                                                                                        |
| -------- | -------------------------------------------------------------------------------------------- |
| P0       | prevents recurrence or removes data-loss risk; done before the document's status is `closed` |
| P1       | an important improvement, scheduled promptly                                                 |
| P2       | worth doing, scheduled as capacity allows                                                    |

The table has exactly these columns:

```markdown
| #   | Action                                       | Owner      | Priority | Ticket          | Status |
| --- | -------------------------------------------- | ---------- | -------- | --------------- | ------ |
| 1   | Add expiry alerting for service certificates | Maintainer | P0       | <plan-or-issue> | Open   |
| 2   | Document the certificate renewal procedure   | Maintainer | P1       | —               | Open   |
```

`Ticket` holds a plan reference or an issue identifier. `—` means the item has not yet been promoted to one, which is a
temporary state; an empty cell is never used.

At least one action item addresses the root cause rather than the trigger, or the post-mortem states why none can. Items
that address only the trigger repair this incident and leave its cause in place.

## Anti-Patterns

| Wrong                | Why                                                               |
| -------------------- | ----------------------------------------------------------------- |
| "Fix the monitoring" | not specific, and no definition of done                           |
| Owner: "Team"        | an item everyone owns is an item nobody does                      |
| every item P0        | priority stops meaning anything, and `closed` becomes unreachable |
| Ticket left blank    | nobody can tell "not yet tracked" from "forgotten"                |
