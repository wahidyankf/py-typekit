---
description: >-
  Fixes the meaning of harness, agent, subagent, agent definition, agent instruction file, and harness directory, so a
  rule about one is never read as a rule about another.
when_to_use: >-
  Use when writing or reviewing governance, documentation, commit messages, or identifiers that mention agents or the
  tools that run them.
---

# Agent Vocabulary

These words name different objects. A sentence that uses one where it means another governs the wrong thing, and nothing
in the sentence tells the reader so.

## Terms

| Term                   | Means                                                                                                                 |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------- |
| harness                | the tool that runs a model: it owns the loop, the tools, the permissions, and the workspace                           |
| agent                  | a model and its harness working as one system — the whole, never either half                                          |
| subagent               | a named role a harness can start, with its own instructions and permissions                                           |
| agent definition       | the file declaring a subagent; the **agent** form in [Capability Forms](../../development/agents/capability-forms.md) |
| agent instruction file | a file a harness reads for repository rules, at a fixed name that harness expects                                     |
| harness directory      | the directory holding one harness's project configuration, or the shared canonical root that several harnesses read   |

A harness-specific file generated from a canonical definition is an **adapter**, governed by
[Harness Adapters](../../development/agents/harness-adapters.md).

## Name the Object

A limit on an instruction file is a limit on a file, not on a harness. Support for a new harness is support for a tool,
not for a file. Write the one meant.

This is not pedantry. One instruction file can be read by several harnesses, and one harness reads several files, so a
rule written against the wrong object either binds nothing or binds far more than intended. An instruction file is
therefore never called a harness file: the harness reads it, and the file outlives any one harness.

## Identifiers Follow the Prose

Code identifiers, script names, and configuration keys use the same vocabulary as the prose that documents them. A
variable named for the harness that actually holds an instruction-file path teaches exactly the confusion the prose
avoids.

An established identifier that names a family of commands rather than the object may keep its name when renaming it
would break every caller for no gain in clarity. Record that exception where the repository adopts this vocabulary, so
it reads as a decision rather than as drift.
