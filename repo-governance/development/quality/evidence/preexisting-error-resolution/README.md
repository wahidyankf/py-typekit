---
description: >-
  Indexes the ordered modules for triaging and investigating a preexisting gate failure and for the bounded exception
  when the pipeline itself is unavailable.
when_to_use: >-
  Use to locate the module that governs one part of resolving a gate failure the current change did not introduce.
---

# Preexisting Error Resolution Modules

The [Preexisting Error Resolution](../preexisting-error-resolution.md) entrypoint indexes the rule these modules hold;
read them in sequence.

## Directory Map

- [001 Triage and Investigation](001-triage-and-investigation.md) — telling a missing regenerable artifact from a
  defect, investigating a real failure, and auditing a mitigation that did not hold
- [002 Pipeline Availability](002-pipeline-availability.md) — the five conditions for proceeding when the pipeline is
  unavailable, when a persistent outage becomes an ordinary defect, and toolchain drift across a runner pool
