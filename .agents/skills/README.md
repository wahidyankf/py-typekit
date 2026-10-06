---
description: >-
  Indexes this repository's canonical skills, one directory per skill, each holding the SKILL.md a harness reads and the
  resources that skill resolves beside it.
when_to_use: >-
  Use when locating a canonical skill or deciding where a new skill's resources belong.
---

# Canonical Skills

Skills in their canonical form. One directory per skill, each containing a `SKILL.md` and whatever resources that skill
resolves relative to its own directory.

Codex and OpenCode read this layout natively, so for those harnesses the canonical file is already the surface and an
adapter would be a second copy of a file they were going to read anyway. Claude Code reads only `.claude/skills/`, so it
is the one harness that needs a generated route.

## Directory Map

- [applying-ci-standards](applying-ci-standards/SKILL.md) — judging hooks, pipelines, and test targets
- [applying-content-quality](applying-content-quality/SKILL.md) — ordering and repairing a document's quality passes
- [applying-diataxis-framework](applying-diataxis-framework/SKILL.md) — classifying pages by the reader need served
- [applying-maker-checker-fixer](applying-maker-checker-fixer/SKILL.md) — judgement inside make, check, and fix loops
- [assessing-criticality-confidence](assessing-criticality-confidence/SKILL.md) — rating a finding's consequence and
  certainty
- [authoring-documentation](authoring-documentation/SKILL.md) — keeping documentation claims grounded and true
- [classifying-review-scope](classifying-review-scope/SKILL.md) — sizing a review pass and choosing disciplines
- [cutting-releases](cutting-releases/SKILL.md) — deciding a version is ready to publish
- [developing-applications](developing-applications/SKILL.md) — placing layers, errors, logs, and input checks
- [generating-validation-reports](generating-validation-reports/SKILL.md) — audit and fix reports that survive
  interruption
- [grill-me](grill-me/SKILL.md) — resolving a decision through recommended options
- [modeling-threats](modeling-threats/SKILL.md) — naming a design's assets, trust boundaries, entry points, and threats
- [plan-creating-project-plans](plan-creating-project-plans/SKILL.md) — authoring a formal plan's six documents
- [plan-validating-quality](plan-validating-quality/SKILL.md) — judging whether a plan draft is executable
- [plan-verifying-execution](plan-verifying-execution/SKILL.md) — checking delivered work against its plan
- [plan-writing-gherkin-criteria](plan-writing-gherkin-criteria/SKILL.md) — acceptance scenarios that can actually fail
- [producing-review-findings](producing-review-findings/SKILL.md) — raising findings that survive their fix
- [programming-python](programming-python/SKILL.md) — Python work under the Python standard
- [propagating-rules](propagating-rules/SKILL.md) — routing rule work through propagation
- [resolving-review-threads](resolving-review-threads/SKILL.md) — answering a published review's findings
- [synthesizing-review-findings](synthesizing-review-findings/SKILL.md) — deduplicating and verifying specialist
  findings
- [understanding-governance-architecture](understanding-governance-architecture/SKILL.md) — reading a repository as
  ordered levels
- [validating-factual-accuracy](validating-factual-accuracy/SKILL.md) — verifying claims against settling sources
- [validating-governance-rules](validating-governance-rules/SKILL.md) — a repository-wide rules check
- [validating-links](validating-links/SKILL.md) — checking links resolve under recorded forms
