---
description: >-
  Forbids tests from touching production users, data, or credentials, and requires synthetic data inside a marked
  per-run boundary that is validated before use and removed exactly afterwards.
when_to_use: >-
  Use when a test, fixture, or manual check needs users, accounts, stored data, or credentials, or when designing test
  setup, parallel workers, or cleanup.
---

# Test Data Isolation

A test that touches real data can harm a real person, and a test that shares data with another test proves nothing about
either. One control prevents both: a boundary each run owns and proves before use.

This standard implements [Fail Closed](../../../principles/fail-closed.md) and
[Reproducibility](../../../principles/reproducibility.md).

## Production Is Out of Reach

No automated or manual test reads, writes, authenticates against, migrates, derives fixtures from, or otherwise touches
production users, data, credentials, or a production user's context, such as acting inside a real user's session. No
exemption, debug session, local environment, or convenient fixture relaxes this.

Tests use synthetic data only, inside a per-run boundary that is validated before the subject starts. When isolation
cannot be proven, setup fails and the subject never runs.

## Each Run Owns a Marked Boundary

| Resource            | Isolated as                                 |
| ------------------- | ------------------------------------------- |
| the run             | a unique run identifier                     |
| files and databases | a root created for this run alone           |
| processes and ports | a separate namespace or a leased port       |
| browser             | a fresh context carrying no earlier session |
| identities          | synthetic accounts created for this run     |

Mark every owned resource before using it. Where an identity takes a username, prefix it `test-user-` so it is
unmistakable in any listing. Never modify an existing identity to impersonate another; that changes someone else's
state.

Setup rejects a root that resolves inside a production location, lacks its ownership marker, or is unexpectedly shared
with another run. Resolve symbolic links before checking, because a path that looks temporary can point anywhere.

## Parallel Workers Never Collide

Parallel workers use distinct identities and distinct paths. No test asserts a mutable aggregate, such as a total
account count or the newest record, because another worker changes it mid-run.

## Synthetic Content Only

Payloads are invented for the test. Content, sessions, cookies, tokens, and identifiers from any real account never
enter fixtures, snapshots, logs, or reports.

Where a test needs the real system's shape, inspect it read-only and structurally — schema versions, record types, field
names, value types — and record only a value-free pass or fail.

## Clean Up Exactly What Was Created

Cleanup runs in guaranteed teardown, after browsers, servers, and child processes have stopped. It removes only the
exact resources validated as owned by this run.

Deletion never selects by a broad glob, a username prefix, or age alone. Each of those eventually matches something the
run did not create.

A cleanup failure fails the test and reports only the safe synthetic location. Leftover data is not cosmetic; it breaks
the assumptions of the next run. The adopter enforces the boundary and marker checks in its own test harness or gate.

## Related Standards

- [End-to-End Testing](end-to-end-testing.md) owns per-case fixture trees.
- [Git Fixture Isolation](git-fixture-isolation.md) applies the same boundary to repositories that tests create.
- [Evidence Safety](../manual-verification/005-evidence-safety.md) owns what recorded evidence may contain.
