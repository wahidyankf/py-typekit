---
description: >-
  Keeps a harness's project configuration to documented settings the repository needs, never rules, requires tested
  discovery behaviour, and refuses a weaker control in place of one a harness lacks.
when_to_use: >-
  Use when adding or editing a harness's project configuration, or before relying on how a harness discovers
  instruction, agent, skill, or index files.
---

# Configuration and Discovery

## Project Configuration Holds Settings, Never Rules

A harness's project configuration holds only settings the harness documents and the repository needs. A rule belongs in
the canonical instruction body or in governance documents.

A rule placed in configuration reaches one harness only and escapes the review the canonical body receives, so
contributors on every other harness work under a different rule without knowing it. An undocumented setting fails the
same way later: it stops working in a release nobody connects to it.

A file the harness already discovers is not listed again as an extra instruction source. The second listing adds a route
to the same text and nothing else.

## Repository Policy and Shared Integrations

User-global approvals and shared integrations do not relocate repository compute admission, protected-path policy,
quality gates, or Git obligations. Claude Code, OpenCode, and Command Code native bindings invoke the repository-owned
endpoint for their physical checkout; a neutral global adapter routes a different destination without duplicating policy
evaluation or containing those policies.

The Claude Code and Command Code Serena proxy activates the physical checkout and requires successful recovery after
activation failure. Tracked project configuration excludes protected indexing paths; caches and local state stay
ignored. Native role translations must preserve semantic capability grants and denials, verified in the actual harness.
OpenCode Serena registration is deferred because its hooks cannot attest the selected MCP client.

Codex 0.161 retains its existing global and repository-native guards. Serena and new destination routing are deferred:
its [release role loader][role] omits MCP overrides, and native shell hook payloads omit the requested working
directory. No role-local MCP environment or filter enforcement is claimed.

[role]: https://github.com/openai/codex/blob/979011409de0a60b52f179721948e65531d26144/codex-rs/core/src/agent/role.rs

## Discovery Is Tested Before It Is Relied On

Which files a harness discovers, where it looks, and what it does with an index file in a directory it scans differ
between harnesses and change between releases. Before a repository relies on a harness finding an instruction file, an
agent, a skill, or a directory index, it tests that behaviour in that harness.

An adapter generated for a discovery rule the harness does not follow can match its expected bytes and still never be
read. Runtime discovery proof remains separate from adapter validation.

## A Missing Control Is Not Substituted

Where a harness cannot enforce a restriction an artifact declares, the artifact is not published for that harness, as
the [entrypoint](../harness-adapters.md) requires. A weaker substitute, such as an instruction telling the agent not to
use a capability the harness still grants, does not satisfy the restriction.

Some repositories accept such a substitute and record it beside the canonical definition. This standard does not,
because a restriction that holds only while the model complies grants in practice what the definition denies, and a
recorded substitute reads as enforcement to everyone who did not read the record.

## Session-Coordinated Profiles

A profile whose native subagents cannot dispatch explicitly selects only canonical leaf agents. Any role declaring
`subagent` or nonempty `dispatches` is read completely in the main session and coordinated there under its named
dispatch allowlist. This is the exception to one native adapter per canonical role: native leaves cannot perform nested
dispatch. The local main-session role is `swe-orchestrator`; adopters record their own roles in their harness contract.

For a session-inheriting profile, omit tier mappings and model, featureModels, effort, and reasoningEffort pins from
adapters, settings, shared global sources, and smoke commands. The active session supplies the model; omitted reasoning
fields use the harness default. Retain the strongest documented native grants and denials for every selected leaf.

Keep declared personal project settings and taste-learning trees local and ignored, preserving contents and active
learning. This native transaction owns only the declared agent root, never local state or project settings.

When canonical agents change, update the explicit selection in the same change. Audit that it equals every canonical
leaf, excluding exactly roles declaring `subagent` or nonempty `dispatches`, after regeneration. Declared-profile parity
checks adapter contents; live discovery and main-session-to-leaf probes check vendor behaviour. Semantic main-session
compliance remains unenforced by decision because adapter validation cannot judge model conduct.
