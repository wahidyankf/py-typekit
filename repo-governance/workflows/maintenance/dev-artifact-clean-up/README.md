---
name: dev-artifact-clean-up
description: >-
  Indexes the modules that explain why clean-up deletion is permanent and how leaked test containers are removed.
when_to_use: >-
  Use when reading the Dev Artifact Clean-Up workflow's reasoning or container recipe beyond its sequence.
---

# Dev Artifact Clean-Up Modules

Read with the [Dev Artifact Clean-Up](../dev-artifact-clean-up.md) entrypoint.

- **001 Irreversible Deletion** holds why deleting scratch is permanent, and so why `unknown` routes to investigation.
- **002 Leaked Test Containers** holds how to detect and remove the containers, volumes, and networks a task's runs
  leaked.

## Directory Map

- [001 Irreversible Deletion](001-irreversible-deletion.md)
- [002 Leaked Test Containers](002-leaked-test-containers.md)
