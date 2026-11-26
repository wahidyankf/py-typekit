---
description: >-
  Holds the enforcement-layer table and its gaps for the agent environment-file access rule.
when_to_use: >-
  Use when judging which layer stops a restricted-file access or what gap a layer admits.
---

# Enforcement Layers

| Layer                   | Stops                                                             |
| ----------------------- | ----------------------------------------------------------------- |
| harness permission deny | agent file tools on restricted paths                              |
| pre-tool hook           | the same, plus shell commands that name a restricted file         |
| leak scan               | a real file reaching pushed history, from any actor               |
| this convention         | what the layers above cannot see, such as an agent-written script |

A guard matching command text is best-effort, and documented as such: it cannot recognize a filename assembled from
innocent pieces.

A new agent harness is supported only once equivalent enforcement exists for it, including pre-tool enforcement. A
harness that cannot provide it is recorded as unenforced rather than assumed covered.
