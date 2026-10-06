---
description: >-
  Defines the four criticality levels, the order in which one is assigned, fixed adjustments for builds, security,
  accessibility, and requirement keywords, and which levels block a gate.
when_to_use: >-
  Use when a checker assigns criticality to a finding, or when deciding whether a finding blocks a quality gate.
---

# Criticality Levels

Criticality measures how much a problem matters, independent of how certain anyone is about it.

## Four Levels

- **`CRITICAL`** — Meaning: breaks functionality, blocks users, weakens security, loses data, or violates a MUST;
  Examples: a failing build, an exposed credential, a broken required link
- **`HIGH`** — Meaning: significantly degrades quality, or violates a documented SHOULD convention; Examples: an
  accessibility failure at level AA, misleading documentation
- **`MEDIUM`** — Meaning: a minor quality issue, a style inconsistency, or a MAY guideline not followed; Examples:
  inconsistent formatting, missing optional metadata
- **`LOW`** — Meaning: a suggestion that would improve an already acceptable artifact; Examples: alternative wording, an
  optional reorganization

## Assign in Order

Stop at the first question answered yes:

1. Does it break something, block a user, weaken security, lose data, or violate a MUST? `CRITICAL`.
2. Does it seriously lower quality, or break a documented SHOULD convention? `HIGH`.
3. Does it amount to a minor quality issue, a style inconsistency, or an unfollowed MAY? `MEDIUM`.
4. Otherwise, `LOW`.

Asking in this order stops a finding from being rated by how easy it is to fix rather than by what it does.

## Fixed Adjustments

Some contexts fix the level whatever category the finding came from:

| Context                                               | Level      |
| ----------------------------------------------------- | ---------- |
| a build failure, or a security weakness of any kind   | `CRITICAL` |
| an accessibility failure at WCAG conformance level A  | `CRITICAL` |
| an accessibility failure at level AA                  | `HIGH`     |
| an accessibility failure at level AAA                 | `MEDIUM`   |
| an unmet MUST or MUST NOT requirement                 | `CRITICAL` |
| an unmet SHOULD or SHOULD NOT requirement             | `HIGH`     |
| an unfollowed MAY guideline, or a style inconsistency | `MEDIUM`   |
| a style preference                                    | `LOW`      |

Requirement keywords carry the meanings given in [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119).

## What Blocks

| Level           | Effect on a gate                                                                        |
| --------------- | --------------------------------------------------------------------------------------- |
| `CRITICAL`      | always blocks; the gate cannot pass until it is fixed                                   |
| `HIGH`          | fixed before publication; blocks unless explicitly dispositioned with a recorded reason |
| `MEDIUM`, `LOW` | never blocks; reported, and each one left unfixed still carries an explicit disposition |

Results and dispositions follow [Quality Gate Results][001-quality-gate-results]. Treating `HIGH` as blocking unless
dispositioned is deliberately the stricter choice: a significant problem left without a recorded decision is silence,
and silence afterwards looks exactly like oversight.

## Status Labels Stay Separate

Some checkers also mark each item's observed status, such as verified or broken. Those labels say what was seen;
criticality says how much it matters. A report keeps both.

[001-quality-gate-results]:
  https://github.com/wahidyankf/ose-rules/blob/97f4d1ca35b5ab65a4f60aff724e210e638d87f4/repo-governance/development/quality/manual-verification/001-quality-gate-results.md
