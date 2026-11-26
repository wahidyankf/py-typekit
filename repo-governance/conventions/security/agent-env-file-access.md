---
description: >-
  Bars coding agents from reading, writing, or editing restricted environment files by any route, keeps every real
  environment file out of commits, and names the restricted-set and filename-pattern decisions.
when_to_use: >-
  Use when an agent needs an environment value, when configuring agent permissions or hooks, or when adding an
  environment tier or an agent harness.
---

# Agent Environment-File Access

A coding agent never reads, writes, or edits a restricted environment file by any route: not with its file tools, not
with a shell command that names the file, and not through a script it writes for that purpose. Running an existing
tracked project command that loads the values itself is the only sanctioned route. What an agent may read and what
anyone may commit are separate rules, and loosening the first never loosens the second.

## One Pattern Names Real Environment Files

The adopter records one filename pattern for real environment files, such as `.env` and `.env.*`, and the single
template filename it excludes, such as `.env.example`. Every enforcement layer matches that one recorded pattern.

A real file named outside the pattern escapes every layer. An environment-shaped example named outside it inside
documentation or teaching content is not a real environment file and falls outside the guards.

## The Restricted Set Is a Decision

The adopter chooses exactly one restricted set and records it in a tracked governance or configuration file:

| Option                      | Restricted from agents                            | Gains                                            | Costs                                                                  |
| --------------------------- | ------------------------------------------------- | ------------------------------------------------ | ---------------------------------------------------------------------- |
| everything but the template | every real environment file                       | no misnamed file exposes a secret                | debugging local or test configuration becomes a handoff                |
| named sensitive tiers       | files holding deployed values, such as production | local and test configuration stay open to agents | depends on naming discipline: a secret in an unrestricted file is open |

The first suits local files holding real credentials; the second suits throwaway local values beside deployed tiers that
hold everything that matters.

Under either option the committed template stays open to ordinary agent work; it holds names and placeholders only, per
[Environment Variable Contract](environment-variable-contract.md).

## Commits Stay Closed for Every Real File

No real environment file enters version history, whichever option applies; only the template is committable. Two
controls enforce this for every actor, not agents alone:

1. **Ignore rules** cover the recorded pattern, with the template re-included, so an ordinary stage cannot pick up a
   real file.
2. **The leak scan** at pre-push and in the pull-request gate, over all commits (equivalent for outbound safety),
   refuses any matching file, catching the forced add ignore rules cannot.

An ignore rule prevents accidents, not a deliberate force. An adopter wires the scan into its pre-push hook and
pull-request gate, and the permission deny and pre-tool hook listed under Enforcement into each agent harness it
supports.

## Existing Commands Are the Sanctioned Route

Tracked project commands may read and write environment files at runtime, and an agent may run them. The rule targets
the agent's direct access, not the work such a command exists to do.

The carve-out is a deliberate trust boundary: a tracked command was reviewed, and the leak scan still stands behind it.
A script an agent writes to reach a restricted file had no review, so it counts as direct access. Closing that route
mechanically would take a sandbox that also blocks legitimate commands, so this convention holds it instead.

Before treating a step as blocked, use a tracked command that already provides the value. If none does, the agent stops,
explains what is blocked and why, and hands the step to a person who can run it, per
[Private-Key and Secret Access](private-key-and-secret-access.md).

## Wrapper and Matrix

Each secret-bearing surface gains one tracked wrapper as its only secret-touching surface, with a closed executor-split
matrix: agent-runnable reads keep values out of output, human-only moves stay operator-terminal-only, and consumed
output to only its consumer stays allowed while any print to transcript stays refused.

## Census, Tiers, and Adoption

Each surface gains a census row recording location never value; unlisted stays reported as unlisted. Tiers stay
canonical versus non-canonical with one template per consumer and tier-free keys; no tier filename is universal.
Adoption: a member gaining a new secret-bearing surface gains its census row, wrapper/matrix, tier-vocab note, and
harness entry-point routing in the same delivery unit
([observations](agent-env-file-access/002-wrapper-census-tiers-adoption.md)).

## Enforcement Layers

Enforcement stays layered; [enforcement layers](agent-env-file-access/001-enforcement-layers.md) hold the table and its
gaps.
