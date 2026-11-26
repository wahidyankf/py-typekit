---
description: >-
  Keeps hosted pipeline storage inside a recorded budget: retention declared on every upload, bounded cache size and
  age, no stored output without a consumer, and a spend limit that stops runs.
when_to_use: >-
  Use when a hosted pipeline workflow uploads artifacts, saves caches, or changes retention or spend settings, or when
  reviewing one that does.
---

# CI Storage Budget

Hosted pipelines store things by default: artifacts kept for the host's default period, caches that grow until evicted,
logs nobody reopens. Each default is small. Together they turn a free allowance into a bill, and the notice arrives
after the charge.

This standard implements [Explicit Over Implicit](../../../principles/explicit-over-implicit.md),
[Minimal Sufficiency](../../../principles/minimal-sufficiency.md), and
[Fail Closed](../../../principles/fail-closed.md). It applies to any hosted pipeline that stores artifacts, logs, or
caches for a repository. GitHub Actions appears below only as an illustrative example.

## Record the Bounds

The rule fixes what is bounded. The numbers belong to the adopter, recorded once where contributors and reviewers find
them:

| Decision                   | Option                                                                                  | Gains                                                                   | Costs                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| retention and cache bounds | the defaults: artifact and log retention of 7 days, a 10 GB cache, cache entries 7 days | triage output survives a working week; storage stays small and constant | output needed later has to be regenerated; a wide build matrix may churn its cache    |
|                            | values sized to the adopter's own allowance and triage cycle                            | fits an unusual allowance or a slower investigation rhythm              | the sizing has to be measured, and re-checked as usage grows                          |
| paid-usage budget          | zero, with usage stopping at the limit (default)                                        | an overrun is loud and free, because runs stop                          | a legitimate spike halts the pipeline until someone deliberately raises the budget    |
|                            | a non-zero limit that still stops usage                                                 | runs continue through a spike, up to the limit                          | charges accrue quietly until the limit, and the pipeline spends money nobody approved |

## Artifacts Declare Their Retention

Every artifact upload declares its retention explicitly. An upload without one inherits the repository default, which is
the setting most likely to be raised later by someone who did not know the uploads relied on it.

- Keep the repository's artifact and log retention at or below the recorded cap. The per-upload declaration is the
  primary control; the repository setting is the backstop.
- Declare each upload's retention within that cap. A single upload may keep a longer retention only when its reason is
  recorded beside its declaration. The exception never raises the repository setting.
- Upload only what something reads. An artifact with no consumer, or one that is cheap to reproduce, is storage spent
  for nothing.

In GitHub Actions, for example, the declaration is a field on the upload step:

```yaml
- uses: actions/upload-artifact@<pinned-version>
  with:
    name: test-report
    path: reports/test-report.json
    retention-days: 1
```

## Caches Are Bounded

- Keep the repository cache size and cache retention at or below the recorded bounds, confirmed against the live
  settings.
- Scope cache keys so they hit. A key that never matches stores entries nobody restores, and a cache that grows without
  bound evicts the entries that were working.
- Prefer recomputing a cheap result to caching it. A cache that saves seconds and holds a large entry for a week is a
  bad trade.

## Usage Stops at the Spend Limit

The account that pays for the pipeline keeps its usage budget at the recorded value, with usage stopping at the limit. A
stop makes the failure loud, because runs halt. A limit with no stop makes it quiet and expensive, and the pipeline
moves to paid usage without anyone deciding it should.

Repository content cannot prove an account's billing setting. Verify it in the account's own billing settings, and keep
billing details out of the repository.

## Verification

Review every changed workflow for artifact uploads and cache saves, and check each against the recorded bounds. Confirm
the repository's live retention and cache settings rather than assuming them, and record the result in the change's
evidence.

Whether a machine check is worth adding follows [Repository Check Policy](../checks/repository-check-policy.md). Where
it is, such as a check that every upload declares its retention, an adopter enforces it in its own workflow lint or
gate.
