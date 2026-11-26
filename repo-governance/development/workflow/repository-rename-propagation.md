---
description: >-
  Treats a repository rename or ownership move as incomplete until a sweep replaces the old name in every file, setting,
  and machine-stored endpoint that uses it, verified by writes rather than reads, and recorded.
when_to_use: >-
  Use when renaming a repository or moving it to another owner, or when writes such as status reports, releases, or
  image pushes start failing after one.
---

# Repository Rename Propagation

A repository rename is finished when nothing uses the old name any more, not when the hosting service accepts the new
one. The service usually keeps the old path answering, making an unfinished rename look finished.

This standard implements [Evidence Over Assertion](../../principles/evidence-over-assertion.md) and
[Explicit Over Implicit](../../principles/explicit-over-implicit.md).

## Why Reads Pass and Writes Fail

Hosting services commonly redirect a renamed repository's old path. Reads follow the redirect: a clone, page, or status
query succeeds, so a read-based health check reports everything working.

A changing API request sent to the old path can come back as an unapplied redirect, which clients commonly do not repeat
against the target; the call fails, or the client counts the redirect as a result. Reporting a status, creating a
release, commenting, dispatching a workflow, and pushing an image are the calls that break, and they are rarely watched.

A redirect also holds only while nothing else claims the old name. Once another repository takes it, every stale
reference reaches the wrong one.

## The Rule

A rename is incomplete until a sweep has replaced the old name on every surface where it can appear, and a write through
each affected path has succeeded. Every hit counts, documentation included, because examples are copied into new
automation.

| Surface                                  | Where the old name hides                                                                                  |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| tracked scripts and pipeline definitions | remote addresses, API paths, owner-and-name pairs, and fallback values                                    |
| service and deployment definitions       | arguments and environment defaults passed to services, and webhook targets                                |
| container images                         | image names, tags, and runner labels derived from the repository name                                     |
| remote settings                          | the remote address in every checkout and mirror, branch rules, and deploy keys                            |
| machine-stored configuration             | registered runners and agents, pipeline secrets and variables, and endpoints saved outside any repository |

A registered agent keeps the address it was registered with. Reads through the redirect keep it running, and its first
write, often its own removal, fails. Re-register each agent at rename time, or record its stale endpoint as an open item
keeping the rename incomplete.

## The Sweep

1. **Search every spelling.** Search the repository, hidden files included, and each repository that refers to it, for
   the full address, the owner-and-name pair, the bare name, and any lowercased or registry form. Match the name joined
   to other words, and search separately for any shorthand.
2. **Order the hits by what breaks first.** Writes in deployment and pipeline automation, and defaults that feed them,
   come first; then reads and references elsewhere; documentation last.
3. **Fix in that order,** one surface at a time, naming the old name in each fix's commit message for history searches.
   A fix to code or declarative configuration is made by `swe-developer`, per
   [SWE Delegation](../agents/swe-delegation.md).
4. **Search each host.** Service-manager definitions, shell profiles, and personal scripts on every machine running the
   automation lie outside any repository. Restart every long-running process that read the old name; a changed file does
   nothing until the process reloads it.
5. **Verify with the write each path performs.** A check proves an operation only when it uses the same kind of request.
   A clean search and a green read prove nothing alone: a value can survive in a secret or deployed file.
   [Automation Loop Observability](../quality/delivery/automation-loop-observability.md) keeps the redirect visible in
   logs.
6. **Search again** for every spelling of the old name. A clean final search is necessary, not sufficient, and a count
   of replacements is not verification.

## Record the Rename

Record the old and new names, when the rename happened, and the repository's stable identifier where the service has
one. A redirect response often cites that identifier rather than either name, so the record connects the two. The record
is the one place the old name stays.

## Enforcement

An adopter may run the final search, excluding the rename record, in its own gate after a rename, so a reintroduced old
name fails.
