---
name: dev-artifact-clean-up
description: >-
  Indexes the artifact cleanup companions on external Nx cache eviction, deletion safety, and leaked test containers.
when_to_use: >-
  Use when following artifact cleanup and a task uses Nx or containers, or when classifying uncommitted artifacts.
---

# Dev Artifact Clean-Up Modules

Read the [cleanup workflow](../dev-artifact-clean-up.md), then its companion when Nx, containers, or deletion safety
applies.

## Directory Map

- [External Nx Cache Eviction](001-external-nx-cache-eviction.md) — approval, retained state, and permanent deletion.
- [Leaked Test Containers](002-leaked-test-containers.md) — detecting and removing the containers, volumes, and networks
  a task's runs leaked.
