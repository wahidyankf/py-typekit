---
description: >-
  Requires a plan touching a platform-deployed surface to probe the platform's agent integration server while planning
  and again at the start of execution, record the outcome, and keep account settings human-owned.
when_to_use: >-
  Use when a plan will observe or verify deployments through a deployment platform's agent integration server, or when
  executing or resuming such a plan.
---

# Deployment Platform Agent Capability

A connected agent integration server makes a deployment platform's state agent-readable: deployment status and
provenance, build logs, runtime logs, and runtime errors. That lets deployment-verification items be written `[AI]`
rather than `[HUMAN]` — but only in a session where the server is actually connected and authenticated. An executor
label is a claim about a capability, so the capability is probed, never remembered from a previous plan.

```binding-example
deployment platform: Vercel; agent integration server: the Vercel MCP server
```

## Scope Is Decided Mechanically

A plan is in scope when any of these holds:

1. a path it changes is covered by the platform's project configuration file;
2. it names a branch the platform deploys from;
3. it changes an application that a deployment agent or pipeline ships to the platform.

Decide from tracked files, never from a remembered list, because the set drifts. A plan that meets none of the three
probes nothing and records nothing; a vacuous check teaches readers to skip the section where it matters.

## Two Gates

| Gate                                               | Owner       | Decides                                                                 |
| -------------------------------------------------- | ----------- | ----------------------------------------------------------------------- |
| planning, before the delivery checklist is written | plan author | whether deployment-observation items are written `[AI]` or `[HUMAN]`    |
| execution, at its start, before any phase runs     | executor    | whether the checklist's assumption still holds or its items must change |

Both outcomes are recorded in the plan. An unrecorded probe leaves a later executor, in a session without the server,
facing `[AI]` items it cannot perform and no statement to check them against.

Probe again when resuming a plan after a pause, because connection state belongs to a session, and when a
deployment-observation step fails, before concluding that the deployment itself is broken.

## Three Outcomes

| Outcome                     | Consequence                                                   |
| --------------------------- | ------------------------------------------------------------- |
| connected and authenticated | deployment-observation items are `[AI]`                       |
| present, unauthenticated    | treated as absent until a human authenticates out of band     |
| absent                      | degraded mode; the plan still ships, its verification changes |

Judge by the tools the server offers, not by its connection status. A server that reports connected while offering only
authentication tools is unauthenticated.

## The Boundary

Observation and deployment are agent-reachable: projects, deployments and their provenance, build and runtime logs,
runtime errors, and triggering a deployment.

Account settings lie outside that boundary, so they stay `[HUMAN]` even with the server connected, on the Delivery
Contract's ground of access the executor does not have: billing and spend, paid observability tiers, firewall rules,
compute settings, and domain and DNS configuration. Group them into one early phase so the human work happens in a
single sitting and the rest of the plan stays executable.

Log counts prove volume and attribution; they never prove cost. A plan whose objective is a monetary figure cannot be
graded from logs. An acceptance command that queries logs states its time window and result limit explicitly, so a
truncated or timed-out query fails visibly instead of returning a partial answer.

## Degraded Mode

| Wanted                          | Fallback                                                    |
| ------------------------------- | ----------------------------------------------------------- |
| deployment state and provenance | the deploy branch history and the pipeline run that shipped |
| cache and header behaviour      | a request to the live URL, recording its response headers   |
| build failure diagnosis         | the pipeline job log                                        |
| per-route invocation volume     | none: the item becomes `[HUMAN]`, or the claim is dropped   |

State the degradation in the plan. An acceptance criterion that silently becomes unfalsifiable is worse than one openly
marked unavailable.

## Identifiers

Committed artifacts name projects and teams by slug wherever the interface accepts a slug, rather than by opaque
identifier. Identifiers grant nothing without a token, but they are stable, not practically rotatable, and permanent
once in a public history. Where the platform's deployment hostnames already carry slugs, using them exposes nothing new.

## Enforcement

Executor labels follow the [Delivery Contract](../../conventions/structure/plans/004-delivery-contract.md). An adopter
enforces the recorded probe and the boundary in its own plan checker and execution checker.
