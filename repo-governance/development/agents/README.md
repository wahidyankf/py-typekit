---
description: >-
  Indexes the standards governing a repository's coding-agent capabilities and how its agents plan, delegate, track,
  review, and report work.
when_to_use: >-
  Use when adding, retiring, or auditing a workflow, skill, or agent definition, or when deciding how an agent should
  carry out multi-step work.
---

# Agent Standards

A repository's coding-agent capabilities are governed material, not incidental configuration. They tell an agent what is
expected, and an inconsistency between two of them is a live contradiction rather than a documentation gap. The same
holds for how an agent works: how it plans, delegates, asks, tracks, and reviews is a standard, not a habit.

## Directory Map

- [Agent Authoring](agent-authoring.md) — what makes an agent definition sound beyond its schema
- [Agent Workflow Orchestration](agent-workflow-orchestration.md) — planning, delegating, verifying, and re-planning
  multi-step work
- [Capability Forms](capability-forms.md) — the four capability forms and the responsibility each holds
- [Harness Adapters](harness-adapters.md) — generating harness-specific files from canonical artifacts
- [Harness Adapters Modules](harness-adapters/README.md) — the one instruction body, vendor notes, and harness
  configuration and discovery
- [Last-Resort Questions](last-resort-questions.md) — when an agent may ask the user, and how little it asks
- [PR Review Agent Procedures](pr-review-agent-procedures/README.md) — the procedure moved out of the pr-review-checker
  definition to fit its word budget
- [Planning Capabilities](planning-capabilities.md) — the planning roster a repository exposes and its uniform contract
- [Planning Capabilities Modules](planning-capabilities/README.md) — rosters, decision gates, executor authority,
  delivery seams, verification, and review
- [Review Disciplines](review-disciplines.md) — specialist review scopes, tie-breaks, and finding requirements
- [Review Disciplines Modules](review-disciplines/README.md) — roster, boundary rulings, findings, cost controls, and
  the plan-document route
- [Subagent Orchestration](subagent-orchestration.md) — concurrency, dispatch order, stall detection, and verified
  results
- [Subagent Orchestration Modules](subagent-orchestration/README.md) — concurrency, stuck detection and recovery, and
  result handling
- [SWE Agent Procedures](swe-agent-procedures/README.md) — the procedure sections moved out of four swe-* agent
  definitions to fit their word budget
- [SWE Delegation](swe-delegation.md) — dispatching coding work to the fitting swe agent, and its exceptions
- [Task Tracking](task-tracking.md) — the task list kept before and during every task
- [Task Tracking Modules](task-tracking/README.md) — list lifecycle, direction and continuity, and bindings
- [Deployment Platform Agent Capability](vercel-mcp-capability.md) — probing a deployment platform's agent integration
  while planning
- [Web Research Delegation](web-research-delegation.md) — routing public-web research to one designated agent
