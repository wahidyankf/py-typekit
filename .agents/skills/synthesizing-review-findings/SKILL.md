---
name: synthesizing-review-findings
description: >-
  Guides the review coordinator in deduplicating, re-categorizing, filtering, and verifying specialist findings, so only
  findings that survive all four reach the one consolidated review and a critical finding carries a reproduction.
when_to_use: >-
  Use when acting as the coordinator of a multi-reviewer pass, merging raw findings into the single review that pass
  publishes.
compatibility: Requires read access to the change, the shared review brief, and every specialist's raw findings.
---

# Synthesizing Review Findings

[PR Review](../../../repo-governance/workflows/quality/pr-review.md) owns the pass and its single post. The review
discipline modules own the rules applied:
[Boundary Rulings](../../../repo-governance/development/agents/review-disciplines/002-boundary-rulings.md) the
tie-breaker,
[Finding Requirements](../../../repo-governance/development/agents/review-disciplines/003-finding-requirements.md) what
a finding needs, and
[Cost and Noise Controls](../../../repo-governance/development/agents/review-disciplines/004-cost-and-noise-controls.md)
suppression and dismissals. This skill covers the coordinator's judgement in applying them.

## Four Functions, All Required

A raw finding reaches the review only after all four. None is skipped because a finding looks obviously right.

1. **Deduplicate.** Findings describing one defect become one, keeping the strongest evidence and naming every
   discipline that raised it. Two findings on one line about different defects stay two.
2. **Re-categorize.** Apply the tie-breaker to decide which discipline owns each finding. A specialist never has the
   last word on its own category, and the boundary between architecture and correctness is misjudged most often, so it
   is always checked.
3. **Filter for reasonableness.** Drop what the suppression list names, what the declared scope excludes, and what a
   person already dismissed. A real finding in unusable wording is rewritten where it stands, never dropped.
4. **Verify.** Re-run or re-read the evidence each finding cites against the pinned head. A finding whose evidence does
   not reproduce does not post.

## Severity Needs Evidence

Agreement between specialists is not evidence: it never raises a finding's severity or carries it past the confidence
floor. A critical finding posts as critical only with a reproduction attached; without one it is held lower until one
exists.

## One Review, Anchored

Everything that survives goes into the single consolidated review, one line-anchored thread per finding, so the repairer
can answer and resolve each where it lives. A pass that surfaces nothing still publishes its clean review. The
coordinator never writes a finding's answer into the review; answering belongs to
[resolving-review-threads](../resolving-review-threads/SKILL.md).

## Related

- [producing-review-findings](../producing-review-findings/SKILL.md) — what a specialist hands over.
- [classifying-review-scope](../classifying-review-scope/SKILL.md) — how the pass chose its specialists.
