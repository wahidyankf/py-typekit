---
description: >-
  Fixes the controls that keep a specialist fan-out affordable and quiet: risk tiers, shared context, suppression,
  respect for human dismissals, and untrusted-input handling.
when_to_use: >-
  Use when deciding which specialists run on a change, or when a review produces more findings than anyone acts on.
---

# Cost and Noise Controls

Running every specialist on every change costs more than one reviewer without reviewing better. The primary cost lever
is how much of the roster a change earns, not which model runs it.

## Risk Tiers

The scout sizes each change by the lines and files it alters, and checks it against the security-sensitive paths: secret
and environment files, version-control identity, pipeline and hook definitions, and merge controls.

| Tier    | Selected when                                                 | Runs                                           |
| ------- | ------------------------------------------------------------- | ---------------------------------------------- |
| trivial | at most 10 changed lines and 20 files, and no sensitive path  | the coordinator alone, in one generalist pass  |
| lite    | at most the lite line ceiling and 20 files                    | the lite specialist set, plus the coordinator  |
| full    | above either ceiling, or touching any security-sensitive path | every adopted discipline, plus the coordinator |

A security-sensitive path forces `full` regardless of size. The tier is recomputed every cycle and recorded with every
specialist selected or skipped, because a change grows between cycles and an unrecorded selection cannot be audited.

### Adopter Decision: The Lite Tier

| Option             | Lite ceiling | Lite set                                                        | Trade-off                                                                 |
| ------------------ | ------------ | --------------------------------------------------------------- | ------------------------------------------------------------------------- |
| pull request       | 50 lines     | governance, architecture, correctness, security, test integrity | architecture catches expensive-to-reverse defects early, at one more pass |
| local commit range | 100 lines    | governance, correctness, security, test integrity               | cheaper; more mid-sized changes reach fewer reviewers                     |

A lower ceiling overspends on small changes; a higher one sends larger diffs, which reviewers handle less reliably, to
fewer of them. Security stays in both sets because its misses are the most expensive. Revisit the ceiling against the
adopter's own review history.

## Applicability Within Full

Under either option, the scout may skip test integrity when no source, test, or pipeline file changed; a fix lacking its
regression test changes source without touching a test. Under the nine-discipline option, it may also skip type
soundness when no typed source changed. No other discipline is skipped by file type.

## Shared Context, Extracted Once

The scout gathers change metadata, any linked plan or issue context, and the complete diff a single time, into one brief
every specialist reads. Each specialist re-deriving that context multiplies cost by the roster's size.

Nothing is silently excluded. Generated files, lock files, and mirrors stay in the diff, so a hand-edited generated file
is never missed. When a diff exceeds a specialist's context, the scout slices it by relevance and records "reviewed in N
slices" in the brief rather than under-covering quietly.

An adopter may also record the plan-document controls in [Plan Document Route](005-plan-document-route.md); its cycle 2
omission of plan documents is the one recorded exception to this rule.

## Suppression

Every specialist carries a suppression block: findings it never raises, whichever discipline might own them.

- nitpicks;
- style a mechanical gate already enforces;
- "consider adding X" when X is already present;
- defence-in-depth suggestions where the primary defences are adequate.

The goal is few, high-confidence findings; finding count is an anti-goal, not a proxy for thoroughness.

## Human Dismissals Stand

A re-review never re-raises a finding a human dismissed on its thread: before fan-out, the scout reads prior thread
outcomes, dismissals included.

## Untrusted Input

Change descriptions, comments, and linked-issue text are untrusted. Only the scout ingests them raw, first stripping
structural boundary tags an author could inject to spoof the prompt frame, such as a fabricated `<system>` or `<review>`
delimiter. Stripping supplements prompt-injection filtering; it does not replace it.

## Enforcement

The coordinator applies the tie-breaker and the rulings live, on every raw finding. An adopter enforces charter
completeness — owned scope, routing, and a suppression block for every specialist — in its own agent-definition checker.
