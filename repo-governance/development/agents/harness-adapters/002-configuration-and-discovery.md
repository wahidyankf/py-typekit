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
dispatch. This repository currently declares no such main-session role; all canonical agents are leaves.

For a session-inheriting profile, omit tier mappings and model, featureModels, effort, and reasoningEffort pins from
adapters, settings, shared global sources, and smoke commands. The active session supplies the model; omitted reasoning
fields use the harness default. Retain the strongest documented native grants and denials for every selected leaf.

Keep declared personal project settings and taste-learning trees local and ignored, preserving contents and active
learning. This native transaction owns only the declared agent root, never local state or project settings.

When canonical agents change, update the explicit selection in the same change. Audit that it equals every canonical
leaf, excluding exactly roles declaring `subagent` or nonempty `dispatches`, after regeneration. Declared-profile parity
checks adapter contents; live discovery and main-session-to-leaf probes check vendor behaviour. Semantic main-session
compliance remains unenforced by decision because adapter validation cannot judge model conduct.
