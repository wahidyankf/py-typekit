---
description: >-
  Records the stack pack py-typekit adopted, the decisions the Python standard leaves open, and every deviation from
  the catalog's testing layers.
when_to_use: >-
  Use when working on the typekit library, adopting or retiring a stack pack, or changing a recorded stack decision.
---

# Repository Adapter

py-typekit holds one project, the `typekit` library, so [`repo-config.yml`](../../../../repo-config.yml) declares no
`extensions.software-development` inventory; Project Applicability below names the project instead.

## Adopted Packs

| Pack     | Status  | Reason                                               |
| -------- | ------- | ---------------------------------------------------- |
| `python` | adopted | the library is written for Python 3.14, as FERRET is |

## Adopter Decisions

- **`python-standards.md`** — Decision: boundary validation; Choice: standard-library checks; Reason: the library has
  zero runtime dependencies
- **`python-standards.md`** — Decision: expected failures; Choice: returned result values; Reason: this library is the
  mechanism
- **`python-standards.md`** — Decision: coverage floor; Choice: 100% branch coverage; Reason: measured over `typekit`,
  in the unit layer only

The standard's "no function returns a union its callers must untangle" is read with the expected-failures decision:
`Result` and `Option` are the sanctioned unions, and every other return is a single type.

Behaviour-driven development is not adopted: a pure library has no behaviour corpus beyond its unit contract. The unit
suite under [Test-Driven Development](../testing/test-driven-development.md) is the only test layer.

## Project Applicability

- `typekit`: the library and its unit suite; its commands are in the root [README](../../../../README.md).

## Version Sources

- `python`: `.python-version` and `requires-python` in `pyproject.toml`.
