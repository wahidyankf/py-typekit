---
description: >-
  Fixes the three-step tie-breaker for a finding that fits no single discipline, and the pre-decided rulings for the
  recurring borderline cases.
when_to_use: >-
  Use when a finding could plausibly belong to two disciplines, or when re-categorizing a misfiled finding.
---

# Boundary Rulings

## The Tie-Breaker

When a finding does not clearly belong to one discipline, apply these in order and stop at the first that fits:

1. **A documented rule a mechanical check could confirm → governance.** A written convention already states the rule,
   and a search, linter, or structural check could in principle detect the violation.
2. **A new tradeoff no rule covers → architecture.** Architecture makes the call, and the resolution is written down as
   a rule so the next occurrence stops at step 1.
3. **Whether the change does what the domain requires → correctness.**

The order runs from most to least checkable. A finding an existing rule already settles should never cost a fresh
judgement, and a judgement made once should become a rule so it is not made again.

## The Highest-Risk Boundary

Architecture and correctness are the pair most easily confused: a structural decision and a domain-behaviour question
can read identically as raw findings. The coordinator owns re-categorizing across this boundary, and once it has placed
a finding, no specialist re-adjudicates the placement.

## Grey-Zone Rulings

These cases recur. Each is the tie-breaker already applied, recorded so the coordinator looks it up instead of deriving
it again every cycle — and so two cycles never place the same kind of finding differently.

- **(a) A new cross-module dependency.** It breaks an existing layering rule → governance. It raises a boundary question
  no rule answers → architecture.
- **(b) Naming versus existence.** Does it follow the documented naming or structure pattern → governance. Should the
  module boundary exist at all → architecture.
- **(c) Error handling.** Does it match the documented error-handling shape → governance. Does it cover the domain's
  actual error scenarios → correctness.
- **(d) Specifications.** Is a required specification file present → governance. Are its scenarios complete for the
  domain → correctness.
- **(e) Performance and design.** A deliberate choice to give up some performance in exchange for a better design →
  architecture. A concrete or likely regression on a hot path → performance.
- **(f) Documentation.** Mechanical conformance such as heading hierarchy, linking, and naming → governance. Substantive
  completeness, clarity, or drift from the code → documentation.
- **(g) Compiles, sound, or should exist.** This boundary has three sides. Use of a type escape hatch → type soundness,
  whether or not the build passes. Whether the code compiles → the build, not a review finding. Whether a new type or
  module boundary should exist → architecture, as in ruling (b).

Ruling (g) exists only where the type-soundness discipline is adopted. Under eight disciplines, escape-hatch findings
follow the tie-breaker like any other finding.

## Worked Placements

**Governance, not architecture.** A new file ignores the documented lowercase kebab-case naming pattern. Ruling (b)
applies: a mechanically checkable rule already covers it, so the finding is governance's even though naming touches
structure.

**Performance, not architecture.** A change adds a quadratic loop inside a request handler known to sit on a hot path.
Ruling (e) applies: nothing is being traded off, and the regression is a fact about the code rather than a design
decision.

**Misfiled and corrected.** A specialist files "this service should validate the refund window" under architecture. The
coordinator reads it as a question of whether the change does what the domain requires, with no structural decision
involved, and moves it to correctness. The architecture specialist does not contest the move.
