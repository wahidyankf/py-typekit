---
description: >-
  Holds the procedure of the swe-web-tester agent, moved verbatim from its definition so the definition fits its word
  budget.
when_to_use: >-
  Use when swe-web-tester judges a running web interface and its definition points here.
---

# SWE Web Tester Procedure

Moved verbatim from [swe-web-tester](../../../../agents/swe-web-tester.md), which links each section here, per
[Document Word Budget](../../../conventions/structure/document-word-budget.md).

## Procedure

1. **Sweep before browsing.** Run the functions of
   [Enumerated Coverage](../../quality/manual-verification/007-enumerated-coverage.md) the charter needs: consistent
   styling for `design`; shared controls, state round-trips, and declared invariants for `spec` and `exploratory`.
2. **Judge under the charter.** `spec` answers the gate's cycle questions, using
   [Exploratory Testing](../../../../.agents/skills/exploratory-testing/SKILL.md) for empty, error, and loading states
   and [Developing Frontend UI](../../../../.agents/skills/developing-frontend-ui/SKILL.md) for focus order, keyboard
   paths, and names. `design` compares each observation with the sources
   [Design-Fidelity Pass](../../../workflows/quality/ux-review-fix-planning/001-design-fidelity-pass.md) lists, as
   [Design Fidelity Review](../../../../.agents/skills/design-fidelity-review/SKILL.md) teaches. `exploratory` runs
   varied tours, probing boundary, invalid, repeated, and out-of-order input, and recomputes any shown total or
   ordering.
3. **Tell a defect from a gap.** Behaviour contradicting a cited source is a defect that quotes it. Correct behaviour no
   scenario protects becomes a scenario proposal, written as
   [Writing Gherkin Criteria](../../../../.agents/skills/plan-writing-gherkin-criteria/SKILL.md) teaches, never written
   into a specification.
4. **Close with the completeness critic** of
   [Usability Probes and Completeness](../../quality/manual-verification/008-usability-probes-and-completeness.md),
   recording each category never enumerated as an open gap.
5. **Rate and record** each finding with its route, viewport class, locale, theme, state, the source it departs from,
   reproduction steps with placeholder credentials, and a criticality from
   [Criticality Levels](../../quality/evidence/finding-criticality-and-confidence/001-criticality-levels.md). A tester
   rating on another severity scale maps severity, never priority, onto it.
