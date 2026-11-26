---
description: >-
  Makes one committed, annotated template the contract for every environment key, with upper snake case tier-free names,
  fail-fast validation, and a census of where real values live.
when_to_use: >-
  Use when adding, renaming, or removing an environment variable, or when adding a place that holds real values.
---

# Environment Variable Contract

Every environment key a program reads is declared, by name, in one committed template. It holds no real value and is the
one place a reader learns what a program needs. Its filename and the pattern naming real environment files are recorded
as [Agent Environment-File Access](agent-env-file-access.md) requires.

## The Template Is the Contract

The template and the code agree in both directions: a key the code reads but the template omits, or one the template
declares but nothing reads, is drift and fails. Reads by every shared library the consumer uses count. An adopter
enforces this in its own pull-request gate.

A recorded, reviewed exemption list excuses only declared keys read by a platform or launcher, not the consumer; it
never hides a read the validator misses, which is fixed at its read site.

Template values are placeholders nobody could mistake for real: a plausible one gets copied into real files unchanged.

## Layout Is a Decision

| Option                            | Suits                    | Costs                                   |
| --------------------------------- | ------------------------ | --------------------------------------- |
| one template at the root          | a single consumer        | mixes keys once a second consumer lands |
| one template beside each consumer | several deployable units | one more file per unit                  |

Each consumer has exactly one template. A shared library owns none; every consumer using it declares the keys it reads,
because the consumer is what moves between environments.

## Annotation Depth Is a Decision

| Option     | Each key carries                                                       | Gains                                                | Costs                                         |
| ---------- | ---------------------------------------------------------------------- | ---------------------------------------------------- | --------------------------------------------- |
| structured | requiredness, type or format, description; optional keys commented out | no code lookup; commented-out keys keep it parseable | more to write and keep true                   |
| minimal    | a one-line description and an empty value                              | cheap to write and read                              | readers learn requiredness and type from code |

```text
# REQUIRED | url | Connection string for the primary database
DATABASE_URL=<database-url>

# OPTIONAL | integer | Listener port (default: <default-port>)
# SERVICE_PORT=
```

## Names Are Upper Snake Case and Carry No Tier

Keys are upper snake case, one spelling each, because a case-insensitive platform merges spellings the code treats as
distinct. A key keeps its name in every environment (`DATABASE_URL`, never `PROD_DATABASE_URL`), and the file or
injection supplying the value chooses the environment.

A tier in the name forks the contract, and the production-only name is first read in production.

## Consumer Prefixes Are a Decision

| Option                  | Example                  | Gains                                              | Costs                                    |
| ----------------------- | ------------------------ | -------------------------------------------------- | ---------------------------------------- |
| prefix app-defined keys | `<CONSUMER>_API_TIMEOUT` | visible ownership; no collisions in a shared scope | longer names; exempt names must be known |
| no prefix               | `API_TIMEOUT`            | short names matching library defaults              | consumers sharing a scope can collide    |

Framework-reserved and conventional shared names such as `NODE_ENV` stay unprefixed, and a prefix never names a tier.

## Precedence

A value already in the process environment is never overridden by a file, so automation runs with no file on disk and an
injected value beats a stale local copy.

## Fail Fast

A missing required value, or one that does not parse, stops the program at startup or build and names the key; it never
falls back to a default. A silent default hides a configuration error until it surfaces elsewhere. See
[Fail Closed](../../principles/fail-closed.md).

## Census of Secret Surfaces

A tracked census records where every real value lives:

| Column     | Records                                                                                                                                                                    |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| surface    | an ignored environment file, secrets directory, platform environment, or secret store                                                                                      |
| location   | a repository-relative path or platform scope, never a value; by kind, not account or project identifier, where [Public Outbound Safety](public-outbound-safety.md) applies |
| managed by | the loader, platform, or client that reads or manages it                                                                                                                   |
| backed up  | whether losing the machine loses the value                                                                                                                                 |
| validated  | what checks it against the contract, if anything                                                                                                                           |

Rotation starts from the census: a surface nobody listed is one nobody rotates.
[No Secrets in Tracked Files](no-secrets-in-tracked-files.md) owns leaks.
