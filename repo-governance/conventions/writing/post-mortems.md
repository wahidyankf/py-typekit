---
description: >-
  Defines the blameless incident post-mortem: where it lives and how it is named, its required sections in order, a
  four-level severity scale, tracked action items, and redaction.
when_to_use: >-
  Use when an incident needs a written retrospective, or when naming, drafting, classifying, or reviewing a post-mortem.
---

# Post-Mortems

A post-mortem is the permanent record of an incident: what happened, why each decision made sense when it was made, and
what will change so the same conditions do not produce the same failure.

It exists for two things. **Learning** — an accurate account of how the system behaved under stress. **Improvement** —
owned, prioritized action items that reduce the chance or the cost of a recurrence. It is never a punishment mechanism,
and a document that reads like one stops receiving honest accounts the next time one is needed.

## Modules

1. [Naming and Blameless Framing](post-mortems/001-naming-and-blameless-framing.md)
2. [Required Sections](post-mortems/002-required-sections.md)
3. [Severity and Action Items](post-mortems/003-severity-and-action-items.md)

## Scope

In scope: the document — its location, name, framing, sections, severity, action items, status, and redaction.

Out of scope: responding to an active incident, on-call and escalation policy, and running the review meeting. Those are
operational procedures with homes of their own; a post-mortem is written after them, about them.

## Write It Promptly

Write the post-mortem within days of the incident, while memory and logs are both still fresh. Delay costs timeline
accuracy first and action-item momentum second, and neither comes back.

## Status

The document records its own status in frontmatter as `doc_status`:

| Status     | Means                                                                                     |
| ---------- | ----------------------------------------------------------------------------------------- |
| `draft`    | written, possibly with gaps                                                               |
| `reviewed` | factual accuracy confirmed by a second perspective: a peer, a second reading, or the logs |
| `closed`   | every P0 action item is done; the document is the settled record                          |

Document status is distinct from the incident's own state, which the metadata table records. An incident can be resolved
while its post-mortem is still a draft, and the two must never be read as one.

## Nothing Secret

A post-mortem is committed and permanent, and incident material — log excerpts, configuration, connection strings — is
exactly where secrets surface. Replace every sensitive value with a named placeholder such as `<api-token>`,
`<db-connection-url>`, or `<private-host>`, and say where the real value lives without stating it.

In a public repository the document is outbound material and passes
[Public Outbound Safety](../security/public-outbound-safety.md) like any other.

A diagram of a causal chain or a triage sequence follows [Diagrams](diagrams.md).
