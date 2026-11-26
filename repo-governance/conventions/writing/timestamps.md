---
description: >-
  Fixes timestamps as ISO 8601 with an explicit offset in one declared zone, requires values generated from the clock
  rather than typed, and leaves the choice of zone to the adopter.
when_to_use: >-
  Use when a script, agent, or author records the time something happened, or when a repository settles which zone its
  recorded times share.
---

# Timestamps

Every timestamp a repository writes is ISO 8601 with an explicit offset, in the one time zone the repository declares,
and is generated from the clock rather than typed.

## Format

| Use              | Form                        | Example                     |
| ---------------- | --------------------------- | --------------------------- |
| a full timestamp | `YYYY-MM-DDTHH:MM:SS±HH:MM` | `2025-11-30T22:45:00+09:00` |
| a date           | `YYYY-MM-DD`                | `2025-11-30`                |
| a filename       | `YYYY-MM-DD--HH-MM`         | `2025-11-30--22-45`         |

Hours run `00` to `23`, `T` separates date from time, and the offset keeps its colon, which makes the full form valid
RFC 3339 as well.

| Wrong                         | Why                                                            |
| ----------------------------- | -------------------------------------------------------------- |
| `2025-11-30T22:45:00`         | no offset, so it names a different moment in every zone        |
| `2025-11-30 22:45:00+09:00`   | a space where `T` belongs                                      |
| `11/30/2025`                  | month and day order depends on the reader's locale             |
| any zone but the declared one | valid ISO 8601, but it no longer compares or sorts at a glance |

## Why an Explicit Offset

A timestamp without an offset does not name a moment; it names a wall-clock reading that occurred at a different moment
in every zone. The offset lets two timestamps be compared without knowing where either was written, and year-first
ordering lets them sort as text.

## Why One Declared Zone

The offset already makes a full timestamp unambiguous, so the declared zone serves people, not parsers. Timestamps in
one zone compare at a glance and sort identically as text and as time. The filename form carries no offset, so only the
declared zone says which moment `2025-11-30--22-45` names.

## The Adopter's Decision: Which Zone

| Zone                | Gains                                                                        | Costs                                                                 |
| ------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| UTC                 | matches servers, hosted logs, and most interfaces; no daylight-saving shifts | a team converts to local time, and dates roll over mid-working-day    |
| a team's local zone | timestamps read as wall-clock time, and dates match working days             | conversion against UTC systems, and daylight saving shifts the offset |

Three rules follow from the zone decision:

1. **Declare the zone once**, in the repository's instructions, as an IANA identifier such as `Etc/UTC` or
   `<area>/<city>`. An identifier carries the zone's daylight-saving rules; a bare offset does not.
2. **Outside UTC, derive the offset from the zone.** A daylight-saving zone changes its offset during the year, so a
   typed offset is right for only part of it.
3. **A declared UTC zone writes the offset as `Z`**, as the UTC commands below produce.

## Generate, Never Type

A timestamp is produced by running a command at the moment it records. A placeholder such as `00-00`, a guessed time, or
a time copied from an earlier report is never written.

A placeholder defeats the only purpose a timestamp has: reports stop sorting into the order they happened, an audit
trail records times at which nothing occurred, and no reader can tell the invented value from a real one. This binds
agents especially — an agent that writes a timestamp without running a clock command has made it up.

```bash
date -u +%Y-%m-%dT%H:%M:%SZ        # full timestamp, UTC
date -u +%Y-%m-%d--%H-%M           # filename, UTC
TZ='<zone>' date +%Y-%m-%d--%H-%M  # filename, another zone
python3 -c 'from datetime import datetime; from zoneinfo import ZoneInfo; print(datetime.now(ZoneInfo("<zone>")).isoformat(timespec="seconds"))'
```

The `date` forms behave the same in GNU and BSD. Outside UTC, a full timestamp uses the last line, because `date` cannot
portably print an offset with its colon.

## Where It Does Not Apply

- **Version-control commit times** — the tool records its own, with the author's offset.
- **An external interface that requires UTC** — send what the interface specifies.
- **Timestamps shown to users** — display in the reader's zone and locale.
- **Database storage** — follow the engine's convention, usually UTC, converting on display.

Out of scope: relative times such as "two hours ago", interface date formatting, and how applications parse timestamps.

## Enforcement

An adopter validates the timestamps its own tools write — report headers, cache fields, and generated filenames —
against this format in its own gate.
