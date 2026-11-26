---
description: >-
  Fixes what makes a canonical agent definition sound beyond its schema: one role, role-derived capabilities, a name
  stating it, progressive reports, and a body that links rather than restates.
when_to_use: >-
  Use when writing an agent definition, deciding whether to extend an existing agent instead, or reviewing one that has
  grown.
---

# Agent Authoring

The [metadata schema](../../conventions/structure/artifact-metadata/001-schemas-by-path.md) decides whether an agent
definition is well formed; this standard decides whether it is good: invoked for the right reason, trustworthy with its
grants, and stopping when done.

## One Role, One Stopping Rule

An agent does one job and knows when it is finished; a definition needing "and" to state its role is two agents.

A combined role first loses independence: an agent producing and reviewing content cannot serve as a review, since
nothing stops it changing what it judges. Separate roles also keep capability lists short enough to believe.

Read the roster before creating an agent. Create one when the need differs from the closest existing agent in domain or
responsibility, required capabilities, or workload tier; extend that agent when only a procedure varies within the role.
A near-duplicate agent is a duplicated body; see [Capability Forms](capability-forms.md).

## Capabilities Follow the Role

Least privilege follows the role, not future convenience. The
[portable capabilities](../../conventions/structure/artifact-metadata/004-portable-capabilities.md) supply the
vocabulary; the role selects.

- **Reviewer or checker:** `repository-read`, plus `shell` when it runs validators, plus the reporting form below.
- **Maker or fixer:** `repository-read` and `repository-write`, plus `shell` when it runs gates.
- **Researcher:** `repository-read`, plus `network` when its sources are external.
- **Orchestrator:** `subagent`, plus only what its own steps do directly.

Each is a starting point, not an entitlement; every capability beyond it needs a reason stated in the body.

An agent declaring `subagent` orchestrates only while top-level; as a delegate it hands further delegation back to its
caller, for the reason [Capability Forms](capability-forms.md) gives under Skills Never Delegate. The exception is an
agent declaring `dispatches`, as [Agent Workflow Orchestration](agent-workflow-orchestration.md) sets out.

### Adopter Decision: How a Checker Reports

Under either option, a checker never modifies what it judges. Record the choice once.

- **Report file.** The checker adds `repository-write` for its own report only, written progressively as below. Findings
  survive interruption, but the body, not the harness, keeps writes off the judged content.
- **Read-only.** The checker declares the `read-only` constraint and returns findings to its caller, like
  [Plan Checker](../../../agents/plan-checker.md). The harness enforces non-modification, but findings live only in the
  caller's context until recorded.

## The Name States the Role

The `name` matches the file basename, as the schema requires, and says what the agent does to what, as
`<domain>-checker` illustrates; no closed role vocabulary is required. A bare `checker`, `helper`, or `assistant` routes
nowhere: harnesses and readers choose an agent by name and trigger before reading its body.

The `description` states what the agent does and `when_to_use` the situation calling for it; a vague pair gets the agent
invoked for the wrong work, or never.

## Reports Are Written as Findings Are Confirmed

An agent producing a report file creates it at start, marked in progress; appends each finding once confirmed; and marks
the report complete, with totals, when it stops.

Buffering findings loses them all when the run is interrupted or compacted, and can leave an empty file that reads as
clean. A report still marked in progress cannot pass for a finished one, the distinction
[Fail Closed](../../principles/fail-closed.md) keeps.

## The Body Applies Rules; It Does Not Restate Them

An agent body holds what is specific to its role: responsibility, procedure, stopping rule, and what it does not do. A
rule other artifacts also follow stays with its owning convention or skill, which the agent links or declares.

An agent declares every skill its work depends on: a delegated agent inherits no session context, so an undeclared skill
never reaches it.

A copied rule gets corrected in its owner and stays wrong in the agent; see
[One Source Per Fact](../../principles/one-source-per-fact.md).

## What Stays Out

Colours, tool names, permission keys, and model identifiers are harness presentation, belonging to the
[generated adapter](harness-adapters.md) or the repository's tier mapping; a canonical definition carrying them has
become one harness's configuration.
